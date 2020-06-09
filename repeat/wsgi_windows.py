# activate_this = 'C:/Users/myuser/Envs/my_application/Scripts/activate_this.py'
activate_this = 'C:/Users/PRENCHAND/secondrepoofdjango/repeat_store_product/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
# site.addsitedir('C:/Users/myuser/Envs/my_application/Lib/site-packages')
site.addsitedir('C:/Users/PRENCHAND/secondrepoofdjango/repeat_store_product/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/PRENCHAND/secondrepoofdjango/repeat_store_product')
sys.path.append('C:/Users/PRENCHAND/secondrepoofdjango/repeat_store_product/repeat')

os.environ['DJANGO_SETTINGS_MODULE'] = 'repeat.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "repeat.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
