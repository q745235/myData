var json =   [{
      "status" : "success",
      "message" : "",
      "data" : [
        {
          cityId: "4442",
          cityName: "Singapore",
          airports: [
            {
              airportId: "SIN",
              airportName: "Singapore Changi",
              longitude: 103.99,
              latitude: 1.35
            },
            {
              airportId: "XSP",
              airportName: "Seletar Airport",
              longitude: 103.87,
              latitude: 1.42
            }
          ]
        },
        {
          cityId: "4869",
          cityName: "Taipei",
          airports: [
            {
              airportId: "TPE",
              airportName: "Taiwan Taoyuan Intl",
              longitude: 121.232822,
              latitude: 25.077731
            }
          ]
        }
      ]
    }];


    const result = data.filter((item) => {
      //console.log(item);
      console.log(item.airports[0]);
      console.log(item.airports.length);
      //for(let= i;i<item.airports.length;i++){
        if(item.airports[0].airports === "TPE"){
          console.log(item.cityName);
          return item.cityName
        }
      //}
    })
    console.log(result);

    const result = json.filter((item) => {
      let data = item.data
      for (var i = 0; i < data.length; i++) {
        for (var j = 0; j < data[i].airports.length; j++) {
          if(data[i].airports[j].airportId === "TPE"){
            console.log(data[i].cityName);
            return data[i].cityName
          }
        }
      }
    })
    console.log(result);

// answer
    const result = json.filter((item) => {
      let data = item.data
      for (var i = 0; i < data.length; i++) {
        for (var j = 0; j < data[i].airports.length; j++) {
          if(data[i].airports[j].airportId === "TPE"){
            console.log(data[i].cityName);
            return data[i].cityName
          }
        }
      }
    });