# Grape Escape
## Introduction:
The project '**Grape Escape**' is and basic eccommerce website for the purchase of wine.
The site will allow the user to be able to log in, select the wine or wines which they would like in various quantities. 
Once this is done the wines can be reviewed in the basket and then purchase via credit card.
For the owner / administrator of the site they will have the functionality to add new wines, edit the existing produces on the site and delete no longer sold wines. 


## UX:
### User Goals
* Colours and fonts should complement site.
* User should be able to create an account.
* User can log into their account if one has already been created.
* Wines can be select with a quantity and added to their basket.
* Basket will only display if the basket has an item.
* Quantity of wine in basket can be updated.
* Prices will be calculated as the quantity changes and grand total is also updated.
* User can go to checkout, complete their details and pay by card.
* Owner can a add new items to the site through a front end form.
* Owner will have the ability to update or delete an item.
* Owner options only available / viewable from admin account.


## User ideas:
* "I should be able to buy more than one bottle from the main order page"
* "Should be able to create an account and login when site is next used"
* "Once I have placed a wine in the basket I should be able to remove the item if I change my mind"
* "If I own the site the ability to manipulate the products, ie delete, edit and add products"
* "Pay for products through credit/debit card and receive a confirmation email"
* "Show how many items I have in my basket"
* "Navigation around the site should be easy"


## Requirements:
The requirements for the application are as follows:
* Navigation bar across all pages.
* Account dropdown with create account, log in and log off.
* Basket icon with basket information displayed.
* Buy button and quantity changer.
* Add product option.
* Edit product option.
* Delete product option.
* Remove from basket option.
* Prices for individual products x quantity are calculated.
* Grand total is calculated.
* Email notification of purchase.
* Card payment function.


## Design:
The design is a multi page website. All pages will be available the a general user except for the add page which is only available to owner / administrator. 
In addition the options for deleting a product and or editting will only appear  from the owner / administrator.
Page will appear through the various button, ie from wine page you can link to the basket and then basket to checkout and back again.
The wines are displayed in individual cards with an image, name, description and price. The basket will show the wine information again with the option to chance quantity or remove complete item. Individual totals and grand total is also displayed.
The checkout will display the grand total and a crsipy form for shipping detals. Wine addition page also contains a cripy form.


### Layout:
* Base layer contains title, navbar, account and basket (which appears if an item is present). Account has a dropdown menu with management, profile, log in, log out and register.
* Home page displays a welcome message and also a wine of the week with button to link to wines page.
* Wines pages displays cards with hold an image, name, description, price, type, region, recommended cheese, quantity and buy button. From this by clicking on the cheese or region you can see more information.
* Basket shows you what you have ordered, the quantity, total price of items, delivery costs and grand total. Also a checkout and continue shopping button.
* Checkout has a form and total, shipping and grand total costs. Checkout, continue shopping, view basket buttons. Option to save profile.
* Checkout success page has thank you message and return to shopping site.
* The cheese and region pages are tables which contain the name and description. Button to return to shopping page.


## Images:
* Main image is by Kymellis [Unsplash.com website](https://unsplash.com/@kymellis?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Kym Ellis"https://unsplash.com/s/photos/winery?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash NOT USED Image by Jill Wellington from Pixabay)
* Example images just for testing taken from [Waitrose website](https://www.waitrose.com/)


## Fonts:
[Google Fonts](https://fonts.google.com).
The fonts used with the website were and Dancing Script and Raleway. Dancing script was mainly used as I thought the style matched to nice wines.


## Colours:
The colours which I have used are in keeping with the main image of the red grapes.
They are:
* #140335. Navbar title, account, basket and all writing is in a purple shade.
* #b9d8b4. Cheese and Region table background colour to make text stand out.


## Wireframe:
The wireframes are an initial representation of how I designed the layout. There have been a few changes during th process but essentially the wireframe matches the production app.
The wireframe document can be found at [wireframes](https://github.com/hob71/Grape-Escape-Ecom/tree/master/wireframes).

## Testing:
Testing was carried out on the functions required for the user. These included  adding records, editting records, deleting record and finding number of records in collection.
* Screen shot of records.
![Screen shot before adding record](https://github.com/hob71/Grape-Escape-Ecom/blob/master/media/wines_before.PNG)

* Added additional recorded, new record displayed.
![Screen shot after record added and counter increases](https://github.com/hob71/Grape-Escape-Ecom/blob/master/media/after_addition.PNG)

* For the addition it is the same process for cheeses and regions.

* Pressed delete. Now one less record.
![Screen shot of delete confirmation](https://github.com/hob71/Grape-Escape-Ecom/blob/master/media/after_deletion.PNG)

* Pressed edit icon and updated the record with a new price, before.
![Screen shot of before edit. Comment added.](https://github.com/hob71/Grape-Escape-Ecom/blob/master/media/wine_details_before_edit_of_price.PNG)

* Pressed edit icon and updated the record with a new price, after.
![Screen shot of editted record. Comment added.](https://github.com/hob71/Grape-Escape-Ecom/blob/master/media/price_change_after_edit.PNG)

* Walkthrough

* Screen shot of basket.
![Screen shot of items in basket and price.](https://github.com/hob71/Grape-Escape-Ecom/blob/master/media/basket.PNG)

* Screen shot of checkout page.
![Screen shot of checkout.](https://github.com/hob71/Grape-Escape-Ecom/blob/master/media/checkout.PNG)

* After successful payment, thank you screen.
![Screen shot of thank you screen](https://github.com/hob71/Grape-Escape-Ecom/blob/master/media/thank_you_message.PNG)

* Stripe payment screen.
![Confirmation payment has gone to stripe](https://github.com/hob71/Grape-Escape-Ecom/blob/master/media/stripe_payment.PNG)

## Bugs:
**Problem-**
Card on front page not displaying any information.
**Fix-**
Under investigation - fix was I had not imported the views to the home page.

**Problem-**
Buttons not working on lower part of screen.
**Fix-**
Footer was blocking buttons. Added a margin bottom to push footer down.

**Problem-**
Images not displaying on wine.html page.
**Fix-**
Corrected path for media.

**Problem-**
Stripe payment was not going through.
**Fix-**
I had two types of order, used wrong naming convention. Changed variable to my_order = ******.

**Problem-**
Three bars on mobile menu icon not showing.
**Fix-**

## Technologies used:
* HTML
* CSS
* Javascript
* Bootstrap
* Django
* Python
* Sqlite3
* Fontawesome
* Stripe
* Pillow

## Deployment:
The project was developed in Gitpod and pushed to GitHub and Heroku.

To deploy my Inventory Manager project in Heroku the process was as follows:-

Opened Heroku in the browser.
* Logged in with my username and password.
* Selected 'new' and 'create new app'.
* Created the name for the app, inventory-manager-mp3. Name has to be unique.
* Chose the region, Europe.
* Opened terminal window in gitpod and logged into heroku using 'heroku login -i'
* Entered my email address and password used to log into heroku app.
* In terminal window typed 'git remote heroku' and the URL provide by Heroku for my app.
* Create a 'requirements.txt' file and 'Procfile'.
* Start up a web process by typing heroku ps:scale web=1 in the terminal.
* In heroku opened up 'settings' and entered in config variables. The IP and PORT.
* In addition in variables connected the MONGO_URI.

The gitignore file contains a env.py file which holds the log in path for Mongodb.

Final 'push' is the change of debug=TRUE to debug=FALSE.

Below are links to my GitHub and Heroku published sites.

#### Published site: https://grape-escape-ecom.herokuapp.com/
#### GitHub site: https://github.com/hob71/Grape-Escape-Ecom

The code in the deployed version is the same as my gitpod repository.


## Future:
Looking at future changes to the site the following could be added:
* On payment to stripe include billing and shipping information.
* Improve notifications when button are clicked.
* Added a rating section and comments section to the wines for customer feedback.
* Multiple images of bottle, ie close up of label.


## Credits:
* Font Awesome for icons.
* Thanks go to the author of the background image. Background photo created by Jill Wellington. 
* Thanks to Waitrose website, used images and part descriptions for test purposes.
* Thanks to Code Institute and Stripe for parts of code especially around Stripe.
* Cheese information taken from https://www.cheese.com/
* Wine information taken from [About France website](https://about-france.com/wines.htm)


## Acknowledge:
I would like to say thank you to my mentor, , and the tutors and student care at the Code Institute for the help and support they gave me.


## Final Notes and Future Additions:
* 