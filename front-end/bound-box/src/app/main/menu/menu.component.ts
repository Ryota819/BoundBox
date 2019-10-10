import { Component, OnInit } from "@angular/core";
import { FormGroup, FormControl } from "@angular/forms";
import { Router } from "@angular/router";
import { CookieService } from "ngx-cookie-service";
import * as $ from "jquery";
@Component({
  selector: "app-menu",
  templateUrl: "./menu.component.html",
  styleUrls: ["./menu.component.css"]
})
export class MenuComponent implements OnInit {
  SearchForm = new FormGroup({
    username: new FormControl(""),
    password: new FormControl("")
  });
  constructor(private cookieService: CookieService, private router: Router) {}

  ngOnInit() {
    const mrToken = this.cookieService.get("mr-token");
    if (!mrToken) {
      this.router.navigate(["/auth"]);
    } else {
      $(".nav-button").click(() => {
        $(".nav-button").toggleClass("change");
      });
      $(window).scroll(function() {
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
    this.router.navigate(["/auth"]);
  }
}
