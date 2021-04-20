import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

import * as moment from "moment";

@Component({
  selector: 'app-bike-stations',
  templateUrl: './bike-stations.component.html',
  styleUrls: ['./bike-stations.component.css']
})
export class BikeStationsComponent implements OnInit {

  bikesAPIUrl = "/api/v1/bikes"

  bikeStations:any[] = []
  updatedAt:string
  refreshInterval = 1000 * 10

  constructor(
    private _api:ApiService
  ) { }

  ngOnInit() {
    this.refreshBikesData()
  }

  private async refreshBikesData() {
    const data = await this._api.get(this.bikesAPIUrl)
    this.bikeStations = data.data
    this.updatedAt = moment(data.updated_at).format("HH:mm")

    setTimeout(this.refreshBikesData.bind(this), this.refreshInterval)
  }

}
