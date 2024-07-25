initial download, with berlin example

`wget https://repo1.maven.org/maven2/com/graphhopper/graphhopper-web/9.1/graphhopper-web-9.1.jar https://raw.githubusercontent.com/graphhopper/graphhopper/9.x/config-example.yml http://download.geofabrik.de/europe/germany/berlin-latest.osm.pbf`

then edit config file manually to focus just on bike, and toggle on elevation
(may need to clear/delete the graph cache to re-run)

copied in Toronto.pbf, then run to get a server

`java -D"dw.graphhopper.datareader.file=toronto-july2024-24.osm.pbf" -jar graphhopper*.jar server config-bike.yml`

web http://localhost:8989/

api http://localhost:8989/route?point=43.700119%2C-79.376482&point=43.702077%2C-79.355109&profile=bike

api docs https://github.com/graphhopper/graphhopper/blob/master/docs/web/api-doc.md

Extra stations in ridership but not in stations, added in manually, with the two exceptions
7905
7795
7793
7690 - bike shop test station, do not include
7638 - warehouse, do not include
7485