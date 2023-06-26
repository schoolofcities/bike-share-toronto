<script>

	import "../assets/global-styles.css";
	import BarChart from "/src/routes/BarChart.svelte";

	import bikeshareData from "/src/data/data.json"; //importing bikeshare data


	// returns a list of years for the x axis

	let trip = "TripCount";
	let stationCount = "StationCount";
	let bikeCount = "BikeCount";
	let averageTripDuration = "AverageTripDuration";
	let AverageBikeUsage = "AverageBikeUsage"
  	let AverageStationUsage = "AverageStationUsage"
	const yTicksStation = [0, 100, 200, 300, 400, 500, 600, 700];
	const yTicksTrip = [
		0, 100000, 200000, 300000, 400000, 500000, 600000, 700000,
	];
	const yTicksBike = [0, 2500, 3500, 4500, 5500, 6500];
	const yTicksDuration = [0, 5, 10, 15, 20, 25, 30];
	const yTicksBikeUsage = [0, 0, 40, 60, 80, 100]
	const yTicksStationUsage = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600]
	// formats the numbers when it is shown on mobile i.e. 2007 --> '07
</script>

<h1> Toronto Bikeshare Usage Since 2017</h1>

<img src ="https://github.com/schoolofcities/bike-share-toronto/blob/main/IMG_2140.jpg">

<h2>Trip Count by Month 2017 - 2023</h2>
<BarChart data = {bikeshareData} xKey = "TripCount" yKey = "YearMonth" colour = "blue"/>
<BarChart data = {bikeshareData} xKey = "StationCount" yKey = "YearMonth" colour = "green"/>
<BarChart data = {bikeshareData} xKey = "BikeCount" yKey = "YearMonth" colour = "orange"/>


<style>
	:global(body) {
		margin: 0px;
		background-color: #f8f6f0;
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
		padding-left: 10%;
		padding-right: 10%;
	}

	p {
		/* should pick a consistent font here probably */
		font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
			Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue",
			sans-serif;
		color: var(--brandBlack);
		text-align: left;
		padding-left: 10%;
		padding-right: 10%;
	}

	h2 {
		text-align: center;
		color: "blue";
	}
</style>


