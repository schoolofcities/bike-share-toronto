<script>
    import { scaleLinear } from "d3-scale";

    var data = [
        { "Year": 2015, "Ridership": 667000},
        { "Year": 2016, "Ridership": 834235},
        { "Year": 2017, "Ridership": 1510802},
        { "Year": 2018, "Ridership": 1975384},
        { "Year": 2019, "Ridership": 2400384},
        { "Year": 2020, "Ridership": 2900000},
        { "Year": 2021, "Ridership": 3575000},
        { "Year": 2022,	"Ridership": 4600000}
]
    let variable = "Ridership"
    let yTicks = [0, 500000, 1500000,2500000, 3500000, 4500000]
    let width = 100;
    let height = 30;


    var yearList = data.map(function (obj) {
        return obj.Year;
    });

    const xTicks = yearList; // label the x axis with years
    const padding = { top: 20, right: 35, bottom: 35, left: 25 };

    function formatMobile(tick) {
        return "'" + tick.toString().slice(-2);
    }

    // converts thousands and million to K and M i.e. (1,000 ==> 1K , 1,000,000 ==> 1M)
    function thousandToK(tick) {
        var newtick;
        if (tick > 1000 && tick < 1000000) {
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
        .range([padding.left, width - padding.right-20]);

    $: yScale = scaleLinear()
        .domain([0, Math.max.apply(null, yTicks)])
        .range([height - padding.bottom, padding.top]);

    $: innerWidth = width - (padding.left + padding.right);

    $: barWidth = innerWidth / xTicks.length -10;

    let selected_datapoint = undefined;

    let mouse_x, mouse_y;
    const setMousePosition = function (event) {
        mouse_x = event.clientX;
        mouse_y = event.clientY;
    };

    console.log(height);
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
                    <text y="-4">{thousandToK(tick)} </text>
                </g>
            {/each}
        </g>

        <g class="axis x-axis">
            {#each data as bike, i}
                <g class="tick" transform="translate({xScale(i)},{height})">
                    <text x={barWidth / 2 + 48} y="-20"
                        >{width > 500
                            ? bike.Year
                            : formatMobile(bike.Year)}</text
                    >
                </g>
            {/each}
        </g>
    

        <g class="bars">
            {#each data as bike, i}
                <!-- Controls the width of the bar graph, 
				width: controls the spacing between the bars-->
                <rect
                    x={xScale(i) + 50}
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
                />
            {/each}
        </g>
    </svg>
</div>

<!-- tooltip-->
{#if selected_datapoint != undefined}
    <div id="tooltip" style="left: {mouse_x}px; top: {mouse_y - 25}px">
        {selected_datapoint.Year.toString().toLocaleString() + // set year as the label
            " : " +
            selected_datapoint[variable].toLocaleString()} <!--set variable as the number it returns-->

    </div>
{/if}

<style>
    .chart {
        width: 100%;
        max-width: 30%;
        margin: 0 auto;
    }

    svg {
        position: relative;
        width: 100%;
        height: 300px;
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
