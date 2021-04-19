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


  ngOnInit() {
    this._weather.newWeatherData.subscribe(data => {

      this.weatherLocationName = data.weather_location_name
      this.currentTemperature = this._weather.kelvinToRoundedCelcius(data.current.temp)

      this.weatherDescriptions = data.current.weather.map(w=>this._weather.titleCase(w.description))

      this.tempHigh = this._weather.kelvinToRoundedCelcius(data.daily[0].temp.max)
      this.tempLow = this._weather.kelvinToRoundedCelcius(data.daily[0].temp.min)
      this.currentHumidity = data.current.humidity
      this.currentWindSpeed = Math.round(data.current.wind_speed)
      this.sunriseAt = data.current.sunrise.format("HH:mm")
      this.sunsetAt = data.current.sunset.format("HH:mm")
      this.lastUpdated = data.current.dt.format("HH:mm")
    })
  }

}
