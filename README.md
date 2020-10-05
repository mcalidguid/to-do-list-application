# to-do-list-application

## Description
This Todo app will have several main features such as below. These are often referred to as CRUD operations for create, read, update and delete.
* Adding items to a list
* Getting all items from the list
* Updating an item in the list
* Deleting an item from the list

The program uses the following concept:
* if else statement
* operators
* loop
* functions
* classes and object
* list
* exception handling

## How to Run
1. Clone this repo to your local machine using https://github.com/mcalidguid/to-do-list-application.git
2. For windows, open cmd
```
cmd > C:\python38\python.exe C:\python\projects\to-do-list-application\to_do.py
```
_Note: Modify the path of the python file accordingly_

## Sample Output
Happy Path:
```
~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 1
------- ADD AN ITEM -------
>>> Add: watch web scraping
Item is added successfully.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 1
------- ADD AN ITEM -------
>>> Add: read python tutorial blogs
Item is added successfully.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 1
------- ADD AN ITEM -------
>>> Add: watch FRIENDS season 6
Item is added successfully.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 1
------- ADD AN ITEM -------
>>> Add: learn German via Duolingo
Item is added successfully.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 2
------- TO DO LISTS -------
1 . watch web scraping
2 . read python tutorial blogs
3 . watch FRIENDS season 6
4 . learn German via Duolingo

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 3
------- UPDATE AN ITEM -------
1 . watch web scraping
2 . read python tutorial blogs
3 . watch FRIENDS season 6
4 . learn German via Duolingo
>>> Enter the item number to modify: 3
>>> New value: write codes for API automation using python
Item is modified successfully.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 2
------- TO DO LISTS -------
1 . watch web scraping
2 . read python tutorial blogs
3 . write codes for API automation using python
4 . learn German via Duolingo

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 4
------- REMOVE AN ITEM -------
1 . watch web scraping
2 . read python tutorial blogs
3 . write codes for API automation using python
4 . learn German via Duolingo
>>> Enter the item number to remove: 2
Item is deleted successfully.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 2
------- TO DO LISTS -------
1 . watch web scraping
2 . write codes for API automation using python
3 . learn German via Duolingo

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 4
------- REMOVE AN ITEM -------
1 . watch web scraping
2 . write codes for API automation using python
3 . learn German via Duolingo
>>> Enter the item number to remove: 3
Item is deleted successfully.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 2
------- TO DO LISTS -------
1 . watch web scraping
2 . write codes for API automation using python

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 5
Danke, tschüss! ^_^
```

Negative Test:
```
~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 0
Invalid input.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: a
Error Type: <class 'ValueError'> is occurring. Please try again.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 2
------- UPDATE AN ITEM -------
The list is currently empty.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 3
------- TO DO LISTS -------
The list is currently empty.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 4
------- TO DO LISTS -------
The list is currently empty.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 1
------- ADD AN ITEM -------
>>> Add: watch web scraping
Item is added successfully.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 1
------- ADD AN ITEM -------
>>> Add: learn German via Duolingo
Item is added successfully.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 3
------- UPDATE AN ITEM -------
1 . watch web scraping
2 . learn German via Duolingo
>>> Enter the item number to modify: 0
Invalid item number. Please try again.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 3
------- UPDATE AN ITEM -------
1 . watch web scraping
2 . learn German via Duolingo
>>> Enter the item number to modify: 3
Invalid item number. Please try again.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 4
------- REMOVE AN ITEM -------
1 . watch web scraping
2 . learn German via Duolingo
>>> Enter the item number to remove: 0
Invalid item number. Please try again.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 4
------- REMOVE AN ITEM -------
1 . watch web scraping
2 . learn German via Duolingo
>>> Enter the item number to remove: 3
Invalid item number. Please try again.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 3
------- UPDATE AN ITEM -------
1 . watch web scraping
2 . learn German via Duolingo
>>> Enter the item number to modify: asad
Error Type: <class 'ValueError'> is occurring. Please try again.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: 4
------- REMOVE AN ITEM -------
1 . watch web scraping
2 . learn German via Duolingo
>>> Enter the item number to remove: q
Error Type: <class 'ValueError'> is occurring. Please try again.

~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter "1" to add an item
    Enter "2" to view the complete list
    Enter "3" to update an item
    Enter "4" to delete an item
    Enter "5" to exit
>>>: a
Error Type: <class 'ValueError'> is occurring. Please try again.
```