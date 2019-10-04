import { Component, OnInit } from "@angular/core";
import { FormGroup, FormControl } from "@angular/forms";
import { ApiService } from "../api.service";

import { Token } from "@angular/compiler/src/ml_parser/lexer";
import { Router } from "@angular/router";
import { CookieService } from "ngx-cookie-service";

interface TokenObj {
  token: string;
}
@Component({
  selector: "app-auth",
  templateUrl: "./auth.component.html",
  styleUrls: ["./auth.component.css"]
})
export class AuthComponent implements OnInit {
  authForm = new FormGroup({
    username: new FormControl(""),
    password: new FormControl("")
  });
  constructor(
    private apiService: ApiService,
    private cookieService: CookieService,
    private router: Router
  ) {}

  ngOnInit() {
    const mrToken = this.cookieService.get("mr-token");
    if (mrToken) {
      this.router.navigate(["/"]);
    }
  }

  saveForm() {
    this.apiService.loginUser(this.authForm.value).subscribe(
      (result: TokenObj) => {
        this.cookieService.set("mr-token", result.token);
        this.router.navigate(["/"]);
      },
      error => console.log(error)
    );
    // console.log(this.authForm.value);
  }
}
