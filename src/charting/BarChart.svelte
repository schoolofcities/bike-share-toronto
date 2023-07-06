<script>
    import { scaleLinear } from "d3-scale";
    import data from "/src/data/data.json";

    //export let data;
    export let variable;
    export let yTicks;

    let width = 100;
    let height = 30;

    var monthList = data.map(function (obj) {
        return obj.Month;
    });
    var yearList = data.map(function (obj) {
        return obj.Year;
    });

    const xTicks = monthList;
    const padding = { top: 20, right: 15, bottom: 35, left: 25 };

    function formatMobile(tick) {
        return "'" + tick.toString().slice(-2);
    }

    $: xScale = scaleLinear()
        .domain([0, xTicks.length])
        .range([padding.left, width - padding.right]);

    $: yScale = scaleLinear()
        .domain([0, Math.max.apply(null, yTicks)])
        .range([height - padding.bottom, padding.top]);

    $: innerWidth = width - (padding.left + padding.right);

    $: barWidth = innerWidth / xTicks.length;

    let selected_datapoint = undefined;

    let mouse_x, mouse_y;
    const setMousePosition = function (event) {
        mouse_x = event.clientX;
        mouse_y = event.clientY;
    };

    console.log(height)
</script>

<div
    id="barchart"
    class="chart"
    bind:clientWidth={width}
    bind:clientHeight={height}
>
    <svg width={xTicks.length * barWidth} {height}>
        <!-- y axis -->
        <g class="axis y-axis">
            {#each yTicks as tick}
                <g
                    class="tick tick-{tick}"
                    transform="translate(0, {yScale(tick)})"
                >
                    <line x2="100%" />
                    <text y="-4">{tick} </text>
                </g>
            {/each}
        </g>

        <!-- Second x axis -->
        <g class="axis x-axis">
            {#each data as bike, i}
                <g class="tick" transform="translate({xScale(i)},{height})">
                    <text x={barWidth / 2 + 8} y="-4"
                        >{width > 500
                            ? bike.Year-2000
                            : formatMobile(bike.Year)}</text
                    >
                </g>
            {/each}
        </g>
        <!--  x axis -->
        <g class="axis x-axis">
            {#each data as bike, i}
                <g class="tick" transform="translate({xScale(i)},{height})">
                    <text x={barWidth / 2 + 8} y="-20"
                        >{width > 500
                            ? bike.Month
                            : formatMobile(bike.Month)}</text
                    >
                </g>
            {/each}
        </g>


        <g class="bars">
            {#each data as bike, i}
                <!-- Controls the width of the bar graph, 
				width: controls the spacing between the bars-->
                <rect
                    x={xScale(i) + 10}
                    y={yScale(bike[variable])}
                    width={barWidth - 1}
                    height={yScale(0) - yScale(bike[variable])}
                    on:mouseover={(event) => {
                        selected_datapoint = bike;
                        setMousePosition(event);
                    }}
                    on:mouseout={() => {
                        selected_datapoint = undefined;
                    }}
                />
            {/each}
        </g>
    </svg>
</div>
{#if selected_datapoint != undefined}
    <div id="tooltip" style="left: {mouse_x}px; top: {mouse_y - 25}px">
        {selected_datapoint.Year.toLocaleString() +
            "/" +
            selected_datapoint.Month.toLocaleString() +
            ": " +
            selected_datapoint[variable].toLocaleString()}
    </div>
{/if}

<style>
    .chart {
        width: 100%;
        max-width: 80%;
        margin: 0 auto;
    }

    svg {
        position: relative;
        width: 100%;
        height: 500px;
    }

    .tick {
        font-family: Helvetica, Arial;
        font-size: 0.725em;
        font-weight: 200;
    }

    .tick line {
        stroke: #404b;
        stroke-width: 3px;
    }
    .tick text {
        fill: #4b4b4b;
        text-anchor: start;
        font-size: 15px;
    }

    .tick.tick-0 line {
        stroke-dasharray: 0;
    }

    .x-axis .tick text {
        text-anchor: middle;
        font-size: 15px;
    }

    .x-label {
        text-anchor: middle;
        transform: translate(-10px, 0px) rotate(-90deg);
    }
    .x-label.tick text {
        font-size: 20px; /* Adjust the font size as desired */
        fill: #000000; /* Adjust the font color as desired */
    }

    .bars rect {
        fill: #aba89e;
        stroke: none;
        opacity: 0.65;
    }
    .bars rect:hover {
        stroke: red;
    }
    #tooltip {
        position: fixed;
        color: white;
        background-color: black;
        font-family: Roboto, sans-serif;
        font-size: 20px;
        border: solid 1px var(--brandGray);
        border-radius: 4px;
        padding: 5px;
    }
    
</style>
