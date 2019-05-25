import web3
import os
from django.conf import settings

keystore = open(os.path.join(settings.BASE_DIR, 'keystore'))
