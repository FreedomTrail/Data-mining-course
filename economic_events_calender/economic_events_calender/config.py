MONGO_USER = "root"
MONGO_URL = "mongodb://localhost:27017/"

try:
    from local_config import *
except ImportError:
    pass
