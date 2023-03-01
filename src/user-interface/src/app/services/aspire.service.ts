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

  selectItems(searchQuery: string): Observable<any> {
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

  initItems(searchQuery: string): Observable<any> {
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

  iniItems(searchQuery: string): Observable<any> {
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
}
