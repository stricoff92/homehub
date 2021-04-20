import { Injectable } from '@angular/core';
import { ApiService } from './api.service';
import { Subject } from "rxjs"

@Injectable({
  providedIn: 'root'
})
export class HolidaysService {

  private api_url = "/api/v1/holidays"

  newHolidayData = new Subject<any>()
  holidayData = []

  refreshInterval = 1000 * 60 * 20

  constructor(
    private _api:ApiService
  ) {
    this.refreshHolidays()
  }

  private async refreshHolidays() {
    const response = await this._api.get(this.api_url)
    this.holidayData = response
    this.newHolidayData.next(response)
    setTimeout(this.refreshHolidays.bind(this), this.refreshInterval)
  }
}
