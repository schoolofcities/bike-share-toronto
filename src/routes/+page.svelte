<script>
	import { scaleLinear } from "d3-scale";
	import "../assets/global-styles.css";
	import BarChart from "/src/routes/BarChart.svelte";

	import bikeshareData from "/src/data/data1.json"; //importing bikeshare data

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
	const yTicksDuration = [0, 5, 10, 15, 20, 25];

	const yTicksBikeUsage = [0, 10, 20, 30, 40, 50, 60,70,80, 90,100, 110]
	const yTicksStationUsage = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600]
	// formats the numbers when it is shown on mobile i.e. 2007 --> '07
</script>

<h1>A City on Bikes: The Growth Story of Bike Share Toronto</h1>
<h2>A Brief History</h2>
<p>
	edited: Bike Share Toronto is a bicycle-sharing system in Toronto, Canada.
	The system consists of 6850 bicycles and 625 stations, and covers over 200
	square kilometres (80 square miles) of the city, from Finch Avenue in the
	north, Rouge Park in the east, Lake Ontario to the south, and to Long Branch
	to the west.[1][2] Bike Share Toronto recorded 3,575,000 trips in 2021.[3]
	The system was launched in 2011 by PBSC Urban Solutions under the BIXI brand
	and was taken over by the Toronto Parking Authority in 2014. (Copied from
	Wikepedia, only for testing)
</p>

<h1>Rapidly Expanding Service</h1>

<h2>Trip Count by Month 2017 - 2023</h2>
<BarChart data={bikeshareData} variable={trip} yTicks={yTicksTrip} />
<p>
	The number of trips have increased over the years
</p>
<h2>Station Count by Month 2017 - 2023</h2>
<BarChart data={bikeshareData} variable={stationCount} yTicks={yTicksStation} />
<h2>Average Station Usage (Trips Per Station) by Month 2017 - 2023</h2>
<BarChart data={bikeshareData} variable={AverageStationUsage} yTicks={yTicksStationUsage}/>


<h2>Bike Count by Month 2017 - 2023</h2>
<BarChart data={bikeshareData} variable={bikeCount} yTicks={yTicksBike} />
<h2>Average Bike Usage (Trips Per Bike) by Month 2017 - 2023</h2>
<BarChart data={bikeshareData} variable={AverageBikeUsage} yTicks={yTicksBikeUsage}/>




<h2>Average Trip Duration by Month 2017 - 2023</h2>
<BarChart data={bikeshareData} variable={averageTripDuration} yTicks={yTicksDuration}/>



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
