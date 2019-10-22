import { Component, OnInit } from "@angular/core";
import {
  FormGroup,
  FormControl,
  Validators,
  FormBuilder
} from "@angular/forms";
import { ApiService } from "../../api.service";

import { Router } from "@angular/router";
import { CookieService } from "ngx-cookie-service";
import { GlobalService } from "../../global.service";

@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.css"]
})
export class LoginComponent implements OnInit {
  authForm: FormGroup;
  loading: boolean;
  error: string;

  constructor(
    private apiService: ApiService,
    private cookieService: CookieService,
    private global: GlobalService,
    private router: Router,
    private fb: FormBuilder
  ) {
    this.authForm = this.fb.group({
      username: new FormControl("", Validators.required),
      password: new FormControl("", Validators.required)
    });
  }

  ngOnInit() {
    this.loading = false;
    this.error = "";
    const mrToken = this.cookieService.get("mr-token");
    if (mrToken) {
      this.router.navigate(["/"]);
    }
  }

  saveForm() {
    this.loading = true;
    this.apiService.loginUser(this.authForm.value).subscribe(
      result => {
        this.loading = false;
        this.cookieService.set("mr-token", result["token"]);
        this.global.me = result["user"];
        this.router.navigate(["/"]);
      },
      error => {
        this.loading = false;
        this.error = error;
      }
    );
  }
}
