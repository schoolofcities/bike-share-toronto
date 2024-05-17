<script>
    import { onMount, afterUpdate } from "svelte";
    import maplibregl from "maplibre-gl";
    import positron from "../../data/positron.json";
    import origin from "../../data/bikeshare relations (origin).geo.json";
    import destination from "../../data/bikeshare relations (destination).geo.json";
    import difference  from "../../data/bikeshare relations (difference).geo.json";
    import * as turf from "@turf/turf"; // this is for fitting the map boundary to GTA municipalities

    //import BaseLayer from "../data/pmtiles.json";
    //import * as pmtiles from "pmtiles";
    /*
    var wards = [ward1,ward2,ward3,ward4,ward5,ward6,ward7,ward8,ward9,ward10,ward11,ward12,ward13,ward14,ward15,ward16,ward17,ward18,ward19,
    ward20,ward21,ward22,ward23,ward24,ward25]

    //import geojsonvt from "geojson-vt";
    //import property from "../data/properties.geo.json";
    //import developments from "../data/development-application.geojson"
    */
    let map;
    let query = ""; //This is the input address from users.
    let distance = ""; // This is the input for buffer distance
    let dist;
    let lat;
    let lon;
    let results;
    let station = 7000;
    let stationName = "Fort York Blvd / Capreol Ct"
    let toStation = ""
    let toStationName = ""
    let popup = false;
    let trips;
    let stationID = "End Station Id"
    let originFilter = true;
    let destinationFilter = false;
    let differenceFilter = false;

    function updateSource(){
        /*if{difference}{
            map.getSource('station').setData(destination);
        }*/
        if(originFilter){
            map.getSource('station').setData(origin);
            stationID = "End Station Id"
        }
        if(destinationFilter){
            map.getSource('station').setData(destination);
            stationID = "Start Station Id"
        }
        
    }

    onMount(() => {
        //let protocol = new pmtiles.Protocol();

        //maplibregl.addProtocol("pmtiles", protocol.tile);
        map = new maplibregl.Map({
            container: "map",
            style: positron, //'https://basemaps.cartocdn.com/gl/positron-gl-style/style.json',
            center: [-79.4, 43.68], // starting position
            minZoom: 11,
            maxZoom: 19,
            scrollZoom: true,
            attributionControl: false,
        });
        map.on("load", () => {
            map.addSource("station", {
                type: "geojson",
                data: origin,
            });

            map.addLayer({id: "station-layer",
                type: "circle",
                source: "station",
                paint: {
                    "circle-radius": [
                        "interpolate",
                        ['linear'],
                        ["get", `${station}`], // make it a function of the value
                        0, 5,
                        500, 25,
                        1000, 50
                    ],
                    "circle-color": [
                        "match",
                        ["get", `${station}`],
                        0, "#DC4633",
                        "#0D534D"
                ]
                        ,
                    "circle-opacity": 0.5,
                    "circle-stroke-color" : [
                        "match",
                        ["get", `${station}`],
                        0, "white",
                        "#0D534D"
                    ],
                    "circle-stroke-width" : 2,
                },
            });
            map.addLayer({id: "station-layer-outline",
                    type: "circle",
                    source: "station",
                    filter: ['==', stationID, station],
                    paint: {
                        "circle-radius": [
                            "interpolate",
                        ['linear'],
                        ["get", `${station}`], // make it a function of the value
                        0, 5,
                        500, 25,
                        1000, 50,],
                        "circle-opacity" : 0,
                        "circle-stroke-width" : 2,
                        "circle-stroke-color" : "#DC4633"

                    },
                });
            map.on("click", "station-layer", function (e) {
                var coordinate = e.features[0].geometry.coordinates;
                console.log(coordinate)
                //const description = e.features[0].properties.description;
                var feature  = e.features[0].properties

                station = feature[stationID];
                stationName = feature['Station']
                
                console.log(station)
             
                map.removeLayer('station-layer-outline');
                map.removeLayer('station-layer');

                map.addLayer({
                    id: "station-layer",
                    type: "circle",
                    source: "station",
                    paint: {
                        "circle-radius": [
                            "interpolate",
                        ['linear'],
                        ["get", `${station}`], // make it a function of the value
                        0, 5,
                        500, 25,
                        1000, 50,
                        ],
                        
                    "circle-color": [
                        "match",
                        ["get", `${station}`],
                        0, "red",
                        "#0D534D"
                ],
                        "circle-opacity": 0.5,
                        "circle-stroke-width" : 1,
                        "circle-stroke-color"  : [
                        "match",
                        ["get", `${station}`],
                        0, "white",
                        "#0D534D"
                    ],
                    },
                });
                map.addLayer({
                    id: "station-layer-outline",
                    type: "circle",
                    source: "station",
                    filter: ['==', stationID, station],
                    paint: {
                        "circle-radius": [
                            "interpolate",
                        ['linear'],
                        ["get", `${station}`], // make it a function of the value
                        0, 5,
                        500, 25,
                        1000, 50,
                        ],
                        "circle-opacity": 0,
                        "circle-stroke-width" : 1,
                        "circle-stroke-color" : "red"

                    },
                });
 
            });

            
            // Boundary of map
            map.fitBounds([
                [-79.14904366238247, 43.87527014932047],
                [-79.60668327438583, 43.56196116510192],
            ]);

            map.on("mouseenter", "station-layer", (e) => {
                map.getCanvas().style.cursor = "pointer";
                var feature = e.features[0].properties
                toStation = feature[stationID]
                toStationName = feature['Station']
                trips = feature[station]

                map.addLayer({id: "station-layer-hover",
                    type: "circle",
                    source: "station",
                    filter: ['==', stationID, toStation],
                    paint: {
                        "circle-radius": [
                            "interpolate",
                        ['linear'],
                        ["get", `${station}`], // make it a function of the value
                        0, 5,
                        500, 25,
                        1000, 50,
                        ],
                        "circle-opacity": 0,
                        "circle-stroke-width" : 3,
                        "circle-stroke-color" : "#F1C500"

                    },
                });

            });

            map.on("mouseleave", "station-layer", () => {
                map.getCanvas().style.cursor = "";
                map.removeLayer('station-layer-hover');
            });
        });
    });
    
</script>

<main>
    <div id="map" class="map" />

    <div class="info-panel">
        <h1>Bikeshare Toronto Stations Relations</h1>
        <h2> {trips} trips from </h2>
        <h3> {station} &nbsp {stationName} </h3>
        <h2>to </h2>
        <h3> {toStation} &nbsp {toStationName}</h3>
        
        <div class="buttons-box">
        <button
                class="application-button"
                on:click={() => {
                    originFilter = !originFilter
                    destinationFilter = false
                    updateSource()
                }}
                style="background-color: {originFilter
                    ? '#a9d6e5'
                    : ''}; color: 'black'">Origin - Destination</button
            ><button
            class="application-button"
            on:click={() => {
                destinationFilter = !destinationFilter
                originFilter = false
                updateSource()
            }}
            style="background-color: {destinationFilter
                ? '#a9d6e5'
                : ''}; color: 'black'">Destination - Origin</button
        ><!--<button
        class="application-button"
        on:click={() => {
            differenceFilter != differenceFilter
            updateSource()
        }}
        style="background-color: {differenceFilter
            ? '#a9d6e5'
            : ''}; color: 'black'">Difference</button
    >-->

    </div>
</div>
</main>

<style>
    main {
        overflow-x: hidden;
    }
    .map {
        height: 60vh;
        width: 100vw;
        top: 0;
        left: 0%;
        position: absolute;
        overflow: hidden;
    }
    .info-panel {
        position: absolute;
        top: 60vh;
        left: 0px;
        width: 100vw;
        height: 40vh;
        font-size: 17px;
        font-family: sans-serif;
        background-color: rgb(254, 251, 249, 1);
        color: #1e3765;
        overflow-x: hidden;
        scrollbar-width: 1px;
    }
    .application {
        left: 10px;
        width: 35vw - 20px;
        height: auto;
        padding-top: 0px;
        background-color: #d3d3d3;
        margin-right: 20px;
        margin-top: 2px;
        position: relative;
        scrollbar-width: 1px;
    }
    .buttons-box {
        left: 0px;
        width: 35vw - 20px;
        height: auto;
        padding-top: 2px;
        margin-right: 20px;
        position: relative;
    }
    h1 {
        font-size: 30px;
        padding-top: 20px;
        padding-left: 10px;
        /*padding-bottom: 3px;*/
        margin: 0px;
        margin-bottom: 0px;
        color: #1e3765;
        /* background-color: #F1C500; */
        /* -webkit-text-stroke: 1px #6FC7EA; */
        font-weight: bold;
    }
    h2 {
        font-size: 20px;

        padding-top: 20px;
        padding-left: 10px;

        /*padding-bottom: 3px;*/
        margin: 0px;
        margin-bottom: 0px;
        color: #1e3765;
        /* background-color: #F1C500; */
        /* -webkit-text-stroke: 1px #6FC7EA; */
        font-weight: bold;
    }
    h3 {
        font-size: 18px;

        padding-top: 10px;
        padding-left: 10px;
        /*padding-bottom: 3px;*/
        margin: 0px;
        margin-bottom: 0px;
        color: #41729f;
        /* background-color: #F1C500; */
        /* -webkit-text-stroke: 1px #6FC7EA; */
        font-weight: bold;
    }
    p {
        padding-top: 0px;
        padding-left: 10px;
        padding-right: 20px;
        padding-bottom: 5px;
        margin-bottom: 20px;
    }
    a {
        color: #41729f;
    }
    .application-button {
        font-size: 12px;
        width: auto;
        height: 28px;
        left: 10px;
        margin-right: 5px;
        margin-bottom: 5px;
        border-width: 0px;
        position: relative;
        font-weight: bold;
    }

    /* Searh Address */
    input {
        left: 10px;
        width: 24vw;
        height: 20px;

        color: #6d247a;
        border-width: 1px;
        margin-right: 5px;

        padding-left: 2px;
        padding-top: 3px;
        padding-bottom: 3px;

        font-weight: bold;
        position: relative;
        border-color: grey;
    }
    .address-button {
        left: 10px;
        width: 24%;
        height: 28px;

        border-width: 1px;
        margin-right: 5px;

        font-weight: bold;
        position: relative;
        border-color: grey;
    }
    /* SCROLL BARS */
    ::-webkit-scrollbar {
        width: 5px;
    } /* Track */
    ::-webkit-scrollbar-track {
        box-shadow: inset 0 0 5px grey;
        border-radius: 5px;
    }

    /* Handle */
    ::-webkit-scrollbar-thumb {
        background: #41729f;
        border-radius: 5px;
    }

    /* Handle on hover */
    ::-webkit-scrollbar-thumb:hover {
        background: #41729f;
    }
    .application-button {
        font-size: 12px;
        width: auto;
        height: 28px;
        left: 10px;
        margin-right: 5px;
        margin-bottom: 5px;
        border-width: 0px;
        position: relative;
        font-weight: bold;
    }


</style>
