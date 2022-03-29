# learn_sql_alchemy
sql alchemy playground base

---

Initial data at `init.sql` for **PostgreSQL**

## To run database and fill it with initial data
```shell
docker build -t sql_alchemy_test_db_img . && docker run -p 5432:5432 --name sql_alchemy_test_db sql_alchemy_test_db_img 
```
---
That gives us simple **_Post_** and **_User_** models for experiments

Example at `basic_sql_models.py`