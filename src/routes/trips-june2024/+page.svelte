<script>
	
	import "../../assets/global-styles.css"; 

</script>



<main>
	<div class="title">
		<h1>Estimating Bike Share Geography in Toronto</h1>
		<p>Finding and mapping routes for ~764k trips in June 2024</p>
		<p>
			<a href="http://jamaps.github.io">~ Jeff Allen</a>
		</p>
	</div>

	<!-- map here -->

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
		<!-- e.g. route on graph -->
	</div>
</main>



<style>

	body {
		padding: 0px;
		margin: 0px;
		background-color: var(--brandDarkGreen);
	}

</style>
