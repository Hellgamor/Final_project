## 1 задание: 
### Нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: вывести список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).  

> SELECT c.login, count(o.id)  
> FROM "Couriers" AS c  
> JOIN "Orders" AS o ON c.id=o."courierId"  
> WHERE "inDelivery" = true  
> GROUP BY c.login;

Результат выполнения запроса:
![Результат выполнения запроса](https://github.com/Hellgamor/Sql_and_autotest_project/blob/master/sql_query_1.png)

## 2 задание:
### Тестируются статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: вывести все трекеры заказов и их статусы.  
Статусы определяются по следующему правилу:  
Если поле finished == true, то вывести статус 2.  
Если поле canсelled == true, то вывести статус -1.  
Если поле inDelivery == true, то вывести статус 1.  
Для остальных случаев вывести 0.

> SELECT track,   
     CASE  
        WHEN finished = true THEN 2  
        WHEN cancelled = true THEN -1  
        WHEN "inDelivery" = true THEN 1  
     ELSE 0 END AS status  
FROM "Orders";

Результат выполнения запроса:
![Результат выполнения запроса](https://github.com/Hellgamor/Sql_and_autotest_project/blob/master/sql_query_2.png)