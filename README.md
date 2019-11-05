# My First Flask App
First sprint will be just to implement CRUD
for a simple weather app
Stack will include:
>firebase | flask | bootstrap

1. Have to make an enviornment
- Using python 3.7.3 -> check using `python --version`
- create virtual enviornment with command `python -m venv <myproject>`
- then make sure to activate the virtual enviornment `source myproject/bin/activate`
- install flask using pip as a package manager 
    - check your pip verison `pip --version`
    - install flask `pip install flask`
    - organize a requirements.txt file `pip freeze > requirements.txt`
    - check flask version `flask --version` i'm using 1.1.1
    - you can quick start with `pip install -r requirements.txt`
    
2. Next thing I want tot do is create an hellowWorld.py file
```
<myproject>
     |_ helloWorld.py
``` 
- from here I'l check if everything's working correctly with this command `python hellWorld.py` //by default the app will run on port 5000

3. Now I will set up Continuous Integration and Continuous development with Heroku
    - Create heroku account
    - download cli `brew tap heroku/brew && brew install heroku`
    - verify install `heroku --version` i'm using heroku/7.33.3
    - log in -> enter your credentials `heroku login -i`
    - go into your project directory `cd myproject`
    - *in this case, because we're running flask, create a profile with the following content* -> `touch Procfile && echo "web: FLASK_APP=helloWorld.py python -m flask run --host=0.0.0.0 --port=$PORT" > Procfile`
    - verify with `cat Procfile` that all the contents are there (this is so that heroku knows how to run the app)
    - run `heroku create`
    - in this portion we are also going to quickly set up a delivery pipeline with heroku
    - first run `heroku pipelines:create -a example-app`
    - then run `heroku pipelines:add example-pipeline -a example-staging-app`
    - and we can promote a heroku slug (you app thats running live) to production with `heroku pipelines:promote -r staging`
    - hit `heroku help pipelines` for any help
    - here's a quick look at the pipeline on Heroku.com 
    
    ![Heroku Pipeline](firstFlaskApp/weatherApp/img/heroku pipelines.png)
    