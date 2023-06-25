<script>
  import Chart from 'chart.js/auto';
  import { onMount } from 'svelte';

  let chartValues = [20, 10, 5, 2, 20, 30, 45];
  let chartLabels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
  let ctx;
  let chartCanvas;

  onMount(async () => {
    ctx = chartCanvas.getContext('2d');
    const chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: chartLabels,
        datasets: [{
          label: 'Revenue',
          backgroundColor: 'rgb(255, 99, 132)',
          borderColor: 'rgb(255, 99, 132)',
          data: chartValues
        }]
      }
    });
  });
</script>

<canvas bind:this={chartCanvas} id="myChart"></canvas>

<style>
  canvas {
    height: 400px;
    width: 80%;
  }
</style>
