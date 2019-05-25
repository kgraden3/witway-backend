import web3
import os
from django.conf import settings

def getKeystore():
    return open(os.path.join(settings.BASE_DIR, 'witway-keystore'))
