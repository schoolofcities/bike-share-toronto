<script>
	import Top from "/src/routes/TopSofC.svelte";
	import {data} from "/src/data/data.js";
	// import Chartss from "/src/charting/chart.js"
	import Charts from "/src/charting/chart.svelte"

	
	function extractValues(data, variable) {
		const stationCounts = data.map((item) => item[variable]);
		return stationCounts;
	}

	var StationCount = extractValues(data, "StationCount")

	var Month = extractValues(data, "YearMonth")
	var TripCount = extractValues(data, "TripCount")
	var BikeCount = extractValues(data, "BikeCount")
	var AverageTripDuration = extractValues(data, "AverageTripDuration")
	var AverageBikeUsage = extractValues(data, "AverageBikeUsage")
	var AverageStationUsage = extractValues(data, "AverageStationUsage")
	
	chartFunction('StationCount', Month, 'Station Count', StationCount, "#BFCCB5")
	chartFunction('AverageStationUsage', Month, 'Average Station Usage', AverageStationUsage, "#BFCCB5")
	chartFunction('TripCount', Month, 'Trip Count', TripCount)
	chartFunction('BikeCount', Month, 'Bike Count', BikeCount,'#F28500')
	chartFunction('AverageBikeUsage', Month, 'Average Bike Usage', AverageBikeUsage,'#F28500')
	chartFunction('AverageTripDuration', Month, 'Average Trip Duration', AverageTripDuration)

	console.log(data)
</script>


<Top/>

<style>

</style>
