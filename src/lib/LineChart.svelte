<script>
    // @ts-nocheck

    import { onMount } from "svelte";
    import * as d3 from "d3";

    let svg;
    let data = [];
    const margin = { top: 20, right: 40, bottom: 50, left: 55 };
    const maxWidth = 650;
    const minWidth = 380;
    const heightPercentage = 0.5; // 60% of the screen width
    let width = Math.min(
        window.innerWidth - margin.left - margin.right,
        maxWidth,
    );
    let height = width * heightPercentage;

    export let csvData;
    export let title;
    export let xlabel;
    export let medianEFIT;
    export let medianICONIC;
    export let suffix; // necessary for state management
    export let xdivider;
    export let xdecimal;
    export let xtickamount;
    export let xunit;
    export let medianadjust;

    let showNormalized = true;
    let yAxisGroup;
    const transitionDuration = 400;
    let enableMouseEvents = true;

    onMount(async () => {
        data = await d3.csv(csvData, (d) => ({
            EFIT: +d.EFIT,
            EFIT_normalized: +d.EFIT_normalized,
            ICONIC: +d.ICONIC,
            ICONIC_normalized: +d.ICONIC_normalized,
            interval_start: +d.interval_start,
        }));

        drawLineChart();
        window.addEventListener('resize', handleResize);
    });

    function handleResize() {
        width = Math.min(
            window.innerWidth - margin.left - margin.right,
            maxWidth,
        );
        width = Math.max(
            width, minWidth
        );
        height = width * heightPercentage;
        drawLineChart();
    }

    // Initialize line chart
    function drawLineChart() {
        d3.select(svg).selectAll("*").remove();

        const x = d3
            .scaleLinear()
            .domain([
                d3.min(data, (d) => d.interval_start),
                d3.max(data, (d) => d.interval_start),
            ])
            .range([0, width]);

        const y = d3
            .scaleLinear()
            .domain([
                0,
                d3.max(data, (d) =>
                    showNormalized
                        ? Math.max(d.EFIT_normalized, d.ICONIC_normalized)
                        : Math.max(d.EFIT, d.ICONIC),
                ),
            ])
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
                d3
                    .axisBottom(x)
                    .ticks(xtickamount)
                    .tickSizeOuter(0)
                    .tickFormat((d) => `${(d / xdivider).toFixed(xdecimal)}`),
            );

        // Y-axis
        yAxisGroup = svgElement.append("g");
        updateYAxis(y);

        // Area generator for ICONIC
        const areaICONIC = d3
            .area()
            .x((d) => x(d.interval_start))
            .y0(y(0))
            .y1((d) => y(showNormalized ? d.ICONIC_normalized : d.ICONIC))
            .curve(d3.curveMonotoneX);

        svgElement
            .append("path")
            .datum(data)
            .attr("class", `area-iconic-${suffix}`)
            .attr("fill", "var(--brandDarkGreen)")
            .attr("opacity", 0.03)
            .attr("d", areaICONIC);

        // Area generator for EFIT
        const areaEFIT = d3
            .area()
            .x((d) => x(d.interval_start))
            .y0(y(0))
            .y1((d) => y(showNormalized ? d.EFIT_normalized : d.EFIT))
            .curve(d3.curveMonotoneX);

        svgElement
            .append("path")
            .datum(data)
            .attr("class", `area-efit-${suffix}`)
            .attr("fill", "#e6841a")
            .attr("opacity", 0.03)
            .attr("d", areaEFIT);

        // Mouse over highlight
        svgElement
            .selectAll(`.area-iconic-${suffix}, .area-efit-${suffix}`)
            .on("mouseover", function () {
                if (enableMouseEvents) {
                    d3.select(this)
                        .transition()
                        .duration(transitionDuration - 200)
                        .attr("opacity", 0.1);
                }
            })
            .on("mouseout", function () {
                if (enableMouseEvents) {
                    d3.select(this)
                        .transition()
                        .duration(transitionDuration - 200)
                        .attr("opacity", 0.03);
                }
            });

        // Line generator for EFIT
        const lineEFIT = d3
            .line()
            .x((d) => x(d.interval_start))
            .y((d) => y(showNormalized ? d.EFIT_normalized : d.EFIT))
            .curve(d3.curveMonotoneX);

        // Add path for EFIT
        svgElement
            .append("path")
            .datum(data)
            .attr("class", `line-efit-${suffix}`)
            .attr("fill", "none")
            .attr("stroke", "#e6841a")
            .attr("stroke-width", 2)
            .attr("d", lineEFIT);

        // Line generator for ICONIC
        const lineICONIC = d3
            .line()
            .x((d) => x(d.interval_start))
            .y((d) => y(showNormalized ? d.ICONIC_normalized : d.ICONIC))
            .curve(d3.curveMonotoneX);

        // Add path for ICONIC
        svgElement
            .append("path")
            .datum(data)
            .attr("class", `line-iconic-${suffix}`)
            .attr("fill", "none")
            .attr("stroke", "var(--brandDarkGreen)")
            .attr("stroke-width", 2)
            .attr("d", lineICONIC);

        // Median line ICONIC
        svgElement
            .append("line")
            .attr("x1", x(medianICONIC))
            .attr("x2", x(medianICONIC))
            .attr("y1", 0)
            .attr("y2", height)
            .attr("stroke", "var(--brandDarkGreen)")
            .attr("stroke-width", 1)
            .attr("stroke-dasharray", "4");

        // Label for medianICONIC
        svgElement
            .append("text")
            .attr("x", x(medianICONIC) + 5) // Slightly to the right of the line
            .attr("y", y(d3.max(data, (d) => d.ICONIC_normalized)) + 7) // Slightly below the top of the line
            .attr("fill", "var(--brandDarkGreen)")
            .style("font-size", "12px")
            .attr("text-anchor", "start") // Justify left
            .append("tspan")
            .text("ICONIC")
            .attr("x", x(medianICONIC) + 5) // Ensure the x position is the same for both lines
            .attr("dy", "0em") // Position the first line
            .append("tspan")
            .text(
                "Median: " +
                    (medianICONIC / xdivider).toFixed(1) +
                    " " +
                    xunit,
            )
            .attr("x", x(medianICONIC) + 5) // Ensure the x position is the same for both lines
            .attr("dy", "1.2em"); // Position the second line below the first

        // Median line EFIT
        svgElement
            .append("line")
            .attr("x1", x(medianEFIT))
            .attr("x2", x(medianEFIT))
            .attr(
                "y1",
                y(d3.max(data, (d) => d.EFIT_normalized)) + medianadjust,
            )
            .attr("y2", height)
            .attr("stroke", "#e6841a")
            .attr("stroke-width", 1)
            .attr("stroke-dasharray", "4");

        // Label for medianEFIT
        svgElement
            .append("text")
            .attr("x", x(medianEFIT) + 5) // Slightly to the right of the line
            .attr(
                "y",
                y(d3.max(data, (d) => d.EFIT_normalized)) + 8 + medianadjust,
            ) // Slightly below the top of the line
            .attr("fill", "#e6841a")
            .style("font-size", "12px")
            .attr("text-anchor", "start") // Justify left
            .append("tspan")
            .text("EFIT")
            .attr("x", x(medianEFIT) + 5) // Ensure the x position is the same for both lines
            .attr("dy", "0em") // Position the first line
            .append("tspan")
            .text(
                "Median: " +
                    (medianEFIT / xdivider).toFixed(1) +
                    " " +
                    xunit,
            )
            .attr("x", x(medianEFIT) + 5) // Ensure the x position is the same for both lines
            .attr("dy", "1.2em"); // Position the second line below the first

        // Add X-axis label
        svgElement
            .append("text")
            .attr("text-anchor", "middle")
            .attr("x", width / 2)
            .attr("y", height + margin.bottom - 10)
            .style("font-size", "14px")
            .style("font-family", "RobotoBold")
            .text(xlabel);
    }

    function updateYAxis(y) {
        yAxisGroup.call(d3.axisLeft(y));
    }

    // Transition line chart between counts and normalized
    function updateLines() {
        const y = d3
            .scaleLinear()
            .domain([
                0,
                d3.max(data, (d) =>
                    showNormalized
                        ? Math.max(d.EFIT_normalized, d.ICONIC_normalized)
                        : Math.max(d.EFIT, d.ICONIC),
                ),
            ])
            .range([height, 0]);

        updateYAxis(y);

        // Update ICONIC line
        d3.select(`.line-iconic-${suffix}`)
            .transition()
            .duration(transitionDuration)
            .attr(
                "d",
                d3
                    .line()
                    .x((d) =>
                        d3
                            .scalePoint()
                            .domain(data.map((d) => d.interval_start))
                            .range([0, width])(d.interval_start),
                    )
                    .y((d) =>
                        y(showNormalized ? d.ICONIC_normalized : d.ICONIC),
                    )
                    .curve(d3.curveMonotoneX),
            );

        // Update ICONIC area
        d3.select(`.area-iconic-${suffix}`)
            .transition()
            .duration(transitionDuration)
            .attr(
                "d",
                d3
                    .area()
                    .x((d) =>
                        d3
                            .scalePoint()
                            .domain(data.map((d) => d.interval_start))
                            .range([0, width])(d.interval_start),
                    )
                    .y0(height)
                    .y1((d) =>
                        y(showNormalized ? d.ICONIC_normalized : d.ICONIC),
                    )
                    .curve(d3.curveMonotoneX),
            );

        // Update EFIT line
        d3.select(`.line-efit-${suffix}`)
            .transition()
            .duration(transitionDuration)
            .attr(
                "d",
                d3
                    .line()
                    .x((d) =>
                        d3
                            .scalePoint()
                            .domain(data.map((d) => d.interval_start))
                            .range([0, width])(d.interval_start),
                    )
                    .y((d) => y(showNormalized ? d.EFIT_normalized : d.EFIT))
                    .curve(d3.curveMonotoneX),
            );

        // Update EFIT area
        d3.select(`.area-efit-${suffix}`)
            .transition()
            .duration(transitionDuration)
            .attr(
                "d",
                d3
                    .area()
                    .x((d) =>
                        d3
                            .scalePoint()
                            .domain(data.map((d) => d.interval_start))
                            .range([0, width])(d.interval_start),
                    )
                    .y0(height)
                    .y1((d) => y(showNormalized ? d.EFIT_normalized : d.EFIT))
                    .curve(d3.curveMonotoneX),
            );
    }

    // Enables mouseover highlight after update lines transition is complete
    function triggerMouseover() {
        const event = new MouseEvent("mouseover");
        const elements = svg.querySelectorAll(
            `.area-iconic-${suffix}, .area-efit-${suffix}`,
        );
        elements.forEach((element) => {
            if (element.matches(":hover")) {
                element.dispatchEvent(event);
            }
        });
    }
</script>

<p class="graph-title">{title}</p>
<div class="svg-container">
    <svg bind:this={svg}></svg>
</div>
<div class="button-container">
    <button
        class={showNormalized ? "button button-on" : "button button-off"}
        on:click={() => {
            showNormalized = !showNormalized;
            updateLines();
            enableMouseEvents = false;
            setTimeout(() => {
                enableMouseEvents = true;
                triggerMouseover();
            }, transitionDuration);
        }}
    >
        Normalized by type of bike
        <!-- {showNormalized ? "Show Raw Data" : "Show Normalized Data"} -->
    </button>
    <button
        class={showNormalized ? "button button-off" : "button button-on"}
        on:click={() => {
            showNormalized = !showNormalized;
            updateLines();
            enableMouseEvents = false;
            setTimeout(() => {
                enableMouseEvents = true;
                triggerMouseover();
            }, transitionDuration);
        }}
    >
        Total number of trips
        <!-- {showNormalized ? "Show Raw Data" : "Show Normalized Data"} -->
    </button>
</div>

<style>
    .svg-container {
        min-width: 420px;
    }
    
    .graph-title {
        font-size: 18px;
        margin-bottom: 10px;
        font-family: RobotoBold;
    }

    .button {
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        color: #333;
        padding: 5px;
        font-size: 12px;
        border-radius: 4px;
        width: 170px;
        cursor: pointer;
        margin-left: 10px;
        transition:
            background-color 0.2s,
            border-color 0.3s;
    }

    .button:hover {
        background-color: #e0e0e0;
        border-color: #bbb;
    }

    /* .button:active {
        background-color: #d0d0d0;
        border-color: #aaa;
    } */

    .button-off {
        opacity: 0.5;
    }
</style>
