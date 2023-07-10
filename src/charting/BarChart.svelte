<script>
    import { scaleLinear } from "d3-scale";
    import data from "/src/data/data.json";
    import "../assets/global-styles.css";

    //export let data;
    export let variable;
    export let yTicks;
    export let colour;

    let width = 100;
    let height = 60;

    var monthList = data.map(function (obj) {
        return obj.Month;
    });

    var variableList = data.map(function (obj) {
        return obj[variable];
    });

    const xTicks = monthList; 
    const padding = { top: 20, right: 25, bottom: 35, left: 15 };

    function formatMobile(tick) {
        return "'" + tick.toString().slice(-2);
    }

     // converts thousands and million to K and M i.e. (1,000 ==> 1K , 1,000,000 ==> 1M)
     function thousandToK(tick) {
        var newtick;
        if (tick >= 1000 && tick < 1000000) {
            newtick = tick / 1000 + "K";
        } else if (tick > 1000000){
            newtick = tick / 1000000 + "M";
        } else{
            newtick = tick
        }
        return newtick;
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


    var barPadding = 10; // controls how much spacing the bars will be from the
</script>

<div
    id="barchart"
    class="chart"
    bind:clientWidth={width}
    bind:clientHeight={height}
>
    <svg width={xTicks.length * barWidth} {height}>
        <!-- this is the year separation lines-->
        <g class="year-tick">
            {#each data as bike, i}
                {#if i % 12 === 0 && i > 0}
                    <line
                        class="year-tick"
                        x1={30 + i * barWidth - barWidth / 2}
                        y1={height - 30}
                        x2={30 + i * barWidth - barWidth / 2}
                        y2={height - 10}
                        stroke="grey"
                    />
                    <line
                        class="year-grid"
                        x1={30 + i * barWidth - barWidth / 2}
                        y1={height - 30}
                        x2={30 + i * barWidth - barWidth / 2}
                        y2={-20}
                        stroke="grey"
                    />
                {/if}
            {/each}
        </g>
        <!-- y axis -->
        <g class="axis y-axis">
            {#each yTicks as tick}
                <g
                    class="tick tick-{tick}"
                    transform="translate(0, {yScale(tick)})"
                >
                    <line x2="100%" />
                    <text y="-4">{thousandToK(tick)} </text>
                </g>
            {/each}
        </g>

        <!-- Second x axis, only appears when the inner window width > 800 -->
        <g class="axis x-axis">
            {#each data as bike, i}
            {#if innerWidth > 800} 
                {#if i % 12 === 0 || (i == 0)} <!-- show the "tick" every 12th bar-->
                    <g class="tick" transform="translate({xScale(i)},{height})">
                        <text x={barWidth / 2 + 40} y="-4"
                            >{bike.Year}</text
                        >
                    </g>
                {/if}
                {/if}
            {/each}
        </g>
        <!--  x axis -->
        <g class="axis x-axis">
            {#each data as bike, i}
                {#if innerWidth > 800} <!-- if the inner window width > 800, show months as label-->
                    <g class="tick" transform="translate({xScale(i)},{height})">
                        <text x={barWidth / 2 + 8} y="-20"
                            >{bike.Month}</text
                        >
                    </g>
                {:else if innerWidth <= 800} <!-- if the inner window width <=800 show years only-->
                    {#if i % 12 === 0 || i == 0}
                        <g
                            class="tick"
                            transform="translate({xScale(i)},{height})"
                        >
                            <text x={barWidth / 2 + 15} y="-20"
                                >{width > 1000
                                    ? bike.Year
                                    : formatMobile(bike.Year)}</text
                            >
                        </g>
                    {/if}
                {/if}
            {/each}
        </g>

        <g class="bars" fill = {colour}>
            {#each data as bike, i}
                <!-- Controls the width of the bar graph, 
				width: controls the spacing between the bars-->
                <rect
                    x={xScale(i)+barPadding}
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
        {selected_datapoint.Year.toString().toLocaleString() +
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
        stroke: var(--brandGray70);
        stroke-width: 0.4px;
    }
    .tick text {
        fill: var(--brandGray70);
        text-anchor: start;
        font-size: 12px;
    }

    .tick.tick-0 line {
        stroke-dasharray: 0;
    }

    .x-axis .tick text {
        text-anchor: middle;
        font-size: 12px;
        text-align: right;

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
    .year-tick {
        stroke-width: 2px;
        z-index: 6;
    }
</style>
