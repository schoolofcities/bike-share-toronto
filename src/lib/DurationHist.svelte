<script>
    import { onMount } from "svelte";
    import * as d3 from "d3";

    let svg;
    let data = [];
    let stats = [];
    const margin = { top: 20, right: 30, bottom: 50, left: 60 }; // Adjusted margins to fit labels
    const width = 600 - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;

    onMount(async () => {
        data = await d3.csv("duration_counts.csv", (d) => ({
            duration_bin: d.duration_bin,
            EFIT: +d.EFIT_normalized,
            ICONIC: +d.ICONIC_normalized,
            interval_start: +d.interval_start,
        }));

        stats = await d3.csv("duration_stats.csv");

        drawHistogram();
    });

    // Draw the bar chart
    function drawHistogram() {
        const x = d3
            .scaleLinear()
            .domain([
                d3.min(data, (d) => d.interval_start),
                d3.max(data, (d) => d.interval_start),
            ])
            .range([0, width]);

        const y = d3
            .scaleLinear()
            .domain([0, d3.max(data, (d) => Math.max(d.EFIT, d.ICONIC))])
            .nice()
            .range([height, 0]);

        const svgElement = d3
            .select(svg)
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        // X-axis
        svgElement
            .append("g")
            .attr("transform", `translate(0,${height})`)
            .call(
                d3.axisBottom(x)
                    .ticks(10)
                    .tickSizeOuter(0)
                    .tickFormat((d) => `${(d / 60).toFixed(2)} min`)
            );

        // Y-axis
        svgElement.append("g").call(d3.axisLeft(y));

        // Bars for ICONIC
        svgElement
            .selectAll(".bar-iconic")
            .data(data)
            .enter()
            .append("rect")
            .attr("class", "bar-iconic")
            .attr("x", (d) => x(d.interval_start))
            .attr("y", (d) => y(d.ICONIC))
            .attr("width", width / data.length - 1)
            .attr("height", (d) => height - y(d.ICONIC))
            .attr("fill", "orange")
            .attr("opacity", 0.8);

                // Bars for EFIT
                svgElement
            .selectAll(".bar-efit")
            .data(data)
            .enter()
            .append("rect")
            .attr("class", "bar-efit")
            .attr("x", (d) => x(d.interval_start))
            .attr("y", (d) => y(d.EFIT))
            .attr("width", width / data.length - 1)
            .attr("height", (d) => height - y(d.EFIT))
            .attr("fill", "steelblue")
            .attr("opacity", 0.8);

        // Add the legend
        const legend = svgElement
            .append("g")
            .attr("transform", `translate(${width - 120}, ${margin.top})`);

        legend
            .append("rect")
            .attr("x", 0)
            .attr("y", 0)
            .attr("width", 18)
            .attr("height", 18)
            .attr("fill", "steelblue")
            .attr("opacity", 0.8);

        legend
            .append("text")
            .attr("x", 25)
            .attr("y", 12)
            .attr("fill", "#000")
            .style("font-size", "12px")
            .text("EFIT");

        legend
            .append("rect")
            .attr("x", 0)
            .attr("y", 25)
            .attr("width", 18)
            .attr("height", 18)
            .attr("fill", "orange")
            .attr("opacity", 0.8);

        legend
            .append("text")
            .attr("x", 25)
            .attr("y", 37)
            .attr("fill", "#000")
            .style("font-size", "12px")
            .text("ICONIC");

        // Add X-axis label
        svgElement
            .append("text")
            .attr("text-anchor", "middle")
            .attr("x", width / 2)
            .attr("y", height + margin.bottom - 10) // Position below the axis
            .style("font-size", "14px")
            .text("Trip Duration (minutes)");

        // Add Y-axis label
        svgElement
            .append("text")
            .attr("text-anchor", "middle")
            .attr("transform", `rotate(-90)`)
            .attr("x", -height / 2)
            .attr("y", -margin.left + 15) // Position to the left of the axis
            .style("font-size", "14px")
            .text("Count (normalized)");
    }
</script>

<!-- Render the SVG element -->
<div class="histogram">
    <p>Trip Duration by Bike Model</p>
    <svg bind:this={svg}></svg>
</div>

<table>
    <thead>
        <tr>
            <th>Bike Model</th>
            <th>Mean</th>
            <th>Median</th>
            <th>Std</th>
            <th>Min</th>
            <th>Max</th>
        </tr>
    </thead>
    <tbody>
        {#each stats as stat}
            <tr>
                <td>{stat.bike_model}</td>
                <td>{stat.mean}</td>
                <td>{stat.median}</td>
                <td>{stat.std}</td>
                <td>{stat.min}</td>
                <td>{stat.max}</td>
            </tr>
        {/each}
    </tbody>
</table>

<style>
</style>
