
  function chartFunction(chartName, labelList, labelName, dataList, colour) {
    
    const ctx = document.getElementById(chartName);
  
    new Chart(ctx, {
      type: "bar",
      
      data: {
        labels: labelList,
        datasets: [{
          label: labelName,
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
  }