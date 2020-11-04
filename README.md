# kattis_scraper
Small script to scrape the names of all solved kattis problems for a user.

### Use
Create a .env file with the two following lines in the same directory as the scraper.py file  
> EMAIL = fakeemail@gmail.com  
> PASSWORD = fakepassword  

Make sure to have selenium, chrome and chromedriver installed  
If chrome or chromedriver are not in enviroment (PATH) specify in scraper.py where to find them  
Run the script  
You will end up with a solved.txt file with the names of the solved kattis problems  
