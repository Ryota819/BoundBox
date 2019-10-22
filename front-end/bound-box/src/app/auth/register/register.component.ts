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

@Component({
  selector: "app-register",
  templateUrl: "./register.component.html",
  styleUrls: ["./register.component.css"]
})
export class RegisterComponent implements OnInit {
  authForm: FormGroup;
  loading: boolean;
  error: string;

  constructor(
    private apiService: ApiService,
    private cookieService: CookieService,
    private router: Router,
    private fb: FormBuilder
  ) {
    this.authForm = this.fb.group({
      username: new FormControl("", Validators.required),
      password: new FormControl("", Validators.required),
      email: new FormControl("", Validators.required)
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
    this.apiService.registerUser(this.authForm.value).subscribe(
      result => {
        this.loading = false;
        this.router.navigate(["/auth/login"]);
      },
      error => {
        this.loading = false;
        this.error = error;
        console.log(error);
      }
    );
  }
}
