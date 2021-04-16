import { Component, OnInit } from '@angular/core';
import { WeatherService } from '../weather.service';

@Component({
  selector: 'app-current-weather',
  templateUrl: './current-weather.component.html',
  styleUrls: ['./current-weather.component.css']
})
export class CurrentWeatherComponent implements OnInit {

  lastUpdated:string

  weatherLocationName:string
  currentTemperature:number
  currentHumidity:number
  currentWindSpeed:number
  sunriseAt:string
  sunsetAt:string
  tempHigh:number
  tempLow:number

  weatherDescriptions:string[] = []

  constructor(
    private _weather:WeatherService
  ) { }

  private kelvinToRoundedCelcius(kelvin:number):number {
    return Math.round(kelvin - 273.15)
  }

  private titleCase(str:string):string {
    let strParts = str.toLowerCase().split(' ');
    for (var i = 0; i < strParts.length; i++) {
      strParts[i] = strParts[i].charAt(0).toUpperCase() + strParts[i].slice(1);
    }
    return strParts.join(' ')
  }

  ngOnInit() {
    this._weather.newWeatherData.subscribe(data => {
      console.log(data)

      this.weatherLocationName = data.weather_location_name
      this.currentTemperature = this.kelvinToRoundedCelcius(data.current.temp)

      this.weatherDescriptions = data.current.weather.map(w=>this.titleCase(w.description))

      this.tempHigh = this.kelvinToRoundedCelcius(data.daily[0].temp.max)
      this.tempLow = this.kelvinToRoundedCelcius(data.daily[0].temp.min)
      this.currentHumidity = data.current.humidity
      this.currentWindSpeed = Math.round(data.current.wind_speed)
      this.sunriseAt = data.current.sunrise.format("HH:mm")
      this.sunsetAt = data.current.sunset.format("HH:mm")
      this.lastUpdated = data.current.dt.format("HH:mm")
    })
  }

}
