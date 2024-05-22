<script>
    import { onMount } from "svelte";
    import maplibregl from "maplibre-gl";
    import positron from "../../data/positron.json";
    import origin from "../../data/bikeshare relations (origin).geo.json";
    import destination from "../../data/bikeshare relations (destination).geo.json";
    import difference from "../../data/bikeshare relations (difference).geo.json";

    let map;
    let prevStation = 7000;
    let station = 7000;
    let stationName = "Fort York Blvd / Capreol Ct";
    let toStation = ""; // displaying the ID of the destination Station
    let toStationName = ""; //displaying the Name of the destination Station
    let trips = 0; // for displaying number of trips between stations
    let stationID = "End Station Id";
    let originFilter = true; // for displaying data that display number of trips from origin station to destination station
    let destinationFilter = false; // for displaying data that display number of trips a destination station receives from origin stations.
    let differenceFilter = false;
    let coordinate = [-79.39595371484756, 43.639831290132605]; // setting the initiating coordinate for lines
    let enterCoordinates = [-79.39595371484756, 43.639831290132605]; // setting the ending coordinate for lines

    function updateSource() {
        /*if{difference}{
            map.getSource('station').setData(destination);
        }*/
        if (originFilter) {
            map.getSource("station").setData(origin);
            map.setLayoutProperty("station-difference-layer", 'visibility', 'none')
            map.setLayoutProperty("station-layer-hover", 'visibility', 'visible')
            map.setLayoutProperty("station-layer-outline", 'visibility', 'visible')
            map.setLayoutProperty("station-layer", 'visibility', 'visible')
            stationID = "End Station Id";
        }  if (destinationFilter) {
            map.getSource("station").setData(destination);
            // turn the layers back on
            map.setLayoutProperty("station-difference-layer", 'visibility', 'none')
            map.setLayoutProperty("station-layer-hover", 'visibility', 'visible')
            map.setLayoutProperty("station-layer-outline", 'visibility', 'visible')
            map.setLayoutProperty("station-layer", 'visibility', 'visible')

            stationID = "Start Station Id";
        }  if (differenceFilter) {
            map.getSource("station").setData(difference);
            map.setLayoutProperty("station-difference-layer", 'visibility', 'visible')
            map.setLayoutProperty("station-layer-hover", 'visibility', 'none')
            map.setLayoutProperty("station-layer-outline", 'visibility', 'none')
            map.setLayoutProperty("station-layer", 'visibility', 'none')
            
        }
    }

    function getInterpolatedRadius(trips) {
    if (trips <= 0) return 5;
    if (trips <= 500) return 5 + (trips / 500) * (25 - 5);
    if (trips <= 1000) return 25 + ((trips - 500) / 500) * (50 - 25);
    return 50;
}

// Esri color ramps - Blue and Orange 2
// #bf5b1dff,#e48043ff,#d6cdcdff,#84a7c4ff,#547a99ff
const colors = ["#a53217ff", "#d2987fff", "#fffee6ff", "#8897a2ff", "#10305eff"];
    
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
            map.addSource("station-difference", {
                type: "geojson",
                data: difference,
            });
            map.addLayer({id: "station-layer",
                type: "circle",
                source: "station",
                paint: {
                    "circle-radius": [
                        "interpolate",
                        ["linear"],
                        ["get", `${station}`], // make it a function of the value
                        0,
                        5,
                        500,
                        35,
                        1000,
                        50,
                    ],
                    "circle-color": [
                        "match",
                        ["get", `${station}`],
                        0,
                        "#DC4633",
                        "#0D534D",
                    ],
                    "circle-opacity": 0.5,
                    "circle-stroke-color": [
                        "match",
                        ["get", `${station}`],
                        0,
                        "white",
                        "#0D534D",
                    ],
                    "circle-stroke-width": 2,
                },
            });
            map.addLayer({id: `label ${station}`,
                type: "symbol",
                source: "station",
                minzoom: 14,
                layout: {
                    "text-field": [
                        "concat",
                        ["get", "Station"],
                        " : ",
                        ["get", `${station}`],
                    ],
                    'text-variable-anchor-offset': ['left', [2, 0]],                        
                    "text-justify": "left",
                },
            });
            map.addLayer({
                id: "station-layer-outline",
                type: "circle",
                source: "station",
                filter: ["==", stationID, station],
                paint: {
                    "circle-radius": [
                        "interpolate",
                        ["linear"],
                        ["get", `${station}`], // make it a function of the value
                        0,
                        5,
                        500,
                        35,
                        1000,
                        50,
                    ],
                    "circle-opacity": 0,
                    "circle-stroke-width": 3,
                    "circle-stroke-color": "#DC4633",
                },
            });
            map.addLayer({id: "station-difference-layer",
                type: "circle",
                source: "station-difference",
                paint: {
                    "circle-color": [
                    "interpolate",
                    ["linear"],
                    ["get", `${station}`],
                    -80, "#a53217ff", 
                    -40, "#d2987fff",
                    0, "#fffee6ff", // Start color (blue) for the lowest value
                    40, "#8897a2ff", // Intermediate color (green)
                    80, "#10305eff" // End color (red) for the highest value
                ], 
                    "circle-radius": 7,
                    "circle-opacity": 1,
                    "circle-stroke-color": "black",
                    "circle-stroke-width": 0.1,
                },
            });
            map.setLayoutProperty("station-difference-layer", 'visibility', 'none')

            map.on("click", "station-layer", function (e) {
                coordinate = e.features[0].geometry.coordinates;
                var feature = e.features[0].properties;

                station = feature[stationID];
                stationName = feature["Station"];
                // remove a few layers to update the display 
                map.removeLayer("station-layer-outline");
                map.removeLayer("station-layer");
                map.removeLayer(`label ${prevStation}`);

                map.addLayer({id: "station-layer",
                    type: "circle",
                    source: "station",
                    paint: {
                        "circle-radius": [
                            "interpolate",
                            ["linear"],
                            ["get", `${station}`], // make it a function of the value
                            0, 5,
                            500,35,
                            1000, 50,
                        ],
                        "circle-color": [
                            "match",
                            ["get", `${station}`],
                            0,"red","#0D534D",
                        ],
                        "circle-opacity": 0.5,
                        "circle-stroke-width": 1,
                        "circle-stroke-color": [
                            "match",
                            ["get", `${station}`],
                            0,"white","#0D534D",
                        ],
                    },
                });
                map.addLayer({id: "station-layer-outline",
                    type: "circle",
                    source: "station",
                    filter: ["==", stationID, station],
                    paint: {
                        "circle-radius": [
                            "interpolate",
                            ["linear"],
                            ["get", `${station}`], // make it a function of the value
                            0,
                            5,
                            500,
                            35,
                            1000,
                            50,
                        ],
                        "circle-opacity": 0,
                        "circle-stroke-width": 3,
                        "circle-stroke-color": "#DC4633",
                    },
                });
                map.addLayer({id: `label ${station}`,
                    type: "symbol",
                    source: "station",
                    minzoom: 13,
                    layout: {
                        "text-field": [
                            "concat",
                            ["get", "Station"],
                            " : ",
                            ["get", `${station}`],
                        ],
                    'text-variable-anchor-offset': ['left', [ 2, 0]],                        
                    "text-justify": "left",
                    },
                });
                
                prevStation = station;
            });
            map.on("click", "station-difference-layer", function (e) {
                var feature = e.features[0].properties;
                station = feature["Start Station Id"];
                map.removeLayer("station-difference-layer");
                map.addLayer({id: "station-difference-layer",
                    type: "circle",
                    source: "station-difference",
                    paint: {
                        "circle-color": [
                        "interpolate",
                        ["linear"],
                        ["get", `${station}`],
                        -80, "#a53217ff", 
                        -40, "#d2987fff",
                        0, "#fffee6ff", // Start color (blue) for the lowest value
                        40, "#8897a2ff", // Intermediate color (green)
                        80, "#10305eff" // End color (red) for the highest value
                    ], 
                        "circle-radius": 7,
                        "circle-opacity": 1,
                        "circle-stroke-color": "black",
                        "circle-stroke-width": 0.1,
                    },
                });
            })


            // Boundary of map

            map.fitBounds([
                [-79.14904366238247, 43.87527014932047],
                [-79.60668327438583, 43.56196116510192],
            ]);

            map.on("mouseenter", "station-layer", (e) => {
                map.getCanvas().style.cursor = "pointer";
                enterCoordinates = e.features[0].geometry.coordinates;
                var feature = e.features[0].properties;

                toStation = feature[stationID];
                toStationName = feature["Station"];
                trips = feature[station];


                map.addSource(`line-${enterCoordinates}`, {
                    type: "geojson",
                    data: {
                        type: "Feature",
                        proterties: {},
                        geometry: {
                            type: "LineString",
                            coordinates: [coordinate, enterCoordinates],
                        },
                    },
                });
                // a line created on the fly to link two stations together
                map.addLayer({id: `station-to-station-${enterCoordinates}`,
                    type: "line",
                    source: `line-${enterCoordinates}`,
                    paint: {
                        "line-color": "#F1C500",
                        "line-width": 8,
                    },
                });
                map.addLayer({id: "station-layer-hover",
                    type: "circle",
                    source: "station",
                    filter: ["==", stationID, toStation],
                    paint: {
                        "circle-radius": [
                            "interpolate",
                            ["linear"],
                            ["get", `${station}`], // make it a function of the value
                            0,
                            5,
                            500,
                            35,
                            1000,
                            50,
                        ],
                        "circle-opacity": 0,
                        "circle-stroke-width": 3,
                        "circle-stroke-color": "#F1C500",
                    },
                });
            });

            map.on("mouseleave", "station-layer", () => {
                map.getCanvas().style.cursor = "";
                map.removeLayer("station-layer-hover");
                map.removeLayer(`station-to-station-${enterCoordinates}`);
                map.removeSource(`line-${enterCoordinates}`);
            });
        });
    });
</script>

<main>
    <div id="map" class="map" />

    <div class="info-panel">
        <h1>Bikeshare Toronto Stations Relations</h1>
        {#if originFilter}
            <h2>{trips} trips from</h2>
            <h3>{station} &nbsp {stationName}</h3>
            <h2>to</h2>
            <h3>{toStation} &nbsp {toStationName}</h3>
        {:else if destinationFilter}
            <h2>{trips} trips from</h2>
            <h3>{toStation} &nbsp {toStationName}</h3>
            <h2>to</h2>
            <h3>{station} &nbsp {stationName}</h3>
        {/if}

        <div class="buttons-box">
            <button
                class="application-button"
                on:click={() => {
                    originFilter = !originFilter;
                    destinationFilter = false;
                    differenceFilter = false;
                    updateSource();
                }}
                style="background-color: {originFilter
                    ? '#a9d6e5'
                    : ''}; color: 'black'"
                ><p>
                    Displaying The Number of Trips From <br /> Clicked Station To
                    Hovered Destination
                </p></button
            ><button
                class="application-button"
                on:click={() => {
                    destinationFilter = !destinationFilter;
                    differenceFilter = false;
                    originFilter = false;
                    updateSource();
                }}
                style="background-color: {destinationFilter
                    ? '#a9d6e5'
                    : ''}; color: 'black'"
                ><p>
                    Displaying The Number of Trips From <br /> Hovered Station To
                    Clicked Destination
                </p></button
            ><button
                class="application-button"
                on:click={() => {
                    differenceFilter = !differenceFilter;
                    originFilter = false;
                    destinationFilter = false;

                    updateSource();
                }}
                style="background-color: {differenceFilter
                    ? '#a9d6e5'
                    : ''}; color: 'black'"><p>Difference ( Greater than 0 means more trips from clicked station to another station <br> Smaller than 0 means more trips from the destination station to the clicked station. )</p></button
            >
        </div>
    </div>
</main>

<style>
    main {
        overflow-x: hidden;
    }
    .map {
        height: 70vh;
        width: 100vw;
        top: 0;
        left: 0%;
        position: absolute;
        overflow: hidden;
    }
    .info-panel {
        position: absolute;
        top: 70vh;
        left: 0px;
        width: 100vw;
        height: 30vh;
        font-size: 17px;
        font-family: sans-serif;
        background-color: rgb(254, 251, 249, 1);
        color: #1e3765;
        overflow-x: hidden;
        scrollbar-width: 1px;
        margin: 0 auto;
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
        padding-top: 5px;
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
        font-size: 18px;
        padding-top: 0px;
        padding-left: 10px;
        padding-right: 10px;
        padding-bottom: 5px;
        margin-bottom: 5px;

    }
    a {
        color: #41729f;
    }
    .application-button {
        font-size: 12px;
        width: auto;
        height: auto;
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
</style>
