<script>
    // @ts-nocheck

    import { onMount } from "svelte";
    import * as d3 from "d3";

    let svg;
    export let data;
    export let title;
    const margin = { top: 50, right: 0, bottom: 0, left: 0 };
    const x = 350;
    const y = x;
    const drawDuration = 2000;
    const radius = Math.min(x, y) / 2 - Math.max(margin.top, margin.bottom);
    let hasDrawn = false;

    onMount(async () => {
        const observer = new IntersectionObserver(handleIntersection, {
            threshold: 0.1,
        });
        observer.observe(svg);

        return () => observer.disconnect();
    });

    // Only draw once
    function handleIntersection(entries) {
        const entry = entries[0];
        if (entry.isIntersecting && !hasDrawn) {
            hasDrawn = true;
            drawRadialHistogram();
        }
    }

    function drawRadialHistogram() {
        const svgElement = d3
            .select(svg)
            .attr("width", x)
            .attr("height", y)
            .append("g")
            .attr("transform", `translate(${x / 2}, ${y / 2})`);

        const angleScale = d3
            .scaleBand()
            .domain(data.map((d) => d.half_hour_intervals))
            .range([0, 2 * Math.PI])
            .padding(0.1);

        const radiusScale = d3
            .scaleLinear()
            .domain([
                0,
                d3.max(data, (d) => Math.max(d.EFIT, d.ICONIC)) + 0.004,
            ])
            .range([0, radius]);

        svgElement
            .selectAll(".x-axis")
            .data(data)
            .enter()
            .append("line")
            .attr("class", "x-axis")
            .attr("x1", 0)
            .attr("y1", 0)
            .attr("x2", (d, i) =>
                i % 2 === 0
                    ? Math.cos(angleScale(d.half_hour_intervals)) * radius
                    : 0,
            )
            .attr("y2", (d, i) =>
                i % 2 === 0
                    ? Math.sin(angleScale(d.half_hour_intervals)) * radius
                    : 0,
            )

            // Stroke customization

            // Coloring stroke for the first and last lines
            .attr("stroke", "lightgray")


            // Thicker stroke for first and last lines
            // .attr("stroke-width", (d, i) =>
            //     i === 12 || i === data.length - 12 ? "3" : "0.5",
            // )

            .attr("stroke-width", (d, i) => (i % 3 === 0 ? "0.6" : "0.3"))
            .attr("stroke-dasharray", (d, i) => (i % 3 === 0 ? "0,0" : "4,3"));

        // Solid stroke for first and last lines
        // .attr("stroke-dasharray", (d, i) =>
        //     i === 12 || i === data.length - 12 ? "0,0" : "6,2",
        // );

        svgElement
            .append("circle")
            .attr("class", "circle-border")
            .attr("cx", 0)
            .attr("cy", 0)
            .attr("r", radius)
            .attr("fill", "none")
            .attr("stroke", "lightgray")
            .attr("stroke-width", 1);

        // Prepare the radial line function for ICONIC
        const lineICONIC = d3
            .lineRadial()
            .angle(
                (d) =>
                    angleScale(d.half_hour_intervals) +
                    angleScale.bandwidth() / 2 +
                    Math.PI,
            )
            .radius((d) => radiusScale(d.ICONIC))
            .curve(d3.curveCardinalClosed);

        // Draw the filled area under the ICONIC curve
        svgElement
            .append("path")
            .datum(data)
            .attr("class", "area-iconic")
            .attr(
                "d",
                d3
                    .areaRadial()
                    .angle(
                        (d) =>
                            angleScale(d.half_hour_intervals) +
                            angleScale.bandwidth() / 2 +
                            Math.PI,
                    )
                    .innerRadius(0)
                    .outerRadius((d) => radiusScale(d.ICONIC))
                    .curve(d3.curveCardinalClosed)(data),
            )
            .attr("fill", "var(--brandDarkGreen)")
            .attr("opacity", 0)
            .transition()
            .delay(1500)
            .duration(drawDuration)
            .ease(d3.easeLinear)
            .attr("opacity", 0.03);

        // Draw the filled area under the EFIT curve
        svgElement
            .append("path")
            .datum(data)
            .attr("class", "area-efit")
            .attr(
                "d",
                d3
                    .areaRadial()
                    .angle(
                        (d) =>
                            angleScale(d.half_hour_intervals) +
                            angleScale.bandwidth() / 2 +
                            Math.PI,
                    )
                    .innerRadius(0)
                    .outerRadius((d) => radiusScale(d.EFIT))
                    .curve(d3.curveCardinalClosed)(data),
            )
            .attr("fill", "#e6841a")
            .attr("opacity", 0) // Start with opacity 0
            .transition()
            .delay(1500)
            .duration(drawDuration)
            .ease(d3.easeLinear)
            .attr("opacity", 0.03);

        // Draw the ICONIC curve
        const pathICONIC = svgElement
            .append("path")
            .datum(data)
            .attr("class", "curve-iconic")
            .attr("fill", "none")
            .attr("stroke", "var(--brandDarkGreen)")
            .attr("stroke-width", 1.5)
            .attr("d", lineICONIC);

        // Get the total length of the ICONIC path
        const totalLengthICONIC = pathICONIC.node().getTotalLength();

        pathICONIC
            .attr("stroke-dasharray", totalLengthICONIC)
            .attr("stroke-dashoffset", totalLengthICONIC)
            .transition()
            .ease(d3.easeLinear)
            .duration(drawDuration)
            .attr("stroke-dashoffset", 0);

        // Prepare the radial line function for EFIT
        const lineEFIT = d3
            .lineRadial()
            .angle(
                (d) =>
                    angleScale(d.half_hour_intervals) +
                    angleScale.bandwidth() / 2 +
                    Math.PI,
            )
            .radius((d) => radiusScale(d.EFIT))
            .curve(d3.curveCardinalClosed);

        const pathEFIT = svgElement
            .append("path")
            .datum(data)
            .attr("class", "curve-efit")
            .attr("fill", "none")
            .attr("stroke", "#e6841a")
            .attr("stroke-width", 1.5)
            .attr("d", lineEFIT);

        // Get the total length of the EFIT path
        const totalLengthEFIT = pathEFIT.node().getTotalLength();

        pathEFIT
            .attr("stroke-dasharray", totalLengthEFIT)
            .attr("stroke-dashoffset", totalLengthEFIT)
            .transition()
            .duration(drawDuration)
            .ease(d3.easeLinear)
            .attr("stroke-dashoffset", 0);

        // Enable mouseover highlight once lines have been drawn
        if (hasDrawn) {
            setTimeout(() => {
                svgElement
                    .selectAll(".area-iconic, .area-efit")
                    .on("mouseover", function () {
                        d3.select(this)
                            .transition()
                            .duration(200)
                            .attr("opacity", 0.1);
                    })
                    .on("mouseout", function () {
                        d3.select(this)
                            .transition()
                            .duration(200)
                            .attr("opacity", 0.03);
                    });
                triggerMouseover();
            }, drawDuration + 100);
        }

        function triggerMouseover() {
            const event = new MouseEvent("mouseover");
            const elements = document.querySelectorAll(
                ".area-iconic, .area-efit",
            );
            elements.forEach((element) => {
                if (element.matches(":hover")) {
                    element.dispatchEvent(event);
                }
            });
        }

        // Add labels for each interval, adjusted for the rotation
        svgElement
            .selectAll(".x-label")
            .data(data)
            .enter()
            .append("text")
            .attr("fill", "rgba(0, 0, 0, 0.7)")
            .attr("class", "x-label")
            .attr("text-anchor", "middle")
            .attr("dominant-baseline", "middle")
            .attr(
                "x",
                (d) =>
                    Math.cos(
                        angleScale(d.half_hour_intervals) -
                            Math.PI / 2 +
                            Math.PI,
                    ) *
                    (radius + 20),
            )
            .attr(
                "y",
                (d) =>
                    Math.sin(
                        angleScale(d.half_hour_intervals) -
                            Math.PI / 2 +
                            Math.PI,
                    ) *
                    (radius + 15),
            )
            .style("font-size", "10px")
            .style("fill", "grey")
            .text((d, i) => (i % 2 === 0 ? d.half_hour_intervals : ""));

        const legend = svgElement
            .append("g")
            .attr("transform", `translate(-60, 270)`);

        svgElement
            .append("circle")
            .attr("class", "x-axis-circle")
            .attr("cx", 0)
            .attr("cy", 0)
            .attr("r", 0)
            .attr("fill", "white")
            .attr("stroke", "lightgray")
            .attr("stroke-width", 0.5);

        // Add PM label
        svgElement
            .append("text")
            .attr("x", 12) // X position
            .attr("y", -radius + 10) // Y position (above the chart)
            .attr("text-anchor", "middle")
            .attr("dominant-baseline", "middle")
            .style("font-size", "10px")
            .style("fill", "grey")
            .text("PM");

        // Add AM label
        svgElement
            .append("text")
            .attr("x", -12) // X position
            .attr("y", radius - 10) // Y position (below the chart)
            .attr("text-anchor", "middle")
            .attr("dominant-baseline", "middle")
            .style("font-size", "10px")
            .style("fill", "grey")
            .text("AM");
    }
</script>

<div class="radial">
    <p class="graph-title">{title}</p>
    <svg bind:this={svg}></svg>
</div>

<style>
    .graph-title {
        font-size: 14px;
        font-family: RobotoRegular;
        margin-bottom: -20px;
    }

    @media (min-width: 700px) {
        .radial {
            margin-bottom: -20px;
        }
    }

    @media (min-width: 400px) and (max-width: 700px) {
        .radial {
            transform: scale(1.2);
            transform-origin: center;
            margin: 40px;
        }
    }
</style>
