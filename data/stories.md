## complete path
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "chinese", "location": "Gurgaon"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Gurgaon"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"restaurant_list": "1. Matchbox in 30, Ground Floor, Sector 29, Gurgaon rated 30, Ground Floor, Sector 29, Gurgaon with avg cost 1500 \n\n2. Yum Yum Cha in Cyber Hub, DLF Cyber City, Gurgaon rated Cyber Hub, DLF Cyber City, Gurgaon with avg cost 1800 \n\n3. Boombox Brewstreet in SCO 53, 1st Floor, Main Market, Sector 29, Gurgaon rated SCO 53, 1st Floor, Main Market, Sector 29, Gurgaon with avg cost 1600 \n\n4. Downtown - Diners & Living Beer Cafe in SCO 34, Main Market, Sector 29, Gurgaon rated SCO 34, Main Market, Sector 29, Gurgaon with avg cost 1800 \n\n5. Bunker in Shop 204-206, Cross Point Mall, DLF Phase 4, Gurgaon rated Shop 204-206, Cross Point Mall, DLF Phase 4, Gurgaon with avg cost 1300 \n\n"}
    - utter_ask_copy
* affirm
    - utter_ask_email
* share_email{"mail_id": "duaanil10@gmail.com"}
    - slot{"mail_id": "duaanil10@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "duaanil10@gmail.com"}
    - utter_mail_sent


## price and location specified
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "Indore"}
    - slot{"location": "Indore"}
    - slot{"price": "high"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"restaurant_list": "1. Square - Sayaji Hotel in Sayaji Hotel, H-1, Scheme 54, Vijay Nagar, Indore rated Sayaji Hotel, H-1, Scheme 54, Vijay Nagar, Indore with avg cost 1500 \n\n2. Nafees Restaurant in 30-B, Apollo Avenue, Opposite Palasia Thana, Old Palasia, Indore rated 30-B, Apollo Avenue, Opposite Palasia Thana, Old Palasia, Indore with avg cost 800 \n\n3. JAL - A Jungle Restaurant in Behind Pushp Kunj Hospital, Khandwa Road, Bhawar Kuan, Indore rated Behind Pushp Kunj Hospital, Khandwa Road, Bhawar Kuan, Indore with avg cost 850 \n\n4. Pishori Restaurant in 910, Khatiwala Tank, Sapna Sangeeta, Indore rated 910, Khatiwala Tank, Sapna Sangeeta, Indore with avg cost 800 \n\n5. Vidorra in 1001, Rooftop, Shekhar Central, Palasia Square, New Palasia, Indore rated 1001, Rooftop, Shekhar Central, Palasia Square, New Palasia, Indore with avg cost 1200 \n\n"}
    - utter_ask_copy
* affirm
    - utter_ask_email
* share_email{"mail_id": "dua.meena5@gmail.com"}
    - slot{"mail_id": "dua.meena5@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "dua.meena5@gmail.com"}
    - utter_mail_sent
