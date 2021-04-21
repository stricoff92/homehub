import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'appclient';

  showWOTD = false
  showBikes = true
  row1CycleInteraval = 1000 * 20

  showVulnerabilities = false
  showHolidatCalendar = true
  row2CycleInteraval = 1000 * 35

  constructor() {

  }

  ngOnInit(){
    setTimeout(this.cycleRow1.bind(this), this.row1CycleInteraval)
    setTimeout(this.cycleRow2.bind(this), this.row2CycleInteraval)
  }

  async cycleRow1() {
    this.showWOTD = !this.showWOTD
    this.showBikes = !this.showBikes
    setTimeout(this.cycleRow1.bind(this), this.row1CycleInteraval)
  }

  async cycleRow2() {
    this.showVulnerabilities = !this.showVulnerabilities
    this.showHolidatCalendar = !this.showHolidatCalendar
    const timeMultiplier = this.showVulnerabilities ? 3 : 1
    setTimeout(this.cycleRow2.bind(this), this.row2CycleInteraval * timeMultiplier)
  }

}
