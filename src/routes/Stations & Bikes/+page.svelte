<script>
	import Top from "/src/CommonFormatting/TopSofC.svelte";
	import Nav from "/src/CommonFormatting/Nav.svelte"
	import "/src/assets/global-styles.css";
	import BarChart from "/src/charting/BarChart.svelte";

	let yTicksStation = [0, 100, 200, 300, 400, 500, 600, 700];
	let yTicksAvStation = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600];
	let yTicksBike = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000];
	let yTicksAvBikeUsage = [0, 20, 30, 40, 60, 80, 100, 120];

</script>

<Top />

<Nav/>

<h1>Rapidly Expanding Service</h1>
<h2>Station Count by Month 2017 - 2023</h2>
<BarChart variable="StationCount" yTicks={yTicksStation} colour="#0D534D" />
<p>
	The bikeshare system has been expanding since 2017, with the number of stations increasing 
	from 200 to 659 by 2023. The chart below illustrates the fast expansion. Before 2020, large 
	expansions would occur in July, with many stations installed in either June or July. The pace 
	of expansion slowed in 2021, resulting in a relatively stable number of stations. In 2022, the 
	expansion occurred incrementally, with a few stations installed each month.

</p>
<p>
	It's worth noting that the number of stations can occasionally decrease, although only by a small 
	amount. This is likely due to construction or maintenance work that temporarily removes a station 
	from the system. It is also possible that these fluctuations are a result of data collection methods. 
	Station count data is obtained by counting the number of unique station IDs in the ridership data each 
	month. Additionally, a station may have no ridership at all for an entire month, although this is unlikely.

</p>


<h2>Average Station Usage by Month 2017 - 2023</h2>

<BarChart
	variable="AverageStationUsage"
	yTicks={yTicksAvStation}
	colour="#007FA3"
/>

<p>
	Average station usage is calculated by dividing ridership by the number of stations. As shown in the chart below, 
	average station usage also fluctuates seasonally, mirroring the ridership pattern. The lowest usage is typically 
	observed in January or February, with fewer than 200 rides started from each station during these months. 
	The highest usage was recorded in June 2017, with 1475 rides per station. In other years (2018 to 2022), the highest 
	average station usage occurred in August. The average ridership per station has increased in 2022 due to the growth 
	in ridership.
</p>


<h1>Expanding Fleet</h1>
<p>
	Each bike in the system is assigned a unique ID, enabling the tracking of the number of bikes. The data shows that the 
	number of bikes also fluctuates seasonally, similar to the number of trips taken. The highest count of bikes was recorded 
	in August 2020, with 6,455 bikes in the system. However, after 2021, the number of bikes in the system stabilized and did 
	not fluctuate as much as in 2019 and 2020. It is unclear whether Bike Share Toronto stores bikes during periods of low 
	ridership or if the bikes remain idle at the stations.
</p>


<h2>Bike Count by Month 2017 - 2023</h2>
<BarChart variable="BikeCount" yTicks={yTicksBike} colour="#DC4633" />
<h2>Average Bike Usage by Month 2017 - 2023</h2>

<p>
	Average bike usage indicates how many times bikes are used on average each month. Typically, average bike usage exceeds 30 rides 
	per month starting in April (approximately one ride per day). In 2020, average bike usage did not surpass 30 rides per day until 
	May due to the pandemic lockdown, which resulted in decreased bikeshare usage. Normally, there are 5-6 months where bikes are used 
	more than twice per day, and in 2022, bikes were used on average more than 90 times per month.

</p>

<BarChart
	variable="AverageBikeUsage"
	yTicks={yTicksAvBikeUsage}
	colour="#0D534D"
/>


<Nav/>
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
