# Emotion And Sentiment Based Video Recommendation (ESV)

*	Description
*	Installation
*	Usage
*	Dataset

## Description
YouTube algorithms recommend videos to its users according to their search and watch history. But as emotional intelligence has recently become a hot topic all over the world so we are going to present an idea of an artificial intelligence app in which we will recommend videos to users according to their emotions with deep learning technique CNN using TensorFlow framework. This artificial intelligence app will first detect the user's emotions using their facial expressions. Later, it will suggest videos according to users' moods/emotions. Moreover, sentiment analysis will also be applied to suggest the best-recommended videos to our customers. 

## Installation

### Install Pycharm and python
Pycharm and python are required in order to run this project.

### Install Django
Command to install Django is following.
```
pip install django
```

###	Install Xampp
 Xampp is required for the creation of database on localhost and to migrate Django models
 
### Start Apache server and Mysql
Create a Database with the name “esv” to run this code. 
Create Database esv
### Commands
``````
pip install mysqlclient
``````
This command will migrate all the data from Django models.

``````
python manage.py migrate
``````
For easy embedding of YouTube and Vimeo videos type the following command on Django Terminal

``````
pip install django-embed-video
``````
Type this command on Pycharm Terminal to run Django project.

``````
python manage.py runserver
``````
This command is used to run entire project.

## Usage
The program will show a web Django app that includes a home page, Feedback page, Videos Page, Login/Signup page, help, and About us page. 

## Dataset
We are going to use Affectiva Dataset. Due to the user license agreement, we can't upload it here. If you want to download it visit the Affectiva website and fill user license agreement in order to get the dataset. 

## Ongoing
This project is ongoing. 

## Issues/Problems
User interface design might look different on different we browser.
