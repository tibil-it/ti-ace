on_search = {
    "context": {
        "domain": "dsep:career",
        "country": "IND",
        "city": "BLR",
        "action": "search",
        "core_version": "1.0.0",
        "bap_id": "Ti-Tej-Ace",
        "bap_uri": "http://localhost:5000",
        "transaction_id": "790bab31-eec3-4b93-aa2d-b2a97ca934b3",
        "message_id": "889ef92b-240a-4779-bd40-f866c25f396c",
        "timestamp": "2023-02-27 20:57:33.960913"
    },
    "message": {
        "catalog": {
            "descriptor": {
                "name": "Catalog"
            },
            "providers": [
                {
                    "id": "Provider 1",
                    "descriptor": {
                        "name": "Provider 1"
                    },
                    "categories": [
                        {
                            "id": "Chemical-Engineering",
                            "parent_category_id": "Engineer 101",
                            "descriptor": {
                                "name": "Engineer"
                            }
                        }
                    ],
                    "items": [
                    ]
                }
            ]
        }
    }
}

on_select = {
    "context": {
        "domain": "dsep:career",
        "version": "1.0.0",
        "action": "on_select",
        "bap_id": "Ti-Tej-Ace",
        "bap_uri": "http://localhost:5000",
        "transaction_id": "a9aaecca-10b7-4d19-b640-b047a7c62196",
        "message_id": "7db91181-718f-4720-83de-88e36e9f854e",
        "ttl": "PT10M",
        "timestamp": "2023-02-22T10:30:18.145Z",
        "bpp_id": "Ti-Tej-Ace-BPP",
        "bpp_uri": "http://localhost:5000"
    },
    "message": {
        "order": {
            "provider": {
                "id": "Provider 1",
                "descriptor": {
                    "name": "Provider 1"
                },
                "category_id": "Engineer 101"
            },
            "items": [
            ],
            "quote": {
                "price": {
                    "value": "10",
                    "currency": "INR"
                }
            }
        }
    }
}

on_init = {
    "context": {
        "domain": "dsep:career",
        "version": "1.0.0",
        "action": "on_init",
        "bap_id": "Ti-Tej-Ace",
        "bap_uri": "http://localhost:5000",
        "transaction_id": "a9aaecca-10b7-4d19-b640-b047a7c62196",
        "message_id": "7db91181-718f-4720-83de-88e36e9f854e",
        "ttl": "PT10M",
        "timestamp": "2023-02-22T10:30:18.145Z",
        "bpp_id": "Ti-Tej-Ace-BPP",
        "bpp_uri": "http://localhost:5000"
    },
    "message": {
        "order": {
            "provider": {
                "id": "Provider 1",
                "descriptor": {
                    "name": "Provider 1"
                },
                "category_id": "Engineer 101",
                "items": [
                ]
            },
            "quote": {
                "price": {
                    "value": "10",
                    "currency": "INR"
                }
            },
            "fulfillments": [
                {
                    "customer": {
                        "person": {
                            "name": "John Doe"
                        }
                    },
                    "tracking": False
                }
            ]
        }
    }
}

on_confirm = {
    "context": {
        "domain": "dsep:career",
        "version": "1.0.0",
        "action": "on_confirm",
        "bap_id": "Ti-Tej-Ace",
        "bap_uri": "http://localhost:5000",
        "transaction_id": "a9aaecca-10b7-4d19-b640-b047a7c62196",
        "message_id": "7db91181-718f-4720-83de-88e36e9f854e",
        "ttl": "PT10M",
        "timestamp": "2023-02-22T10:30:18.145Z",
        "bpp_id": "Ti-Tej-Ace-BPP",
        "bpp_uri": "http://localhost:5000"
    },
    "message": {
        "order": {
            "id": "a9aaecca-10b7-4d19-b640-b047a7c621961",
            "state": "COMPLETE",
            "provider": {
                "id": "Provider 1",
                "descriptor": {
                    "name": "Provider 1"
                },
                "category_id": "Engineer 101",
                "items": [
                ]
            },
            "quote": {
                "price": {
                    "value": "10",
                    "currency": "INR"
                }
            },
            "fulfillments": [
                {
                    "customer": {
                        "person": {
                            "name": "John Doe"
                        }
                    },
                    "tracking": False
                }
            ],
            "payment": {
                "type": "ON-ORDER",
                "status": "PAID"
            }
        }
    }
}

items_on_category = {
    "Chemical-Engineering": [
                        {
                            "id": "id001",
                            "parent_item_id": "id001",
                            "descriptor": {
                                "name": "Basics of Chemical Engineering",
                                "long_desc": "What a chemical engineer does? how to become a chemical engineer"
                            },
                            "price": {
                                "currency": "INR",
                                "value": "10"
                            },
                            "category_id": "Chemical-Engineering",
                            "recommended": False,
                            "time": {
                                "label": "Course Schedule",
                                "duration": "P1W",
                                "range": {
                                    "start": "2023-02-26T18:29:00.000000Z",
                                    "end": "2023-03-04T18:29:00.000000Z"
                                }
                            },
                            "rating": "3",
                            "tags": {
                                "content_type": "Book"
                            },
                            "rateable": False
                        },
                        {
                            "id": "id002",
                            "parent_item_id": "id002",
                            "descriptor": {
                                "name": "Advanced topic of Chemical Engineering",
                                "long_desc": ""
                            },
                            "price": {
                                "currency": "INR",
                                "value": "10"
                            },
                            "category_id": "Chemical-Engineering",
                            "recommended": False,
                            "time": {
                                "label": "Course Schedule",
                                "duration": "P2W",
                                "range": {
                                    "start": "2023-02-26T18:29:00.000000Z",
                                    "end": "2023-03-11T18:29:00.000000Z"
                                }
                            },
                            "rating": "1",
                            "tags": {
                                "related_courses": [
                                    {
                                        "id": "basics 0001",
                                        "name": "Basics of Engineering"
                                    },
                                    {
                                        "id": "CE-001",
                                        "name": "Know about Chemicals"
                                    }
                                ]
                            },
                            "rateable": False
                        }
                    ],

    "Software-Engineering": [
                        {
                            "id": "id-001",
                            "parent_item_id": "id-001",
                            "descriptor": {
                                "name": "Guide to software engneering career path",
                                "long_desc": "What are the possibilities in software engineering ",
                                "3d_render": "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=&cad=rja&uact=8&ved=2ahUKEwjgl_ztzrj9AhU8TGwGHXx9CBMQtwJ6BAgFEAI&url=https%3A%2F%2Fwww.tryexponent.com%2Fblog%2Fsoftware-engineer-career-path&usg=AOvVaw2s6XIeurMRaI3stUCcs4ru"
                            },
                            "price": {
                                "currency": "INR",
                                "value": "5"
                            },
                            "category_id": "Software-Engineering",
                            "recommended": False,
                            "time": {
                                "label": "Course Schedule",
                                "duration": "P2M",

                            },
                            "rating": "3",
                            "tags": {
                                "content_type": "Video"
                            },
                            "rateable": False
                        },
                        {
                            "id": "id-002",
                            "parent_item_id": "id-002",
                            "descriptor": {
                                "name": "19 career paths for software engineers",
                                "long_desc": "What are the possibilities in software engineering. Showcases 19 possibilities",
                                "3d_render": "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=&cad=rja&uact=8&ved=2ahUKEwjgl_ztzrj9AhU8TGwGHXx9CBMQtwJ6BAgDEAI&url=https%3A%2F%2Fwww.indeed.com%2Fcareer-advice%2Ffinding-a-job%2Fsoftware-engineer-career-paths&usg=AOvVaw0fsHC8bEnWpNggrN754WSl"
                            },
                            "price": {
                                "currency": "INR",
                                "value": "15"
                            },
                            "category_id": "Software-Engineering",
                            "recommended": False,
                            "time": {
                                "label": "Course Schedule",
                                "duration": "P10M",

                            },
                            "rating": "3",
                            "tags": {
                                "content_type": "Blog"
                            },
                            "rateable": False
                        },
                        {
                            "id": "id-003",
                            "parent_item_id": "id-003",
                            "descriptor": {
                                "name": "19 career paths in software engineers",
                                "long_desc": "What are the possibilities in software engineering. Showcases 19 possibilities",
                                "3d_render": "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=&cad=rja&uact=8&ved=2ahUKEwjgl_ztzrj9AhU8TGwGHXx9CBMQtwJ6BAgHEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DxuxTJUIi7nQ&usg=AOvVaw280Z34WvxN5W4kH0iauHTZ"
                            },
                            "price": {
                                "currency": "INR",
                                "value": "10"
                            },
                            "category_id": "Software-Engineering",
                            "recommended": False,
                            "time": {
                                "label": "Course Schedule",
                                "duration": "P13M",

                            },
                            "rating": "3",
                            "tags": {
                                "content_type": "Video"
                            },
                            "rateable": False
                        }
                    ],
    "Civil-Engineering": [
                        {
                            "id": "id-001",
                            "parent_item_id": "id-001",
                            "descriptor": {
                                "name": "Civil Engineering Body of Knowledge: Preparing the Future ",
                                "long_desc": "This report focuses on outcomes of proposed changes in the way civil engineering is taught and learned, including the knowledge, skills, and attitudes necessary",
                                "3d_render": "https://books.google.co.in/books?id=WcPvwQEACAAJ&dq=civil+engineering+career+path&hl=en&newbks=1&newbks_redir=1&sa=X&ved=2ahUKEwjUpv-c0rj9AhVjmFYBHZmNCX4Q6AF6BAgHEAI"
                            },
                            "price": {
                                "currency": "INR",
                                "value": "5"
                            },
                            "category_id": "Civil-Engineering",
                            "recommended": False,
                            "time": {
                                "label": "Course Schedule",
                                "duration": "P2M",

                            },
                            "rating": "3",
                            "tags": {
                                "content_type": "Book"
                            },
                            "rateable": False
                        },
                        {
                            "id": "id-002",
                            "parent_item_id": "id-002",
                            "descriptor": {
                                "name": "Guide to Hiring and Retaining Great Civil Engineers",
                                "long_desc": "What are the possibilities in Civil engineering.",
                                "3d_render": "https://books.google.com/books?id=E5kK3wYJ1OQC&dq=civil+engineering+career+path&hl=en&newbks=1&newbks_redir=1&sa=X&ved=2ahUKEwjUpv-c0rj9AhVjmFYBHZmNCX4Q6AF6BAgBEAI"
                            },
                            "price": {
                                "currency": "INR",
                                "value": "15"
                            },
                            "category_id": "Civil-Engineering",
                            "recommended": False,
                            "time": {
                                "label": "Course Schedule",
                                "duration": "P10M",

                            },
                            "rating": "3",
                            "tags": {
                                "content_type": "Book"
                            },
                            "rateable": False
                        },
                        {
                            "id": "id-003",
                            "parent_item_id": "id-003",
                            "descriptor": {
                                "name": "Negotiating Your Career in Structural Engineering: A Guide ",
                                "long_desc": "Negotiating Your Career in Structural Engineering: A Guide ",
                                "3d_render": "https://books.google.com/books?id=4F4IzgEACAAJ&dq=civil+engineering+career+path&hl=en&newbks=1&newbks_redir=1&sa=X&ved=2ahUKEwjUpv-c0rj9AhVjmFYBHZmNCX4Q6AF6BAgKEAI"
                            },
                            "price": {
                                "currency": "INR",
                                "value": "10"
                            },
                            "category_id": "Civil-Engineering",
                            "recommended": False,
                            "time": {
                                "label": "Course Schedule",
                                "duration": "P13M",

                            },
                            "rating": "3",
                            "tags": {
                                "content_type": "Book"
                            },
                            "rateable": False
                        }
                    ]
}
