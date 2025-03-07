_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organise my records,
I want to keep a list of albums' release years.

As a music lover,
So I can organise my records,
I want to keep a list of albums' artist_ids.
```

```
Nouns:

album, title, release year, artist_id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| album                 | title, release year, artist_id |

Name of the table (always plural): `albums`

Column names: `title`, `release_year`, `artist_id`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
id: SERIAL
title: text
release_year: int,
artist_id: int foreign key -> artists
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, column names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int,
  CONSTRAINT fk_artist foreign key(artist_id) references artists(id) on delete cascade
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```