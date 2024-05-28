<script>

    import TopSofC from "../../lib/TopSofC.svelte";
    import MonthlyChart from "../../lib/MonthlyChart.svelte";
    import Bicycle from "../../assets/bicycle.svg";
    import YearlyTripsPictograph from "../../lib/YearlyTripsPictograph.svelte";
    import "../../assets/global-styles.css";
    //import StationRelations from "../station-relations/station-relations.svelte";

    let yTicksTrip = [0, 100000, 200000, 300000, 400000, 500000, 600000, 700000];
    let yTicksStation = [0, 100, 200, 300, 400, 500, 600, 700];
    let yTicksAvStation = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600];
    let yTicksBike = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000];
    let yTicksAvBikeUsage = [0, 20, 40, 60, 80, 100, 120];

</script>



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

        <p><a href="https://www.linkedin.com/in/chun-fu-liu/">Michael Liu</a> & <a href="http://jamaps.github.io">Jeff Allen</a> -- 08/2023</p>
    </div>

    <div class="text">
        
        <div class="buttons-box">
            

        <button onclick="location.href = '/bike-share-toronto/station-relations';"
                class="application-button" 
                >
                    Trip Destinations
                </button
            >        </div>

            <p>
                Toronto's Bike Share system has grown substantially over the
                past decade, providing a healthy and sustainable mode of travel to thousands of Torontonians and visitors. Ridership has increased from about 665,000 trips in 2015 to over 4.5 million in 2022 (if you build it they will ride!). In the chart below, one <img class="bike-img" src={Bicycle} alt="Bike" width="25px" height="15px"> = 25,000 Bike Share trips. Almost every year, ridership records for daily, weekly, monthly, and annual trips have been broken.
            </p>
            <YearlyTripsPictograph/>
    </div>            
            <div class="text">
            <p>
                That's a lot of trips!
            </p>
            <p>
                Below we chart this growth month-by-month to track seasonal patterns of expansion and uptake. We'll hopefully update this page as more data is released into late 2023 and beyond!
            </p>
            <p>
                The data presented on this page are sourced from the <a href="https://open.toronto.ca/dataset/bike-share-toronto-ridership-data/">City of Toronto's Open Data Portal</a>. The data from 2017 onward denote the duration of each trip. We noticed that there were a number of 'trips' where the duration was quite low and which started and ended at the same location. We think that these trips are mostly people unlocking bikes and then locking them back up because something on the bike is broken or that it doesn't match their preferences (e.g. the seat height is stuck). As such, we have filtered out all trips that were less than 2 minutes and which started and ended at the same station, as we felt these weren't 'true' trips. Therefore, the numbers presented here may be slightly different than reported elsewhere.
            </p>
    </div>

    <div class="text">
        <h3>Bike Share Ridership by Month</h3>
        <p class="note">(we are missing monthly data from 0ct 2015 to June 2016)</p>
    </div>
    <MonthlyChart
        variable="TripCount"
        yTicks={yTicksTrip}
        colour="#fff"
        maxHeight="600"
        type="bar"
    />

    <div class="text">
        <p>
            August consistently records the highest ridership between 2019 and 2022, while February tends to have the lowest ridership. In August 2022, the highest monthly ridership reached almost 700,000 rides, over 200,000 more than the same period in 2021. Colder months (November to March) have also recently witnessed much higher ridership compared to previous years. The relatively higher ridership in Fall 2022 could be attributed to a <a href="https://globalnews.ca/news/9258382/canada-fall-weather-outlook-nov-2022/">warmer winter</a>, with November experiencing record-breaking temperatures.
        </p>
        <p>
            A notable difference in trip patterns occurred during the early months of the pandemic. While the number of trips usually increased after February, this was not the case in 2020. After a small growth in March, the province went into a lockdown on March 24, 2020, resulting in a drop in ridership in April and lower ridership in May compared to previous years. However, ridership quickly bounced back starting in June, and by July 2020, it exceeded the ridership of August 2019, the highest month in 2019.
        </p>
    </div>

    <div class="text">
        <p>
            The Bike Share system has expanded from  79 in 2014 to 659 by March, 2023. The chart below illustrates this expansion. Before 2020, large expansions would occur in July, with many stations installed in either June or July. The pace of expansion slowed in 2021, resulting in a relatively stable number of stations. In 2022, the expansion occurred incrementally, with a few stations installed each month.
        </p>
        <h3>Number of Operating Bike Share Stations</h3>
        <p class="note">(we are missing monthly data from 0ct 2015 to June 2016)</p>
    </div>

    <MonthlyChart
        variable="StationCount"
        yTicks={yTicksStation}
        colour="#F1C500"
        maxHeight="250"
        type="line"
    />

    <div class="text">
        <p>
            We can also calculate average station usage by dividing ridership by the number of stations. As shown in the chart below, average station usage also fluctuates seasonally, similar to overall ridership totals. The lowest usage is typically observed in January or February, with fewer than 200 rides started from each station during these months, and much higher usage in the summer months.
        </p> 
        <h3>Trips Per Station</h3>
        <p class="note">(we are missing monthly data from 0ct 2015 to June 2016)</p>
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
            While there are clearly seasonal fluctuations, the relative stability of this chart (each year has approximately the same pattern) highlights that the rate of trips per station remains consistent, even as new stations are added to the system. This bodes well that ridership will continue to increase as new stations are added to the system.
        </p>
        <p>
            We can similarly track the growth of the Bike Share fleet. Each bike in the system is assigned a unique ID, and for any particular month, we can count how many of these unique IDs there are in the ridership data. The highest count of bikes was recorded in August 2020, with 6,455 bikes in the system. However, after 2021, the number of bikes in the system stabilized and did not fluctuate as much as in 2019 and 2020. It is unclear whether Bike Share Toronto stores bikes during periods of low ridership or if the bikes remain idle at the stations or both.
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
            Average bike usage indicates how many times bikes are used on average each month. Typically, average bike usage exceeds 30 rides per month starting in April (approximately one ride per day). In 2020, average bike usage did not surpass 30 rides per day until May due to COVID-19, which resulted in decreased Bike Share usage. Normally, there are 5-6 months where bikes are used more than twice per day.
        </p>
        <p>
            This content was built using Svelte and D3. Code is on <a href="https://github.com/schoolofcities/bike-share-toronto">GitHub</a>. More to come soon!
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
        left: 10px;
        font-size: 12px;
        width: auto;
        height: auto;
        margin-right: 5px;
        margin-bottom: 5px;
        padding: 10px 20px;  /* Adds padding for better click area */
        border: 2px solid white;  /* Corrected syntax for border */
        border-radius: 5px;  /* Adds rounded corners */
        position: relative;
        font-weight: bold;
        background-color: #f0f0f0;  /* Light grey background */
        color: black;  /* Text color */
        cursor: pointer;  /* Changes cursor to pointer on hover */
        transition: background-color 0.3s, color 0.3s;  /* Smooth transition for hover effect */
    }
</style>
