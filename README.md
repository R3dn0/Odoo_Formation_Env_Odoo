Setup
```bash
createuser odoo
createdb -U odoo my_odoo_db

python3.12 -m venv .venv
source .venv/bin/activate

pip install -r odoo/requirements.txt

python odoo/odoo-bin -c odoo.conf -i base
```

For futur launch from `./` use 
```bash
source .venv/bin/activate
python3.12 odoo/odoo-bin -c odoo.conf
```
