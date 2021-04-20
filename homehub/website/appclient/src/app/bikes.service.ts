import { Injectable } from '@angular/core';
import * as moment from "moment";
import { ApiService } from './api.service';
import { Subject } from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class BikesService {

  bikesAPIUrl = "/api/v1/bikes"

  bikeStations:any[] = []
  updatedAt:string
  refreshInterval = 1000 * 30

  newBikeData = new Subject<any>()

  constructor(
    private _api:ApiService
  ) {
    this.refreshBikesData()
  }

  private async refreshBikesData() {
    const data = await this._api.get(this.bikesAPIUrl)

    this.bikeStations = data.data
    this.updatedAt = moment(data.updated_at).format("HH:mm")

    this.newBikeData.next(data)

    setTimeout(this.refreshBikesData.bind(this), this.refreshInterval)
  }

}
