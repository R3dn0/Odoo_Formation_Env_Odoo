Install requirement from odoo and create a `postgres` db for user odoo with  using
```
createdb -U odoo my_odoo_db
```

Launch from `./` with 
```bash
# Option 1 : Activer le venv
source .venv/bin/activate
python odoo/odoo-bin -c odoo.conf

# Option 2 : Utiliser directement le binaire du venv
./.venv/bin/python odoo/odoo-bin -c odoo.conf
```
