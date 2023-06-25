<script>
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';

  let chart;

  onMount(() => {
    const renderChart = () => {
      const ctx = document.getElementById('myChart').getContext('2d');

      const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Italy', 'France', 'Spain', 'USA', 'Argentina'],
          datasets: [
            {
              label: 'World Wine Production 2018',
              data: [55, 49, 44, 24, 15],
              backgroundColor: 'grey',
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });

      chart = myChart;
    };

    // Delay chart rendering until canvas is available in the DOM
    requestAnimationFrame(renderChart);
  });
</script>

<canvas id="myChart"></canvas>

<style>
  canvas {
    width: 1000px;
    max-width: 100px;
    height: 1000px;
  }
</style>
