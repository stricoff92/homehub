import { Component, OnInit } from '@angular/core';

import * as moment from 'moment';

@Component({
  selector: 'app-clock-widget',
  templateUrl: './clock-widget.component.html',
  styleUrls: ['./clock-widget.component.css']
})
export class ClockWidgetComponent implements OnInit {

  currentTime:moment.Moment
  currentHour:string
  currentMinute:string
  currentSecond:string

  dayOfWeek:string
  month:string
  dayOfMonth:string
  year:string

  showClockColon = true
  clockColonColor = "#ffffff"

  constructor() { }

  ngOnInit() {
    this.updateCurrentDateTime()
  }

  async updateCurrentDateTime():Promise<void> {
    this.currentTime = moment()

    const timeParts = this.currentTime.format("HH:mm:ss").split(":")
    this.currentHour = timeParts[0]
    this.currentMinute = timeParts[1]
    this.currentSecond = timeParts[2]
    this.showClockColon = !this.showClockColon
    this.clockColonColor = this.showClockColon ? "#ffffff" : "#000000"

    this.dayOfWeek = this.currentTime.format("dddd")
    this.month = this.currentTime.format("MMMM")
    this.dayOfMonth = this.currentTime.format("D")
    this.year = this.currentTime.format("YYYY")

    setTimeout(this.updateCurrentDateTime.bind(this), 1000)
  }



}
