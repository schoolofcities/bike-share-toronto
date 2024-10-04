<script>
  import TopSofC from "../../lib/TopSofC.svelte";
  import DurationHist from "../../lib/DurationHist.svelte";
  import DistanceHist from "../../lib/DistanceHist.svelte";
  // import * as d3 from "d3";
  import { onMount } from "svelte";
  import "../../assets/global-styles.css";
  import "../../assets/global-styles.css";

  // Example duration data (in minutes, for instance)
  onMount(() => {});
</script>

<svelte:head>
  <title>Bike Share Toronto Growth | School of Cities</title>
  <meta
    name="description"
    content="Visualizing Bike Share system expansion and ridership growth trends in Toronto"
  />
  <meta name="author" content="Jeff Allen" />

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
  />
</svelte:head>

<TopSofC />

<div class="top-margin">
  <DurationHist />
  <DistanceHist />
</div>

<style>
  .top-margin {
    margin-top: 50px;
  }
</style>
