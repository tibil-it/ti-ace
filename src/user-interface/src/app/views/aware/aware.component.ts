import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-aware',
  templateUrl: './aware.component.html',
  styleUrls: ['./aware.component.scss']
})
export class AwareComponent implements OnInit {
  items = [
    {
      id: '112',
      imageUrl: '/assets/images/vlog_img.jpg',
      title: 'A day in the life of a software Tester',
      description: 'Follow along with Rahul Kalekar to experience aday as a software tester',
      type: 'vlog'
    },
    {
      id: '113',
      imageUrl: '/assets/images/podcast_img.jpg',
      title: 'Journey to be a data scientist',
      description: 'Listen to the podcast to hear about Preethi’s journey to being a data scientist',
      type: 'podcast'
    },
    {
      id: '114',
      imageUrl: '/assets/images/book1_img.jpg',
      title: 'Basics of testing for mobile',
      description: 'This book teaches the basic principles of testing applications for mobile devices',
      type: 'book'
    },
    {
      id: '115',
      imageUrl: '/assets/images/guide2_img.jpg',
      title: 'Guidance from Career counselor John M',
      description: 'Sign up for a 6 month access to consultation from career counselor John M',
      type: 'guidance'
    },
    {
      id: '116',
      imageUrl: '/assets/images/guide1_img.jpg',
      title: 'Guidance from data engineer Suma T',
      description: 'Sign up for a year’s access to Suma’s guided roadmap to studying data engineering',
      type: 'guidance'
    },
    {
      id: '117',
      imageUrl: '/assets/images/book2_img.jpg',
      title: 'How to succeed at work',
      description: 'Zen master Rohit teaches how to prioritize and focus to achieve success in this book',
      type: 'book'
    }
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
