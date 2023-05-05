import { Component, OnInit } from '@angular/core';
import { Company } from '../models';
import { ActivatedRoute } from '@angular/router';
import { CompanyService } from '../company.service';

@Component({
  selector: 'app-company-details',
  templateUrl: './company-details.component.html',
  styleUrls: ['./company-details.component.css']
})
export class CompanyDetailsComponent implements OnInit{
  company: Company;
  constructor( private route: ActivatedRoute, private service: CompanyService) {
    this.company = {} as Company;
  }
  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      let _id = params.get('id');
      if (_id) {
        let id = +_id;
        this.service.getCompany(id).subscribe((company) => {
          this.company = company;
        })
      }
    });
  }
}
