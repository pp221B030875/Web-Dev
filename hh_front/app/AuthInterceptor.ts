import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpEvent, HttpHandler, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
//Interceptors help us ensure to process
// all HTTP requests and responses before
// sending or getting the request, giving us the power to manage communication.
export class AuthInterceptor implements HttpInterceptor {
  constructor() {}
  //Observable in Angular is a feature
  // that provides support for delivering
  // messages between different parts of your single-page application.
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const token = localStorage.getItem('token');
    if (token){
      //creating a new request by clonning the current request but updating the headers
      const newReq = req.clone({
        headers: req.headers.set('Authorization', `JWT ${token}`),
        //A request header is an HTTP header
        // that can be used in an HTTP request
        // to provide information about the request
        // context, so that the server can tailor the response.
        //
      })
      return next.handle(newReq);
    }

    return next.handle(req);
  }
}
