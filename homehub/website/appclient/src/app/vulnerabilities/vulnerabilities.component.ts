import { Component, OnInit } from '@angular/core';
import { VulnerabilitiesService } from '../vulnerabilities.service';

@Component({
  selector: 'app-vulnerabilities',
  templateUrl: './vulnerabilities.component.html',
  styleUrls: ['./vulnerabilities.component.css']
})
export class VulnerabilitiesComponent implements OnInit {

  newVulnerabilitySubscription:any
  cve_identifier:string
  cve_description:string

  constructor(
    private _vulnerabilities:VulnerabilitiesService
  ) { }

  ngOnInit() {
    this.newVulnerabilitySubscription = this._vulnerabilities.newVulnerability.subscribe(data=>{
      this.cve_identifier = data.cve_identifier
      this.cve_description = data.description
    })
    this.cve_identifier = this._vulnerabilities.cve_identifier
    this.cve_description = this._vulnerabilities.cve_description
  }

  ngOnDestroy(){
    this.newVulnerabilitySubscription.unsubscribe()
  }

}
