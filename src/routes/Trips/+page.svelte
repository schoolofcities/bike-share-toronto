<script>
	import Top from "/src/CommonFormatting/TopSofC.svelte";
	import Nav from "/src/CommonFormatting/Nav.svelte";
	import "/src/assets/global-styles.css";
	import BarChart from "/src/charting/BarChart.svelte";
	import BarChart2 from "/src/charting/BarChart2.svelte";

	let yTicksTrip = [
		0, 100000, 200000, 300000, 400000, 500000, 600000, 700000,
	];
</script>

<Top />

<Nav />
<h1>Bikeshare Usage: Number of Trips Made</h1>

<h2>Annual Ridership 2015 - 2023</h2>
<p>
	Since 2014, ridership has experienced significant growth, along with an
	expansion of the service network. Almost every year, ridership records for
	daily, weekly, monthly, and annually trips were broken.
</p>

<BarChart2 />

<h2>Ridership by Month 2017 - 2023</h2>
<p>
	Breaking annual data into monthly intervals reveals a seasonal pattern in
	bike trips, with more rides during warmer months and fewer rides in colder
	months. August consistently records the highest ridership between 2019 and
	2022, while February tends to have the lowest ridership. Since 2018, each
	year has seen record-breaking ridership. In August 2022, the highest monthly
	ridership reached almost 700,000 rides, over 200,000 more than the same
	period in 2021. Interestingly, the colder months (September to December)
	also showed higher ridership compared to previous years. An analysis by
	<a
		href="https://medium.com/@siglimumuni/bike-share-toronto-an-exploration-of-trip-patterns-and-user-behaviour-with-python-part-2-22d1fead5f8c"
	>
		Sigli Mumuni
	</a>
	on Toronto's Bikeshare ridership found a positive correlation between temperature
	and ridership, indicating that warmer weather leads to increased ridership. The
	higher ridership between September and December 2022 could be attributed to a
	<a
		href="https://globalnews.ca/news/9258382/canada-fall-weather-outlook-nov-2022/"
		>warmer winter</a
	>, with November experiencing record-breaking temperatures.
</p>

<BarChart variable="TripCount" yTicks={yTicksTrip} colour="#AB1368" />

<p>
	A notable difference in trip patterns occurred during the early months of
	the pandemic. While the number of trips usually increased after February,
	this was not the case in 2020. After a small growth in March, the province
	went into a lockdown on March 24, 2020, resulting in a drop in ridership in
	April and the lowest ridership in May across the five-year period. However,
	ridership quickly bounced back starting in June, and by July 2020, it
	exceeded the ridership of August 2019, the highest month in 2019.
</p>

<Nav />

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
