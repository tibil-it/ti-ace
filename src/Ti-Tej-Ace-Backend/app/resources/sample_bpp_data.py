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
                "name": "Catalog for undefined"
            },
            "providers": [
                {
                    "id": "Provider 1",
                    "descriptor": {
                        "name": "Provider 1"
                    },
                    "categories": [
                        {
                            "id": "Engineer 101",
                            "parent_category_id": "Engineer 101",
                            "descriptor": {
                                "name": "Engineer"
                            }
                        },
                        {
                            "id": "Chemical Engineer 001",
                            "parent_category_id": "Chemical Engineer 001",
                            "descriptor": {
                                "name": "Chemical Engineer"
                            }
                        }
                    ],
                    "items": [
                        {
                            "id": "Q291cnNlTGlzdDovbmQyX25jZTIyX3NjMjk=",
                            "parent_item_id": "Q291cnNlTGlzdDovbmQyX25jZTIyX3NjMjk=",
                            "descriptor": {
                                "name": "Basics of Chemical Engineering",
                                "long_desc": "What a chemical engineer does? how to become a chemical engineer"
                            },
                            "price": {
                                "currency": "INR",
                                "value": "0"
                            },
                            "category_id": "Engineer 101",
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
                                "related_courses": [
                                    {
                                        "id": "basics 0001",
                                        "name": "Basics of Engineering"
                                    },
                                    {
                                        "id": "CE-001",
                                        "name": "Know about Chemicals"
                                    }
                                ],
                                "content_type": "Book"
                            },
                            "rateable": False
                        },
                        {
                            "id": "Q291cnNlTGlzdDovbmQyX25jZTIyX3NjMzA=",
                            "parent_item_id": "Q291cnNlTGlzdDovbmQyX25jZTIyX3NjMjk=",
                            "descriptor": {
                                "name": "Advanced topic of Chemical Engineering",
                                "long_desc": ""
                            },
                            "price": {
                                "currency": "INR",
                                "value": "0"
                            },
                            "category_id": "Chemical Engineer 001",
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
                {
                    "id": "Q291cnNlTGlzdDovbmQyX25jZTIyX3NjMjk==",
                    "parent_item_id": "Q291cnNlTGlzdDovbmQyX25jZTIyX3NjMjk==",
                    "descriptor": {
                        "name": "Basics of Chemical Engineering",
                        "long_desc": "What a chemical engineer does? how to become a chemical engineer",
                    },
                    "price": {
                        "currency": "INR",
                        "value": "10"
                    },
                    "category_id": "Engineer 101",
                    "recommended": False,
                    "time": {
                        "label": "Course Schedule",
                        "duration": "P1W",
                        "range": {
                            "start": "2023-02-26T18:29:00.000000Z",
                            "end": "2023-03-04T18:29:00.000000Z"
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
                    }
                }
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
                "category_id": "Engineer 101"
            },
            "items": [
                {
                    "id": "Q291cnNlTGlzdDovbmQyX25jZTIyX3NjMjk==",
                    "parent_item_id": "Q291cnNlTGlzdDovbmQyX25jZTIyX3NjMjk==",
                    "descriptor": {
                        "name": "Basics of Chemical Engineering",
                        "long_desc": "What a chemical engineer does? how to become a chemical engineer"
                    },
                    "price": {
                        "currency": "INR",
                        "value": "10"
                    },
                    "category_id": "Engineer 101",
                    "recommended": False,
                    "time": {
                        "label": "Course Schedule",
                        "duration": "P1W",
                        "range": {
                            "start": "2023-02-26T18:29:00.000000Z",
                            "end": "2023-03-04T18:29:00.000000Z"
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
                    }
                }
            ],
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
                "category_id": "Engineer 101"
            },
            "items": [
                {
                    "id": "Q291cnNlTGlzdDovbmQyX25jZTIyX3NjMjk==",
                    "parent_item_id": "Q291cnNlTGlzdDovbmQyX25jZTIyX3NjMjk==",
                    "descriptor": {
                        "name": "Basics of Chemical Engineering",
                        "long_desc": "What a chemical engineer does? how to become a chemical engineer"
                    },
                    "price": {
                        "currency": "INR",
                        "value": "10"
                    },
                    "category_id": "Engineer 101",
                    "recommended": False,
                    "time": {
                        "label": "Course Schedule",
                        "duration": "P1W",
                        "range": {
                            "start": "2023-02-26T18:29:00.000000Z",
                            "end": "2023-03-04T18:29:00.000000Z"
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
                    }
                }
            ],
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
