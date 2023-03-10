import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-side-nav',
  templateUrl: './side-nav.component.html',
  styleUrls: ['./side-nav.component.scss']
})
export class SideNavComponent implements OnInit {

  constructor(public router: Router) { }

  ngOnInit(): void {
  }

  isActive(basepath: string): boolean {
    return this.router.url.indexOf(basepath) > -1;
  }

}
