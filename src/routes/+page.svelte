<script>
	import Top from "/src/routes/TopSofC.svelte";
	//import testing from "/src/charting/testing.svelte";
	import data from '/src/data/data.json';
	//import BarChart from "/src/charting/BarChart.svelte"
	//import {chartFunction} from '/src/charting/chart.js'
	import Chart from '/src/charting/chart.svelte'

	var yTicks = [0, 100,200,300,400,500,600,700]
	/*
	console.log(data)
	console.log("Here")
	// import {data} from "/src/data/data.js";
	 //import Charts from "/src/charting/chart.js"
	//import Charts from "/src/charting/chart.svelte"
	//import BarChart from "../charting/BarChart.svelte";

	*/
	function extractValues(data, variable) {
		const stationCounts = data.map((item) => item[variable]);
		return stationCounts;
	}

	var StationCount = extractValues(data, "StationCount")

	var Month = extractValues(data, "YearMonth")
	var TripCount = extractValues(data, "TripCount")
	var BikeCount = extractValues(data, "BikeCount")
	var AverageTripDuration = extractValues(data, "AverageTripDuration")
	var AverageBikeUsage = extractValues(data, "AverageBikeUsage")
	var AverageStationUsage = extractValues(data, "AverageStationUsage")
	
	//chartFunction('StationCount', Month, StationCount, "#BFCCB5")
	/*
	chartFunction('AverageStationUsage', Month, 'Average Station Usage', AverageStationUsage, "#BFCCB5")
	chartFunction('TripCount', Month, 'Trip Count', TripCount)
	chartFunction('BikeCount', Month, 'Bike Count', BikeCount,'#F28500')
	chartFunction('AverageBikeUsage', Month, 'Average Bike Usage', AverageBikeUsage,'#F28500')
	chartFunction('AverageTripDuration', Month, 'Average Trip Duration', AverageTripDuration)
	*/

</script>
<Top />
<!--<canvas bind:this={portfolio} width={400} height={400} />
{chartFunction(Month, StationCount, "#BFCCB5")}
<canvas class = "myChart"></canvas>
<canvas id ="myChart2"></canvas>-->
<h1>Toronto on Bikes: Toronto Bikeshare Usage Since 2017</h1>
<p><b>Prepared by: Michael Liu | July 2023</b></p>

<Chart labelList = {Month} dataList = {TripCount} colour = "#DC4633"></Chart>

<h2>From Bixi Toronto to Bike Share Toronto: A Brief History</h2>
<p>
	Bike Share Toronto was originally branded as Bixi Bike, a branch of the
	successful Bikeshare system in Montreal, when it first launched by PBSC
	Urban Solutions in 2011. However, the success was not replicated. Bixi
	suffered great financial losses and was unable to repay the City a $3.9
	million loan. Toronto Parking Authority took over the bikeshare system and
	rebranded as Bike Share Toronto. With funding from various sources over the
	years, Bike Share Toronto tells a great comeback story of a bikeshare system
	on the verge of shutting down that transformed into a popular method of
	urban mobility in Toronto. This page visualizes the changes in bikeshare
	usage in Toronto, showing various aspects of how the system has been used
	since 2017, with data from the City of Toronto.
</p>

<h1>Bikeshare Usage: Number of Trips Made</h1>
<h2>Ridership by Month 2017 - 2023</h2>
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
	found positive correlations between temperature and ridership. This means
	that when the weather is warmer, ridership tends to be higher. Therefore,
	the higher ridership between September and December of 2022 could be
	correlated to a warmer winter in 2022, with
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

<h1>Rapidly Expanding Service</h1>
<h2>Station Count by Month 2017 - 2023</h2>
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

<p>
	Average station useage is calculated by dividing the number of trips per
	month by the number of bike station per month.
</p>

<h1>Expanding Fleet</h1>
<p>
	Each bike is given a unique ID, which makes it possible to count the number
	of bikes in the system. Data shows that the number of bikes also fluctuates
	seasonally, like the number of trips taken. The number of bikes is highest
	in August 2020, with 6,455 bikes counted in the system.
</p>
<h2>Bike Count by Month 2017 - 2023</h2>

<h2>Average Bike Usage by Month 2017 - 2023</h2>

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

	
<h2>About the Data</h2>
<p>
	The data for bikeshare usage is shared on <a
		href="https://open.toronto.ca/dataset/bike-share-toronto-ridership-data/"
		>City of Toronto's Open Data Catalogue</a
	>. Data stretches from 2014 to 2023 March at the time of writing. However,
	data from 2014, 2015 and 2016 are incomplete. Data for 2014 is missing the
	first 9 months, 2015 misses the months starting October, and 2016 data
	misses Q1 and Q2 data. This is the reason why this analysis only visualize
	bikeshare usages starting January 2017.
</p>

<style>


	
	canvas {
		padding-left: 10%;
		padding-right: 10%;
		width: 80%;
		height: 100px;
		max-height: 500px;
		padding-bottom: 30px;
		padding-top: 20px;
	}

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
		
		color: #333333;
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
		color: #333333;
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
	canvas {
		padding-left: 5%;
		padding-right: 5%;
		width: 90%;
		
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
