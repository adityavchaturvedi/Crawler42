Crawler42
By Aditya Vinayak Chaturvedi

Given two wikipedia links and a maximum link distance, it does BFS to find the least number of clicks required to get from page one to page two.

Two links are connected if one link can be reached from another by clicking links on the same page.

So, from https://en.wikipedia.org/wiki/Shah_Rukh_Khan you can get to https://en.wikipedia.org/wiki/Raj_Kapoor in 2 links through the path:

Shah Rukh Khan -> Dilip Kumar -> Raj Kapoor i.e. it takes 2 clicks to get from one page to another.

This project was started with the help of this website: http://www-rohan.sdsu.edu/~gawron/python_for_ss/course_core/book_draft/web/HTMLParser.html. Beginning from there, I kept tinkering till I got the aim I was looking for.
