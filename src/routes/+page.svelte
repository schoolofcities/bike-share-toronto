<script>
	import "../assets/global-styles.css";
	import bikeshareData from "/src/data/data.json"; //importing bikeshare data
	import Chart from "chart.js/auto";
	import { onMount } from "svelte";

	// returns a list of years for the x axis

	let trip = "TripCount";
	let stationCount = "StationCount";
	let bikeCount = "BikeCount";
	let averageTripDuration = "AverageTripDuration";
	let AverageBikeUsage = "AverageBikeUsage";
	let AverageStationUsage = "AverageStationUsage";

	const yTicksStation = [0, 100, 200, 300, 400, 500, 600, 700];
	const yTicksTrip = [
		0, 100000, 200000, 300000, 400000, 500000, 600000, 700000,
	];
	const yTicksBike = [0, 2500, 3500, 4500, 5500, 6500];
	const yTicksDuration = [0, 5, 10, 15, 20, 25, 30];

	const yTicksBikeUsage = [0, 0, 40, 60, 80, 100];
	const yTicksStationUsage = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600];
	// formats the numbers when it is shown on mobile i.e. 2007 --> '07'

	let chartValues = [20, 10, 5, 2, 20, 30, 45];
	let chartLabels = [
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
	];
	let ctx;
	let chartCanvas;

	onMount(async () => {
		ctx = chartCanvas.getContext("2d");
		const chart = new Chart(ctx, {
			type: "line",
			data: {
				labels: chartLabels,
				datasets: [
					{
						label: "Revenue",
						backgroundColor: "rgb(255, 99, 132)",
						borderColor: "rgb(255, 99, 132)",
						data: chartValues,
					},
				],
			},
		});
	});
</script>

<canvas bind:this={chartCanvas} id="myChart" />

<style>
	canvas {
		height: 400px;
		width: 80%;
	}
</style>
