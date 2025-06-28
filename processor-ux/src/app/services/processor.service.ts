import { HttpClient, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProcessorService {

  readonly api: string = 'http://localhost:8000/api/v1/transformation';

  constructor(private httpClient: HttpClient) { }

  public submitJsonData(json: object): Observable<Blob> {
    return this.httpClient.post(`${this.api}/j2c`, json, { responseType: 'blob' as 'blob' });
  }
}
