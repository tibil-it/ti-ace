import { Component, OnInit, Input, ContentChild } from '@angular/core';

@Component({
  selector: 'app-basic-horizontal-card',
  templateUrl: './basic-horizontal-card.component.html',
  styleUrls: ['./basic-horizontal-card.component.scss']
})
export class BasicHorizontalCardComponent implements OnInit {

  @Input() data: any;
  @ContentChild("cardFooter") cardFooter: any;

  constructor() { }

  ngOnInit(): void {
  }

}
