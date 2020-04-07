# QUESTIONS

## 1.  How is this project structure different than a Flask (or Node) application? What role are the urls.py and views.py files responsible for?
*Very* different from Flask. The structure is a lot more complex, but a lot more variable and accounts for things being created through the app much more effectively.
The urls.py and views.py files are responsible for directing where to go and what to show respectively.

## 2.  Why do we use 2 separate urls.py files? How do they interact?
One is for the overarching structure of the project itself, which handles macro redirection. The other is for direction within the paramters of the subfolder, like microredirection.

## 3. When is it desirable to split our code over multiple apps? Why would we want to do so?
When you're going to be doing a lot more complex and minute changes. We do this because we can make modifications to each part of the app without changing the other portions of it.

