<script>
    import { onMount, afterUpdate } from "svelte";
    import maplibregl from "maplibre-gl";
    import positron from "../../data/positron.json";
    import stationRelations from "../../data/station-relations2.geo.json";
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
            map.addSource("station-relations", {
                type: "geojson",
                data: stationRelations,
            });
            map.addLayer({
                id: "station-relationship",
                type: "circle",
                source: "station-relations",
                paint: {
                    "circle-radius": [
                        "step",
                        ["get", `${station}`],
                        1, 0,
                        3, 1,
                        4, 10,
                        5, 20,
                        6, 40,
                        7, 60,
                        8, 80,
                        9, 100,
                        10, 200,
                        15, 300,
                        18, 360,
                        20, 400,
                        25, 500,
                        30, 600,
                        50,
                    ],
                    "circle-color": [
                        "match",
                        ["get", `${station}`],
                        0, "red",
                        "#0D534D"
                ]
                        ,
                    "circle-opacity": 1,
                    "circle-stroke-color" : [
                        "match",
                        ["get", `${station}`],
                        0, "white",
                        "#0D534D"
                    ],

                    "circle-stroke-width" : 1,
                },
            });
            map.addLayer({
                    id: "station-relationship-outline",
                    type: "circle",
                    source: "station-relations",
                    filter: ['==', 'Start Station Id', station],
                    paint: {
                        "circle-radius": [
                            "step",
                            ["get", `${station}`],
                            1, 0,
                            3, 1,
                            4, 10,
                            5, 20,
                            6, 40,
                            7, 60,
                            8, 80,
                            9, 100,
                            10, 200,
                            15, 300,
                            18, 360,
                            20, 400,
                            25, 500,
                            30, 600,
                            50,
                        ],
                        "circle-opacity" : 0,
                        "circle-stroke-width" : 1,
                        "circle-stroke-color" : "red"

                    },
                });

            map.on("click", "station-relationship", function (e) {
                console.log(
                    e.features[0].properties["Start Station Id"],
                    e.features[0].properties[
                        e.features[0].properties["Start Station Id"]
                    ],
                );
                station = e.features[0].properties["Start Station Id"];
                map.removeLayer('station-relationship-outline');
                map.removeLayer('station-relationship');

                map.addLayer({
                    id: "station-relationship",
                    type: "circle",
                    source: "station-relations",
                    paint: {
                        "circle-radius": [
                            "step",
                            ["get", `${station}`],
                            1, 0,
                            3, 1,
                            4, 10,
                            5, 20,
                            6, 40,
                            7, 60,
                            8, 80,
                            9, 100,
                            10, 200,
                            15, 300,
                            18, 360,
                            20, 400,
                            25, 500,
                            30, 600,
                            50,
                        ],
                        
                    "circle-color": [
                        "match",
                        ["get", `${station}`],
                        0, "red",
                        "#0D534D"
                ],
                        "circle-opacity": 0.4,
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
                    id: "station-relationship-outline",
                    type: "circle",
                    source: "station-relations",
                    filter: ['==', 'Start Station Id', station],
                    paint: {
                        "circle-radius": [
                            "step",
                            ["get", `${station}`],
                            1, 0,
                            3, 1,
                            4, 10,
                            5, 20,
                            6, 40,
                            7, 60,
                            8, 80,
                            9, 100,
                            10, 200,
                            15, 300,
                            18, 360,
                            20, 400,
                            25, 500,
                            30, 600,
                            50,
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

            map.on("mouseenter", "station-relationship", (e) => {
                map.getCanvas().style.cursor = "pointer";
                console.log(
                    station, 
                    e.features[0].properties["Start Station Id"],
                    e.features[0].properties[station],
                );

            });

            map.on("mouseleave", "station-relationship", () => {
                map.getCanvas().style.cursor = "";
            });
        });
    });

    // Geocoder for people to input their address and zoom to input address
    const baseUrl =
        "https://nominatim.openstreetmap.org/search.php?format=jsonv2&q=";

    const getResults = async () => {
        results = await fetch(baseUrl + query + ", Toronto").then((res) =>
            res.json(),
        );
        if (results.length > 0) {
            //this is to remove the previous address point searched (if true)
            if (map.getSource(`address ${lon}`)) {
                map.removeSource(`address ${lon}`);
                map.removeLayer(`address-layer ${lon}`);
                map.removeSource(`buffer ${lon} ${dist}`);
                map.removeLayer(`buffer-layer ${lon} ${dist}`);
            }
            if (distance == "") {
                distance = 500;
            }
            dist = distance;
            //get long - lat
            lat = +results[0].lat;
            lon = +results[0].lon;

            /* CREATE BUFFER */
            var point = turf.point([lon, lat]);
            var buffered = turf.buffer(point, distance, { units: "meters" });

            // add point to show the searched address
            map.addSource(`buffer ${lon} ${dist}`, {
                type: "geojson",
                data: buffered,
            });

            map.addLayer({
                id: `buffer-layer ${lon} ${dist}`,
                type: "line",
                source: `buffer ${lon} ${dist}`,
                paint: {
                    "line-color": "red",
                    "line-width": 5, // Set the color of the point
                },
            });

            // Calculate the bounding box of the polygon
            var bbox = turf.bbox(buffered);

            /* CREATE BUFFER */
            map.addSource(`address ${lon}`, {
                type: "geojson",
                data: {
                    type: "Point",
                    coordinates: [lon, lat],
                },
            });

            map.addLayer({
                id: `address-layer ${lon}`,
                type: "circle",
                source: `address ${lon}`,
                paint: {
                    "circle-radius": 8,
                    "circle-color": "#FF0000", // Set the color of the point
                },
            });

            // Get the coordinates of the buffer
            var coordinates = buffered.geometry.coordinates;

            // Extract all coordinates of the buffer
            var allCoordinates = [];
            coordinates.forEach(function (ring) {
                ring.forEach(function (coord) {
                    allCoordinates.push(coord);
                });
            });

            // Fit the map to the bounding box
            map.fitBounds(
                [
                    [bbox[0], bbox[1]],
                    [bbox[2], bbox[3]],
                ],
                { padding: 20 },
            );
        } else {
            alert("Sorry, no geocoding results for " + query);
        }
    };
</script>

<main>
    <div id="map" class="map" />

    <div class="info-panel">
        <h1>Application Information Centre</h1>

        <p>Last Updated: April 09, 2024</p>

        <!-- THIS BUTTON ALLOWS PEOPLE TO SELECT DEVELOPMENT APPLICATION TYPES-->
        <div class="buttons-box">
            <h3>Filter By Application Type</h3>

            <h3><b>Search Address</b></h3>
            <input bind:value={query} placeholder="i.e. 100 St George St" />
            <input
                bind:value={distance}
                placeholder="i.e. 500, distance is in meters"
            /> <br />
            <button
                class="address-button"
                on:click={getResults}
                disabled={query.length < 1}>Search</button
            >
        </div>
    </div>
</main>

<style>
    main {
        overflow-x: hidden;
    }
    .map {
        height: 100%;
        width: 65%;
        top: 0;
        left: 35%;
        position: absolute;
        overflow: hidden;
    }
    .info-panel {
        position: absolute;
        top: 0px;
        left: 0px;
        width: 35vw;
        height: 100%;
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
</style>
