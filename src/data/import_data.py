import pandas as pd
import numpy as np
import yaml
import s3fs

# enabling conexion to s3 storage for data retrieving
def import_(key_id, access_key, token):
    fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': 'https://'+'minio.lab.sspcloud.fr'}, 
        key=key_id, secret=access_key, token=token)
    return pd.read_sas(fs.open("ikonkobo/commsdata/commsdata.sas7bdat"), format='sas7bdat')