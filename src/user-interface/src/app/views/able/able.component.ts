import { Component, OnInit } from '@angular/core';
import { CartService } from 'src/app/services/cart.service';

@Component({
  selector: 'app-able',
  templateUrl: './able.component.html',
  styleUrls: ['./able.component.scss']
})
export class AbleComponent implements OnInit {

  items = [
    {
      id: '112',
      imageUrl: 'assets/images/sigmund-Im_cQ6hQo10-unsplash_2.png',
      title: 'Web development bootcamp - Front End',
      description: 'Complete guide to front end development with HTML,CSS,Bootstrap and Javascript',
      type: 'vlog'
    },
    {
      id: '113',
      imageUrl: '/assets/images/Angular.png',
      title: 'Angular bootcamp',
      description: 'All about Angular ! Find out all about Angular adn how it work\'s here',
      type: 'podcast'
    },
    {
      id: '114',
      imageUrl: '/assets/images/xd.png',
      title: 'UI/UX Design with Adobe XD',
      description: 'User Experience Design (Bachelor’s Degree) at National Institute at Fashion Technology',
      type: 'book'
    },
    {
      id: '115',
      imageUrl: '/assets/images/guide2_img.jpg',
      title: 'User Experience Design at NIFT (Bachelor’s)',
      description: 'Sign up for a 6 month access to consultation from career counselor John M',
      type: 'guidance'
    },
    {
      id: '116',
      imageUrl: '/assets/images/guide1_img.jpg',
      title: 'User Experience Design at NIFT (Master’s)',
      description: 'User Experience Design (Master\'s Degree) at National Institute  at Fashion Technology',
      type: 'guidance'
    },
    {
      id: '117',
      imageUrl: '/assets/images/Vector.png',
      title: 'Selenium 4 WebDriver with Java',
      description: 'Covers all everything from the basics to expert level of usage and also provides projects to practice',
      type: 'book'
    }
  ];

  constructor(private readonly _cartService: CartService) { }

  ngOnInit(): void {
  }

  addCartItem(cartItem: any): void {
    this._cartService.addCartItem(cartItem);
  }

  onSearch(searchQuery: string): void {
    console.log(searchQuery);
    
  }

}
