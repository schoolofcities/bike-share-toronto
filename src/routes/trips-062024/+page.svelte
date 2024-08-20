<script>
	
	import logo from '/src/assets/top-logo-full.svg';
	import "../../assets/global-styles.css"; 

</script>



<svelte:head>

	<title>Bike Share Toronto Trip Map | School of Cities</title>
	<meta name="description" content="Estimating and visualizing routes for every Bike Share trip in Toronto in 06/2024">
	<meta name="author" content="Jeff Allen">

	<meta property="og:title" content="Bike Share Toronto Trip Map" />
	<meta property="og:description" content="Estimating and visualizing routes for every Bike Share trip in Toronto in 06/2024" />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/bike-share-toronto/trips-062024/" />
	<meta property="og:image" content="https://schoolofcities.github.io/bike-share-toronto/web-card-trips.png" />
	<meta property="og:locale" content="en_CA">

	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:site" content="https://schoolofcities.github.io/bike-share-toronto/trips-062024/" />
	<meta name="twitter:creator" content="@UofTCities" />
	<meta name="twitter:title" content="Bike Share Toronto Trip Map" />
	<meta name="twitter:description" content="Estimating and visualizing routes for every Bike Share trip in Toronto in 06/2024" />
	<meta name="twitter:image" content="https://schoolofcities.github.io/bike-share-toronto/web-card-trips.png" />

</svelte:head>



<div id="bar">

	<div id="logo">
		<a href="https://www.schoolofcities.utoronto.ca/"><img src={logo} alt="School of Cities"></a>
	</div>
	<!-- <p> School of Cities</p> -->

</div>

<main>
	<div class="title">
		<h1>Mapping Bike Share Trips In Toronto </h1>
		<p>Estimating and mapping routes for every Bike Share trip in Toronto in 06/2024 based on origin-destination ridership data and a cycling network graph. 762,760 trips in total! Click on the map to view at a higher resolution.</p>
		<p>
			<a href="http://jamaps.github.io" target="_blank">Jeff Allen</a> / <a href="https://www.schoolofcities.utoronto.ca/" target="_blank">School of Cities</a>
		</p>
	</div>

	<div class="big-map">
		<a href="/bike-share-toronto/bike-share-trip-map-june2024-3600x2300.png">
			<img src="/bike-share-toronto/bike-share-trip-map-june2024-3600x2300.png">
		</a>
	</div>

	<div class="text">
		<h2>Why & How</h2>
		<p>
			There has been substantial <a href="./growth">growth</a> in Bike Share ridership in Toronto over the past few years. We recently wanted to A) improve our understanding about <i>where</i> people use Bike Share and B) estimate the characteristics of these trips (network distance, speed, elevation gain/loss, etc.) to use in future analyses on how people cycle in the city.
		</p>
		<p>
			From Bike Share Toronto, we graciously received a dataset which included a record for every trip in June 2024. There were 764,177 records in this dataset. 762,760 of these represented normal trips that were not terminated shortly after a bike was unlocked and returned to the same station.
		</p>
		<p>
			Each record in the dataset includes the date and the time of the trip, and which station that each trip started and ended at. Here's a map of every station in June 2024.
		</p>
	</div>
	<div class="small-map">
		<img src="/bike-share-toronto/trips-june2024-stations.png">
	</div>
	<div class="text">
		<p>
			Each record in this dataset also had attributes like the type of bike (electric or classic) and type of user (annual member or pay-per-ride). But we didn't know the route taken, the distance of the trip along this route, and the elevation gain or loss. These are key for understanding the nuances of where, how, and why people ride. We set out to estimate this additional information with the help of open data and software. 
		</p>
		<p>
			To do this, we needed a <a href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)" target="_blank">graph</a> representing the cycling network in the City of Toronto. We created this using data from <a href="https://www.openstreetmap.org/#map=14/43.6586/-79.3833" target="_blank">OpenStreetMap</a> and <a href="https://www.openstreetmap.org/#map=14/43.6586/-79.3833" target="_blank">GraphHopper</a>, an open source network analysis software, to build a network graph that works off a local computer. From this network graph we can make queries, similar to Google Maps, where we input the start location and end location, and ask the graph to return us the most likely route taken alongside information on trip duration, distance, and change in elevation. This route query takes into account a variety of attributes. For example designated cycling trails away from cars, like the Waterfront Trail, have greater priority; while busy car-centric roads without cycling infrastructure have less priority. 
		</p>
		<p>
			Here's an example output for a short trip.
		</p>
		<img src="/bike-share-toronto/single-trip.png">	
		<p>	
			The upshot is that since we have this data and software stored locally, is that we can do calculations at scale, i.e. estimate 1,000s of routes like this in just a few seconds.
		</p>
		<p>
			One tricky consideration is what to do for trips that begin and end at the same docking station. If we input the same start and end location into the network graph, it will return a trip of length = 0. But in reality, these are trips that people will likely ride somewhere and then cycle back to where they started, often for leisure rather than other purposes. Since we don't know where they actually travel to, we used a random number generator to estimate a location within a 5km radius of the starting Bike Share station. This of course is a bit arbitrary, but was based on our best guess on how far most people would bike from/to a single location for leisure. We made a couple exceptions to this for the stations with the most of these out-and-back leisure trips, which were along the waterfront and the base of the Leslie Spit. For these we constrained this random number generator to locations on the Leslie Spit, the Waterfront, and Toronto Island depending on the location of the docking station. 
		</p>
		<p>
			The output of this data crunching allowed us to create the visualization at the top of this page, created by overlaying all 762,760 routes onto a single map. There were a couple of visual tricks here to help the visualization. We add some noise to the path geometry (i.e. randomly jittered coordinates a bit) and then visualized each trip as a very very very thin line. The goal here was to help highlight segments of greater travel flow when there are many trips along a corridor. Here's a super zoomed in view to a bundle of trips on the Danforth near Pape.
		</p>
		<img src="/bike-share-toronto/many-trips.png">
		<p>
			The map at the top of this page was prepped in <a href="https://qgis.org/" target="_blank">QGIS</a> and then tinkered with in <a href="https://www.gimp.org/" target="_blank">GIMP</a> using a combination of colour and filter settings. A mean curvature blur and a bloom filter were used to try to highlight more well-traveled paths. GIMP is a bit of a rabbit hole; one can tinker with colours and effects for hours. Below are a couple interesting outputs, first is pixelate and cartoon filters to create a gridded heat map, the second using a mean curvature blur with many more iterations to create a watercolour effect.
		</p>
		<p>
			Anyways, that's it for now, thanks for viewing / reading! We'll be doing some analysis on how riders use EV bikes compared to classic bikes (do they take longer trips? more likely to travel uphill?), and hopefully have something to share on that front in a couple months or so.
		</p>

	</div>

	<div class="small-map">
		<img src="/bike-share-toronto/trips-june2024-grid.png">
		<br>
		<br>
		<br>
		<br>
		<br>
		<br>
		<img src="/bike-share-toronto/trips-june2024-watercolour.png">
	</div>

	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>

</main>



<style>

	#bar {
		position: fixed;
		overflow: hidden;
   		top: 0px;
		height: 50px;
		background-color: black;
		margin-bottom: 20px;
		border-bottom: 1px solid var(--brandGray80);
		width: 100%;
		min-width: 200px;
		padding-left: 0px;
		padding-right: 0px;
		z-index: 5;
		opacity: 0.9;
	}

	#bar #logo {
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

	main {
		padding: 0px;
		margin: 0px;
		margin-top: -40px;
		margin-bottom: -40px;
		background-color: #000;
	}

	h1 {
		font-family: TradeGothicBold, sans-serif;
		font-weight: normal;
		font-style: normal;
		font-size: 39px;
		color: #ffc169;
		text-shadow:
				0 0 5px #11959a,
				0 0 30px #11959a;
		text-decoration: none;
	}

	h2 {
		font-family: TradeGothicBold, sans-serif;
		font-size: 27px;
		color: #ffc169;
		text-shadow: 
				0 0 10px #11959a;
		font-style: italic;
	}

	p {
		color: white;
		font-family: RobotoRegular, sans-serif;
		font-size: 17px;
		line-height: 25px;
		opacity: 0.94;
	}

	a {
		color: #bcf9ff;
		text-decoration: underline;
	}
	p a:hover {
		color: #24edff
	}

	.title {
		position: relative;
		background-color: none;
		max-width: 590px;
		margin: 0 auto;
		padding-top: 140px;
		padding-bottom: 15px;
		padding-left: 15px;
		padding-right: 15px;
	}

	.big-map {
		margin: 0px auto;
	}
	.big-map img {
		width: 100%;
		height: auto;
	}

	.text {
		position: relative;
		background-color: none;
		max-width: 590px;
		margin: 0 auto;
		padding: 15px;
	}

	.text img {
		width: 100%;
		height: auto;
		margin: 0 auto;
		border: solid 1px var(--brandGray90);
	}

	.small-map {
		position: relative;
		max-width: 900px;
		margin: 0 auto;
	}

	.small-map img {
		width: 100%;
		max-width: 900px;
		height: auto;
	}

</style>
