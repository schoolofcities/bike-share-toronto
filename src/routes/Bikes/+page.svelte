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


<h1>Expanding Fleet</h1>
<p>
	Each bike is given a unique ID, which makes it possible to count the number
	of bikes in the system. Data shows that the number of bikes also fluctuates
	seasonally, like the number of trips taken. The number of bikes is highest
	in August 2020, with 6,455 bikes counted in the system.
</p>
<h2>Bike Count by Month 2017 - 2023</h2>
<BarChart variable="BikeCount" yTicks={yTicksBike} colour="#DC4633" />
<h2>Average Bike Usage by Month 2017 - 2023</h2>
<BarChart
	variable="AverageBikeUsage"
	yTicks={yTicksAvBikeUsage}
	colour="#0D534D"
/>
<h1>Time on Bike</h1>
<h2>Average Trip Duration by Month 2017 - 2023</h2>
<p>
	The average trip duration also shows seasonality influence. Trip duration
	tend to be shorter in the colder months (January to March, November to
	December). Average trip duration tends to stay between 10 to 20 minutes,
	with 2020 and 2021 having longer average trip durations. The longest trip
	was in May 2020, when the average trip duration reaching 20.34 minutes.
</p>
<p>
	First, in 2020 and 2021, the average trip duration is higher than previous
	years and 2022. This could be the purpose of bikes usage were different
	during the two years. During the pandemic years of 2020 and 2021, bikes were
	likely to be used as a method of exercise and for pleasure trips with no set
	destinations. On the other hand, bikes are used for commuting or travelling
	to a certain destination. This would explain why average trip duration
	decreased in 2022 when many businesses and institutions announced returning
	to workers, either full-time or part-time.
</p>
<p>
	Second, average trip duration might be affected by the ways bikes are
	charged. Bike Share Toronto offers two usage plans, a 30-minute plan or a
	45-minute plans. For members, it is unlimited 30-minute plan or unlimited
	45-minute plan, meaning members can have borrow unlimited times, but have to
	return the bike to a dock after 30 minutes or 45 minutes, based on their
	plan. However, after April 2023, Bike Share Toronto changed the fee
	structure. Non-member bike users who does not purchase a short-term or
	long-term plan will be charged by minute instead of a 30 minute period.
	Members and those who purchase short-term plans can still use the bike for a
	30 or 45-minute period, and will be charged by the minute if exceed the 30
	or 45-minute period. This change in fee structure could have impact on
	average trip duration in the future.
</p>
<BarChart
	variable="AverageTripDuration"
	yTicks={yTicksDuration}
	colour="#6D247A"
/>


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
