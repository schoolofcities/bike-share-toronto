<script>
  import Chart from "chart.js/auto";
  import data from "/src/data/data.json";
  import { onMount } from "svelte";

  export let variable; // the list of data
  export let colour;
  export let chartName;

  function extractValues(data, variable) {
    const values = data.map((item) => item[variable]);
    return values;
  }

  var labelList = extractValues(data, "YearMonth"); // x-axis labels
  var dataList = extractValues(data, variable);

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
  function drawChart() {
    onMount(() => {
      const ctx = document.getElementById(chartName);

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
                  color: (context) =>{
                    console.log(context)
                    var i =0;
                    while (i< labelList.length){
                      console.log(context.tick.value)
                      i++;
                    }
                    
                    
                    var tickIndex = context.index;
                    
                    if (context.index === 20){
                      return "#DC4633";
                    }
                    else{
                      return 'grey'
                    }
                  }
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
              xAxis2: {
                type: "category",

                ticks: {
                  autoSkip: false,
                  maxRotation: 0,
                  minRotation: 0,
                  callback: function (label) {
                    let realLabel = this.getLabelForValue(label);
                    var month = realLabel.split(";")[1];
                    var year = realLabel.split(";")[0] - 2000;
                    if (month === "1") {
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
                  lineWidth: 0,
                },
              },
            },

            backgroundColor: colour =>{
              let colours;
              if (Math.floor(colour.index/12)==0){
                colours = '#1E3765'
              }
              else if (Math.floor(colour.index/12)==1){
                colours = '#F1C500'
              }
              else {
              colours = '#000000'
              }
              return colours;
            },
            //plugins: [multiArbitraryLine]
            plugins: {
              legend: {
                display: true,
              },
            },
          },
        });
      }
    });
  }
  drawChart();
  window.onload = function () {
    console.log(window.innerWidth);
    if (window.innerWidth >= 1100) {
      Chart.defaults.font.size = 60;
      console.log(window.innerWidth);
      drawChart()
    } else {
      Chart.defaults.font.size = 10;
      drawChart();
    }
    //Chart.options.scales.ticks.display = true;
  };
</script>

<div>
  <canvas id={chartName} style="height: 400px; width: 100%;" />
</div>

<style>
  div {
    height: 50vh;
    padding-left: 10%;
    padding-right: 10%;
    width: 80%;
  }
  @media screen and (max-width: 1100px) {
    div {
      height: 40vh;
      padding-left: 1%;
      padding-right: 5%;
      width: 90vw;
    }
  }
</style>
