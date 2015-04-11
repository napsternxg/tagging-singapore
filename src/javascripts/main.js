gothere.load("maps");
var geocoder;
var amenities;
var map;
var directions;

		function initialize() {
			if (GBrowserIsCompatible()) {
				// Create the Gothere map object.
				map = new GMap2(document.getElementById("map"));
				// Set the center of the map.
				var coords=new GLatLng(center.latitude, center.longitude);
				map.setCenter(coords, 11);
				// Add zoom controls on the top left of the map.
				map.addControl(new GSmallMapControl());
				// Add a scale bar at the bottom left of the map.
				map.addControl(new GScaleControl());
				var marker=new GMarker(coords);
				map.addOverlay(marker);
				marker.bindInfoWindow("<h3>" + center.location + "</h3>");
						
				// Create a marker for each location.
				for (var i = 0, n = locations.length; i < n; i++) {
				    var location = locations[i];
				    var marker = new GMarker(new GLatLng(location[1][0], location[1][1]));
					map.addOverlay(marker);
					// Show an infowindow when the marker is clicked.
					marker.bindInfoWindow("<h3>" + location[0] + "</h3><br /><h4>Tags:</h4>"+location[2]);
				}
				geocoder = new GClientGeocoder();
            	amenities = new GAmenities(map, document.getElementById("panelAmenities"));
            	directions = new GDirections(map, document.getElementById("panelDirection"));

			}
		}
		function getAmenities(query, category) {
            map.closeInfoWindow();
            amenities.clear();
            map.clearOverlays();
            var categoryToRequest;
            switch(category) {
                case "supermarkets":
                    categoryToRequest = GAmenities.AMENITY_SUPERMARKET;
                    break;
                case "clinics":
                    categoryToRequest = GAmenities.AMENITY_CLINIC;
                    break;
                case "postoffices":
                    categoryToRequest = GAmenities.AMENITY_POST_OFFICE;
                    break;
                case "schools":
                    categoryToRequest = GAmenities.AMENITY_SCHOOL;
                    break;
                case "atms":
                    categoryToRequest = GAmenities.AMENITY_ATM;
                    break;
                case "banks":
                    categoryToRequest = GAmenities.AMENITY_BANK;
                    break;
                case "petrolkiosks":
                    categoryToRequest = GAmenities.AMENITY_PETROL_KIOSK;
                    break;
                case "busstops":
                    categoryToRequest = GAmenities.AMENITY_BUS_STOP;
                    break;
                case "railstations":
                default:
                    categoryToRequest = GAmenities.AMENITY_RAIL_STATION;
                    break;
            }
            amenities.clearCategories();
            amenities.addCategory(categoryToRequest, GAmenities.LARGE_RESULTSET);
            geocoder.getLatLng(query, function(latlng) {
                if (latlng) {
                    amenities.load(latlng);
                    map.addOverlay(new GMarker(latlng));
                    for (var i = 0, n = locations.length; i < n; i++) {
    				    var location = locations[i];
    				    var marker = new GMarker(new GLatLng(location[1][0], location[1][1]));
    					map.addOverlay(marker);
    					// Show an infowindow when the marker is clicked.
    					marker.bindInfoWindow("<h3>" + location[0] + "</h3><br /><h4>Tags:</h4>"+location[2]);
    				}
    				geocoder = new GClientGeocoder();
                	amenities = new GAmenities(map, document.getElementById("panelAmenities"));
                }
            });
        }
		function getDirections(from, to, mode) {
            var travelMode;
            switch(mode) {
                case "pt":
                    travelMode = G_TRAVEL_MODE_TRANSIT;
                    break;
                case "t":
                    travelMode = G_TRAVEL_MODE_TAXI;
                    break;
                case "d":
                default:
                    travelMode = G_TRAVEL_MODE_DRIVING;
                    break;
            }
            directions.load("from: " + from + " to: " + to, {travelMode: travelMode});
        }

gothere.setOnLoadCallback(initialize);
