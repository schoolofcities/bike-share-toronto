<script>
	import { scaleLinear } from "d3-scale";
	import * as d3 from 'd3';

	export let data;
	export let variable;
	export let yTicks;

	let width = 100;
	let height = 2000;

	var monthList = data.map(function (obj) {
		return obj.Month;
	});

	const xTicks = monthList;
	const padding = { top: 20, right: 15, bottom: 20, left: 25 };

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



</script>

<div id = "barchart" class="chart" bind:clientWidth={width} bind:clientHeight={height}>
	<svg width={xTicks.length * barWidth} height={height}>
		<!-- y axis -->
		<g class="axis y-axis">
			{#each yTicks as tick}
				<g class="tick tick-{tick}" transform="translate(0, {yScale(tick)})">
					<line x2="100%" />
					<text y="-4">{tick} </text>
				</g>
			{/each}
		</g>

		<!-- x axis -->
		<g class="axis x-axis">
			{#each data as bike, i}
				<g class="tick" transform="translate({xScale(i)},{height})">
					<text x={barWidth / 2 + 10} y="-4">{width > 380 ? bike.Month : formatMobile(bike.Month)}</text>
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
				/>
			{/each}
		</g>

		<!-- Bar Labels  -->
		<g id = "bars" class="x-axis">
			{#each data as bike, i}
				<g class="tick" transform="translate({xScale(i) + barWidth / 2 + 25},{yScale(bike[variable]) + 22})">
					<text class="x-label">{width > 380 ? bike[variable] : formatMobile(bike[variable])}</text>
				</g>
			{/each}
		</g>
	</svg>
</div>




<style>
	.chart {
		width: 100%;
		max-width: 80%;
		margin: 0 auto;
		overflow-x: scroll;
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
		stroke: #404b
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
	}

	.x-label {
		text-anchor: middle;
		transform: translate(-10px, 0px) rotate(-90deg);
		
	}
	.x-label.tick text{
		font-size: 10px; /* Adjust the font size as desired */
		fill: #000000; /* Adjust the font color as desired */
	}

	.bars rect {
		fill: #ABA89E;
		stroke: none;
		opacity: 0.65;
	}
</style>
