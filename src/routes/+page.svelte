<script>
	import Top from "/src/CommonFormatting/TopSofC.svelte";
	import Nav from "/src/CommonFormatting/Nav.svelte";
	import "../assets/global-styles.css";
</script>

<Top />

<Nav />

<h1>Toronto on Bikes: Bikeshare Usage Since 2017</h1>
<p><b>Prepared by: Michael Liu | July 2023</b></p>

<h2>From Bixi Toronto to Bike Share Toronto: A Brief History</h2>
<p>
	The bikeshare system in Toronto was launched in 2011 by PBSC Urban Solutions
	as Bixi Bike. While Bixi was successful in Montreal, it faced significant
	financial losses in Toronto. Unable to repay its $3.9 million loan from the
	City of Toronto, Bixi was taken over by the Toronto Parking Authority in
	2014 and rebranded as Bike Share Toronto. This change in ownership led to
	increased funding from sources such as TD Canada, Metrolinx, the Federal
	Government, the City of Toronto, and most recently, Tangerine Bank. These
	funds supported the system's operations, expansion costs, and special
	programs.
</p>

<h2>About the Data</h2>
<p>
	The data for bikeshare usage is shared on <a
		href="httIn-person knowledge mobilization workshops – coordinated by School of Cities Director Karen Chapple and faculty lead Stanka Radovic, and featuring School of Cities-affiliated experts – which focus on identifying ways to reach a broader audience via data visualization, op-eds, policy briefs, blogs, videos, podcasts, and more 
<style>
	:global(body) {
		margin: 0px;
		background-color: #f8f6f0;
	}


	h1 {
		font-family: "Helvetica Neue", Arial, sans-serif;
		font-weight: bolder;
		font-size: 35px;

		color: var(--brandDarkGreen);
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
		color: var(--brandYellow);
		padding-left: 20%;
		padding-right: 20%;
		padding-top: 20px;
	}

	nav {
		position: relative;
		display: flex;
		gap: 1em;
		padding: 1em;
		background: var(--brandGray70);
		z-index: 2;
		margin: 0 0 1em 0;
	}

	nav a {
		text-decoration: none;
		color: white;
	}

	nav a[aria-current="true"] {
		border-bottom: 2px solid;
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
