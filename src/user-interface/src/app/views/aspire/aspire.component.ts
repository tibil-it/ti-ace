import { AfterViewInit, Component, OnInit } from '@angular/core';
import { AspireService } from 'src/app/services/aspire.service';
import { CartService } from 'src/app/services/cart.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-aspire',
  templateUrl: './aspire.component.html',
  styleUrls: ['./aspire.component.scss']
})
export class AspireComponent implements OnInit, AfterViewInit {
  items = [
    {
      id: '112',
      imageUrl: '/assets/images/vlog_img.jpg',
      title: 'A day in the life of a software Tester',
      description: 'Follow along with Rahul Kalekar to experience aday as a software tester',
      type: 'vlog',
      price: '200'
    },
    {
      id: '113',
      imageUrl: '/assets/images/podcast_img.jpg',
      title: 'Journey to be a data scientist',
      description: 'Listen to the podcast to hear about Preethi’s journey to being a data scientist',
      type: 'podcast',
      price: '200'
    },
    {
      id: '114',
      imageUrl: '/assets/images/book1_img.jpg',
      title: 'Basics of testing for mobile',
      description: 'This book teaches the basic principles of testing applications for mobile devices',
      type: 'book',
      price: '200'
    },
    {
      id: '115',
      imageUrl: '/assets/images/guide2_img.jpg',
      title: 'Guidance from Career counselor John M',
      description: 'Sign up for a 6 month access to consultation from career counselor John M',
      type: 'guidance',
      price: '200'
    },
    {
      id: '116',
      imageUrl: '/assets/images/guide1_img.jpg',
      title: 'Guidance from data engineer Suma T',
      description: 'Sign up for a year’s access to Suma’s guided roadmap to studying data engineering',
      type: 'guidance',
      price: '200'
    },
    {
      id: '117',
      imageUrl: '/assets/images/book2_img.jpg',
      title: 'How to succeed at work',
      description: 'Zen master Rohit teaches how to prioritize and focus to achieve success in this book',
      type: 'book',
      price: '200'
    }
  ];
  searchResults!: any[];

  constructor(private readonly _cartService: CartService, private readonly aspireService: AspireService, private toastr: ToastrService) { }

  ngOnInit(): void {
  }

  ngAfterViewInit(): void {
    window.scrollTo(0, 0);
  }
  
  addCartItem(cartItem: any): void {
    this._cartService.addCartItem(cartItem);
  }

  onSearch(searchQuery: string): void {
    this.aspireService.getItems(searchQuery).subscribe(res => {
      let searchResults: any[] = [];

      if (typeof res.message === 'object') {
        res.message.catalog.providers.forEach((provider: any) => {
          searchResults = [...searchResults, ...provider.items.map((item: any) => {
            return {
              id: item.id,
              imageUrl: '/assets/images/vlog_img.jpg',
              title: item.descriptor.name,
              description: item.descriptor.long_desc,
              type: item.tags.content_type,
              currency: item.price.currency,
              price: item.price.value
            }
          })];        
        });

        this.searchResults = searchResults;
      } else {
        this.toastr.error('Oops!', 'Something went wrong!', {
          positionClass: 'toast-bottom-center',
          timeOut: 500
        });
      }
    }, error => {
      this.searchResults = [];
      this.toastr.error('Oops!', 'Something went wrong!',  {
        positionClass: 'toast-bottom-center',
        timeOut: 500
      });
    });
  }

}
