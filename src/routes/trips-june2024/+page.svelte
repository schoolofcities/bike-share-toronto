<script>
	
	import logo from '/src/assets/top-logo-full.svg';
	import "../../assets/global-styles.css"; 

</script>

	<div id="bar">

		<div id="logo">
			<a href="https://www.schoolofcities.utoronto.ca/"><img src={logo} alt="School of Cities"></a>
		</div>
		<p> School of Cities </p>
	</div>

	<main>
		<div class="title">
			<h1>Toronto's Bike Share Geography</h1>
			<p>Estimating and mapping routes for almost every Bike Share trip in June 2024 based on origin-destination ridership data and a cycling network graph. 762,760 trips in total! Click on the image to view at a higher resolution.</p>
			<p>
				<a href="http://jamaps.github.io" target="_blank">Jeff Allen</a> / <a href="https://www.schoolofcities.utoronto.ca/" target="_blank">School of Cities</a>
			</p>
		</div>

		<div class="big-map">
			<a href="/bike-share-toronto/3600x2400-og.png">
				<img src="/bike-share-toronto/3600x2400-og2.png">
			</a>
		</div>

		<div class="text">
			<h2>Why & How</h2>
			<p>
				There has been substantial <a href="./growth">growth</a> in Bike Share ridership in Toronto over the past few years. We recently wanted to A) improve our understanding about <i>where</i> people use Bike Share and B) estimate the characteristics of these trips (network distance, speed, elevation gain/loss, etc.) to use in future analyses on how people cycle in the city.
			</p>
			<p>
				From Bike Share Toronto, we graciously received a dataset which included a record for every trip in June 2024. There were 764,177 records in this dataset. 762,760 of these represented normal trips that were not terminated shortly after a bike was unlocked and returned to the same station. That's over 25,000 trips per day!
			</p>
			<p>
				Each record in this dataset had information about when and where trips started and ended as well as attributes like the type of bike (electric or classic) and type of user (annual member or pay-per-ride). But we didn't know the route taken, the distance of the trip along this route, and the elevation gain or loss. 
				<!-- We can pretty easily calculate the straight line (i.e. as the crow flies) distance between the start and end stop, but in reality, the distance cyclists travel is longer, since there is rarely a perfectly straight path between the start and end locations. So -->
				We set out to estimate this additional information with the help of open data and software. 
				<!-- Once this was calculated, we layered the route for every trip onto a map to look at overall travel patterns. -->
			</p>
			<p>
				To do this, we needed the help of a <a href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)" target="_blank">graph</a> representing the cycling network in the City of Toronto. We created this using network data from <a href="https://www.openstreetmap.org/#map=14/43.6586/-79.3833" target="_blank">OpenStreetMap</a> and <a href="https://www.openstreetmap.org/#map=14/43.6586/-79.3833" target="_blank">GraphHopper</a>, an open source network analysis software, to build a routable network graph that works off a local computer. From this network graph we can make queries, similar to Google Maps, where we input the start location and end location, and ask the graph to return us the most plausible route along with information on trip duration, distance, and change in elevation. Routing takes into account a variety of attributes. For example designated cycling trails away from cars, like the Waterfront Trail, have greater priority; busy car-centric roads without cycling infrastructure have less priority. 
			</p>
			<p>
				Here's an example output for a short trip.
			</p>
			<img src="/bike-share-toronto/single-trip.png">	
			<p>	
				The upshot is that since we have this data and software stored locally, is that we can do calculations it at scale, i.e. calculate 1,000s of routes like this in just a few seconds.
			</p>
			<p>
				One tricky consideration is what to do for trips that begin and end at the same docking station. If we input the same start and end location into the network graph, it will return a trip of length = 0. But in reality, these are trips that people will likely ride somewhere and then cycle back to where they started, often for leisure rather than other purposes. Since we don't know where they actually travel to, we used a random number generator to estimate a location within a 5km radius of the starting Bike Share station. This of course is a bit arbitrary, but was based on our best guess on how far most people would bike from/to a single location for leisure. We made a couple exceptions to this for the stations with the most of these out-and-back leisure trips, which were along the waterfront and the base of the Leslie Spit. For these we constrained this random number generator to locations on the Leslie Spit, the Waterfront, and Toronto Island depending on the location of the docking station. 
			</p>
			<p>
				The output of this data crunching allowed us to create the visualization at the top of this page, created by overlaying all 762,760 routes onto a single map. There were a couple of visual tricks here to help the visualization. We add some noise to the path geometry (i.e. randomly jittered coordinates a bit) and then visualized each trip as a very very very thin line. The goal here was to help highlight segments of greater travel flow when there are many trips along a corridor. Here's a super zoomed in view to a bundle of trips on the Danforth near Pape.
			</p>
			<img src="/bike-share-toronto/many-trips.png">
			<p>
				The map at the top of this page was tinkered with in <a href="https://www.gimp.org/" target="_blank">GIMP</a> using a combination of colour and filter settings. The 'bloom' filter was used to try to highlight more well-traveled paths. GIMP is a bit of a rabbit hole; one can tinker with colours and effects for hours. Below are a couple interesting iterations, first is pixelate and cartoon filter to create a gridded heat map, the second using curvature blur to create a water colour effect.
			</p>
			<p>
				Anyways, that's it for now, thanks for viewing / reading!
			</p>


		</div>

		<div class="small-map">
			<img src="/bike-share-toronto/gimp1.png">
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<img src="/bike-share-toronto/gimp2.png">
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
		opacity: 0.92;
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
		font-size: 40px;
		color: #ffc169;
		text-shadow: 
                0 0 5px #11959a,
                0 0 15px #11959a;
		text-decoration: none;
	}

	h2 {
		font-family: TradeGothicBold, sans-serif;
		font-size: 27px;
		color: #ffc169;
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
		opacity: 0.8;
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
