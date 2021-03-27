## complete path
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "chinese", "location": "Gurgaon"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Gurgaon"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_loc_flag" : "True" }
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
    - utter_goodbye


## complete path with incorrect location exit
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "chinese", "location": "Gurgaon"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Gurgaon"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_loc_flag" : "False"}
    - utter_another_location
* negative
    - utter_goodbye


## complete path with incorrect location 1
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "Italian", "location": "Secunderabad"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Secunderabad"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_loc_flag" : "False"}
    - utter_another_location
* affirm
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"check_loc_flag" : "True"}
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
    - utter_goodbye

## complete path with incorrect location 2
* greet
    - utter_greet
* restaurant_search{"price": "mid", "cuisine": "North Indian", "location": "Panchkula"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Panchkula"}
    - slot{"price": "mid"}
    - action_check_location
    - slot{"check_loc_flag" : "False"}
    - utter_another_location
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_check_location
    - slot{"check_loc_flag" : "True"}
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
    - utter_goodbye

## complete path with incorrect location 3
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "chinese", "location": "Nasik"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Nasik"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_loc_flag": false}
    - utter_another_location
* share_location{"location": "Belgaum"}
    - slot{"location": "Belgaum"}
    - action_check_location
    - slot{"check_loc_flag": false}
    - utter_another_location
* share_location{"location": "Panchkula"}
    - slot{"location": "Panchkula"}
    - action_check_location
    - slot{"check_loc_flag": false}
    - utter_another_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_location
    - slot{"check_loc_flag": true}
    - action_search_restaurants
    - slot{"restaurant_list": "1. Pa Pa Ya in Dome, Level 4, Select Citywalk, A-3, District Centre, Saket, New Delhi rated 4.7 with avg cost 2000 \n\n2. Spezia Bistro in 2525, 1st Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi rated 4.6 with avg cost 900 \n\n3. Qubitos - The Terrace Cafe in C-7, Vishal Enclave, Opposite Metro Pillar 417, Rajouri Garden, New Delhi rated 4.5 with avg cost 1500 \n\n4. Ghar Bistro Cafe in J-198, 2nd Floor, Rajouri Garden, New Delhi rated 4.4 with avg cost 800 \n\n5. The Hudson Cafe in 2524, 1st Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi rated 4.4 with avg cost 850 \n\n6. Karate Kitchen in Greater Kailash (GK) 1, New Delhi rated 4.4 with avg cost 950 \n\n7. Locale in 17, Community Centre, Next to PVR Anupam, Saket, New Delhi rated 4.4 with avg cost 1400 \n\n8. Rajinder Da Dhaba in AB 14, Safdarjung Enclave Market, Safdarjung, New Delhi rated 4.3 with avg cost 800 \n\n9. Local in 11, KG Marg, Scindia House, Connaught Place, New Delhi rated 4.3 with avg cost 1600 \n\n10. Tamra - Shangri-La's - Eros Hotel in Shangri-La's Eros Hotel, 19, Ashoka Road, Janpath, New Delhi rated 4.3 with avg cost 3800 \n\n"}
    - utter_ask_copy
* affirm
    - utter_ask_email
* share_email{"mail_id": "shalakhavirmani07@gmail.com"}
    - slot{"mail_id": "shalakhavirmani07@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "shalakhavirmani07@gmail.com"}
    - utter_mail_sent

## price and location specified
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "Indore"}
    - slot{"location": "Indore"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"check_loc_flag" : "True"}
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
    - utter_goodbye

## Nothing is specified
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_loc_flag" : "True"} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"restaurant_list": "1. Kopper Kadai in J2/6B, 1st & 2nd Floor, B.K. Dutta Market, Rajouri Garden, New Delhi rated J2/6B, 1st & 2nd Floor, B.K. Dutta Market, Rajouri Garden, New Delhi with avg cost 1400 \n\n2. Zabardast Indian Kitchen in E-13/29, Ground Floor, Middle Circle, Connaught Place, New Delhi rated E-13/29, Ground Floor, Middle Circle, Connaught Place, New Delhi with avg cost 1800 \n\n3. Band Baaja Baaraat in A-6 Ground Floor, Vishal Enclave, Rajouri Garden, New Delhi rated A-6 Ground Floor, Vishal Enclave, Rajouri Garden, New Delhi with avg cost 1300 \n\n4. Midnight Hunger Hub in Janakpuri, New Delhi rated Janakpuri, New Delhi with avg cost 800 \n\n5. Cafe Lota in National Crafts Museum, Gate 2, Bhairon Marg, Pragati Maidan, New Delhi rated National Crafts Museum, Gate 2, Bhairon Marg, Pragati Maidan, New Delhi with avg cost 1200 \n\n"}
    - utter_ask_copy
* affirm
    - utter_ask_email
* share_email{"mail_id": "shalakhavirmani07@gmail.com"}
    - slot{"mail_id": "shalakhavirmani07@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "shalakhavirmani07@gmail.com"}
    - utter_mail_sent
* affirm
    - utter_goodbye

## Only Price specified
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_loc_flag" : "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"restaurant_list": "1. Sevilla - The Claridges in The Claridges, 12, Dr. A.P.J. Abdul Kalam Road, Dr APJ Abdul Kalam Road, Delhi NCR rated The Claridges, 12, Dr. A.P.J. Abdul Kalam Road, Dr APJ Abdul Kalam Road, Delhi NCR with avg cost 4500 \n\n2. MOB Brewpub in M 44, Outer Circle, Connaught Place, New Delhi rated M 44, Outer Circle, Connaught Place, New Delhi with avg cost 1500 \n\n3. Spezia Bistro in 2525, 1st Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi rated 2525, 1st Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi with avg cost 900 \n\n4. Big Chill in 35, Khan Market, New Delhi rated 35, Khan Market, New Delhi with avg cost 1500 \n\n5. Music & Mountains - Hillside Cafe in M-23, M Block Market, Greater Kailash (GK) 1, New Delhi rated M-23, M Block Market, Greater Kailash (GK) 1, New Delhi with avg cost 2100 \n\n"}
    - utter_ask_copy
* affirm
    - utter_ask_email
* share_email{"mail_id": "shalakhavirmani07@gmail.com"}
    - slot{"mail_id": "shalakhavirmani07@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "shalakhavirmani07@gmail.com"}
    - utter_mail_sent
* affirm
    - utter_goodbye


## User does not ask for a copy of email
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* restaurant_search{"location": "Ranchi"}
    - slot{"location": "Ranchi"}
    - action_check_location
    - slot{"check_loc_flag" : "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"restaurant_list": "1. Chicken Plaza in Kamil Bulke Path, , Fatima Nagar, Dangartoli ,  Ranchi rated Kamil Bulke Path, , Fatima Nagar, Dangartoli ,  Ranchi with avg cost 200 \n\n"}
    - utter_ask_copy
* negative
    - utter_goodbye
