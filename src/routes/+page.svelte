<script>

    import "../assets/global-styles.css"
    let name = "Michael"


</script>



<main>

    <h1>Bike Share Toronto</h1>

    <p>Charts and text on the growth of bike share ridership in Toronto</p>
    <h1> A Brief History </h1>
    <p> {name} edited: Bike Share Toronto is a bicycle-sharing system in Toronto, Canada. The system consists of 6850 bicycles and 625 stations, and covers over 200 square kilometres (80 square miles) of the city, from Finch Avenue in the north, Rouge Park in the east, Lake Ontario to the south, and to Long Branch to the west.[1][2] Bike Share Toronto recorded 3,575,000 trips in 2021.[3] The system was launched in 2011 by PBSC Urban Solutions under the BIXI brand and was taken over by the Toronto Parking Authority in 2014. (Copied from Wikepedia, only for testing)</p>
    
</main>



<style>

    :global(body) {
		padding: 0px;
		margin: 0px;
		background-color: var(--brandDarkBlue);
	}

	main {
		text-align: center;
		padding: 0px;
		margin: 0px;
	}

    h1 {
        font-family: TradeGothicBold, sans-serif;
        font-size: 35px;
        font-weight: normal;
        color: var(--brandYellow);
    }

    p { 
        /* should pick a consistent font here probably */
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        color: var(--brandWhite);
        text-align: left;
        padding-left: 10%;
        padding-right: 10%;
    }

</style>