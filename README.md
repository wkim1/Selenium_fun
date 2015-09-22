# selenium_fun
My first project using Selenium (http://www.seleniumhq.org/). Automates the process of signing up for 
Stanford classes on Axess.

General usage directions: <br />
-Download <br />
-Within directory selenium_fun, run 'python persistentEnroll.py USERNAME PASSWORD AUTHCODE CLASSNAME'
where you replace the values in all caps with appropriate inputs (authcode is for 2-step, using Google Auth) <br />
-This will open up Firefox and log in, search up the specified class, and attempt to enroll. If you cannot
enroll (due to space or whatever), it will continue to query the site in 30-second intervals. <br />
