#### Configure MongoDB Connection Variables

`mongoSettings.py` Python program to configure MongoDB Connection Variables.

#### SalesApp Python code written to use mongo-python-driver (aka PyMongo)

`SalesApp_GenerateInitialLookupData.py` Generates Initial Lookup Data. Typically executed only 1 time during initial setup.

`SalesApp_GenerateUsers.py` Generates Users. Typically executed only 1 time during initial setup. Code will generate 10000 users.

`SalesApp_GenerateProducts.py` Generates Products. Typically executed only 1 time during initial setup. Code will generate 50000 products.

`SalesApp_GenerateOrders.py` Generates Orders. Execute it whenever you want to generate Orders or automate the execution using cron.

---

#### crontab

`crontab_for_auto_order_generation.md` crontab entries to automatically generate Orders.

---

NOTE : PYTHON CODE IS WRITTEN FOR DEMONSTRATION PURPOSES ONLY. IT IS NOT OPTIMIZED, NOR WRITTEN BY A PROFESSIONAL PYTHON PROGRAMMER.

<br><br>
![SalesOrder_SampleDocument.jpg](https://github.com/sarma1807/mongo-python-driver/blob/main/31_SalesApp_AutoSalesGenerator/SalesOrder_SampleDocument.jpg)

