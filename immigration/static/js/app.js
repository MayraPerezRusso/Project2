// Create the map object with options
var myMap = L.map("map1", {
  center: [38, -97],
  zoom: 4,
});

// Create the tile layer that will be the background of our map
var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
}).addTo(myMap);

// Link to GeoJSON
var MetaData = `/metadata/${sample}/${sample2}`;
var dataline=`/metadata/${sample}`;
var histoURL = `/metadata/Histogram`;
// var APILink = "http://data.beta.nyc//dataset/d6ffa9a4-c598-4b18-8caf-14abde6a5755/resource/74cdcc33-512f-439c-" +
// "a43e-c09588c4b391/download/60dbe69bcd3640d5bedde86d69ba7666geojsonmedianhouseholdincomecensustract.geojson";



// Grab data with d3
d3.json(MetaData, function(response) {
  console.log(response);

  var heatArray=[];

  for(var i=0; i<response.length; i++){
    var location= response[i];
    if (location){
      heatArray.push([location.Lat, Location.Lon])
    }
    
  }

  var heat =L.heatLayer(heatArray,{
    radius: 20,
    blur:35
  }).addTo(myMap)

  //Histogram_of_immingration_to_US

  d3.json(histoURL).then(function(data) {
    var trace1 = {
      x: data[Total],
      y: data[Country],
      name: 'Top ten countries',
      type: 'bar'
    };
  
    var data = [trace1];
  
    var layout = {barmode: 'group'};
  
    Plotly.newPlot('myDiv', data, layout);
  });

  // Create a new choropleth layer
  // geojson = L.choropleth(data, {

  //   // Define what  property in the features to use
  //   valueProperty: "MHI",

  //   // Set color scale
  //   scale: ["#ffffb2", "#b10026"],

  //   // Number of breaks in step range
  //   steps: 10,

  //   // q for quartile, e for equidistant, k for k-means
  //   mode: "q",
  //   style: {
  //     // Border color
  //     color: "#fff",
  //     weight: 1,
  //     fillOpacity: 0.8
  //   },

  //   // Binding a pop-up to each layer
  //   onEachFeature: function(feature, layer) {
  //     layer.bindPopup(feature.properties.LOCALNAME + ", " + feature.properties.State + "<br>Median Household Income:<br>" +
  //       "$" + feature.properties.MHI);
  //   }
  // }).addTo(myMap);

  // Set up the legend
  // var legend = L.control({ position: "bottomright" });
  // legend.onAdd = function() {
  //   var div = L.DomUtil.create("div", "info legend");
  //   var limits = geojson.options.limits;
  //   var colors = geojson.options.colors;
  //   var labels = [];

  //   // Add min & max
  //   var legendInfo = "<h1>Median Income</h1>" +
  //     "<div class=\"labels\">" +
  //       "<div class=\"min\">" + limits[0] + "</div>" +
  //       "<div class=\"max\">" + limits[limits.length - 1] + "</div>" +
  //     "</div>";

  //   div.innerHTML = legendInfo;

  //   limits.forEach(function(limit, index) {
  //     labels.push("<li style=\"background-color: " + colors[index] + "\"></li>");
  //   });

  //   div.innerHTML += "<ul>" + labels.join("") + "</ul>";
  //   return div;
  // };

  // // Adding legend to the map
  // legend.addTo(myMap);

});
