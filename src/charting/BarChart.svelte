<script>

    import {yGrids} from './YGrids.js';

    import data from '/src/data/data.json';
    import { max } from "d3-array";

   // export let type;
    export let variable;
    /*
    let dataAllDates = data.filter(item => item.t === "All").map(({ y, m }) => ({ y, m }));

    var dataTypeSubset;
    $: dataTypeSubset = data.filter(item => item.t === type);
    */

    var dataChart;

    // this code is to find matching records between the dataType Subset in dataAll DAtes
    
    $: dataChart = dataAllDates.map((obj) => {
        const matchingObj = dataTypeSubset.find(
            (o) => o.y === obj.y && o.m === obj.m
        ) || { c: 0, s: 0 };
        console.log(obj.y)
        
        return { ...obj, ...matchingObj };
    });*/

    // find a way to add data to dataChart
    
    dataChart = data


    console.log(dataChart)

    console.log(data)
    var monthList = data.map(function (obj) {
		return obj.Month;
	});

    var yearList = data.map(function (obj) {
		return obj.Year;
	});

    

    var maxValue;
    $: maxValue = max((item) => item[variable]);
    
    console.log(maxValue);

    
    let divWidth;    
    
    $: svgWidth = divWidth;
    $: svgHeight = svgWidth / 2;

    $: barSpacing = (svgWidth - 55) / 60

    let grids;
    $: grids = yGrids(maxValue);
    $: console.log(grids);

    let selected_datapoint = undefined;
	let mouse_x, mouse_y;
	const setMousePosition = function (event) {
		mouse_x = event.clientX;
		mouse_y = event.clientY;
	};

      
</script>


<div id="barChart" bind:offsetWidth={divWidth}>

    <svg height={svgHeight} width={svgWidth} id="svgChart">

        <!-- <line x1="{5}" y1="{svgHeight - 40}" x2="{svgWidth - 5}" y2="{svgHeight - 40}" stroke="white" /> -->
        
        
        {#each dataChart as d, index}
            <!-- label Years in June-->
            {#if index % 6 === 0 && index % 12 !== 0}
                <text 
                    class="label" 
                    x = "{10 + index * barSpacing - barSpacing /2}" 
                    y = "{svgHeight - 25}"
                >{d.y}</text>
            {/if}

            <!-- Add a thick separation tick between each year-->
            {#if index % 12 === 0 && index > 0}
                <line class="year-tick" x1="{50 + index * barSpacing - barSpacing/2}" y1="{svgHeight - 30}" x2="{50 + index * barSpacing - barSpacing/2}" y2="{svgHeight - 40}" stroke="white" />

                <line class="year-grid" x1="{50 + index * barSpacing - barSpacing/2}" y1="{svgHeight - 30}" x2="{50 + index * barSpacing - barSpacing/2}" y2="{0}" stroke="gray" />
            {/if}


            {#if d[variable] > 0}
                <g>
                    <line 
                    class="bar-line" 
                    x1="{50 + index * barSpacing}" 
                    y1="{(svgHeight - 40) * (1 - d[variable] / maxValue)}" 
                    x2="{50 + index * barSpacing}" 
                    y2="{svgHeight - 40}"  
                    on:mouseover={(event) => {
                        selected_datapoint = d;
                        setMousePosition(event);
                    }}
                    on:mouseout={() => {
                        selected_datapoint = undefined;
                    }}
                    />
                </g>
            {/if}

        {/each}
        

        {#each grids as grid}

            <line class="amount-grid" 
                x1="{5}" 
                y1="{0 + (svgHeight - 40) * (1 - grid / maxValue)}" 
                x2="{svgWidth - 5}" 
                y2="{0 + (svgHeight - 40) * (1 - grid / maxValue)}"
            />

            {#if grid !== 0}
                <text 
                        class="labelY" 
                        x = "35" 
                        y = "{10 + (svgHeight - 40) * (1 - grid / maxValue)}" 
                    >{grid}</text>
            {/if}

        {/each}

        <line x1="{5}" y1="{svgHeight - 40}" x2="{svgWidth - 5}" y2="{svgHeight - 40}" stroke="white" />
 
    </svg>

</div>

{#if selected_datapoint != undefined}
    <div id="tooltip" style="left: {mouse_x}px; top: {mouse_y - 25}px">
        {selected_datapoint.Year.toLocaleString() + "/" + selected_datapoint.Month.toLocaleString() + ": " +  selected_datapoint[variable].toLocaleString()}
    </div>
{/if}



<style>
    
    #barChart {
        margin: 0 auto;
        max-width: 820px;
        min-width: 375px;
    }

    #svgChart {
        background-color: var(--brandGray90);
    }


    .bar-line {
        stroke: var(--brandRed);
        stroke-width: 5;
        cursor: pointer;
    }
    .bar-line:hover {
        stroke: var(--brandWhite);
    }

    .label {
        fill: var(--brandWhite);
        font-size: 12px;
        text-anchor: middle;
    }
    .labelY {
        fill: var(--brandGray);
        font-size: 12px;
        text-anchor: end;
    }

    .year-grid {
        stroke: var(--brandGray);
    }
    .amount-grid {
        stroke: var(--brandGray70);
        stroke-width: 1; 
    }

    #tooltip {
		position: fixed;
		color: white;
        background-color: var(--brandGray90);
		font-family: Roboto, sans-serif;
		font-size: 12px;
        border: solid 1px var(--brandGray);
        border-radius: 4px;
        padding: 5px;
	}

</style>
