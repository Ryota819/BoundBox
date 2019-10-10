import { Component, OnInit, HostListener } from "@angular/core";
import { ApiService } from "../../api.service";
import { FormGroup, FormBuilder } from "@angular/forms";
import { GlobalService } from "../../global.service";
import { User } from "../../models/user";
import { Subscription } from "rxjs/Subscription";
import { Router } from "@angular/router";

@Component({
  selector: "app-likebox",
  templateUrl: "./likebox.component.html",
  styleUrls: ["./likebox.component.css"]
})
export class LikeboxComponent implements OnInit {
  baseurl = "http://localhost:8000";
  files: any = [];
  imageSrc: string | ArrayBuffer = "";
  reader = new FileReader();
  form: FormGroup;
  account: User = new User();
  userSub: Subscription;
  next: string = "";

  constructor(
    private apiService: ApiService,
    private formBuilder: FormBuilder,
    private global: GlobalService,
    private router: Router
  ) {}

  ngOnInit() {
    this.form = this.formBuilder.group({
      profile: [""],
      user: [""]
    });
    this.userSub = this.global.user.subscribe(me => (this.account = me));
    this.global.me = JSON.parse(localStorage.getItem("account"));
    this.form.get("user").setValue(this.account.id);
    this.apiService.getUserImage(this.account.id).subscribe(
      res => {
        this.files = res["result"];
        this.next = res["next"];
        console.log(res);
      },
      err => {}
    );
    $(".gallery-list-item").click(function() {
      let value = $(this).attr("data-filter");
      if (value === "all") {
        $(".filter").show(300);
      } else {
        $(".filter")
          .not("." + value)
          .hide(300);
        $(".filter")
          .filter("." + value)
          .show(300);
      }
    });
    $(".gallery-list-item").click(function() {
      $(this)
        .addClass("active-item")
        .siblings()
        .removeClass("active-item");
    });
  }

  uploadFile(event) {
    for (let index = 0; index < event.length; index++) {
      const element = event[index];
      this.form.get("profile").setValue(element);
      const formData = new FormData();
      formData.append("file", this.form.get("profile").value);
      formData.append("owner", this.form.get("user").value);
      formData.append("viewable", "true");
      this.apiService
        .upload(formData)
        .subscribe(res => console.log(res), err => console.log(err));
    }
  }

  // deleteAttachment(index) {
  //   this.files.splice(index, 1);
  // }
  @HostListener("window:scroll", ["$event"])
  onWindowScroll() {
    if (window.innerHeight + window.scrollY === document.body.scrollHeight) {
      this.apiService.getNextImage(this.next).subscribe(
        res => {
          Array.prototype.push.apply(this.files, res["result"]);
          this.next = res["next"];
          console.log(res["next"]);
        },
        err => {}
      );
    }
  }
}
