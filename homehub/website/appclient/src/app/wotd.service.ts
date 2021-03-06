import { Injectable } from '@angular/core';
import { ApiService } from './api.service';
import * as moment from 'moment'

@Injectable({
  providedIn: 'root'
})
export class WotdService {

  private wotdAPIUrl = "/api/v1/wotd"

  wordOfTheDay:string
  note:string
  definitions:string[] = []
  lastFetch:moment.Moment

  constructor(
    private _api:ApiService
  ) {
  }

  abbreviatePartOfSpeech(partOfSpeech:string):string {
    if (partOfSpeech == 'noun') {
      return 'n.'
    } else if (partOfSpeech == 'adjective') {
      return 'adj.'
    } else if (partOfSpeech == 'verb') {
      return 'v.'
    }
    return partOfSpeech
  }

  async fetchWOTD():Promise<void> {
    if (!this.lastFetch || moment(this.lastFetch).add(2, 'hours') < moment()) {
      const response = await this._api.get(this.wotdAPIUrl)
      this.lastFetch = moment()
      this.wordOfTheDay = response.word
      this.note = response.note
      this.definitions = []
      for (let i in response.definitions){
        let d = response.definitions[i]
        this.definitions.push(`(${this.abbreviatePartOfSpeech(d.partOfSpeech)}) ${d.text}`)
      }
    }
  }

}
