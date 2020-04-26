## SHUJAAZ COMIC APPLICATION

[![CircleCI](https://circleci.com/gh/salma-nyagaka/shujaaz-comic.svg?style=svg&circle-token=4134ce23d56f8512d56b50033c196f5d57d8fe20)](https://circleci.com/gh/salma-nyagaka/shujaaz-comic)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9db5d6439d174747814e9bfedb56761a)](https://www.codacy.com/manual/salma-nyagaka/shujaaz-comic?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=salma-nyagaka/shujaaz-comic&amp;utm_campaign=Badge_Grade)


#### TEST DOCUMENTATION

- [Link](https://circleci.com/api/v1.1/project/github/salma-nyagaka/shujaaz-comic/72/output/106/0?file=true&allocation-id=5ea58761b40dc80282801bde-0-build%2F311DB503)

#### API DOCUMENTATION

- [Link](https://circleci.com/api/v1.1/project/github/salma-nyagaka/shujaaz-comic/72/output/106/0?file=true&allocation-id=5ea58761b40dc80282801bde-0-build%2F311DB503)

#### AWS DEPLOYMENT

- Link

#### DESCRIPTION
#### This is an API that achieves the following:-
- Fetches a list of all comics available
- Fetches a single comic
- Fetches a list of all creators
- Fetches a single creator
- Fetches a list of stories within a comic
- Fetches a character/characters within a comic


#### DEVELOPMENT SETUP
-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.7.1
    ```

-   Install virtualenv:

    ```
    brew install virtualenv
    ```

-   Check virtualenv is installed:

    ```
    virtualenv --version
    >> virtualenv 20.0.18
    ```
    
-   Check that postgres is installed:

    ```
    postgres --version
    >> postgres (PostgreSQL) 12.2
    ```

-   Clone the shujaaz-comic repo and cd into it:

    ```
    git clone https://github.com/salma-nyagaka/shujaaz-comic.git
    ```

-   Install dependencies:

    ```
    pip3 install -r requirements.txt
    ```

-  Create .env file at the root of the project and update the variables accordingly:

    ```
    DATABASE_URL = "postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_DATABASE_NAME"
    TEST_DATABASE_URL = "postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_TEST_DATABASE_NAME" 
    ```

-   Activate a virtual environment:

    ```
    virtualenv venv
    ```
    
-   Export the environment settings:

    ```
    source .env
    ```

-   Apply migrations and load the fixtures:

    ```
    source releashe.sh
    ```

-   Run the application with this command:

    ```
    python manage.py runserver 
    ```

 #### ENDPOINTS
| REQUEST | DESCRIPTION  | URL  |
| :-----: | :-: | :-: |
| GET | Fetch a list of all creators |  http://127.0.0.1:8000/api/users/ |
| GET | Fetch a single creator |  http://127.0.0.1:8000/api/users/1/ |
| GET | Fetch a list of all comics available |   http://127.0.0.1:8000/api/comics/ |
| GET | Fetch a single comic |   http://127.0.0.1:8000/api/comics/1/ |
| GET | Fetch a list of stories within a comic |   http://127.0.0.1:8000/api/comics/3/stories/ |
| GET | Fetch a character/characters within a comic |  http://127.0.0.1:8000/api/comics/3/characters/ |



