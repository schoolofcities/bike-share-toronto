<script>

import "../assets/global-styles.css";
import Bicycle from "../assets/bicycle.svg";

var data = [
    { Year: 2015, Ridership: 667000 },
    { Year: 2016, Ridership: 834235 },
    { Year: 2017, Ridership: 1510802 },
    { Year: 2018, Ridership: 1975384 },
    { Year: 2019, Ridership: 2400384 },
    { Year: 2020, Ridership: 2900000 },
    { Year: 2021, Ridership: 3575000 },
    { Year: 2022, Ridership: 4600000 },
];

</script>


{#each data as d}

    <div id="wrapper">
        <p><b>{d.Year}</b> / {d.Ridership.toLocaleString()} Trips</p>
        <div class="all-bike-img">
            {#each Array(Math.round(d.Ridership / 10000)) as _}
                <img class="bike-img" src={Bicycle} alt="Bike">
            {/each}
        </div>
    </div>

{/each}




<style>
    #wrapper {
        width: 100%;
        /* max-width: 800px; */
        /* align-content: center; */
    }
    p {
        margin-bottom: -1px;
        font-size: 13px;
        line-height: 14px;
        border-bottom: solid 1px rgba(25, 107, 66, 0.501);
    }
    .all-bike-img {
        margin-top: 3px;
        margin-bottom: 20px;
    }
    .bike-img {
        max-width: 18px;
        max-height: 12px;
        padding-right: 2px;
    }
    b {
        color: var(--brandYellow);
    }
</style>