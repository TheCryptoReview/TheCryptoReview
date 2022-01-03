# The Crypto Review

## Introduction
Welcome to our project, TheCryptoReview, created for the STEM Warriors Hackathon! For easy access, check out our site publicly hosted on Heroku here: https://the-crypto-review.herokuapp.com/index.html. To view our website locally, download the repository, then run pip install -r requirements.txt, and finally run the app.py file. For more information on how our project works, check out our YouTube video describing it linked here: [INSERT LINK].

## Inspiration
One of our teammates Anuj was heavily interested in blockchain and cryptocurrency with its increasing popularity in the news, even amongst big tech CEOs like Elon Musk, who is a role model and inspiration for all of our team. However, without much experience in the complicated topic of cryptocurrency, Anuj found himself heavily intimidated by the complexity of cryptocurrency data and how to trade based on it. Thus, we created The Crypto Review to help fellow cryptocurrency novices find a simpler introduction to the field of cryptocurrency investing and trade safely.

## What It Does
Our project The Crypto Review is a website providing crypto enthusiasts, especially beginners, an introduction to the world of cryptocurrency so they can trade and earn money without risk. Using accurate Machine Learning and custom mathematical algorithms, our website provides historical and current data about 5000 different cryptocurrencies, including price, volatility, and market cap, and predicts their prices for the next 180 days. The site’s dashboard also displays live updates about top coins and calculates and displays a confidence rating that shows how safe of an investment that cryptocurrency would be for the investor. Lastly, the website includes an education page that provides users a concise and simplified introduction to major topics of cryptocurrency.

## How We Built It
We chose to create our web application using Flask, Python, HTML, CSS, and JavaScript. We used Python, its Flask library, and JavaScript for our backend code. To utilize large datasets with historical cryptocurrency data, we used Python and the Pandas library. We used this data along with various cryptocurrency APIs (CoinMarketCap, Alternative) and additionally implemented web scraping with Python to read data from Yahoo finance. Lastly, we utilized an FBProphet time series machine learning model to make predictions for future cryptocurrency prices using historical data and create an algorithm comparing predicted data to past data to calculate a confidence rating for the user.

For our frontend, we used the latest versions of Flask and Jinja2 to run our HTML, CSS, and JavaScript code on our website. We hosted our site on Heroku, a Platform as a Service (PaaS), and connected it directly to our Github Repo. We set it up so that each time we pushed a commit, the app would update automatically. This made collaboration more efficient and we were able to integrate our various parts effectively. We also created code to embed live updates and visuals on important data like Price and Greed Indices into our website with HTML and JavaScript.

## Challenges We Ran Into
There were various issues concerning Heroku deployment that took an extensive amount of time to solve. We had to familiarize ourselves with the Heroku Command Line interface and utilize its build and application logs to do live debugging during our application's runtime to fix the numerous errors we encountered while building on Heroku. One such error was that the number of files in our repository was too large, so we had to make sure only necessary files were kept in the repository. Another error was that our application was timing out due to the time the application was taking during launch, so we had to optimize our backend code, especially the Machine Learning Model, to ensure that they were within Heroku's free plan's time constraints.

We also had trouble integrating the backend with the front-end visuals in javascript, as it did not use contemporary Flask syntax. Thus, we had to learn new parts of Flask that allowed us to properly integrate it with our visuals in JavaScript.

## Accomplishments That We're Proud Of
The accomplishment that we are most proud of is how fast and accurate our Machine Learning Model was able to predict large amounts of data in a very short time using an even larger dataset to train on. This was an aspect of our project we hadn’t worked with before and were able to successfully implement. Additionally, following the several errors produced by our Heroku deployment of our Flask application, we were able to resolve them and deploy the app with no error. This process took a long time and required much debugging in which we had to work together to overcome.

## What We Learned
Jahsh - I learned more about cryptocurrencies, formatting extremely large and complex JSON data from APIs and integrating them in the backend, and debugging using Heroku CLI
Anuj - I learned about integrating APIs into the backend, developing time-forecasted machine learning, and using Flask to transfer data between different parts of the code
Abhijith - I got more experience with Flask and JavaScript, specifically integrating javascript into HTML to properly load all our graphs and visuals
Theo - I learned how to manipulate and display data in graphs and visuals using javascript and integrating widgets in the front-end HTML code

## What's Next For The Crypto Review
The next step would be to create a mobile app by integrating the backend with Flutter and Dart. This app would also work for both iOS and Android operating systems. To take our website to the next level, we would like to use PHP and a MySQL database to allow users to create accounts and log in where they can pin certain cryptocurrencies to their account dashboard and get email notifications for important news on each of these cryptocurrencies. Additionally, we’d like to deploy it online with its own custom domain so that people can search for The Crypto Review and use it on their web browser. This would allow for more people to use it and for it to impact more crypto-enthusiasts.

Through these next steps for Crypto Review, we hope to expand its reach and make it even easier and more convenient to use for users around the world!


## Thank you, and we hope you enjoy our application The Crypto Review!
