import { Component, OnInit } from '@angular/core';
import { HolidaysService } from '../holidays.service';
import * as moment from "moment";

@Component({
  selector: 'app-holidays',
  templateUrl: './holidays.component.html',
  styleUrls: ['./holidays.component.css']
})
export class HolidaysComponent implements OnInit {

  holidayData = []
  newHolidayDataSubscription:any

  constructor(
    private _holiday:HolidaysService
  ) { }

  ngOnInit() {
    this.holidayData = this._holiday.holidayData
    this.newHolidayDataSubscription = this._holiday.newHolidayData.subscribe(data=>{
      this.holidayData = data.map(this.castToMoment)
    })

  }

  ngOnDestroy() {
    this.newHolidayDataSubscription.unsubscribe()
  }

  castToMoment(obj) {
    obj.dateStr = moment(obj.date.iso).format("ddd. MMM. DD")
    return obj
  }

}
