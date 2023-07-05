<script>
  import Chart from "chart.js/auto";
  import data from "/src/data/data.json";
  import { onMount } from "svelte";

  export let labelList; // x-axis labels
  export let variable;
  export let colour;


  var width, height;
  var displays;
  window.onresize = window.onload = function () {
    width = this.innerWidth;
    height = this.innerHeight;
    if (width < 1200){
      console.log(width);
      displays = false
      console.log(displays)
    }
    else{
      displays = true
    }
  };

  function extractValues(data, variable) {
    const values = data.map((item) => item[variable]);
    return values;
  }
 
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
              display: displays, 
              grid: {
                drawOnChartArea: false,
                color: 'black'
                
              },
              border:{
                width: 2
              },
              ticks: {
                autoSkip: false,
                maxRotation: 0,
                minRotation: 0,
                callback: function (label) {
                  let realLabel = this.getLabelForValue(label);
                  var month = realLabel.split(";")[1];
                  return month;
                },
                align: "center",
              },
            },
            x2: {
              ticks: {
                autoSkip: false,
                maxRotation: 0,
                minRotation: 0,
                callback: function (label) {
                  let realLabel = this.getLabelForValue(label);
                  
                  var year = realLabel.split(";")[0];
                  if (realLabel.split(";")[1] === "2") {
                    return year;
                  } else {
                    return "";
                  }
                },
                align: "end",
              },
            },
            y: {
              beginAtZero: true,
              grid: {
                borderWidth: 5,
                lineWidth: 1,
              },
              border:{
                width: 2
              }
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
