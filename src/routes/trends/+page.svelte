<script>

    import TopSofC from "../../lib/TopSofC.svelte";
    import MonthlyChart from "../../lib/MonthlyChart.svelte";
    import YearlyChart from "../../lib/YearlyChart.svelte";
    import "../../assets/global-styles.css";

    let yTicksTrip = [0, 100000, 200000, 300000, 400000, 500000, 600000, 700000];
    let yTicksStation = [0, 100, 200, 300, 400, 500, 600, 700];
	let yTicksAvStation = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600];
	let yTicksBike = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000];
	let yTicksAvBikeUsage = [0, 20, 40, 60, 80, 100, 120];

</script>




<TopSofC/>

<img src="/toronto-green-bike-map.png" alt="map of bike lanes and bike-share stations in toronto with a green background">

<main>

    <div class="title">

        <h1>Exploring Bike Share Growth in Toronto</h1>

        <p><a>Michael Liu</a> & <a>Jeff Allen</a> -- 07/2023</p>

    </div>

    <div class="text">

        <div id="two-column-wrapper">
            
            <div id="left-column">
                <YearlyChart/>
            </div>

            <div id="right-column">
                <p>
                    Toronto's Bike Share system has grown substantially over the past decade. Ridership has more than quadrupled from 2014 to 2022 as a result (if you build it they will ride!). Almost every year, ridership records for
                    daily, weekly, monthly, and annually trips have been broken.
                </p>
                <p>
                    We're interested in charting this growth month-by-month level to track seasonal variations of  expansion and uptake. We'll hopefully update this page as more data is released into late 2023 and beyond :)
                </p>
                <p>
                    Most of the charts in this page start in January 2017 because of different data formats and some incomplete data prior to this date. We're hoping to backfill this as well though.
                </p>
            </div>

        </div>

    </div>

    <div class="text">
        <h3>Bike Share Ridership by Month</h3>
    </div>  
    <MonthlyChart 
        variable="TripCount" 
        yTicks={yTicksTrip} 
        colour="#fff" 
        maxHeight=600 
        type="bar"
    />
      
    <div class="text">
        <p>        
            August consistently records the highest ridership between 2019 and 2022, while February tends to have the lowest ridership. Since 2018, each year has seen record-breaking ridership. In August 2022, the highest monthly ridership reached almost 700,000 rides, over 200,000 more than the same period in 2021. Interestingly, the colder months (September to December) also showed higher ridership  compared to previous years. An analysis by <a href="https://medium.com/@siglimumuni/bike-share-toronto-an-exploration-of-trip-patterns-and-user-behaviour-with-python-part-2-22d1fead5f8c">Sigli Mumuni</a> on Toronto's Bikeshare ridership found a positive correlation between temperature and ridership, indicating that warmer weather leads to increased ridership. The higher ridership between September and December 2022 could be attributed to a <a href="https://globalnews.ca/news/9258382/canada-fall-weather-outlook-nov-2022/">warmer winter</a>, with November experiencing record-breaking temperatures.
        </p>
        <p>
            A notable difference in trip patterns occurred during the early months of the pandemic. While the number of trips usually increased after February, this was not the case in 2020. After a small growth in March, the province went into a lockdown on March 24, 2020, resulting in a drop in ridership in April and the lowest ridership in May across the five-year period. However, ridership quickly bounced back starting in June, and by July 2020, it exceeded the ridership of August 2019, the highest month in 2019.
        </p>
    </div>

    <div class="text">
        <p>
            The bikeshare system has been expanding since 2017, with the number of stations increasing from 200 to 659 by 2023. The chart below illustrates the fast  expansion. Before 2020, large expansions would occur in July, with many stations installed in either June or July. The pace of expansion slowed in 2021, resulting in a relatively stable number of stations. In 2022, the expansion occurred incrementally, with a few stations installed each month.
        </p>
        <h3>Number of Operating Bike Share Stations</h3>
    </div>

    <MonthlyChart 
        variable="StationCount" 
        yTicks={yTicksStation} 
        colour="#fff" 
        maxHeight=250
        type="bar"
    />

    <div class="text">
        <p>
            We can also calculate average station usage is by dividing ridership by the number of stations. As shown in the chart below, average station usage also fluctuates seasonally, mirroring the ridership pattern. The lowest usage is typically observed in January or February, with fewer than 200 rides started from each station during these months. The highest usage was recorded in June 2017, with 1475 rides per station. In other years (2018 to 2022), the highest average station usage occurred in August. The average ridership per station has increased in 2022 due to growth in ridership.
        </p>
        <h3>Trips Per Station</h3>
    </div>

    <MonthlyChart
        variable="AverageStationUsage"
        yTicks={yTicksAvStation}
        colour="#fff"
        maxHeight=300
        type="line"
    />

    <div class="text">
       
        <p>
            We can also track the growth of the bike-share fleet. Each bike in the system is assigned a unique ID. The data shows that the number of bikes also fluctuates seasonally, similar to the number of trips taken. The highest count of bikes was recorded in August 2020, with 6,455 bikes in the system. However, after 2021, the number of bikes in the system stabilized and did not fluctuate as much as in 2019 and 2020. It is unclear whether Bike Share Toronto stores bikes during periods of low ridership or if the bikes remain idle at the stations.
        </p>
        <h3>Number of Bikes in Operation</h3>
        <p>(data only available from 2019 onwards)</p>
    </div>

    <MonthlyChart 
        variable="BikeCount" 
        yTicks={yTicksBike} 
        colour="#fff" 
        maxHeight=300
        type="bar"
    />

    <div class="text">
        <h3>Trips Per Bike</h3>
    </div>

    <MonthlyChart
        variable="AverageBikeUsage"
        yTicks={yTicksAvBikeUsage}
        colour="#fff"
        maxHeight=300
        type="line"
    />

    <div class="text">
        <p>
            Average bike usage indicates how many times bikes are used on average each month. Typically, average bike usage exceeds 30 rides per month starting in April (approximately one ride per day).  In 2020, average bike usage did not surpass 30 rides per day until May due to the pandemic lockdown, which resulted in decreased bike share usage. Normally, there are 5-6 months where bikes are used more than twice per day, and in 2022, bikes were used on average more than 90 times per month.
        </p>
    </div>

    <br>
    <div class="title">
    </div>
    <br><br><br>

</main>



<style>
    /* page specific styling */
    #two-column-wrapper {
        display: flex;
        flex-wrap: wrap;
    }
    #right-column {
        flex: 1;
        min-width: 300px;
    }
    #left-column {
        padding-top: 20px;
        flex: 1;
        min-width: 300px;
    }
</style>
