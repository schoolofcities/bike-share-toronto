<script>
    import { scaleLinear } from "d3-scale";
    import data from "/src/data/data.json";
    import "../assets/global-styles.css";

    //export let data;
    export let variable;
    export let yTicks;
    export let colour;
    export let maxHeight;
    export let type;

    let width = 100;
    let height = 60;

    $: height = Math.min(width / 2.42, maxHeight);

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

    $: barWidth = Math.max(Math.min(innerWidth / xTicks.length, 9),5);

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
>
    <svg width={xTicks.length * barWidth} {height}>
        <!-- this is the year separation lines-->
        <g class="year-tick">
            {#each data as bike, i}
                {#if i % 12 === 0 && i > 0}
                    
                    <line
                        class="year-grid"
                        x1={xScale(i)+barPadding/2}
                        y1={height - 3}
                        x2={xScale(i)+barPadding/2}
                        y2={0}
                        stroke-width={1}
                        stroke="#fff"
                        stroke-dasharray="5 3"
                        opacity=0.7
                    />
                {/if}
            {/each}
        </g>
        

        <!-- Second x axis, only appears when the inner window width > 800 -->
        <g class="axis x-axis">
            {#each data as bike, i}
            {#if innerWidth > 800} 
                {#if i % 12 === 0 || (i == 0)} <!-- show the "tick" every 12th bar-->
                    <g class="tick" transform="translate({xScale(i)},{height})">
                        <text x={barWidth / 2 + 20} y="-4"
                            >{bike.Year}</text
                        >
                    </g>
                {/if}
                {/if}
            {/each}
        </g>
        <!--  x axis - monthly-->
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

        {#if type === "bar"}
            <g>
                {#each data as bike, i}
                    <!-- Controls the width of the bar graph, 
                    width: controls the spacing between the bars-->
                    <rect class="bar"
                        x={xScale(i)+barPadding}
                        y={yScale(bike[variable])}
                        width={barWidth - 2}
                        height={yScale(0) - yScale(bike[variable])}
                        on:mouseover={(event) => {
                            selected_datapoint = bike;
                            setMousePosition(event);
                        }}
                        on:mouseout={() => {
                            selected_datapoint = undefined;
                        }}
                        color="white"
                    />

                    <rect class="tip"
                        x={xScale(i)+barPadding}
                        y={yScale(bike[variable]) + 0}
                        width={barWidth - 2}
                        height={8}
                    />

                    
                    
                {/each}
                
            </g>
        {/if}

        {#if type === "line"}
            <g>
                {#each data as bike, i}

                    {#if i > 0 && bike[variable] !== null}
                        <line
                        x1={barWidth - 2 + xScale(i - 1) + barPadding}
                        y1={yScale(data[i - 1][variable])}
                        x2={barWidth - 2 + xScale(i) + barPadding}
                        y2={yScale(bike[variable])}
                        stroke="#F1C500"
                        stroke-width="2"
                        />
                    {/if}

                    {#if bike[variable] !== null}
                    <circle class="point"
                        r = 4
                        cx={barWidth - 2 + xScale(i)+barPadding}
                        cy={yScale(bike[variable])}
                        fill="#F1C500" 
                    />
                    {/if}

                    

                {/each}
            </g>
        {/if}


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
        max-width: 100%;
        
        margin: 0 auto;
    }

    svg {
        position: relative;
        width: 100%;
    }

    .tick {
        font-family: Helvetica, Arial;
        font-size: 0.725em;
        font-weight: 200;
    }

    .tick line {
        stroke: var(--brandGray);
        stroke-width: 1px;
        opacity: 0.1;
    }
    .tick text {
        fill: var(--brandGray);
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

    .bar {
        stroke: var(--brandDarkGreen);
        stroke-width: 1px;
        stroke-opacity: 1;
        fill: var(--brandWhite);
        cursor: pointer;
    }
    .bar:hover {
        fill: var(--brandLightBlue);
    }
    .tip {
        stroke: var(--brandDarkGreen);
        stroke-width: 1px;
        fill: var(--brandYellow);
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

    .point {
        r: 4px;
    }
</style>
