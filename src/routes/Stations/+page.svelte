<script>
	import Top from "/src/CommonFormatting/TopSofC.svelte";
	import Nav from "/src/CommonFormatting/Nav.svelte"
	import "/src/assets/global-styles.css";
	import data from "/src/data/data.json";
	import Chart from "/src/charting/chart.svelte";
	import BarChart from "/src/charting/BarChart.svelte";
	import BarChart2 from "/src/charting/BarChart2.svelte";

	let yTicksTrip = [
		0, 100000, 200000, 300000, 400000, 500000, 600000, 700000,
	];
	let yTicksStation = [0, 100, 200, 300, 400, 500, 600, 700];
	let yTicksAvStation = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600];
	let yTicksBike = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000];
	let yTicksAvBikeUsage = [0, 20, 40, 60, 80, 100, 120];
	let yTicksDuration = [0, 10, 20, 30];
</script>

<Top />

<Nav/>
<h1>Toronto on Bikes: Bikeshare Usage Since 2017</h1>
<p><b>Prepared by: Michael Liu | July 2023</b></p>


<h1>Rapidly Expanding Service</h1>
<h2>Station Count by Month 2017 - 2023</h2>
<BarChart variable="StationCount" yTicks={yTicksStation} colour="#0D534D" />
<p>
	The Bikeshare system has been expanding, with 200 stations in 2017 and 659
	stations in 2023. The data is btained by counting the number of unique
	station IDs each month. Based on what is shown from the data, major epansion
	usually happens in June and July. It is also interesting to observe small
	fluctions in the number of stations. It is likely due to constructions
	happening in various parts of the city, causing the stations to be
	temporarily removed.
</p>

<h2>Average Station Usage by Month 2017 - 2023</h2>
<BarChart
	variable="AverageStationUsage"
	yTicks={yTicksAvStation}
	colour="#007FA3"
/>

<p>
	Average station useage is calculated by dividing the number of trips per
	month by the number of bike station per month.
</p>


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
		font-family: "Helvetica Neue", Arial, sans-serif;
		font-weight: bolder;
		font-size: 35px;

		color: var(--brandDarkGreen);
		padding-left: 20%;
		padding-right: 20%;
		padding-top: 10px;
	}

	p {
		/* should pick a consistent font here probably */
		font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
			Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue",
			sans-serif;
		color: #4d4d4d;
		text-align: left;
		padding-left: 20%;
		padding-right: 20%;
		padding-bottom: 5px;
		padding-top: 5px;
		line-height: 150%;
		font-size: 15px;
	}

	h2 {
		text-align: left;
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		font-weight: bold;
		color: "blue";
		color: var(--brandYellow);
		padding-left: 20%;
		padding-right: 20%;
		padding-top: 20px;
	}

	nav {
		position: relative;
		display: flex;
		gap: 1em;
		padding: 1em;
		background: var(--brandGray70);
		z-index: 2;
		margin: 0 0 1em 0;
		
	}

	nav a {
		text-decoration: none;
		color: white;
	}

	nav a[aria-current="true"] {
		border-bottom: 2px solid;
	}

	@media screen and (max-width: 1300px) {
		h1 {
			font-size: 35px;
			padding-left: 5%;
			padding-right: 5%;
			padding-top: 5px;
		}

		p {
			/* should pick a consistent font here probably */
			padding-left: 5%;
			padding-right: 5%;
			padding-bottom: 5px;
		}

		h2 {
			padding-left: 5%;
			padding-right: 5%;
			padding-top: 0px;
		}
	}
	@media screen and (max-width: 415px) {
		h1 {
			font-size: 25px;
			padding-left: 5%;
			padding-right: 5%;
			padding-top: 5px;
		}
		h2 {
			font-size: 20px;
		}
	}
</style>
