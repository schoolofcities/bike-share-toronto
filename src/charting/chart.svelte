<script>
  import Chart from "chart.js/auto";
  import data from "/src/data/data.json";
  import { onMount } from "svelte";

  export let labelList; // x-axis labels
  export let dataList; // the list of data
  export let colour;

  var w = window.innerWidth;

  $: console.log(w);

  function extractValues(data, variable) {
    const values = data.map((item) => item[variable]);
    return values;
  }
  var YearList = extractValues(data, "Year");
  let Year = [...new Set(YearList)]
  console.log(Year)
  var Month = extractValues(data, "Month");
  var dataList = extractValues(data, variable)

  /*
//multi-arbitrary line
const multiArbitraryLine = {
  id: "multiArbitraryLine", 
  beforeDatasetDraw(chart, args, pluginOptions){
    const {ctx, chartArea: {top, bottom, left, right, width, height}, scales:{x, y}} = chart;
    ctx.save()

    ctx.strokeStyle = 'black';
    ctx.lineWidth = 30;
    ctx.beginPath(); // create a line
    ctx.moveTo(x.getPixelForValue(12),y.getPixelForValue(1)) // move to the position that it wants to start drawing
    ctx.lineTo(x.getPixelForValue(12), top) // draw the line to the end position
    ctx.stroke();
  }
}
*/
function drawChart(){
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
              borderWidth: 0,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              grid: {
                drawOnChartArea: false,
                borderWidth: 50,
                width:20,
              },
              ticks: {
                callback: function (label) {
                  let realLabel = this.getLabelForValue(label);
                  var month = realLabel.split(";")[1];
                  return month;
                },
                align: 'center'
                
              },
            },
            xAxis2: {
              type: "category",
              
              ticks: {
                callback: function (label) {
                  let realLabel = this.getLabelForValue(label);
                  var month = realLabel.split(";")[1];
                  var year = realLabel.split(";")[0]-2000;
                  if (month === "1") {
                    return year;
                  } else {
                    return "";
                  }
                },
                align: 'end'
              },
            },
            y: {
              beginAtZero: true,
              grid: {
                borderWidth: 5,
                lineWidth: 0
              },
            },
          },

          backgroundColor: colour,
          //plugins: [multiArbitraryLine]
          
        },
      });
    }
  });
}
  drawChart()


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
      height: 40vh;
      padding-left: 1%;
      padding-right: 5%;
      width: 90vw;
    }
  }
</style>
