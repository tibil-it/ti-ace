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
      imageUrl: 'assets/images/markus-spiske-8OyKWQgBsKQ-unsplash_1.png',
      title: 'Data Scientist',
      description: 'A data scientist uses data to understand and explain the phenomena around them, and help organizations make better decisions.',
      type: 'vlog'
    },
    {
      id: '113',
      imageUrl: '/assets/images/campaign-creators-pypeCEaJeZY-unsplash _1.png',
      title: 'Data Analyst',
      description: 'Data analysts examine information using data analysis tools and  help their teams develop insights and business strategies. You\'ll  need skills in math, statistics, communications, and working with tools designed to do data analytics and data visualization.',
      type: 'podcast'
    },
    {
      id: '114',
      imageUrl: '/assets/images/sigmund-Im_cQ6hQo10-unsplash _2.png',
      title: 'Web Developer',
      description: 'A web developer is a programmer who develops World Wide  Web applications using a client–server model. The applications typically use HTML, CSS, and JavaScript in the client, and any  general-purpose programming language in the server.',
      type: 'book'
    },
    {
      id: '115',
      imageUrl: '/assets/images/sigmund-Im_cQ6hQo10-unsplash _2.png',
      title: 'Data Engineer',
      description: 'A data engineer is responsible for collecting, managing, and converting raw data into information that can be interpreted by data scientists and business analysts. Data accessibility is their ultimate goal, which is to enable organizations to utilize data for performance evaluation and optimization.',
      type: 'guidance'
    },
    {
      id: '116',
      imageUrl: '/assets/images/scott-graham-5fNmWej4tAA-unsplash_1.png',
      title: 'Software Tester',
      description: 'As a software tester, you\'ll be involved in the quality assurance  stage of software development and deployment. You\'ll conduct automated and manual tests to ensure the software created by  developers is fit for purpose and any bugs or issues are removedwithin a product before it gets deployed to everyday users.',
      type: 'guidance'
    },
    {
      id: '117',
      imageUrl: '/assets/images/guide1_img.jpg',
      title: 'Software Developer',
      description: 'Software developers create software to meet user needs by employing diagrams and models, writing code, and ensuring overall functionality. These professionals design, build, and implement computer programs and applications.',
      type: 'book'
    }
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
