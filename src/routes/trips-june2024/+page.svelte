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
		<h1>Bike Share Geography in Toronto</h1>
		<p>Estimating and mapping routes for all ~764k trips in June 2024. Click on the image to view at a higher resolution.</p>
		<p>
			~ <a href="http://jamaps.github.io" target="_blank">Jeff Allen</a>
		</p>
	</div>

	<!-- map here -->

	<div class="big-map">
		<img src="/bike-share-toronto/3600x2400-og.png">
	</div>

	<div class="text">
		<h2>Technical Details</h2>
		<p>
			Interesting to visualize to show patterns of where people use bike share across the city (which is what's shown above) 2) use these trips to derive data on trip distance and elevation gain/loss (to use in a future project).
		</p>
		<p>
			From Bike Share Toronto, we received a dataset which included a record for every trip in June 2024 including the when of trips, and where those trips started and ended. But we didn't know a few other attributes of those trips, specifically the distance of the trip, the route taken, and the elevation gain or loss of the trip. For the former, distance, it's pretty easy to calculate the straight line (as the crow flies) distance between the start and end stop, but in reality, the network distance, is longer, since there is often not a perfectly direct street or path between the start and end locations.
		</p>
		<p>
			764,124 trips in total. a few of these were tagged as "TERMINATED", meaning.
			
			Created a network graph, using OpenStreetMap data, using software called Graphhopper.
		<!-- e.g. image of graph -->
			From this network graph we can make queries, very similar to Google Maps and similar online tools, where we input the starting location, end location, and ask the graph to return us the most plausible route, alongside with information like duration, distance, and elevation gain.
		</p>
		<p>
			Polyline string?
		</p>
		<p>
			Visualize as very very thin lines that when on their own are barely visible, but when many are layered near each other highlights paths of greater journey flow.
		</p>
		<p>
			Anyways, that's it for now, might try 
		</p>


		<p>

		</p>
		<br>
		<br>
		<br>
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
		/* background-color: aquamarine; */
	}

	#bar a {
		color: black;
	}
	#bar a:hover {
		opacity: 0.7;
	}

	#bar img {
		height: 50px;
		color: blue;
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
		font-size: 36px;
		color: var(--brandWhite);
		text-decoration: none;
	}

	h2 {
		font-family: RobotoBold, sans-serif;
		font-size: 28px;
		color: white;
		text-decoration: underline;
	}

	p {
		color: white;
		font-family: RobotoRegular, sans-serif;
		font-size: 16px;
		line-height: 24px;
		opacity: 0.87;
	}


	a {
		color: white;
		text-decoration: underline;
	}
	a:hover {
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
