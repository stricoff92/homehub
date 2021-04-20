import { Component, OnInit } from '@angular/core';

import * as moment from "moment";
import { BikesService } from '../bikes.service';

@Component({
  selector: 'app-bike-stations',
  templateUrl: './bike-stations.component.html',
  styleUrls: ['./bike-stations.component.css']
})
export class BikeStationsComponent implements OnInit {

  bikesAPIUrl = "/api/v1/bikes"

  bikeStations:any[] = []
  updatedAt:string

  newBikeSubscription:any


  constructor(
    private _bikes:BikesService
  ) { }

  ngOnInit() {
    this.bikeStations = this._bikes.bikeStations
    this.updatedAt = this._bikes.updatedAt

    this.newBikeSubscription = this._bikes.newBikeData.subscribe(data=>{
      this.bikeStations = data.data
      this.updatedAt = moment(data.updated_at).format("HH:mm")
    })

  }

  ngOnDestroy() {
    this.newBikeSubscription.unsubscribe()
  }

}
