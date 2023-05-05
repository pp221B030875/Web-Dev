import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {AuthToken, Company, Vacancy} from "./models";

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  BASE_URL = 'http://127.0.0.1:8001'
  constructor(private client:HttpClient){

  }
  login(username:string,password:string):Observable<AuthToken>{
    return this.client.post<AuthToken>(
      `${this.BASE_URL}/api/login`,
      {username:username,password:password}
      )
  }
  createCompany(companyName: string): Observable<Company> {
    return this.client.post<Company>(
      `${this.BASE_URL}/api/companies/`,
      {'name': companyName}
    )
  }
  deleteCompany(company_id: number): Observable<any> {
    return this.client.delete(
      `${this.BASE_URL}/api/companies/${company_id}/`
    )
  }
}
