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

  constructor() {

  }

  ngOnInit(){
    setTimeout(this.cycleRow1.bind(this), this.row1CycleInteraval)
  }

  async cycleRow1() {
    this.showWOTD = !this.showWOTD
    this.showBikes = !this.showBikes
    setTimeout(this.cycleRow1.bind(this), this.row1CycleInteraval)
  }

}
