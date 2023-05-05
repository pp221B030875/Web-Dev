import { Component, OnInit } from '@angular/core';
import { Company } from '../models';
import { CompanyService } from '../company.service';
import {Router} from "@angular/router";

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit{
  companies: Company[] = [];
  newCompany:string="";
  constructor(private service: CompanyService,private router: Router){}
  ngOnInit(){

    this.service.getCompanies().subscribe((companies)=>{
      this.companies = companies
    })
    console.log(this.companies)
  }

  addCompany(){
    const company={
      title: this.newCompany
    };
    // @ts-ignore
    this.service.addCompany(company as Company).subscribe((company)=>{
      console.log(company);
      // @ts-ignore
      this.company.unshift(company);
    })
  }

  deleteCompany(id: number){
    //@ts-ignore
    this.company=this.companies.filter((x)=>x.id!==id)
    this.service.deleteCompany(id).subscribe(()=>{
      console.log('deleted', id);
    })
  }

}
