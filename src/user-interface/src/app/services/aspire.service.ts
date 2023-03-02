import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AspireService {

  constructor(private readonly http: HttpClient) { }

  getItems(searchQuery: string): Observable<any> {
    let data = {
      "intent": {
          "item": {
              "descriptor": {
                  "name": searchQuery
              }
          }
      }
    };

    return this.http.post<any>(`${environment.apiUrl}/search`, data);
  }

  selectItems(cartItems: any): Observable<any> {
    let data = {
      "order": {
          "items": cartItems.map((item: any) => { id: item.id }),
          "fulfillments": [
              {
                  "customer": {
                      "person": {
                          "name": "John Doe"
                      }
                  }
              }
          ]
      }
    };

    return this.http.post<any>(`${environment.apiUrl}/select`, data);
  }

  initItems(cartItems: any): Observable<any> {
    let data = {
      "order": {
          "items": cartItems.map((item: any) => {
            return { id: item.id };
          }),
          "fulfillments": [
              {
                  "customer": {
                      "person": {
                          "name": "John Doe"
                      }
                  }
              }
          ]
      }
    };

    return this.http.post<any>(`${environment.apiUrl}/init`, data);
  }

  confirmItems(cartItems: any): Observable<any> {
    let data = {
      "order": {
          "items": cartItems.map((item: any) => {
            return { id: item.id };
          }),
          "fulfillments": [
              {
                  "customer": {
                      "person": {
                          "name": "John Doe"
                      }
                  }
              }
          ]
      }
    };

    return this.http.post<any>(`${environment.apiUrl}/confirm`, data);
  }
}
