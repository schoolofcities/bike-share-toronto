<script>
    import { scaleLinear } from "d3-scale";

    export let data;
    export let variable;
    export let yTicks;

    let width = 1000;
	let height = 1000;

    var monthList = data.map(function (obj) {
		return obj.Month;
	}); 

    const xTicks = monthList;
	const padding = { top: 20, right: 15, bottom: 20, left: 25 };

    

    function formatMobile(tick) {
        return "'" + tick.toString().slice(-2);
    }
    console.log(xTicks);
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
	<svg>
		<!-- y axis -->
		<g class="axis y-axis">
			{#each yTicks as tick}
				<g
					class="tick tick-{tick}"
					transform="translate(0, {yScale(tick)})"
				>
					<line x2="100%" />
					<text y="-4"
						>{tick}
						</text
					>
				</g>
			{/each}
		</g>

		<!-- x axis -->
		<g class="axis x-axis">
			{#each data as bike, i}
				<g class="tick" transform="translate({xScale(i)},{height})">
					<text x={barWidth / 2} y="-4"
						>{width > 380
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
					x={xScale(i) + 0}
					y={yScale(bike[variable])}
					width={barWidth - 1}
					height={yScale(0) - yScale(bike[variable])}
				/>
			{/each}
		</g>
	</svg>
</div>
<style>
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
		font-size: 0.725em;
		font-weight: 200;
	}
	

	.tick line {
		stroke: Gray;
		stroke-dasharray: 2;
	}

	.tick text {
		fill: #ccc;
		text-anchor: start;
		font-size: 15px;
	}

	.tick.tick-0 line {
		stroke-dasharray: 0;
	}

	.x-axis .tick text {
		text-anchor: middle;
	}

	.x-axis.label{
		font-family: Helvetica, Arial;
		font-size: 0.725em;
		font-weight: 200;
		writing-mode: vertical-rl; /* Rotate 90 degrees */
  		transform: rotate(180deg); /* Flip vertically */
		font-size: 50px;
	}

	.bars rect {
		fill: #006C00;
		stroke: none;
		opacity: 0.65;
	}
</style>