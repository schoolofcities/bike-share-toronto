<script>
	import { scaleLinear } from "d3-scale";
	import "../assets/global-styles.css";
	import BarChart from "/src/routes/BarChart.svelte";

	import bikeshareData from "/src/data/data.json"; //importing bikeshare data

	// returns a list of years for the x axis

  let trip = "TripCount"
  let stationCount = "StationCount"
  let bikeCount = "BikeCount"
  let averageTripDuration = "AverageTripDuration"

	const yTicksStation = [0, 100, 200, 300, 400, 500, 600, 700];
	const yTicksTrip = [0, 100000, 200000, 300000, 400000, 500000, 600000, 700000];
	const yTicksBike = [0, 2500, 3500, 4500, 5500, 6500]
  const yTicksDuration = [0,5,10,15,20,25, 30]
	// formats the numbers when it is shown on mobile i.e. 2007 --> '07
	
</script>
<BarChart data = {bikeshareData} variable = {trip} yTicks = {yTicksTrip}/>
<BarChart data = {bikeshareData} variable = {stationCount} yTicks = {yTicksStation}/>
<BarChart data = {bikeshareData} variable = {bikeCount} yTicks = {yTicksBike}/>
<BarChart data = {bikeshareData} variable = {averageTripDuration} yTicks = {yTicksDuration}/>

<h1>A City on Bikes: The Growth Story of Bike Share Toronto</h1>

<p>Charts and text on the growth of bike share ridership in Toronto</p>
<h1>A Brief History</h1>
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


<style>
	:global(body) {
		margin: 0px;
		background-color: #F8F6F0;
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
