<script>

	import "../assets/global-styles.css";
	import Bicycle from "../assets/bicycle.svg";

	var data = [
		{ Year: 2015, Ridership: 665000 },
		{ Year: 2016, Ridership: 830000 },
		{ Year: 2017, Ridership: 1460000 },
		{ Year: 2018, Ridership: 1918000 },
		{ Year: 2019, Ridership: 2421000 },
		{ Year: 2020, Ridership: 2900000 },
		{ Year: 2021, Ridership: 3560000 },
		{ Year: 2022, Ridership: 4600000 },
		{ Year: 2023, Ridership: 5700000 }
	];

</script>


{#each data as d}

	<div id="wrapper">
		<p><b>{d.Year}</b> / {d.Ridership.toLocaleString()} Trips</p>
		<div class="all-bike-img">
			{#each Array(Math.round(d.Ridership / 25000)) as _}
				<img class="bike-img" src={Bicycle} alt="Bike">
			{/each}
		</div>
	</div>

{/each}



<style>
	#wrapper {
		width: 100%;
		/* max-width: 800px; */
		/* align-content: center; */
	}
	p {
		margin-bottom: -1px;
		font-size: 14px;
		line-height: 15px;
		border-bottom: solid 1px rgba(25, 107, 66, 0.501);
	}
	.all-bike-img {
		margin-top: 3px;
		margin-bottom: 20px;
	}
	.bike-img {
		max-width: 22px;
		max-height: 16px;
		padding-right: 2px;
		width: 100%;
	}
	b {
		color: var(--brandYellow);
	} 
</style>