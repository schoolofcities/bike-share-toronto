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
  </style>