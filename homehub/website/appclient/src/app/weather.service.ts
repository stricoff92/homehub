import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

import * as moment from 'moment';

import { ApiService } from './api.service';


@Injectable({
  providedIn: 'root'
})
export class WeatherService {

  private weatherUrl = "/api/v1/weather"
  private refreshIntervalMilliSeconds = 1000 * 30 // 30 Seconds
  private weatherDataHash:string
  private autoRefresh = true

  newWeatherData = new Subject<any>()
  weatherData:any

  constructor(
    private _api:ApiService
  ) {
    this.refreshData()
  }

  private castMoment(obj:any):any {
    const objKeys = Object.keys(obj)
    const keysToCheck = ['dt', 'sunrise', 'sunset',]
    for (let i in keysToCheck) {
      if (objKeys.indexOf(keysToCheck[i]) != -1) {
        obj[keysToCheck[i]] = moment.unix(obj[keysToCheck[i]])
      }
    }
    return obj
  }

  private async refreshData() {
    let response = null
    try {
      response = await this._api.get(this.weatherUrl)
    } catch (e) {
      console.error("error fetching weather from api")
      console.error(e)
    }

    if(this.autoRefresh) {
      setTimeout(
        this.refreshData.bind(this), this.refreshIntervalMilliSeconds)
    }

    if(!response) {
      return
    }

    if (this.weatherDataHash == response.hash) {
      return
    }

    this.weatherDataHash = response.hash
    this.weatherData = response

    this.weatherData.current = this.castMoment(this.weatherData.current)
    this.weatherData.daily = this.weatherData.daily.map(this.castMoment)
    this.weatherData.hourly = this.weatherData.hourly.map(this.castMoment)

    this.newWeatherData.next(this.weatherData)

  }

  kelvinToRoundedCelcius(kelvin:number):number {
    return Math.round(kelvin - 273.15)
  }

  titleCase(str:string):string {
    let strParts = str.toLowerCase().split(' ');
    for (var i = 0; i < strParts.length; i++) {
      strParts[i] = strParts[i].charAt(0).toUpperCase() + strParts[i].slice(1);
    }
    return strParts.join(' ')
  }


}
