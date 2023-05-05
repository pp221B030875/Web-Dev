export interface Company{
  id: number;
  name: string;
  description: string;
  city: string;
  address: string;
}
export interface Category{
  name: string;
}
export interface Vacancy{
  id: number;
  name: string;
  description: string;
  salary: number;
  company:number;
  category:number;
}
export interface AuthToken{
  token:string;
}

