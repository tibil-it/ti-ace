import { Component, OnInit, Input, ContentChild } from '@angular/core';

@Component({
  selector: 'app-basic-card',
  templateUrl: './basic-card.component.html',
  styleUrls: ['./basic-card.component.scss']
})
export class BasicCardComponent implements OnInit {

  @Input() data: any;
  @ContentChild("cardFooter") cardFooter: any;

  constructor() { }

  ngOnInit(): void {
  }

}
