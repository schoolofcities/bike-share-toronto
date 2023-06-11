
<script>
	import { scaleLinear } from 'd3-scale';
    import "../assets/global-styles.css";

    import bikeshareData from '/src/data/data.json' //importing bikeshare data

    // returns a list of years for the x axis
    var yearList = bikeshareData.map(function(obj){
        return obj.Year
    });
	var monthList = bikeshareData.map(function(obj){
        return obj.Month
    });
    var tripCounList = bikeshareData.map(function(obj){
        return obj.TripCount
    });

    console.log([...new Set(yearList)])

    console.log() //[...new Set(yearList)] helps removes duplicates in the list
	const xTicks = monthList;
	const yTicks = [0, 100, 200, 300, 400, 500, 600, 700];
	const padding = { top: 20, right: 15, bottom: 20, left: 25 };

	let width = 1000;
	let height = 1000;

	// formats the numbers when it is shown on mobile i.e. 2007 --> '07
	function formatMobile(tick) {
		return "'" + tick.toString().slice(-2);
	}
    console.log(xTicks)
	$: xScale = scaleLinear()
		.domain([0, xTicks.length])
		.range([padding.left, width - padding.right]);

	$: yScale = scaleLinear()
		.domain([0, Math.max.apply(null, yTicks)])
		.range([height - padding.bottom, padding.top]);

	$: innerWidth = width - (padding.left + padding.right);
    
	$: barWidth = innerWidth / xTicks.length;
</script>

<h2>Bikeshare Station Count By Month 2017 - 2022</h2>

<div class="chart" bind:clientWidth={width} bind:clientHeight={height}>
	<svg>
		<!-- y axis -->
		<g class="axis y-axis">
			{#each yTicks as tick}
				<g class="tick tick-{tick}" transform="translate(0, {yScale(tick)})">
					<line x2="100%"></line>
					<text y="-4">{tick} {tick === 20 ? ' per 1,000 population' : ''}</text>
				</g>
			{/each}
		</g>
        
		<!-- x axis -->
		<g class="axis x-axis">
			{#each bikeshareData as bike, i}
				<g class="tick" transform="translate({xScale(i)},{height})">
					<text x="{barWidth/2}" y="-4">{width > 380 ? bike.Month : formatMobile(bike.Month)}</text>
				</g>
			{/each}
		</g>

		<g class='bars'>
			{#each bikeshareData as bike, i}
			<!-- Controls the width of the bar graph, 
				width: controls the spacing between the bars-->
				<rect
					x="{xScale(i) + 0}"
					y="{yScale(bike.StationCount)}"
					width="{barWidth-1}" 
					height="{yScale(0) - yScale(bike.StationCount)}"
				></rect>
			{/each}
		</g>
	</svg>
</div>

<main>
    <h1>A City on Bikes: The Growth Story of Bike Share Toronto</h1>

    <p>Charts and text on the growth of bike share ridership in Toronto</p>
    <h1> A Brief History </h1>
    <p>  edited: Bike Share Toronto is a bicycle-sharing system in Toronto, Canada. The system consists of 6850 bicycles and 625 stations, and covers over 200 square kilometres (80 square miles) of the city, from Finch Avenue in the north, Rouge Park in the east, Lake Ontario to the south, and to Long Branch to the west.[1][2] Bike Share Toronto recorded 3,575,000 trips in 2021.[3] The system was launched in 2011 by PBSC Urban Solutions under the BIXI brand and was taken over by the Toronto Parking Authority in 2014. (Copied from Wikepedia, only for testing)</p>
    <p> </p>
</main>



<style>
    :global(body) {
            margin: 0px;
            background-color: var(--brandWhite);
	}

	main {
		text-align: center;
		padding: 0px;
		margin: 0px;
	}

    h1 {
        font-family: TradeGothicBold, sans-serif;
        font-size: 35px;
        font-weight: normal;
        color: var(--brandYellow);
    }

    p { 
        /* should pick a consistent font here probably */
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        color: var(--brandBlack);
        text-align: left;
        padding-left: 10%;
        padding-right: 10%;
    }


    h2 {
		text-align: center;
        color: 'blue';
	}

	.chart {
		width: 100%;
		max-width: 80%;
		margin: 0 auto;
	}

	svg {
		position: relative;
		width: 100%;
		height: 300px;
	}

	.tick {
		font-family: Helvetica, Arial;
		font-size: .725em;
		font-weight: 200;
	}

	.tick line {
		stroke: red;
		stroke-dasharray: 2;
	}

	.tick text {
		fill: #ccc;
		text-anchor: start;
		font-size: 8px;
	}

	.tick.tick-0 line {
		stroke-dasharray: 0;
	}

	.x-axis .tick text {
		text-anchor: middle;
	}

	.bars rect {
		fill: #a11;
		stroke: none;
		opacity: 0.65;
	}
</style>