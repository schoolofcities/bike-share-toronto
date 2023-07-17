<script>
	import logo from '/src/assets/top-logo-full.svg';
	import "/src/assets/global-styles.css"
</script>

<div id="bar">

	<div id="logo">
		<a href="https://www.schoolofcities.utoronto.ca/"><img src={logo} alt="School of Cities"></a>
	</div>
	<p> School of Cities </p>
</div>

<style>
	#bar {
		position: fixed;
		overflow: hidden;
   		top: 0px;
		height: 50px;
		background-color: var(--brandDarkGreen);
		margin-bottom: 20px;
		border-bottom: 1px solid var(--brandWhite);
		width: 100%;
		min-width: 200px;
		padding-left: 0px;
		padding-right: 0px;
		z-index: 5;
		opacity: 0.92;
	}

	#logo {
		margin: auto;
		max-width: 230px;
		height: 50px;
		z-index: 6;
		/* background-color: aquamarine; */
	}

	a {
		color: black;
	}
	a:hover {
		opacity: 0.7;
	}

	img {
		height: 50px;
		color: blue;
	}
	img:hover {
		height: 50px;
		opacity: 0.5;
		cursor: pointer;
	}
	p{
		fill: white;
	}
</style>
