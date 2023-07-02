<script>
  import Chart from 'chart.js/auto';
  import { onMount } from 'svelte';

  export let chartName;
  export let labelList; // x-axis labels
  export let dataList; // the list of data
  export let label; 
  export let colour;
  
  const ctx = chartName.getContext('2d')
  
  new Chart(ctx, {
    type: "bar",
    
    data: {
      labels: labelList,
      datasets: [{
        data: dataList,
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        x: {
          ticks: {
            callback: function(label) {
              let realLabel = this.getLabelForValue(label)
              var month = realLabel.split(";")[1];
              var year = realLabel.split(";")[0];
              return month;
            }
          }
        },
        xAxis2: {
          type: "category",
          grid: {
            drawOnChartArea: false, // only want the grid lines for one axis to show up
          },
          ticks: {
            callback: function(label) {
              let realLabel = this.getLabelForValue(label)
  
              var month = realLabel.split(";")[1];
              var year = realLabel.split(";")[0];
              if (month === "1") {
                return year;
              } else {
                return "";
              }
            }
          }
        },
        y: {
  
          beginAtZero: true
  
        }
      },
      backgroundColor: colour
    }
  });
</script>

<canvas bind:this={chartName} id="myChart"></canvas>

<style>
  canvas {
    height: 400px;
    width: 80%;
  }
</style>
