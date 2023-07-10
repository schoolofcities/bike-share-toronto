<script>
	import Top from "/src/CommonFormatting/TopSofC.svelte";
	import Nav from "/src/CommonFormatting/Nav.svelte";
	import "/src/assets/global-styles.css";
	import BarChart from "/src/charting/BarChart.svelte";

	let yTicksDuration = [0, 10, 20, 30];
</script>

<Top />

<Nav />

<h1>Time on Bike</h1>
<h2>Average Trip Duration by Month 2017 - 2023</h2>
<p>
	The average trip duration also shows seasonality influence. Trip durations
	tend to be shorter in the colder months (January to March, November to
	December). The average trip duration usually stays between 10 to 20 minutes,
	but in 2020 and 2021, it was longer. The longest trip occurred in May 2020,
	with an average duration of 20.34 minutes.
</p>
<p>
	Firstly, in 2020 and 2021, the average trip duration was higher compared to
	previous years and 2022. This could be due to a difference in the purpose of
	bike usage during these two years. During the pandemic years of 2020 and
	2021, bikes were likely used for exercise and pleasure trips without
	specific destinations. However, in 2022, bikes were predominantly used for
	commuting or traveling to specific destinations. This explains the decrease
	in average trip duration in 2022, as many businesses and institutions
	announced the return of workers, either full-time or part-time.
</p>
<p>
	Secondly, the average trip duration might be affected by the bike charging
	methods. Bike Share Toronto offers two usage plans: a 30-minute plan or a
	45-minute plan. For members, there is an unlimited 30-minute or 45-minute
	plan, allowing them to borrow bikes an unlimited number of times but
	requiring them to return the bike to a dock within 30 minutes or 45 minutes,
	depending on their plan. However, starting from April 2023, Bike Share
	Toronto changed the fee structure. Non-member bike users who do not purchase
	a short-term or long-term plan will be charged by the minute instead of a
	30-minute period. Members and those who purchase short-term plans can still
	use the bike for a 30 or 45-minute period but will be charged by the minute
	if they exceed the designated time. This change in fee structure could have
	an impact on the average trip duration in the future.
</p>
<BarChart
	variable="AverageTripDuration"
	yTicks={yTicksDuration}
	colour="#6D247A"
/>

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
