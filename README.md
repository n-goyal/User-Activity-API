# FullThrottle Backend Engineer - Python/Django Assignment 🏴‍☠️

(Problem statement 📃 is provided in the repository )

A short walk through of the implementation:

**Database**: MongoDB Atlas, I had a free tier cluster running :P

**Django Database Engine**: Djongo, pymongo

## I. Database Models 📚

### 1. User 👳

User has `tz, real_name, id` fields. All fields are made mandatory

### 2. ActivityPeriod 〽️

ActivityPeriod has `activity_id, start_time, end_time, user` fields

`Considering the fact that the User has one-to-many relationship with activity periods,User id has been added as Foriegn Key to the ActivityPeriod`

## II. Custom Management Command 🎛️- populatedb 🍔

command: `python3.7 manage.py populatedb <no_of_records>`

-   Command takes **no_of_records** argument, which is basically to declare how
    many dummy user records you want to insert in the database.
-   Acvitiy period generation is also random i.e. One user can have **2 to 18
    activity period records**.
-   `faker, random, datetime and nanoid` packages were used to fake data

## III. API end point: GET /api/v1/users 🌏

-   Fetches a list of users, following the given json format 🖥️🖥️ App is hosted
    at

        https://stark-escarpment-05147.herokuapp.com/

### IV. Deployment🚀 - Docker 🐋 + Heroku #️⃣

-   I tried a couple of ways to deploy the application but hosting docker
    container on Heroku was smooth so I stopped figuring out the wrongs in my
    pythonanywhere deployment 🏃‍♂️.
-   Database url, username and password are configured as enviornment variables
    on Heroku itself.
