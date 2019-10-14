import { Component, OnInit } from "@angular/core";
import { FormGroup, FormControl } from "@angular/forms";
import { ApiService } from "../../api.service";

import { Router } from "@angular/router";
import { CookieService } from "ngx-cookie-service";
import { GlobalService } from "../../global.service";

@Component({
  selector: "app-register",
  templateUrl: "./register.component.html",
  styleUrls: ["./register.component.css"]
})
export class RegisterComponent implements OnInit {
  authForm = new FormGroup({
    username: new FormControl(""),
    password: new FormControl(""),
    email: new FormControl("")
  });
  registerMode = false;
  constructor(
    private apiService: ApiService,
    private cookieService: CookieService,
    private global: GlobalService,
    private router: Router
  ) {}

  ngOnInit() {
    const mrToken = this.cookieService.get("mr-token");
    if (mrToken) {
      this.router.navigate(["/"]);
    }
  }

  saveForm() {
    this.apiService.registerUser(this.authForm.value).subscribe(
      result => {
        this.router.navigate(["/"]);
      },
      error => {
        alert("Emailアドレスを正しく入力してください。");
      }
    );
  }
}
