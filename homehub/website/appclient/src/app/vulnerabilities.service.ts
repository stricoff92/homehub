import { Injectable } from '@angular/core';
import { Subject } from 'rxjs'
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class VulnerabilitiesService {


  private apiUrl = "/api/v1/vulnerability"
  refreshInterval = 1000 * 60 * 8

  cve_identifier:string
  cve_description:string

  newVulnerability = new Subject<any>()

  constructor(
    private _api:ApiService
  ) {
    this.refreshData()
  }

  private async refreshData() {
    const response = await this._api.get(this.apiUrl)
    this.cve_identifier = response.cve_identifier
    this.cve_description = response.description
    this.newVulnerability.next(response)

    setTimeout(this.refreshData.bind(this), this.refreshInterval)
  }

}
