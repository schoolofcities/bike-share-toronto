<script>
  import logo from "/src/assets/top-logo-full-green.svg";
  import "../../assets/global-styles.css";
  import "../../assets/white-page-styles.css";

  import { onMount } from "svelte";
  import * as d3 from "d3";
  import RadialHist from "$lib/RadialHist.svelte";
  import LineChart from "$lib/LineChart.svelte";

  let freqData = [];
  let freqData2 = [];
  let dayData = {
    Monday: [],
    Tuesday: [],
    Wednesday: [],
    Thursday: [],
    Friday: [],
    Saturday: [],
    Sunday: [],
  };

  let Weekday = [];
  let Weekend = [];

  async function loadCSVData() {
    // Data for radial charts
    freqData = await d3.csv("freq_counts_by_day.csv", (d) => ({
      half_hour_intervals: d.half_hour_intervals,
      EFIT: +d.EFIT_normalized,
      ICONIC: +d.ICONIC_normalized,
      day_of_week: d.day_of_week,
    }));
    // Data for radial charts for each day of the week
    for (let day in dayData) {
      dayData[day] = freqData.filter((d) => d.day_of_week === day);
    }
    // Data for radial charts for weekend and weekday
    freqData2 = await d3.csv("freq_counts_by_day_category.csv", (d) => ({
      half_hour_intervals: d.half_hour_intervals,
      EFIT: +d.EFIT_normalized,
      ICONIC: +d.ICONIC_normalized,
      day: d.day_category,
    }));
    // Filter between weekend and weekday
    Weekday = freqData2.filter((d) => d.day === "Weekday");
    Weekend = freqData2.filter((d) => d.day === "Weekend");
  }

  onMount(() => {
    loadCSVData();
  });
</script>

<svelte:head>
  <title>Bike Share Toronto E-Bike Analysis | School of Cities</title>
  <meta
    name="description"
    content="Exploring e-bike usage in Toronto’s Bike Share system via charts and data"
  />
  <!-- <meta name="author" content="Jeff Allen" />

  <meta property="og:title" content="Bike Share Toronto Growth" />
  <meta
    property="og:description"
    content="Visualizing Bike Share system expansion and ridership growth trends in Toronto"
  />
  <meta property="og:type" content="website" />
  <meta
    property="og:url"
    content="https://schoolofcities.github.io/bike-share-toronto/growth/"
  />
  <meta
    property="og:image"
    content="https://schoolofcities.github.io/bike-share-toronto/web-card-growth.png"
  />
  <meta property="og:locale" content="en_CA" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta
    name="twitter:site"
    content="https://schoolofcities.github.io/bike-share-toronto/growth/"
  />
  <meta name="twitter:creator" content="@UofTCities" />
  <meta name="twitter:title" content="Bike Share Toronto Growth" />
  <meta
    name="twitter:description"
    content="Visualizing Bike Share system expansion and ridership growth trends in Toronto"
  />
  <meta
    name="twitter:image"
    content="https://schoolofcities.github.io/bike-share-toronto/web-card-growth.png"
  /> -->
</svelte:head>

<!-- <TopSofC /> -->

<div id="bar">
  <div id="logo">
    <a href="https://www.schoolofcities.utoronto.ca/"
      ><img src={logo} alt="School of Cities" /></a
    >
  </div>
  <!-- <p> School of Cities</p> -->
</div>

<div class="topImg">
	<img
		src="/bike-share-toronto/top-map-2.png"
		alt="map of bike lanes and bike-share stations in toronto with a white background"
	/>
</div>

<main>
  <div class="title">
    <h1>Exploring E-Bike Usage in Toronto’s Bike Share System</h1>
    <p>
      <a href="">Lanrick Bennett Jr.</a>, <a href="">Scott McCallum</a>, <a href="">Jeff Allen</a>
    <br>
      December, 2024
    </p>
  </div>
  <div class="text">
    <p>
      As cycling becomes an increasingly popular mode of transportation in Toronto, one trend is gaining significant traction: the rise of electric bikes (e-bikes) within Toronto's Bike Share system. Recent data shared by Bike Share Toronto from June 2024 has given us a detailed look at how these e-bikes, known as EFIT, compare to their classic non-electric counterparts, the ICONIC bikes.
    </p>
    <p>
      Overall, in June 2024, there were <a href="https://schoolofcities.github.io/bike-share-toronto/trips-062024" target="_blank">more than 762,000 Bike Share trips in Toronto</a>. 17.4% of these trips were by e-bikes. Looking at the relative characteristics of these trips and reveals some intriguing patterns that could shape the future of urban mobility in Toronto.
    </p>
    <p>
      One of the most notable differences between e-bikes and classic bikes is the distance covered during trips. On average, e-bike users tend to ride
      further, capitalizing on the extra power that electric motors provide.
      These longer trips suggest that e-bikes are enabling riders to explore
      parts of the city that might have been less accessible via traditional
      pedal bikes. Whether it's covering more ground on commutes or leisurely
      rides, the data reflects how e-bikes are expanding the possibilities for
      cycling trips across Toronto.
    </p>
  </div>

  <div class="chart-container">
    <div class="line-chart">
      <LineChart
        title="Distribution of trips by distance"
        suffix="distance"
        csvData="distance_counts.csv"
        medianEFIT={2806.437}
        medianICONIC={2303.089}
        xlabel="Trip distance (kilometers)"
        xdivider={1000}
        xdecimal={0}
        xtickamount={10}
        xunit="km"
        medianadjust={0}
      />
    </div>
  </div>

  <div class="text">
    <p>
      Interestingly, despite these longer trips, there is little difference in
      the duration of e-bike trips compared to classic bikes. Riders are thus traveling faster on e-bikes on average, which makes sense given their
      assisted pedaling capabilities.   
      Higher speeds not only allow cyclists to
      reach destinations quicker but could also make cycling more attractive to
      those who may have previously found it too time-consuming or physically
      demanding. With e-bikes, the barriers to entry for cycling are lowered,
      making it a more practical and inclusive option for a broader demographic.
    </p>
  </div>

  <div class="chart-container">
    <div class="line-chart">
      <LineChart
        title="Distribution of trips by duration"
        suffix="duration"
        csvData="duration_counts.csv"
        medianEFIT={747}
        medianICONIC={720}
        xlabel="Trip duration (minutes)"
        xdivider={60}
        xdecimal={0}
        xtickamount={20}
        xunit="minutes"
        medianadjust={30}
      />
    </div>
  </div>

  <div class="text">
    <p>
      Another key insight from the data is that e-bike trips tend to involve
      slightly more elevation gain. In a city like Toronto, where hills and
      slopes can make cycling more challenging, the extra boost from an e-bike's
      motor can make a big difference. For example, riders can now tackle
      steeper routes, such as those leading to neighborhoods like Rosedale or
      the Scarborough Bluffs, with greater ease. This ability to flatten out the
      city’s topography opens up new opportunities for riders, making cycling a
      more attractive option in areas that were previously considered difficult
      to navigate on a bike.
    </p>
  </div>

  <div class="chart-container">
    <div class="line-chart">
      <LineChart
        title="Distribution of trips by elevation gain"
        suffix="elevation"
        csvData="elevation_counts.csv"
        medianEFIT={0}
        medianICONIC={-0.5}
        xlabel="Elevation gain or loss (metres)"
        xdivider={1}
        xdecimal={0}
        xtickamount={20}
        xunit="m"
        medianadjust={0}
      />
    </div>
  </div>
  
  <div class="text">
    <p>
      The data also shows some intriguing differences in the time of day when e-bikes are used. While we’re still investigating the reasons behind this
      trend, it could be related to the availability of bikes at different
      stations during peak and off-peak hours. E-bikes may also be more popular
      for commuters who are looking for a reliable and faster way to get to work
      or run errands during busy periods. Understanding these temporal patterns
      will be crucial as we explore how to optimize the distribution and
      availability of e-bikes throughout the day.
    </p>
  </div>

  <!-- Title for Radial Charts -->
  <div class="radial-title">
    <h4>24-hour trip distributions</h4>
  </div>

  <!-- Legend for Radial Charts -->
  <div class="radial-legend">
    <div class="legend-item">
      <svg class="legend-circ">
        <circle
          cx="20"
          cy="15"
          r="8"
          fill="var(--brandDarkGreen)"
          fill-opacity="0.1"
          stroke="var(--brandDarkGreen)"
          stroke-width="2"
        ></circle>
      </svg>
      <p>ICONIC</p>
    </div>

    <div class="legend-item">
      <svg class="legend-circ">
        <circle
          cx="20"
          cy="15"
          r="8"
          fill="darkorange"
          fill-opacity="0.1"
          stroke="darkorange"
          stroke-width="2"
        ></circle>
      </svg>
      <p>EFIT</p>
    </div>
  </div>

  <!-- Weekday and Weekend Radial Charts  -->
  <div class="radial-container">
    {#if Weekday.length > 0}
      <RadialHist data={Weekday} title="Weekdays" />
    {/if}
    {#if Weekend.length > 0}
      <RadialHist data={Weekend} title="Weekends" />
    {/if}
  </div>

  <!-- Every day of the week Radial Charts -->
  <div class="flex-container-weekday">
    {#each Object.entries(dayData).slice(0, 4) as [day, data]}
      {#if data.length > 0}
        <div class="weekday-item">
          <RadialHist {data} title={day} />
        </div>
      {/if}
    {/each}
  </div>
  <div class="flex-container-weekend">
    {#each Object.entries(dayData).slice(4, 7) as [day, data]}
      {#if data.length > 0}
        <div class="weekend-item">
          <RadialHist {data} title={day} />
        </div>
      {/if}
    {/each}
  </div>

  <div class="text">
    <p>
      These findings reflect broader shifts in how cycling is being integrated
      into urban mobility strategies. The introduction of e-bikes in Toronto is
      not just about offering a new mode of transportation—it’s about making
      cycling more accessible, efficient, and appealing to a wider range of
      people. Whether it’s older adults who may need extra assistance with
      pedaling, people with longer commutes, or those who want to avoid arriving
      at their destination sweaty, e-bikes have the potential to address many of
      the challenges that have historically limited bike usage in the city.
    </p>
    <p>
      From a sustainability perspective, the growing use of e-bikes aligns with
      Toronto’s push towards reducing greenhouse gas emissions. By providing a
      viable alternative to cars for longer trips, e-bikes can help cut down on
      vehicle emissions, especially during peak traffic hours. As the city works
      towards its ambitious net-zero targets, the role of EV bikes in
      encouraging a shift from motorized transport to more sustainable,
      human-powered options cannot be understated.
    </p>
    <p>
      As we continue to analyze the data and explore the impacts of e-bikes on
      Toronto’s cycling culture, the early results are encouraging. E-bikes are
      not just another addition to the Bike Share system—they represent a step
      towards a more dynamic, sustainable, and inclusive urban mobility
      landscape. Stay tuned as we delve deeper into the numbers and uncover more
      about how e-bikes are reshaping the way Torontonians move through their
      city.
    </p>
  </div>
  <div class="text">
    <br>
    <br>
    <h3>Data & Methodology</h3>
    <p>
      Bike Share Toronto shared with us data on all Bike Share trips in June 2024, which included for each trip, start station, end station, duration, and type of bike (EFIT or ICONIC). We additionally computed the network distance and elevation gain of each trip via Graphhopper, a network analysis software (<a href="https://schoolofcities.github.io/bike-share-toronto/trips-062024" target="_blank">as described in this post</a>).
    </p>
    <p>
      All the charts shown on this page were created via analyzing data in Python and visualizing with D3. All medians and distributions shown for each category are significantly different from each other via Mann-Whitney U (for testing difference in medians) and Kolmogorov-Smirnov (for testing difference in distributions) tests.
    </p>
    <p>
      Code and data for this page are on <a href="https://github.com/schoolofcities/bike-share-toronto" target="_blank">GitHub</a>
    </p>
    <br>
    <br>
    <br>

  </div>
</main>

<style>

  /* .radial-container {
    max-width: 500px;
  } */

  .radial-title {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
  }

  .radial-legend {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 0px;
    margin-bottom: 0px;
    height: 30px;
    
  }

  .legend-item {
    display: flex;
    align-items: center;
    margin: 0 20px;
  }
  .legend-circ {
    width: 30px;
    height: 30px;
    margin-right: 10px;
  }

  .legend-item p {
    font-size: 12px;
    color: black;
    font-family: RobotoRegular;
  }

  #bar {
    position: fixed;
    overflow: hidden;
    top: 0px;
    height: 50px;
    background-color: var(--brandWhite);
    margin-bottom: 20px;
    border-bottom: 1px solid var(--brandDarkGreen);
    width: 100%;
    min-width: 200px;
    padding-left: 0px;
    padding-right: 0px;
    z-index: 5;
    opacity: 0.9;
  }

  #bar #logo {
    /* filter: invert(100%); */
    margin: auto;
    max-width: 230px;
    height: 50px;
    z-index: 6;
  }

  #bar a {
    color: black;
  }
  #bar a:hover {
    opacity: 0.7;
  }

  #bar img {
    height: 50px;
  }
  #bar img:hover {
    height: 50px;
    opacity: 0.5;
    cursor: pointer;
  }

  .chart-container {
    margin: 0px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%; /* Adjust as needed */
  }

  .radial-container {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;

    justify-content: center;
    align-items: center;
    height: 100%;
  }

  .flex-container-weekday {
    display: flex;
    justify-content: center;
    align-items: normal;
    flex-wrap: wrap;
    width: 100%;
    margin: 0;
    padding: 0;
  }

  .flex-container-weekend {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
  }

  .weekday-item {
    /* width: 100%; */
    flex: 1 1 25%; /* Default to 4 columns */
    text-align: center;
  }

  @media (width > 1460px) {
    .radial-container {
      display: none;
    }
  }

  @media (width < 1460px) {
    .flex-container-weekday {
      display: none;
    }
    .flex-container-weekend {
      display: none;
    }
  }

  @media (max-width: 1460px) {
    .weekday-item {
      flex: 1 1 50%; /* 2 columns for widths <= 1200px */
      width: 20%;
    }

    /* main {
      width: 750px;
    } */
  }

  @media (max-width: 700px) {
    .weekday-item {
      flex: 1 1 100%; /* 1 column for widths <= 600px */
      transform: scale(1.5);
      margin: 100px 0 100px 0;
      display: none;
    }

    .weekend-item {
      display: none;
    }
  }
</style>
