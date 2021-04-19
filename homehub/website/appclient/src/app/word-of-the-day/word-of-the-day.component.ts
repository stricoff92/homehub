import { Component, OnInit } from '@angular/core';
import { WotdService } from '../wotd.service';

@Component({
  selector: 'app-word-of-the-day',
  templateUrl: './word-of-the-day.component.html',
  styleUrls: ['./word-of-the-day.component.css']
})
export class WordOfTheDayComponent implements OnInit {

  wordOfTheDay:string
  note:string
  definitions:string[]

  constructor(
    private _wotd:WotdService
  ) { }

  ngOnInit() {
    this.fetchWOTD()
  }

  async fetchWOTD() {
    await this._wotd.fetchWOTD()
    this.wordOfTheDay = this._wotd.wordOfTheDay
    this.note = this._wotd.note
    this.definitions = this._wotd.definitions.slice(0, 3)
  }

}
