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


<h1>Bikeshare Usage: Number of Trips Made</h1>

<BarChart2 />
<h2>Ridership by Month 2017 - 2023</h2>
<BarChart variable="TripCount" yTicks={yTicksTrip} colour="#AB1368" />
<p>
	Ridership have increased over the years. Data also shows that bike trips
	shows a seasonal pattern, with more rides in the warmer months and fewer
	rides during the colder months. August is the month with the highest
	ridership between 2019 and 2022 while February tends to have the lowest
	ridership. Since 2018, ridership has been breaking record each year.
	Currently, the highest monthly ridership was in August 2022, reaching almost
	700,000 rides. This is over 200 thousand more trips made in the same period
	in 2021. Not only in August, the colder months (September to December) also
	have higher ridership than previous years. An analysis on Toronto's
	Bikeshare ridership by
	<a
		href="https://medium.com/@siglimumuni/bike-share-toronto-an-exploration-of-trip-patterns-and-user-behaviour-with-python-part-2-22d1fead5f8c"
	>
		Sigli Mumuni
	</a>
	found positive correlations between temperature and ridership. This means that
	when the weather is warmer, ridership tends to be higher. Therefore, the higher
	ridership between September and December of 2022 could be correlated to a warmer
	winter in 2022, with
	<a
		href="https://globalnews.ca/news/9258382/canada-fall-weather-outlook-nov-2022/"
	>
		with record breaking warmer temperature in November.
	</a>
</p>
<p>
	One interesting difference in the trip pattern is during the earliest month
	of the pandemic. While the number of trips tend to increase after February,
	it was not the case in 2020. After a small growth of ridership in March, the
	Province went into a lockdown on March 24, 2020. This impact is reflected in
	the ridership in April 2020, which showed ridership drop from March. It also
	caused the lowest May riderships across the 5 year period. However,
	ridership quickly bounced back starting June, and ridership in July 2020 is
	higher than August 2019, the highest month of 2019.
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
