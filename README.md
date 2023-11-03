# CRUD-django


## Financial Project

The aim of this project is to build a data model embedded in a database and an API to perform CRUD operations using the
financial data.

### Set up

-----------

Pre requirements:

* You will need to have Docker installed, if not please
download [here](https://www.docker.com/products/docker-desktop/) and install it.
* You will need an env file called env.dev with the following content:

```
DEBUG=1
SECRET_KEY=admin
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=financial_project_dev
SQL_USER=financial_project
SQL_PASSWORD=financial_project
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

First, we want build the docker compose image. You can see the file to make this build [here](docker-compose.yml).  
For this we move to the path that we have the [project folder](./) (in our console/terminal/bash).

```cd financial-analysis```

After that, we can build the docker image. Remember to have your docker app (docker daemon) running.

```bash 
docker-compose build
```

We can use docker-compose up; it will create to docker containers, one for the API and one for the database.

```bash
docker-compose up -d
```

Once our containers are running you can create the table in our database with the following  command:

```bash
docker-compose run web python manage.py migrate
```

After that, you can fill the database with the provided data or any data with the same json structure.

```bash
docker-compose run web python manage.py load_financial_data data/financial_data.json
```

Now, you have your API ready.

### Usage

To use this API you just have to make request with CRUD methods to one of the following urls:

http://localhost:8000/api/financialmeasures

http://localhost:8000/api/financialmeasure?financial_measure={financial_measure_name}

http://localhost:8000/api/financialmeasure/{record_number}

You can make the request [Postman](https://www.postman.com/), [Insomnia](https://insomnia.rest/) or simply using the above urls in your browser.

### Example

__________
We are going to give you and example of usage using the browser.

First we are going to see the different finance measures we have and how we
can create a new record in the database: http://localhost:8000/api/financialmeasures

![img.png](financial_project/data/images/financial_measures.png)

Now, let's see data with financial measure = Assets: http://localhost:8000/api/financialmeasure?financial_measure=Assets

![img.png](financial_project/data/images/data_of_a_financial_measure.png)

Finally, we can see, update and delete a record in the database: http://localhost:8000/api/financialmeasure/6

![img.png](financial_project/data/images/see_delete_update_record.png)


Enjoy it!

Please, see [technical notes](financial_project/docs/technical_notes.md) to know more about the technical part of the project (it also includes future improvements).

