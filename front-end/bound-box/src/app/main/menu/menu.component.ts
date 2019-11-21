import { Component, OnInit } from "@angular/core";
import { FormGroup, FormBuilder } from "@angular/forms";
import { Router } from "@angular/router";
import { CookieService } from "ngx-cookie-service";
import { User } from "../../models/user";
import { Subscription } from "rxjs/Subscription";
import { GlobalService } from "../../global.service";
import * as $ from "jquery";
@Component({
  selector: "app-menu",
  templateUrl: "./menu.component.html",
  styleUrls: ["./menu.component.css"]
})
export class MenuComponent implements OnInit {
  userSub: Subscription;
  account: User = new User();
  form: FormGroup;
  admin: boolean;

  constructor(private cookieService: CookieService, private router: Router, private global: GlobalService, private formBuilder: FormBuilder) { }

  ngOnInit() {

    const mrToken = this.cookieService.get("mr-token");
    if (!mrToken) {
      this.router.navigate(["/auth/login"]);
    } else {
      this.form = this.formBuilder.group({
        user: [""]
      });
      this.admin = false;
      this.userSub = this.global.user.subscribe(me => (this.account = me));
      this.global.me = JSON.parse(localStorage.getItem("account"));
      this.form.get("user").setValue(this.account.id);
      if (this.account.is_staff == true) {
        this.admin = true;
      }
      $(".nav-button").click(() => {
        $(".nav-button").toggleClass("change");
      });
      $(window).scroll(function () {
        let position = $(this).scrollTop();
        if (position >= 200) {
          $(".nav-menu").addClass("custom-navbar");
        } else {
          $(".nav-menu").removeClass("custom-navbar");
        }
      });
    }
  }

  logout() {
    this.cookieService.delete("mr-token");
    localStorage.removeItem("account");
    this.router.navigate(["/auth/login"]);
  }
}
