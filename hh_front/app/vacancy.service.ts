import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Vacancy} from "./models";

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  BASE_URL = 'http://127.0.0.1:8001'
  constructor(private client: HttpClient) { }

  getVacancies(): Observable<Vacancy[]>{
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/vacancies/`)
  }
  getVacancy(id: number): Observable<Vacancy>{
    return this.client.get<Vacancy>(`${this.BASE_URL}/vacancies/${id}`)
  }
  //top ten with the highest salary
  getTopVacancies(): Observable<Vacancy[]>{
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/vacancies/top_ten/`)
  }
  getTop15Vacancies():Observable<Vacancy[]>{
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/vacancies/top_fiveteen/`)
  }
  createVacancy(vacancyName: string): Observable<Vacancy> {
    return this.client.post<Vacancy>(
      `${this.BASE_URL}/api/vacancies/`,
      {'name': vacancyName}
    )
  }
  deleteVacancy(vacancy_id: number): Observable<any> {
    return this.client.delete(
      `${this.BASE_URL}/api/categories/${vacancy_id}/`
    )
  }
  }



