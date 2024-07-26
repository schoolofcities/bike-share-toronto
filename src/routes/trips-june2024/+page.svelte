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
			<p>We estimated and mapped routes for every Bike Share trip in June 2024 based on origin-destination ridership data and a cycling network graph. Click on the image to view at a higher resolution.</p>
			<p>
				~ <a href="http://jamaps.github.io" target="_blank">Jeff Allen</a>
			</p>
		</div>

		<div class="big-map">
			<a href="/bike-share-toronto/3600x2400-og.png">
				<img src="/bike-share-toronto/3600x2400-og.png">
			</a>
		</div>

		<div class="text">
			<h2>Why & How</h2>
			<p>
				We've seen a lot of <a href="./growth">growth</a> in Bike Share ridership in Toronto over the past several years.
				We recently wanted to A) improve our understanding where people use Bike Share across the city and B) estimate the characteristics of these trips (network distance, speed, elevation gain/loss, etc.) to use in future analyses on how people cycle in the city.
			</p>
			<p>
				From Bike Share Toronto, we graciously received a dataset which included a record for every trip in June 2024 including when and where trips started and ended as well as attributes like the type of bike (electric or classic) and type of user (annual member or pay-per-ride). But we didn't know the route taken, the distance of the trip, and the elevation gain or loss. 
				<!-- We can pretty easily calculate the straight line (i.e. as the crow flies) distance between the start and end stop, but in reality, the distance cyclists travel is longer, since there is rarely a perfectly straight path between the start and end locations. So -->
				We set out to estimate this route information with the help of open data and software, and then once calculated, layer the route for every trip on a map to look at overall travel patterns (i.e. what's visualized above)
			</p>
			<p>
				To do this, we needed the help of a <a href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)" target="_blank">graph</a> representing the cycling network in the City of Toronto. We created this using network data from <a href="https://www.openstreetmap.org/#map=14/43.6586/-79.3833" target="_blank">OpenStreetMap</a> and the open source routing software <a href="https://www.openstreetmap.org/#map=14/43.6586/-79.3833" target="_blank">Graphhopper</a> to build a routable network graph that works off a local computer. From this network graph we can make queries, very similar to Google Maps and similar routing applications, where we input the starting location, end location, and ask the graph to return us the most plausible route, along with information on trip duration, distance, and change in elevation. The bonus since we built this locally is that we can do this it at scale, i.e. calculate 1000s of routes in just a few seconds.
			</p>
			<p>
				Polyline string?
			</p>
			<p>
				Visualize as very very thin lines that when on their own are barely visible, but when many are layered near each other highlights paths of greater journey flow.
			</p>

			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>

			<p>:)</p>
			<!-- e.g. route on graph -->
		</div>

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
		/* text-decoration: underline; */
	}

	p {
		color: white;
		font-family: RobotoRegular, sans-serif;
		font-size: 17px;
		line-height: 25px;
		opacity: 0.87;
	}

	a {
		color: white;
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
		max-width: 750px;
		margin: 0 auto;
		padding: 15px;
	}



</style>
