// Create the map object with options
var year;
var country;
var heat;

var myMap = L.map("map1", {
  center: [38, -97],
  zoom: 4,
});

// Create the tile layer that will be the background of our map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

function buildmap(sample, sample2) {
  // L.heatLayer([38, -97, 0]).addTo(myMap)
  

// Link to GeoJSON
var MetaData = `/metadata/${sample}/${sample2}/`;


// Grab data with d3

d3.json(MetaData).then(function(response){
  //console.log(response.country);

  let heatArray=[];
  // let clean=[];

  for(var i=0; i<response.latitude.length; i++){
      heatArray.push([response.latitude[i], response.longitude[i], response.country[i]]);
      // clean.push([response.latitude[i], response.longitude[i], 0]);

  }
  //console.log(heatArray);

  heat =L.heatLayer(heatArray,{
    radius: 20,
    blur:35,
  }).addTo(myMap)

  });
}

//   //Histogram_of_immingration_to_US
function buildhistogram(sample, sample2) {
  var MetaData = `/metadata/${sample}/${sample2}/`;
  d3.json(MetaData).then(function(response) {
    var trace1 = {
      x: response.NAME.slice(0,10),
      y: response.country,
      name: 'Top ten cities',
      type: 'bar'
    };
  
    var data = [trace1];
  
    var layout = {
      autosize: false,
      width: 600,
      height: 700,
      margin: {
        l: 100,
        r: 50,
        b: 300,
        t: 100,
        pad: 4
      },
      barmode: 'group',
      title: {
        text : `<b>Top 10 Cities for ${sample} Immigrates(${sample2})`,
        font: {
          size: 15,
          color: '#3e4444'
        }
      },
      xaxis: {
        tickangle: 90,
        autorange: true
      },
      yaxis: {
        title: 'Immigrates Population'
      }
  };
  
    Plotly.newPlot('hist', data, layout);
  });
};

function buildline(sample) {
  var MetaData = `/metadata/${sample}/`;
  d3.json(MetaData).then(function(response) {
    var trace1 = {
      x: response.Year,
      y: response.country,
      name: `${sample}`,
      mode: 'lines+markers',
      type: 'scatter'
    };
  
    var data = [trace1];
  
    var layout = {
      autosize: false,
      width: 600,
      height: 700,
      margin: {
        l: 100,
        r: 50,
        b: 300,
        t: 100,
        pad: 4
      },
      barmode: 'group',
      title: {
        text: `<b>${sample} Immigrates (2014-2017)</b>`,
        font: {
          size: 15,
          color: '#3e4444'
        }
      },
      xaxis: {
        title: 'Years'
      },
      yaxis: {
        title: 'Immigrates Population'
      }
      };
  
    Plotly.newPlot('line', data, layout);
  });
};


function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset2"); //country
  var selector2 = d3.select("#selDataset"); //year
  var years=[2017,2016,2015,2014]

  // Use the list of sample names to populate the select options
  d3.json("/names").then((samplecountry, sampleyear) => {
    samplecountry.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

     for (var i = 0; i < years.length; i++) {
    selector2.append("option")
    .text(years[i])
    .property("value", years[i]);
    }
    // sampleyear=selector2;
    //console.log(d3.select("#selDataset").node().value);
    // Use the first sample from the list to build the initial plots
    country = samplecountry[0];//Country
    year = d3.select("#selDataset").node().value;//year

    // d3.select("#selDataset").property('value', firstSample2);
    // d3.select("#selDataset2").property('value', firstSample);
    // // const firstSample2 = 2017;
    buildmap(country, year);
    buildhistogram(country, year);
    buildline(country);
  });
}

function optionChanged(newSample2) {
    // Fetch new data each time a new sample is selected
  //console.log(`sample: ${country} \n sample2: ${newSample2}`);
  year=newSample2;
  myMap.removeLayer(heat);
  buildmap(country, newSample2);
  buildhistogram(country, newSample2);
  buildline(country);
}
function optionChanged2(newSample) {
    // Fetch new data each time a new sample is selected
  //console.log(`sample: ${newSample} \n sample2: ${year}`);
  country=newSample;
  myMap.removeLayer(heat);
  buildmap(newSample, year);
  buildhistogram(newSample, year);
  buildline(newSample);
}

// Initialize the dashboard
init();
