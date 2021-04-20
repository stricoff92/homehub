import { Component, OnInit } from '@angular/core';
import { WeatherService } from '../weather.service';

import * as moment from 'moment';

@Component({
  selector: 'app-upcoming-weather',
  templateUrl: './upcoming-weather.component.html',
  styleUrls: ['./upcoming-weather.component.css']
})
export class UpcomingWeatherComponent implements OnInit {

  upcomingWeather = []

  constructor(
    private _weather:WeatherService
  ) { }

  ngOnInit() {
    this._weather.newWeatherData.subscribe(data => {
      this.upcomingWeather = this.getUpcomingGroupedWeather(data, 6, 4)
    })
  }

  getUpcomingGroupedWeather(data, hoursToBlock, hoursToShow):any[] {
    let hoursFromNow:moment.Moment = moment()
    hoursFromNow.add(2, "hours")
    let futureHourlyForcast = data.hourly.filter(h => h.dt > hoursFromNow)

    futureHourlyForcast.sort((v1, v2)=>{return v1.dt > v2.dt ? 1 : -1}) // Sort ASC
    let groupedHours = []
    for(let i=0; i<futureHourlyForcast.length; i+= hoursToBlock) {
      groupedHours.push(futureHourlyForcast.slice(i, i+hoursToBlock))
    }

    let aggregatedHours = []
    for(let i=0; i<groupedHours.length; i++) {
      if(aggregatedHours.length >= hoursToShow) {
        break
      }
      let hours = groupedHours[i]
      let aggregatedHour = {weatherDescriptions:[], temp:0, windSpeed:0, dt:null, humidity:4}

      let weatherDesciptions:string[] = []
      let temps:number[] = []
      let windSpeeds:number[] = []
      let humidities:number[] = []
      for (let j in hours) {
        for(let k in hours[j].weather) {
          if (weatherDesciptions.indexOf(hours[j].weather[k].description) == -1) {
            weatherDesciptions.push(hours[j].weather[k].description)
          }

        }
        aggregatedHour.weatherDescriptions = weatherDesciptions.map(this._weather.titleCase)
        temps.push(hours[j].temp)
        windSpeeds.push(hours[j].wind_speed)
        humidities.push(hours[j].humidity)
        aggregatedHour.dt = aggregatedHour.dt || hours[j].dt.format("HH:mm")
      }

      aggregatedHour.temp = this._weather.kelvinToRoundedCelcius(temps.reduce((a, b)=>a + b) / temps.length)
      aggregatedHour.windSpeed = Math.round(Math.max(...windSpeeds))
      aggregatedHour.humidity = Math.round(humidities.reduce((a, b)=>a + b) / humidities.length)


      aggregatedHours.push(aggregatedHour)
    }
    return aggregatedHours
  }



}
