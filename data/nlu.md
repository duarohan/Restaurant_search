## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- Yes
- Thanks
- Thank
- Thank you

## intent:negative
- No
## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- Hi

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [American](cuisine)
- [Mexican](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- can you find me a [cheap]{"entity": "price", "value": "low"} [Chinese](cuisine) restaurant in [bangalore](location)
- can you find me an [expensive]{"entity": "price", "value": "high"} [mexican](cuisine) restaurant in [Mumbai](location)
- can you find me a [fine]{"entity": "price", "value": "high"} dine in [Mumbai](location) which serves [mexican](cuisine)
- Can you find me some [expensive]{"entity": "price", "value": "high"} [chinese](cuisine) restaurant in [Mumbai](location)?
- Can you find me some [expensive]{"entity": "price", "value": "high"} [Chinese]{"entity": "cuisine", "value": "chinese"} restaurants in [Mumbai](location)?
- Can you find me some mid range [Chinese]{"entity": "cuisine", "value": "chinese"} restaurants in [Indore](location)?
- Can you find me some [expensive]{"entity": "price", "value": "high"} [Chinese]{"entity": "cuisine", "value": "chinese"} restaurants in [Gurgaon](location)?
- [low](price)
- [mid](price)
- [high](price)
- Can you find me some restaurants?
- [Delhi](location)
- Can you find me some [expensive]{"entity": "price", "value": "high"} restaurants in [Indore](location)?
- [Ranchi](location)
- Can you find me some [expensive]{"entity": "price", "value": "high"} restaurants?
- Can you find me some [cheap]{"entity": "price", "value": "low"} restaurants?

## intent:share_email
- yes. Please send it to [ahbcdj@dkj.com](mail_id)
- yes. Please
- no
- No
- not required
- Please send it to [ahbcdj@dkj.com](mail_id)
- Send it to [ahbcdj@dkj.com](mail_id)
- Email it to [ahbcdj@dkj.com](mail_id)
- [shalakhavirmani07@gmail.com](mail_id)
- [ishita.kekre@gmail.com](mail_id)
- [duaanil10@gmail.com](mail_id)
- [dua.meena5@gmail.com](mail_id)

## synonym:4
- four

## synonym:Delhi
- New Delhi
- Dilli

## synonym:Mumbai
- Bombay
- Bambai
## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:high
- expensive
- fine

## synonym:low
- cheap

## synonym:mid
- moderate
- moderately
- mid-range

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:mail_id
- [\S]*@[\S]*.com
- [a-z0-9]*@[a-z0-9]*.com
- ^[a-z0-9][\S]*@[\S]*.com

## regex:pincode
- [0-9]{6}
