<script>
	import { LayerCake, Svg, Html } from "layercake";
	import Bar from "./Bar.svelte";
	import AxisX from "./AxisX.svelte";
	import AxisY from "./AxisY.svelte";
	import Tooltip from "./Tooltip.html.svelte";
	import { scaleBand } from "d3-scale";
	export let data;
	
	export let xKey;
	export let  yKey;
	export let colour;
	

	let xTipLabel = xKey;
	let yTipLabel = yKey


	data.forEach((d) => {
	  d[xKey] = +d[xKey];
	});


	let evt;
	let hideTooltip = false;
  </script>

	  <div id="chart-container">
		<LayerCake
		  padding={{ top: 20, bottom: 80, left: 60, right:40 }}
		  x={xKey}
		  y={yKey}
		  yScale={scaleBand().paddingInner([0.15])}
		  xDomain={[0, null]}
		  data={data}
		>
		  <Svg>
			<AxisX gridlines={true} baseline={true} snapTicks={true} ticks="4" />
			<AxisY gridlines={false} />
			<Bar 
				on:mousemove={event => evt = hideTooltip = event}
				on:mouseout={() => (hideTooltip = true)}
				fill = {colour}
			/>
		  </Svg>
		  <Html
			pointerEvents={false}
		  >
		  {#if hideTooltip !== true}
			<Tooltip
			  {evt}
			  let:detail
			>
			{@const tooltipData = { ...detail.props }}
				  <div class="row">{tooltipData[yTipLabel]}:    {tooltipData[xTipLabel]}</div>
			</Tooltip>
		{/if}
	  </Html>
		</LayerCake>
	  </div>
  <style>
	#chart-container {
	  width: 80%;
	  height: 1200px;
	  padding-left: 10%;
	}
<<<<<<< HEAD
  </style>
=======

	$: xScale = scaleLinear()
		.domain([0, xTicks.length])
		.range([padding.left, width - padding.right]);

	$: yScale = scaleLinear()
		.domain([0, Math.max.apply(null, yTicks)])
		.range([height - padding.bottom, padding.top]);

	$: innerWidth = width - (padding.left + padding.right);

	$: barWidth = innerWidth / xTicks.length;
</script>

<div class="chart" bind:clientWidth={width} bind:clientHeight={height}>
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
		<g class="x-axis">
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
>>>>>>> 06e8560fe931a7b95aa745725fadd0878608d812
