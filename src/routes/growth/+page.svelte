<script>
	import TopSofC from "../../lib/TopSofC.svelte";
	import MonthlyChart from "../../lib/MonthlyChart.svelte";
	import Bicycle from "../../assets/bicycle.svg";
	import YearlyTripsPictograph from "../../lib/YearlyTripsPictograph.svelte";
	import "../../assets/global-styles.css";
	import "../../assets/green-page-styles.css";
	//import StationRelations from "../station-relations/station-relations.svelte";

	let yTicksTrip = [
		0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000
	];
	let yTicksStation = [0, 100, 200, 300, 400, 500, 600, 700, 800];
	let yTicksAvStation = [0, 200, 400, 600, 800, 1000, 1200, 1400];
	let yTicksBike = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000];
	let yTicksAvBikeUsage = [0, 20, 40, 60, 80, 100, 120];
</script>


<svelte:head>

	<title>Bike Share Toronto Growth | School of Cities</title>
	<meta name="description" content="Visualizing Bike Share system expansion and ridership growth trends in Toronto">
	<meta name="author" content="Jeff Allen">

	<meta property="og:title" content="Bike Share Toronto Growth" />
	<meta property="og:description" content="Visualizing Bike Share system expansion and ridership growth trends in Toronto" />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/bike-share-toronto/growth/" />
	<meta property="og:image" content="https://schoolofcities.github.io/bike-share-toronto/web-card-growth.png" />
	<meta property="og:locale" content="en_CA">

	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:site" content="https://schoolofcities.github.io/bike-share-toronto/growth/" />
	<meta name="twitter:creator" content="@UofTCities" />
	<meta name="twitter:title" content="Bike Share Toronto Growth" />
	<meta name="twitter:description" content="Visualizing Bike Share system expansion and ridership growth trends in Toronto" />
	<meta name="twitter:image" content="https://schoolofcities.github.io/bike-share-toronto/web-card-growth.png" />

</svelte:head>


<TopSofC />

<div class="topImg">
	<img
		src="/bike-share-toronto/top-map.png"
		alt="map of bike lanes and bike-share stations in toronto with a green background"
	/>
</div>

<main>
	<div class="title">
		<h1>Exploring Bike Share Growth in Toronto</h1>
		<p>
			<a href="https://www.linkedin.com/in/chun-fu-liu/">Michael Liu</a> &
			<a href="http://jamaps.github.io">Jeff Allen</a>
			<br>
			Created 08/2023, Updated 10/2024
		</p>
	</div>

	<div class="text">
		<p></p>
		<!-- <div class="buttons-box">
			<button
				onclick="window.open('/bike-share-toronto/station-relations', '_blank');"
				class="application-button"
			>
				View Station Relationship Map
			</button>
			
		</div> -->
		<p>
			Toronto's Bike Share system has grown substantially over the past
			decade, providing a healthy and sustainable mode of travel to
			thousands of Torontonians and visitors. Ridership has increased from
			about 665,000 trips in 2015 to 5.7 million in 2023 (if you
			build it they will ride!). In the chart below, one <img
				class="bike-img"
				src={Bicycle}
				alt="Bike"
				width="25px"
				height="15px"
			/> = 25,000 Bike Share trips. Almost every year, ridership records for
			daily, weekly, monthly, and annual trips have been broken.
		</p>
		<YearlyTripsPictograph />
	</div>
	<div class="text">
		<p>That's a lot of trips!</p>
		<p>
			Below we chart this growth month-by-month to track seasonal patterns
			of expansion and uptake. We'll hopefully update this page as more
			data is released into 2025 and beyond!
		</p>
		<p>
			The data presented on this page are sourced from the <a
				href="https://open.toronto.ca/dataset/bike-share-toronto-ridership-data/"
				>City of Toronto's Open Data Portal</a
			>. The data from 2017 onward denote the duration of each trip. We
			noticed that there were a number of 'trips' where the duration was
			quite low and which started and ended at the same location. We think
			that these trips are mostly people unlocking bikes and then locking
			them back up because something on the bike is broken or that it
			doesn't match their preferences (e.g. the seat height is stuck). As
			such, we have filtered out all trips that were less than 2 minutes
			and which started and ended at the same station, as we felt these
			weren't 'true' trips. Therefore, the numbers presented here may be
			slightly different than reported elsewhere.
		</p>
	</div>

	<div class="text">
		<h3>Bike Share Ridership by Month</h3>
		<p class="note">
			(we are missing monthly data from 0ct 2015 to June 2016)
		</p>
	</div>
	<MonthlyChart
		variable="TripCount"
		yTicks={yTicksTrip}
		colour="#fff"
		maxHeight="800"
		type="bar"
	/>

	<div class="text">
		<p>
			August consistently records the highest ridership between 2019 and
			2024. In August 2024, monthly ridership reached more than 900,000 trips,
			over 400,000 more than the same period in 2021. Colder months
			(November to March) have also recently experienced much higher
			ridership compared to the same months in previous years. 
		</p>
		<p>
			A notable difference in trip patterns occurred during the early
			months of the pandemic. While the number of trips usually increased
			after February, this was not the case in 2020. After a small growth
			in March, the province went into a lockdown on March 24, 2020,
			resulting in a drop in ridership in April and lower ridership in May
			compared to previous years. However, ridership quickly bounced back
			starting in June, and by July 2020, it exceeded the ridership of
			August 2019, the highest month in 2019. January and February of 2022 
			also have low ridership likely due to a similar lockdown. Since then, 
			winter cycling has more than tripled.
		</p>
	</div>

	<div class="text">
		<br>
		<p>
			The Bike Share system has expanded from 79 stations in 2014 to 855 by September,
			2024 (based on the number of unique station IDs in the ridership data). 
			The chart below illustrates this expansion. Before 2020, large
			expansions would occur in July, with many stations installed in
			either June or July. The pace of expansion slowed in 2021, resulting
			in a relatively stable number of stations. In 2022, the expansion
			occurred incrementally, with a few stations installed each month.
		</p>
		<h3>Number of Operating Bike Share Stations</h3>
		<p class="note">
			(we are missing monthly data from 0ct 2015 to June 2016)
		</p>
	</div>

	<MonthlyChart
		variable="StationCount"
		yTicks={yTicksStation}
		colour="#F1C500"
		maxHeight="300"
		type="line"
	/>

	<div class="text">
		<p>
			We can also calculate average station usage by dividing ridership by
			the number of stations. As shown in the chart below, average station
			usage also fluctuates seasonally, similar to overall ridership
			totals. The lowest usage is typically observed in January or
			February, with fewer than 200 rides started from each station during
			these months, and much higher usage in the summer months.
		</p>
		<h3>Trips Per Station</h3>
		<p class="note">
			(we are missing monthly data from 0ct 2015 to June 2016)
		</p>
	</div>

	<MonthlyChart
		variable="AverageStationUsage"
		yTicks={yTicksAvStation}
		colour="#8DBF2E"
		maxHeight="300"
		type="line"
	/>

	<div class="text">
		<p>
			While there are clearly seasonal fluctuations, the relative
			stability of this chart (each year has approximately the same
			pattern) highlights that the rate of trips per station remains
			consistent, even as new stations are added to the system. This bodes
			well that ridership will continue to increase as new stations are
			added to the system.
		</p>
		<br>
		<p>
			We can similarly track the growth of the Bike Share fleet. Each bike
			in the system is assigned a unique ID, and for any particular month,
			we can count how many of these unique IDs there are in the ridership
			data. It is unclear to us whether Bike Share Toronto stores bikes
			during periods of low ridership, or if the bikes remain idle at the
			stations, or both.
		</p>
		<h3>Number of Bikes in Operation</h3>
		<p class="note">(data only available from 2019 onwards)</p>
	</div>

	<MonthlyChart
		variable="BikeCount"
		yTicks={yTicksBike}
		colour="#F1C500"
		maxHeight="300"
		type="line"
	/>

	<div class="text">
		<h3>Trips Per Bike</h3>
		<p class="note">(data only available from 2019 onwards)</p>
	</div>

	<MonthlyChart
		variable="AverageBikeUsage"
		yTicks={yTicksAvBikeUsage}
		colour="#8DBF2E"
		maxHeight="300"
		type="line"
	/>

	<br />
	<div class="text">
		<p>
			Average bike usage indicates how many times bikes are used on
			average each month. Typically, average bike usage exceeds 30 rides
			per month starting in April (approximately one ride per day). In
			2020, average bike usage did not surpass 30 rides per day until May
			due to COVID-19, which resulted in decreased Bike Share usage.
			Normally, about half the year bikes are used more than twice
			per day.
		</p>
		<p>
			This content was built using Svelte and D3. Code is on <a
				href="https://github.com/schoolofcities/bike-share-toronto"
				>GitHub</a
			>. More to come soon!
		</p>
	</div>
	<br /><br />
</main>

<style>

	/* page specific styling */
	.bike-img {
		max-width: 25px;
		max-height: 15px;
		padding-right: 0px;
	}
	.application-button {
		left: 0px;
		font-size: 12px;
		width: auto;
		height: auto;
		margin-right: 5px;
		margin-bottom: 5px;
		padding: 10px 20px; /* Adds padding for better click area */
		border: 2px solid white; /* Corrected syntax for border */
		border-radius: 5px; /* Adds rounded corners */
		position: relative;
		font-weight: bold;
		background-color: var(--brandDarkGreen); /* Light grey background */
		color: white; /* Text color */
		cursor: pointer; /* Changes cursor to pointer on hover */
		transition:
			background-color 0.3s,
			color 0.3s; /* Smooth transition for hover effect */
	}
	.application-button:hover {
		background-color: var(--brandYellow);
		color: black;
	}
	.buttons-box {
		left: 0px;
		width: 35vw - 20px;
		height: auto;
		padding-top: 2px;
		padding-top: 5px;
		margin-right: 20px;
		position: relative;
	} 
</style>
