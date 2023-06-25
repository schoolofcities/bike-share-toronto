<!DOCTYPE html>
<html>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
<body>

<canvas id="myChart" style="width:100%;max-width:600px"></canvas>

<script>

import Chart from 'chart.js/auto'
import data from "/src/data/data.json"
export const chart = {
    type: 'bar', 
    data: {
        labels: xValues,
        datasets: [{
            backgroundColor: "Black",
            data: yValues
        }]
    },
    options: {
        legend: {display: false},
        title: {
          display: true,
          text: "World Wine Production 2018"
        }
      }

}
</script>

</body>
</html>
