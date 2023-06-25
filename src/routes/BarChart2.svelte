<script>
    import { onMount } from 'svelte';
  
    let myChart;
  
    onMount(() => {
      // Get the canvas element
      const ctx = document.getElementById('myChart').getContext('2d');
  
      // Create the chart
      myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Label 1', 'Label 2', 'Label 3'], // Array of labels for the x-axis
          datasets: [
            {
              label: 'My Dataset', // Label for the dataset
              data: [10, 20, 30], // Array of data values
              backgroundColor: 'rgba(0, 123, 255, 0.5)', // Background color of the bars
            },
          ],
        },
        options: {
          responsive: true, // Make the chart responsive
          scales: {
            y: {
              beginAtZero: true, // Start the y-axis at zero
            },
          },
        },
      });
    });
  </script>
  
  <canvas id="myChart"></canvas>
  
  <style>
    canvas {
      max-width: 600px;
      margin: 0 auto;
    }
  </style>
  