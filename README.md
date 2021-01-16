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
* Base layer - this consists of the title, navbar, account nav, basket and footer and will be the same across all pages. On smaller devices the navbar headers change to a collapsable icon.
* Index/Home - the contains a welcome message * Solvent / Consumables - here you will see what is available in stock. A record of number of item will be displayed and there is the functionality to search, edit and delete items. 
The search function is not case sensitive and will display the results after button press or return key pressed. The display will change to show results, show how many results are displayed and addition button to show all records again.
Edit will take you to edit page and delete will take you to a confirmation edit page.
* Edit page - allows you to edit any field and submit. On submit you are returned to the solvent or consumable page.
* Requests - displays a form, details can be entered and submitted the request page.
* Add solvents / consumables - is a form page which allows new products t be entered and submitted to the database.
* New Requests - a page which displays all new requests as cards with details of what is needed to be ordered. Once ordered requested can be cleared by pressing the ordered button.