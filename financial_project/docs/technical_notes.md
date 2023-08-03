# Technical notes

These notes are intended to explain technical decisions made in this project.

## TOOLS USED

* Django and Django Rest Framework: The challenge involves creating a database and an API connected to the database.
  Django is a high-level framework to do this and make development faster, more organized, and maintainable.

  Note: [Challenge explanation](Python Engineer Coding Challenge.pdf) said that we should write
  the SQL scripts to create the tables. Django manages it with [models](../financial_api/models.py)
  and [migrations,](../financial_api/migrations) but you can still see the SQL code to create and update
  the database with the following command:

```docker-compose run web python manage.py sqlmigrate financial_api 0001``` where 0001 is the number of the migration.

* PostgreSQL: Most popular choice for various projects, especially in web development. It is scalable and open source.
* Pandas: Most popular choice for data manipulation.

## Folder Structure

We follow Django suggestion where we have a [project](../) and an [app](../financial_api). 
With this way we ensure we have files well organised, and we have a scalable project (we can add as many app as we want). 
On the other, I have added two more folders [docs](/) to have all the documentation, [notebooks](../notebooks) to play with data interactively and [data](../data).

## Data model
Our data model only has one table called financial_data with the following columns:
* financial_measure
* date
* amount
* currency
* unit

With this structure, we can add as many different financial measures to our table as we want. For example, we want to add equity multiplier, we only need to add key value like this in our [json](../data/financial_data.json):

```json
{
   "equity multiplier": {
          "2011-12-31": 30520.04,
          "2012-12-31": 47468.32,
          "2013-12-31": 57888.2,
          "2014-12-31": 50415.58,
          "2015-12-31": 55230.9,
          "2016-12-31": 69160.86,
          "2017-12-31": 15701.32,
          "2018-12-31": 79005.99,
          "2019-12-31": 74318.8
        }}
```
