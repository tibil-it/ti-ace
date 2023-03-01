import { Component, OnInit,ChangeDetectorRef, AfterViewInit, ChangeDetectionStrategy, AfterContentInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { IDropdownSettings } from 'ng-multiselect-dropdown';
import { FormsModule }   from '@angular/forms';


@Component({
  selector: 'app-create-user-profile',
  templateUrl: './create-user-profile.component.html',
  styleUrls: ['./create-user-profile.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class CreateUserProfileComponent implements OnInit, AfterViewInit,AfterContentInit {

  userProfile!: FormGroup;
  dropdownSettings:IDropdownSettings = {};
  myTextarea:string='';
  devdropdownList:any=[]
  // devdropdownList = [
  //   { item_id: 1, item_text: 'Web Development' },
  //     { item_id: 2, item_text: 'Data Science' },
  //     { item_id: 3, item_text: 'Mobile Development' },
  //     { item_id: 4, item_text: 'Programming Languages' },
  //     { item_id: 5, item_text: 'Game Development' },
  //     { item_id: 6, item_text: 'Database Design and Development' },
  //     { item_id: 7, item_text: 'Software Testing' }
  // ];
  businessdropdownList = [
    { item_id: 1, item_text: 'Enterpreneurship' },
      { item_id: 2, item_text: 'Management' },
      { item_id: 3, item_text: 'Communication' },
      { item_id: 4, item_text: 'Sales' },
      { item_id: 5, item_text: 'Business Strategy' },
      { item_id: 6, item_text: 'Operations' },
      { item_id: 7, item_text: 'Project Management' }
  ];
  financedropdownList = [
    { item_id: 1, item_text: 'Accounting and Bookkeeping' },
      { item_id: 2, item_text: 'Compliance' },
      { item_id: 3, item_text: 'Cryptocurrency and Blockchain' },
      { item_id: 4, item_text: 'Economics' },
      { item_id: 5, item_text: 'Finance' },
      { item_id: 6, item_text: 'Finance cert and Exam Prep' },
      { item_id: 7, item_text: 'Financial Modelling and Analysis' }
  ];
  itandSoftwaredropdownList = [
    { item_id: 1, item_text: 'IT Certifications' },
      { item_id: 2, item_text: 'Network and Security' },
      { item_id: 3, item_text: 'Hardware' },
      { item_id: 4, item_text: 'Operating System and Servers' },
      { item_id: 5, item_text: 'Other IT and Software' }
  ];
  officeProddropdownList = [
    { item_id: 1, item_text: 'Microsoft' },
      { item_id: 2, item_text: 'Apple' },
      { item_id: 3, item_text: 'Google' },
      { item_id: 4, item_text: 'SAP' },
      { item_id: 5, item_text: 'Oracle' },
      { item_id: 6, item_text: 'Other Office Prod' }
  ];
  personalDevdropdownList = [{ item_id: 1, item_text: 'Personal Transformation' },
  { item_id: 2, item_text: 'Personal Productivity' },
  { item_id: 3, item_text: 'Leadership' },
  { item_id: 4, item_text: 'Career Development' },
  { item_id: 5, item_text: 'Parenting and Relationships' },
  { item_id: 6, item_text: 'Happiness' },
  { item_id: 7, item_text: 'Esoteric Practices' }];
  designdropdownList = [{ item_id: 1, item_text: 'Web Design' },
  { item_id: 2, item_text: 'Graphic design and illustration' },
  { item_id: 3, item_text: 'Design tools' },
  { item_id: 4, item_text: 'USer experience and design' },
  { item_id: 5, item_text: 'Game Design' },
  { item_id: 6, item_text: '3D and animation' },
  { item_id: 7, item_text: 'Fashion design' }];
  marketingdropdownList = [{ item_id: 1, item_text: 'Digital Marketing' },
  { item_id: 2, item_text: 'Search Engine and Optimization' },
  { item_id: 3, item_text: 'Socail Media Marketing' },
  { item_id: 4, item_text: 'Branding' },
  { item_id: 5, item_text: 'Marketing Fundamentals' },
  { item_id: 6, item_text: 'Marketing Analytics and automation' },
  { item_id: 7, item_text: 'Public Relations' }];
  lifestyledropdownList = [{ item_id: 1, item_text: 'Arts and Crafts' },
  { item_id: 2, item_text: 'Beauty and Makeup' },
  { item_id: 3, item_text: 'Mobile Development' },
  { item_id: 4, item_text: 'Esoteric Practices' },
  { item_id: 5, item_text: 'Food and Beverages' },
  { item_id: 6, item_text: 'Gaming' },
  { item_id: 7, item_text: 'Home Improvement and Gardening' },
  { item_id: 8, item_text: 'Pet Caring and Training' }];
  photographydropdownList = [{ item_id: 1, item_text: 'Digital Photography' },
  { item_id: 2, item_text: 'Photography' },
  { item_id: 3, item_text: 'Portarit Photography' },
  { item_id: 4, item_text: 'Photography Tools' },
  { item_id: 5, item_text: 'Commercial Photography' },
  { item_id: 6, item_text: 'Video design' },
  { item_id: 7, item_text: 'Other Photography and Video'} ];
  healthandFitnessmarketingdropdownList = [{ item_id: 1, item_text: 'Fitness' },
  { item_id: 2, item_text: 'General Health' },
  { item_id: 3, item_text: 'Sports' },
  { item_id: 4, item_text: 'Nutrition and diet' },
  { item_id: 5, item_text: 'Yoga' },
  { item_id: 6, item_text: 'Mental health' },
  { item_id: 7, item_text: 'Martial Arts and Self Defense' },
  ];
  musicdropdownList = [{ item_id: 1, item_text: 'Instruments' },
  { item_id: 2, item_text: 'Music Production' },
  { item_id: 3, item_text: 'Music Fundamentals' },
  { item_id: 4, item_text: 'Vocal' },
  { item_id: 5, item_text: 'Music Techniques' },
  { item_id: 6, item_text: 'Music Software' },
  { item_id: 7, item_text: 'Other Music' }];
  teachingmusicdropdownList = [{ item_id: 1, item_text: 'Engineering' },
  { item_id: 2, item_text: 'Humanities' },
  { item_id: 3, item_text: 'Math' },
  { item_id: 4, item_text: 'Science' },
  { item_id: 5, item_text: 'Online education' },
  { item_id: 6, item_text: 'Social Science' },
  { item_id: 7, item_text: 'Language Learning' }];
  devselectedItems:any = [];
  businessselectedItems:any = [];
  financeselectedItems:any = [];
  itdevselectedItems:any = [];
  persdevselectedItems:any = [];
  officeProddevselectedItems:any = [];
  designselectedItems:any = [];
  marketingdselectedItems:any = [];
  lifestyleselectedItems:any = [];
  PhotographyselectedItems:any = [];
  healthdevselectedItems:any = [];
  musicdevselectedItems:any = [];
  teachingdevselectedItems:any = [];


  constructor(private cdr:ChangeDetectorRef) {

  }
ngOnInit() {
    this.userProfile = new FormGroup({
      aadhar_no: new FormControl(''),
      name: new FormControl(''),
      mobile: new FormControl(''),
      email: new FormControl(''),
      designation: new FormControl('')
    });

    this.devselectedItems = [
    ];

    this.dropdownSettings = {
      singleSelection: false,
      idField:'item_id',
      textField: 'item_text',
      selectAllText: 'Select All',
      unSelectAllText: 'UnSelect All',
      itemsShowLimit: 5,
      allowSearchFilter: true
    };

    this.devdropdownList = [
      { item_id: 1, item_text: 'Web Development' },
        { item_id: 2, item_text: 'Data Science' },
        { item_id: 3, item_text: 'Mobile Development' },
        { item_id: 4, item_text: 'Programming Languages' },
        { item_id: 5, item_text: 'Game Development' },
        { item_id: 6, item_text: 'Database Design and Development' },
        { item_id: 7, item_text: 'Software Testing' }
    ];

this.cdr.detectChanges();
  }

  ngAfterViewInit(): void {
    this.cdr.detectChanges();
  }

  ngAfterContentInit(): void {
    this.cdr.detectChanges();
  }

  onItemSelect(item: any) {
    console.log(item);
  }
  onSelectAll(items: any) {
    console.log(items);
  }




  onSubmit(form: FormGroup) {

  }




}
