Install requirement from odoo and create a `postgres` db for user odoo with  using
```
createdb -U odoo my_odoo_db
```

Launch from `./` with 
```
python3.12 odoo/odoo-bin -c odoo.conf -d my_odoo_db
```
