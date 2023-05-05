import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Company, Vacancy} from "./models";

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL = 'http://127.0.0.1:8001'
  constructor(private client: HttpClient) { }
  getCompanies(): Observable<Company[]>{
    return this.client.get<Company[]>(`${this.BASE_URL}/api/companies/`)
  }
  getCompany(id: number): Observable<Company>{
    return this.client.get<Company>(`${this.BASE_URL}/api/companies/${id}/`)
  }
  getCompanyVacancies(id: number): Observable<Vacancy[]> {
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies/`)
  }
  createCompany(companyName: string): Observable<Vacancy> {
    return this.client.post<Vacancy>(
      `${this.BASE_URL}/api/vacancies/`,
      {'name': companyName}
    )
  }
  deleteCompany(vacancy_id: number): Observable<any> {
    return this.client.delete(
      `${this.BASE_URL}/api/categories/${vacancy_id}/`
    )
  }
}
