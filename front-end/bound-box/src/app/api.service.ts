import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { CookieService } from "ngx-cookie-service";
import { environment } from "./../environments/environment";
@Injectable({
  providedIn: "root"
})
export class ApiService {
  baseUrl = `${environment.baseurl}/`;
  baseImageUrl = `${this.baseUrl}api/images/`;
  baseEmpathyUrl = `${this.baseUrl}api/empathys/`;
  token = this.cookieService.get("mr-token");
  headers = new HttpHeaders({
    "Content-Type": "application/json"
  });

  constructor(
    private httpClient: HttpClient,
    private cookieService: CookieService
  ) {}

  loginUser(authData) {
    const body = JSON.stringify(authData);
    return this.httpClient.post(`${this.baseUrl}api/auth/`, body, {
      headers: this.getAuthHeaders()
    });
  }

  registerUser(authData) {
    const body = JSON.stringify(authData);
    return this.httpClient.post(`${this.baseUrl}api/users/`, body, {
      headers: this.getAuthHeaders()
    });
  }

  upload(formData) {
    return this.httpClient.post<any>(`${this.baseImageUrl}`, formData, {
      headers: this.getMultiAuthHeaders()
    });
  }
  getImage() {
    return this.httpClient.get<any>(`${this.baseImageUrl}`);
  }
  getUserImage(user) {
    return this.httpClient.get<any>(`${this.baseImageUrl}?owner=${user}`);
  }

  getLikeImage(user) {
    return this.httpClient.get<any>(
      `${this.baseEmpathyUrl}?empathizer=${user}`
    );
  }

  getNextImage(next) {
    return this.httpClient.get<any>(next);
  }
  deleteImage(id) {
    return this.httpClient.delete(`${this.baseImageUrl}?file=${id}`);
  }
  createEmpathy(formData) {
    const body = JSON.stringify(formData);
    return this.httpClient.post<any>(`${this.baseEmpathyUrl}`, body, {
      headers: this.getAuthHeaders()
    });
  }

  getAuthHeaders() {
    const token = this.cookieService.get("mr-token");
    return new HttpHeaders({
      "Content-Type": "application/json",
      Authorization: `Token ${this.token}`
    });
  }
  getMultiAuthHeaders() {
    const token = this.cookieService.get("mr-token");
    return new HttpHeaders({
      enctype: "multipart/form-data",
      Authorization: `Token ${this.token}`
    });
  }
}
