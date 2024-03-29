import { Component, OnInit } from "@angular/core";
import { FormGroup, FormControl } from "@angular/forms";
import { ApiService } from "../api.service";

import { Token } from "@angular/compiler/src/ml_parser/lexer";
import { Router } from "@angular/router";
import { CookieService } from "ngx-cookie-service";
import { GlobalService } from "../global.service";
import { from } from "rxjs";

@Component({
  selector: "app-auth",
  templateUrl: "./auth.component.html",
  styleUrls: ["./auth.component.css"]
})
export class AuthComponent implements OnInit {
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
    if (!this.registerMode) {
      this.apiService.loginUser(this.authForm.value).subscribe(
        result => {
          this.cookieService.set("mr-token", result["token"]);
          console.log(result);
          console.log(result["user"]);
          this.global.me = result["user"];
          this.router.navigate(["/"]);
        },
        error => console.log(error)
      );
    } else {
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
}
