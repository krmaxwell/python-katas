# Grocery Store Kata

From <https://github.com/Gianfrancoalongi/incremental_katas/tree/master/Grocery_store>

## Step 1

Welcome to the Grocery store, we have some pretty nice cash registers which have an interface to a ROM containing daily sale info, through which we can collect the sales reports from all the tills at the end of the day. You see, there is this script which connects to the registers and reads the daily transactions, generating a Record Of Sales (ROS) which is a file containing an item name, quantity sold of this item, and the total price paid for quantity amount of item name.

We collect all of these ROS's and email them for manuall processing by the accountant, Mr Bean.C.Ounter. However, we will team you up with Mr Bean, so you can facilitate his job a bit, as we plan to open 30 new Grocery stores.

Your first task is to write a program that reads ROS files and generates the grand total income for each ROS file.

Thus, the contents of one example ROS file can be found below:

```csv
bread, 1, 2
12-pack of eggs, 1, 2
milk (1L), 4, 8
coca cola (33cl), 10, 10
chicken clubs (frozen), 1, 4
carrots, 4, 1
apples (red, 1Kg bag), 1, 2
butter (500 g), 3, 6
cheese (1Kg), 1, 7
bacon ("tasty" brand, 3 pack), 2, 7
orange juice (1L), 2, 3
cheese (gouda, 1Kg), 1, 5
bottled water (1.5L), 5, 5
twixies (1 whole box, 3 rows, 5 per row), 1, 20
sirloin (100g), 1, 30
tomatoes, 12, 3
bananas, 3, 1
```

## Step 2

Mr.Bean.Counter approaches you

> Great job with the ROS files! You know what, I think we can start collecting more interesting information of these sales if we do some post processing on the ROS files.
> It would be nice if we could categorize the items to be able to spot trends in which type of categories our customers are most interested in.
> I would like you to enrich the ROS files with a new field, containing the category, in order to categorize the items, I have supplied you with a list here containing the items and their categories.
> After that you program has categorized the ROS, I would like it to output the total amount of money for each category, together with the grand total kind of like this:

   wheat and pasta: 10
   fruit: 20
   dairy: 40
   meat: 30
   total: 100

---
bread, wheat and pasta
eggs, animalic
milk, dairy
coca cola, sodas
chicken, meat
beef, meat
carrots, greens
apples, fruit
butter, dairy
cheese, dairy
bacon, meat
juice, drinks
water, drinks
twixies, candy
tomatoes, greens
bananas, fruit
