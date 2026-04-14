
df <- df |>
  filter(TripCount > 0) |>
  mutate(
    t     = Year + (Month - 1) / 12,
    theta = (Month - 1) / 12 * 2 * pi,
    r     = TripCount,
    x     = r * sin(theta),
    y     = r * cos(theta)
  ) |>
  arrange(t)

# ── 2. Build spline segment-by-segment between consecutive points ───────────
# Instead of one global smooth, interpolate densely between each pair of
# adjacent observed points in (x, y) space. This guarantees the curve
# starts and ends exactly on each dot.

n        <- nrow(df)
steps    <- 30   # interpolation points between each pair

spline_df <- map_dfr(1:(n - 1), function(i) {
  x0 <- df$x[i];   x1 <- df$x[i + 1]
  y0 <- df$y[i];   y1 <- df$y[i + 1]
  t0 <- df$t[i];   t1 <- df$t[i + 1]
  
  # Use the two neighbours on either side for a Catmull-Rom-style tension.
  # For interior points, grab prev & next; for edges, reflect.
  xprev <- if(i > 1)     df$x[i - 1] else 2 * x0 - x1
  yprev <- if(i > 1)     df$y[i - 1] else 2 * y0 - y1
  xnext <- if(i < n - 1) df$x[i + 2] else 2 * x1 - x0
  ynext <- if(i < n - 1) df$y[i + 2] else 2 * y1 - y0
  
  # Catmull-Rom tangents (alpha = 0.5 for centripetal)
  tx0 <- (x1 - xprev) / 2;  ty0 <- (y1 - yprev) / 2
  tx1 <- (xnext - x0) / 2;  ty1 <- (ynext - y0) / 2
  
  s <- seq(0, 1, length.out = steps + 1)
  s <- if(i < n - 1) head(s, -1) else s   # avoid duplicating shared endpoints
  
  # Hermite basis
  h00 <- 2*s^3 - 3*s^2 + 1
  h10 <- s^3 - 2*s^2 + s
  h01 <- -2*s^3 + 3*s^2
  h11 <- s^3 - s^2
  
  tibble(
    x = h00*x0 + h10*tx0 + h01*x1 + h11*tx1,
    y = h00*y0 + h10*ty0 + h01*y1 + h11*ty1,
    t = h00*t0 + h01*t1          # interpolate t for colour
  )
})

# ── 3. Reference rings ──────────────────────────────────────────────────────
ring_vals <- pretty(df$r, n = 4)
ring_vals <- ring_vals[ring_vals > 0]

ring_df <- expand_grid(
  r     = ring_vals,
  theta = seq(0, 2 * pi, length.out = 361)
) |> mutate(x = r * sin(theta), y = r * cos(theta))

ring_label_df <- tibble(
  r     = ring_vals,
  theta = 0.08,
  x     = r * sin(theta),
  y     = r * cos(theta),
  label = scales::comma(r)
)

# ── 4. Month spokes ─────────────────────────────────────────────────────────
label_r  <- max(ring_vals) * 1.13
spoke_df <- tibble(
  Month = 1:12,
  label = month.abb,
  theta = (Month - 1) / 12 * 2 * pi,
  x     = label_r * sin(theta),
  y     = label_r * cos(theta)
)

# ── 5. Plot ─────────────────────────────────────────────────────────────────
ggplot() +
  geom_path(data = ring_df, aes(x, y, group = factor(r)),
            colour = "grey88", linewidth = 0.3) +
  geom_text(data = ring_label_df, aes(x, y, label = label),
            size = 2.6, colour = "grey55", hjust = 0) +
  geom_segment(data = spoke_df,
               aes(x = 0, y = 0, xend = x * 0.96, yend = y * 0.96),
               colour = "grey90", linewidth = 0.3) +
  geom_text(data = spoke_df, aes(x, y, label = label),
            size = 3, fontface = "bold", colour = "grey45") +
  geom_path(data = spline_df, aes(x, y, colour = t),
            linewidth = 1.1, lineend = "round") +
  # geom_point(data = df, aes(x, y, colour = t),
  #            size = 2.4, shape = 21, fill = "white", stroke = 0.9) +
  scale_colour_viridis_c(
    name = "Year", option = "plasma",
    breaks = unique(floor(df$t)),
    labels = unique(floor(df$t))
  ) +
  coord_equal() +
  theme_void(base_size = 12) +
  theme(
    legend.position  = "bottom",
    legend.key.width = unit(2.5, "cm"),
    plot.title    = element_text(hjust = 0.5, size = 14, face = "bold",
                                 margin = margin(b = 6)),
    plot.subtitle = element_text(hjust = 0.5, colour = "grey50",
                                 margin = margin(b = 16)),
    plot.margin   = margin(20, 20, 20, 20)
  ) +
  labs(
    title    = "Bike share trips — monthly spiral",
    subtitle = "Distance from centre = total trips  ·  colour = year"
  )