<script>
  import Chart from "chart.js/auto";
  import { onMount } from "svelte";

  export let labelList; // x-axis labels
  export let dataList; // the list of data
  export let colour;

  onMount(() => {
    const ctx = document.getElementById("myChart");

    if (labelList && dataList) {
      var myChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: labelList,
          datasets: [
            {
              data: dataList,
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
        maintainAspectRatio: false,
          scales: {
            x: {
              ticks: {
                callback: function (label) {
                  let realLabel = this.getLabelForValue(label);
                  var month = realLabel.split(";")[1];
                  var year = realLabel.split(";")[0];
                  return month;
                },
                grid:{
                  borderWidth: 5,
                  lineWidth: 0.2,
                }
                
              },
            },
            xAxis2: {
              type: "category",
              grid: {
                drawOnChartArea: false,
                
              },
              ticks: {
                callback: function (label) {
                  let realLabel = this.getLabelForValue(label);
                  var month = realLabel.split(";")[1];
                  var year = realLabel.split(";")[0];
                  if (month === "5") {
                    return year;
                  } else {
                    return "";
                  }
                },
              },
            },
            y: {
              beginAtZero: true,
              grid:{
                borderWidth: 5,
                lineWidth: 0.2,
              }
              
            },
          },
          backgroundColor: colour,
          plugins:{
            legend:{
              display: false,
            }
          }
        },
      });
    }
  });

  console.log(dataList);
  console.log(labelList);
  console.log(colour);
</script>

<div>
  <canvas id="myChart" style="height: 400px; width: 100%;" />
</div>

<style>
  div {
    height: 50vh;
    padding-left: 10%;
    padding-right: 10%;
    width: 80%;
  }
  @media screen and (max-width: 1300px) {
    div {
    height: 60vh;
    padding-left: 1%;
    padding-right: 5%;
    width: 90vw;
  }
}
</style>
