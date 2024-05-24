<script>
    import { onMount } from "svelte";
    import maplibregl from "maplibre-gl";
    import positron from "../../data/positron.json";
    import origin from "../../data/bikeshare relations (origin).geo.json";
    import destination from "../../data/bikeshare relations (destination).geo.json";
    import difference from "../../data/bikeshare relations (difference).geo.json";
    import "../../assets/global-styles.css";

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

    
    // update displayed datat based on the buttons clicked. 
    function updateSource() {
        if (destinationFilter ===  false && differenceFilter === false && originFilter === false){
            console.log("Non-clicked, default to origin")
            originFilter = true
        }
        if (originFilter) {
            console.log("Origin:", station)
            stationID = "End Station Id";

            map.getSource("station").setData(origin);

            map.setLayoutProperty("station-layer", "visibility", "visible");

            map.setLayoutProperty("station-difference-layer","visibility","none");
            map.setLayoutProperty("station-difference-layer-outline","visibility","none");
            
            //remove the label from the previous display and change to current displayed data values
            map.removeLayer(`label ${prevStation}`);
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
                    "text-font": ["Open Sans Bold", "Arial Unicode MS Bold"], // Example fonts
                    "text-size": 14, // Font size
                    "text-variable-anchor-offset": ["left", [2, 0]],
                    "text-justify": "left",
                },
                paint: {
                    "text-color": "#4d4d4d", // Text color
                    "text-halo-color": "#ffffff", // Optional: text halo color for better readability
                    "text-halo-width": 1.1, // Optional: halo width
                },
            });

            map.removeLayer("station-layer-outline");
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

            
        }
        if (destinationFilter) {
            console.log("Destination:", station)
            map.getSource("station").setData(destination);
            
            stationID = "Start Station Id";
            // turn the layers back on
            map.setLayoutProperty("station-difference-layer","visibility", "none");
            map.setLayoutProperty("station-difference-layer-outline","visibility","none",);
            
            //remove the label from the previous display and change to current displayed data values
            map.setLayoutProperty("station-layer", "visibility", "visible");

            map.removeLayer(`label ${prevStation}`);
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
                    "text-font": ["Open Sans Bold", "Arial Unicode MS Bold"], // Example fonts
                    "text-size": 14, // Font size
                    "text-variable-anchor-offset": ["left", [2, 0]],
                    "text-justify": "left",
                },
                paint: {
                    "text-color": "#4d4d4d", // Text color
                    "text-halo-color": "#ffffff", // Optional: text halo color for better readability
                    "text-halo-width": 1.1, // Optional: halo width
                },
            });

            map.removeLayer("station-layer-outline");
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
            
        }
        if (differenceFilter) {
            console.log("Difference:", station)
            map.setLayoutProperty("station-difference-layer", "visibility","visible");
            map.setLayoutProperty("station-layer-outline", "visibility", "none");
            map.setLayoutProperty("station-layer", "visibility", "none");
            //remove the label from the previous display and change to current displayed data values
            map.removeLayer(`label ${prevStation}`);
            map.addLayer({id: `label ${station}`,
                    type: "symbol",
                    source: "station-difference",
                    minzoom: 14,
                    layout: {
                        "text-field": [
                            "concat",["get", "Station"],
                            " : ",
                            ["get", `${station}`],
                        ],
                        "text-font": [
                            "Open Sans Bold",
                            "Arial Unicode MS Bold",
                        ], // Example fonts
                        "text-size": 14, // Font size
                        "text-variable-anchor-offset": ["left", [2, 0]],
                        "text-justify": "left",
                    },
                    paint: {
                        "text-color": "#4d4d4d", // Text color
                        "text-halo-color": "#ffffff", // Optional: text halo color for better readability
                        "text-halo-width": 1.1, // Optional: halo width
                    },
                });
            
            map.removeLayer("station-difference-layer-outline");
            map.addLayer({id: "station-difference-layer-outline", // this is to show the outline of the clicked station
                type: "circle",
                source: "station-difference",
                filter: ["==", "Start Station Id", station],
                paint: {
                    "circle-radius": 7,
                    "circle-opacity": 0,
                    "circle-stroke-width": 5,
                    "circle-stroke-color": "#DC4633",
                },
            });

            map.removeLayer("station-difference-layer");
            map.addLayer({id: "station-difference-layer",
                type: "circle",
                source: "station-difference",
                paint: {
                    "circle-color": [
                        "interpolate",
                        ["linear"],
                        ["get", `${station}`],
                        -80,
                        "#a53217ff",
                        -40,
                        "#d2987fff",
                        0,
                        "white", // Start color (blue) for the lowest value
                        40,
                        "#8897a2ff", // Intermediate color (green)
                        80,
                        "#10305eff", // End color (red) for the highest value
                    ],
                    "circle-radius": 7,
                    "circle-opacity": 1,
                    "circle-stroke-color": "#4d4d4d",
                    "circle-stroke-width": 1,
                },
            });
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
                    "text-font": ["Open Sans Bold", "Arial Unicode MS Bold"], // Example fonts
                    "text-size": 14, // Font size
                    "text-variable-anchor-offset": ["left", [2, 0]],
                    "text-justify": "left",
                },
                paint: {
                    "text-color": "#4d4d4d", // Text color
                    "text-halo-color": "#ffffff", // Optional: text halo color for better readability
                    "text-halo-width": 1.1, // Optional: halo width
                },
            });
            // outline on hovering over points
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
            map.addLayer({id: "station-difference-layer",
                type: "circle",
                source: "station-difference",
                paint: {
                    "circle-color": [
                        "interpolate",
                        ["linear"],
                        ["get", `${station}`],
                        -50,
                        "#a53217ff",
                        -25,
                        "#d2987fff",
                        0,
                        "white", // Start color (blue) for the lowest value
                        25,
                        "#8897a2ff", // Intermediate color (green)
                        50,
                        "#10305eff", // End color (red) for the highest value
                    ],
                    "circle-radius": 7,
                    "circle-opacity": 1,
                    "circle-stroke-color": "#4d4d4d",
                    "circle-stroke-width": 1,
                },
            });
            // outline on hovering over points
            map.addLayer({id: "station-difference-layer-outline",
                type: "circle",
                source: "station-difference",
                filter: ["==", stationID, station],
                paint: {
                    "circle-radius": 7,
                    "circle-opacity": 0,
                    "circle-stroke-width": 3,
                    "circle-stroke-color": "#DC4633",
                },
            });
            // turn the difference layers off for now. 
            map.setLayoutProperty("station-difference-layer",
                "visibility",
                "none",
            );
            map.setLayoutProperty("station-difference-layer-outline","visibility","none",
            );
            // On Click 
            map.on("click", "station-layer", function (e) {
                coordinate = e.features[0].geometry.coordinates;
                var feature = e.features[0].properties;

                station = feature[stationID];
                stationName = feature["Station"];
                // remove a few layers to update the display
                map.removeLayer("station-layer-outline");
                map.removeLayer("station-layer");
                map.removeLayer(`label ${prevStation}`);

                map.addLayer({id: "station-layer", // this is to show the data
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
                            "red",
                            "#0D534D",
                        ],
                        "circle-opacity": 0.5,
                        "circle-stroke-width": 1,
                        "circle-stroke-color": [
                            "match",
                            ["get", `${station}`],
                            0,
                            "white",
                            "#0D534D",
                        ],
                    },
                });
                map.addLayer({id: "station-layer-outline", // this is to show the outline of the clicked station
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
                map.addLayer({id: `label ${station}`, // label the station
                    type: "symbol",
                    source: "station",
                    minzoom: 14,
                    layout: {
                        "text-field": [
                            "concat",                            ["get", "Station"],
                            " : ",
                            ["get", `${station}`],
                        ],
                        "text-font": [
                            "Open Sans Bold",
                            "Arial Unicode MS Bold",
                        ], // Example fonts
                        "text-size": 14, // Font size
                        "text-variable-anchor-offset": ["left", [2, 0]],
                        "text-justify": "left",
                    },
                    paint: {
                        "text-color": "#4d4d4d", // Text color
                        "text-halo-color": "#ffffff", // Optional: text halo color for better readability
                        "text-halo-width": 1.1, // Optional: halo width
                    },
                });
                prevStation = station;
            });
            // On click for the difference in origin and destination ridership
            map.on("click", "station-difference-layer", function (e) {
                coordinate = e.features[0].geometry.coordinates;
                var feature = e.features[0].properties;
                stationName = feature["Station"];
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
                            -80,
                            "#a53217ff",
                            -40,
                            "#d2987fff",
                            0,
                            "white", // Start color (blue) for the lowest value
                            40,
                            "#8897a2ff", // Intermediate color (green)
                            80,
                            "#10305eff", // End color (red) for the highest value
                        ],
                        "circle-radius": 7,
                        "circle-opacity": 1,
                        "circle-stroke-color": "#4d4d4d",
                        "circle-stroke-width": 1,
                    },
                });
                map.removeLayer("station-difference-layer-outline");
                map.addLayer({id: "station-difference-layer-outline", // this is to show the outline of the clicked station
                    type: "circle",
                    source: "station-difference",
                    filter: ["==", "Start Station Id", station],
                    paint: {
                        "circle-radius": 7,
                        "circle-opacity": 0,
                        "circle-stroke-width": 5,
                        "circle-stroke-color": "#DC4633",
                    },
                });
                map.removeLayer(`label ${prevStation}`);
                map.addLayer({id: `label ${station}`,
                    type: "symbol",
                    source: "station-difference",
                    minzoom: 14,
                    layout: {
                        "text-field": [
                            "concat",["get", "Station"],
                            " : ",
                            ["get", `${station}`],
                        ],
                        "text-font": [
                            "Open Sans Bold",
                            "Arial Unicode MS Bold",
                        ], // Example fonts
                        "text-size": 14, // Font size
                        "text-variable-anchor-offset": ["left", [2, 0]],
                        "text-justify": "left",
                    },
                    paint: {
                        "text-color": "#4d4d4d", // Text color
                        "text-halo-color": "#ffffff", // Optional: text halo color for better readability
                        "text-halo-width": 1.1, // Optional: halo width
                    },
                });
                prevStation = station;
            });

            // Boundary of map

            map.fitBounds([
                [-79.14904366238247, 43.87527014932047],
                [-79.60668327438583, 43.56196116510192],
            ]);
            map.on("mouseenter", "station-difference-layer", (e) => {
                map.getCanvas().style.cursor = "pointer";
                enterCoordinates = e.features[0].geometry.coordinates;
                var feature = e.features[0].properties;

                toStation = feature["Start Station Id"];
                toStationName = feature["Station"];
                trips = feature[station];
                console.log(toStation)

                map.addSource(`line-difference-${enterCoordinates}`, {
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
                map.addLayer({id: `station-to-station-difference-${enterCoordinates}`,
                    type: "line",
                    source: `line-difference-${enterCoordinates}`,
                    paint: {
                        "line-color": "#F1C500",
                        "line-width": 8,
                    },
                });
                map.addLayer({id: "station-difference-layer-hover",
                    type: "circle",
                    source: "station-difference",
                    filter: ["==", "Start Station Id", toStation],
                    paint: {
                        "circle-color": [
                            "interpolate",
                            ["linear"],
                            ["get", `${station}`],
                            -80,
                            "#a53217ff",
                            -40,
                            "#d2987fff",
                            0,
                            "white", 
                            40,
                            "#8897a2ff", 
                            80,
                            "#10305eff",
                        ],
                        "circle-radius": 7,
                        "circle-opacity": 1,
                        "circle-stroke-width": 3,
                        "circle-stroke-color": "#F1C500",
                    },
                });
            })

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
            map.on("mouseleave", "station-difference-layer", () => {
                map.getCanvas().style.cursor = "";
                map.removeLayer("station-difference-layer-hover");
                map.removeLayer(`station-to-station-difference-${enterCoordinates}`);
                map.removeSource(`line-difference-${enterCoordinates}`);
            });
        });
    });
</script>

    <div id="map" class="map" />

    <div class="info-panel">
        <h1>Bikeshare Toronto Stations Relations</h1>
        
        {#if originFilter}
            <h2>{station} {stationName}</h2>
            <h4>{trips}</h4><h5>trips from this station</h5>
            <h5>to</h5>
            <h4>{toStation} &nbsp {toStationName}</h4>
        {:else if destinationFilter}
            <h2>{station} {stationName}</h2>
            <h4>{trips}</h4><h5>trips from</h5>
            <h4>{toStation} &nbsp {toStationName}</h4>
            <h5>to this station</h5>
        {:else if differenceFilter}
            {#if trips > 0}
                <h2>{station} {stationName}</h2>
                <h5> Riders tend to bike from this station to </h5><h4>{toStationName}</h4>
                <br><h5> with </h5>
                <h4>{trips}</h4><h5>more trip(s) from</h5>
                <h4>{stationName}</h4><h5>to</h5><h4>{toStationName}</h4>
                <h5>than from</h5>
                <h4>{toStationName}</h4> <h5>to</h5><h4>{stationName}</h4>
            
            {:else if trips < 0}
                <h2>{station} {stationName}</h2>
                <h5> Riders tend to bike from </h5><h4>{toStationName}</h4> <h5>to this station</h5>
                <br><h5> with </h5>
                <h4>{Math.abs(trips)}</h4><h5>more trip(s) from</h5>
                <h4>{toStationName}</h4> <h5>to</h5><h4>{stationName}</h4>
                <h5>than from</h5>
                <h4>{stationName}</h4><h5>to</h5><h4>{toStationName}</h4> 
                

            {:else if trips == 0}
                <h2>{station} {stationName}</h2>
                <h4>{trips}</h4><h5>trip difference. </h5>
            {/if}
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
                    ? '#1E3765'
                    : '#4d4d4d'}; color: 'black'"
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
                    ? '#1E3765'
                    : '#4d4d4d'}; color: 'black'"
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
                    ? '#1E3765'
                    : '#4d4d4d'}; color: 'black'"
                ><p>
                    Difference ( Greater than 0 means more trips from clicked
                    station to another station <br /> Smaller than 0 means more trips
                    from the destination station to the clicked station. )
                </p></button
            >
        </div>
    </div>

<style>
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
        background-color: var(--brandDarkGreen);
        color: #1e3765;
        overflow-x: hidden;
        scrollbar-width: 1px;
        margin: 0 auto;
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
        padding-left: 10px;
        margin: 0 auto;
        font-weight: bold;
        position: relative;
    }
    h2 {
        padding-top: 20px;
        padding-left: 10px;
        margin: 0 auto;
        font-weight: bold;
        position: relative;
    }
    h4 {
        padding-top: 20px;
        padding-left: 10px;
        margin: 0px;
        font-weight: bold;
        display: inline-block;
    }
    h5 {
        padding-top: 10px;
        padding-left: 10px;
        margin: 0px;
        font-weight: bold;
        display: inline-block;
    }
    p {
        padding-top: 0px;
        padding-left: 10px;
        padding-right: 10px;
        padding-bottom: 5px;
        margin-bottom: 5px;
        color: var(--brandWhite);
        font-weight: bold;
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
        border-width: 1px;
        border-color: 'white';
        position: relative;
        font-weight: bold;
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
