import yaml
import os
from tcia_utils import  nbia
import requests
    

def download():
    print('Downloading CMMD TCIA...')
    url = 'https://www.cancerimagingarchive.net/wp-content/uploads/The-Chinese-Mammography-Database.tcia'
    try:
        r = requests.get(url, allow_redirects=True)
        open('/tcia/CMMD.tcia', 'wb').write(r.content)
        print('TCIA downloaded.')
        return True
    except requests.exceptions.RequestException as e:
        print('Error downloading TCIA data.')
        return False

def download_clinical_data():
    print('Downloading CMMD clinical data...')
    url = 'https://www.cancerimagingarchive.net/wp-content/uploads/CMMD_clinicaldata_revision.xlsx'
    try:
        r = requests.get(url, allow_redirects=True)
        open('/tciaDownload/CMMD_clinicaldata_revision.xlsx', 'wb').write(r.content)
        print('CMMD clinical data downloaded.')
        return True
    except requests.exceptions.RequestException as e:
        print('Error downloading clinical data.')
        return False


def download_tcia_data(config):
    download_clinical_data()
    if config['dataSet']['tcia']:
        tcia = config['dataSet']['tcia']
        print('Checking TCIA file exist...')
        # Check if TCIA data already exists
        if os.path.exists('/tcia/' + tcia):
            print('TCIA data already exists.')
            # rename the file to CMMD.tcia
            os.rename('/tcia/' + tcia, '/tcia/CMMD.tcia')
            return True
        else:
            print('TCIA data does not exist.')
            return download()
        
    else:
        return download()

def patient_to_be_removed(config):
    if not config['dataSet']['patientToBeRemoved']:
        return
    listPatientsToRemove = config['dataSet']['patientToBeRemoved'] 
    
    # each item is a pair of range of patient's ID  to be removed
    # We  need to get the Study UID of the patients to be removed and remove them from the TCIA manifest
    manifest = '/tcia/CMMD.tcia'
    
    uids = nbia.manifestToList(manifest)
    df = nbia.getSeriesList(uids)
    df = df.sort_values(by=['Subject ID'])
    for items in listPatientsToRemove:
        item = items.split(',')
        start = item[0]
        end = item[1]
        df2 = df[df['Subject ID'].between(start, end)]
        SID_list = df2['Series ID'].to_list()
        
        with open('/tcia/CMMD.tcia','r') as f:
            lines = f.readlines()
        with open('/tcia/CMMD.tcia','w') as f:
            for line in lines:
                if not any(SID in line for SID in SID_list):
                    f.write(line)

def config_read():
    try:
        with open('/config/config.yaml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        print('Config file not found. Set to default values.')
        config = {}
    try:
        config['dataSet']
    except KeyError:
        config['dataSet'] = None
    try:
        config['dataSet']['tcia']
    except KeyError:
        config['dataSet']['tcia'] = None
    try:
        config['dataSet']['patientToBeRemoved']
    except KeyError:
        config['dataSet']['patientToBeRemoved'] = None
    return config
    
def main():
    config = config_read()
    download_tcia_data(config)
    patient_to_be_removed(config)


if __name__ == '__main__':
    main()
