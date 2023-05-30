<script>

    import "../assets/global-styles.css"

</script>



<main>

    <h1>Bike Share Toronto</h1>

    <p>Charts and text on the growth of bike share ridership in Toronto</p>
    
</main>



<style>

    :global(body) {
		padding: 0px;
		margin: 0px;
		background-color: var(--brandDarkGreen);
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
    }

</style>