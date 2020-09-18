from django.conf import settings
import logging
import requests
from django.utils import timezone
from data_ocean.converter import Converter, BulkCreateManager
from data_ocean.downloader import Downloader
from data_ocean.models import Register
from data_ocean.utils import clean_name, change_to_full_name
from location_register.models.ratu_models import RatuRegion, RatuDistrict, RatuCity, RatuCityDistrict, RatuStreet

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class RatuConverter(Converter):
    def __init__(self):
        self.API_ADDRESS_FOR_DATASET = Register.objects.get(
            source_register_id=settings.LOCATION_RATU_SOURCE_REGISTER_ID
        ).api_address
        self.LOCAL_FOLDER = settings.LOCAL_FOLDER
        self.LOCAL_FILE_NAME = settings.LOCAL_FILE_NAME_RATU
        self.CHUNK_SIZE = settings.CHUNK_SIZE_RATU
        self.bulk_manager = BulkCreateManager()
        self.region_dict = {}  # dictionary uses for keeping whole model class objects
        self.district_list = list()  # lists use for keeping cells content
        self.city_list = list()
        self.citydistrict_list = list()
        super().__init__()

        # format record's data

    record = {
        'RECORD': '',
        'OBL_NAME': '',
        'REGION_NAME': '',
        'CITY_NAME': '',
        'CITY_REGION_NAME': '',
        'STREET_NAME': ''
    }

    def rename_file(self, file):
        new_filename = file
        if file.upper().find('ATU') >= 0:
            new_filename = 'ratu.xml'
        return new_filename

    # writing entry to db
    def save_to_db(self, record):
        region = self.save_to_region_table(record)
        district = self.save_to_district_table(record, region)
        city = self.save_to_city_table(record, region, district)
        citydistrict = self.save_to_citydistrict_table(record, region, district, city)
        # self.save_to_category_id(record['CITY_NAME'], City)
        # self.save_to_category_id(record['CITY_REGION_NAME'], CityDistrict)
        self.save_to_street_table(record, region, district, city, citydistrict)
        print('saved')

    # writing entry to region table
    def save_to_region_table(self, record):
        record['OBL_NAME'] = change_to_full_name(record['OBL_NAME'])
        if record['OBL_NAME'] not in self.region_dict:
            region = RatuRegion(
                name=record['OBL_NAME']
            )
            region.save()
            self.region_dict[record['OBL_NAME']] = region
            return region
        region = self.region_dict[record['OBL_NAME']]
        return region

    # writing entry to district table
    def save_to_district_table(self, record, region):
        if record['REGION_NAME']:
            district_name = clean_name(record['REGION_NAME'])
            district_name = change_to_full_name(district_name)
        else:
            district_name = RatuDistrict.EMPTY_FIELD
        if [region.id, district_name] not in self.district_list:
            district = RatuDistrict(
                region=region,
                name=district_name
            )
            district.save()
            self.district_list.insert(0, [region.id, district_name])
        district = RatuDistrict.objects.get(
            name=district_name,
            region=region.id
        )
        return district

    # writing entry to city table
    def save_to_city_table(self, record, region, district):
        if record['CITY_NAME']:
            city_name = clean_name(record['CITY_NAME'])
        else:
            city_name = RatuCity.EMPTY_FIELD
        if [region.id, district.id, city_name] not in self.city_list:
            city = RatuCity(
                region=region,
                district=district,
                name=city_name
            )
            city.save()
            self.city_list.insert(0, [region.id, district.id, city_name])
        city = RatuCity.objects.get(
            name=city_name,
            region=region.id,
            district=district.id
        )
        return city

    # writing entry to citydistrict table
    def save_to_citydistrict_table(self, record, region, district, city):
        if record['CITY_REGION_NAME']:
            citydistrict_name = clean_name(record['CITY_REGION_NAME'])
        else:
            citydistrict_name = RatuCityDistrict.EMPTY_FIELD
        if [region.id, district.id, city.id, citydistrict_name] not in self.citydistrict_list:
            citydistrict = RatuCityDistrict(
                region=region,
                district=district,
                city=city,
                name=citydistrict_name
            )
            citydistrict.save()
            self.citydistrict_list.insert(0, [region.id, district.id, city.id, citydistrict_name])
        citydistrict = RatuCityDistrict.objects.get(
            name=citydistrict_name,
            region=region.id,
            district=district.id,
            city=city.id
        )
        return citydistrict

    # writing entry to street table
    def save_to_street_table(self, record, region, district, city, citydistrict):
        if record['STREET_NAME']:
            street = RatuStreet(
                region=region,
                district=district,
                city=city,
                citydistrict=citydistrict,
                name=record['STREET_NAME'].lower()
            )
            self.bulk_manager.add(street)
        if len(self.bulk_manager.queues['location_register.RatuStreet']):
            self.bulk_manager.commit(RatuStreet)
        self.bulk_manager.queues['location_register.RatuStreet'] = []

    print(
        'Ratu already imported.',
        'For start rewriting RATU to the DB run > RatuConverter().process()\n',
        'For clear all RATU tables run > RatuConverter().clear_db()'
    )


class RatuDownloader(Downloader):
    chunk_size = 16 * 1024 * 1024
    reg_name = 'location_ratu'
    zip_required_file_sign = 'xml_atu'
    unzip_required_file_sign = 'xml_atu'
    unzip_after_download = True
    source_dataset_url = settings.LOCATION_RATU_SOURCE_PACKAGE

    def get_source_file_url(self):

        r = requests.get(self.source_dataset_url)
        if r.status_code != 200:
            print(f'Request error to {self.source_dataset_url}')
            return

        for i in r.json()['result']['resources']:
            if self.zip_required_file_sign in i['url']:
                return i['url']

    def get_source_file_name(self):
        return self.url.split('/')[-1]

    def update(self):

        logger.info(f'{self.reg_name}: Update started...')

        self.log_init()
        self.download()

        self.log_obj.update_start = timezone.now()
        self.log_obj.save()

        logger.info(f'{self.reg_name}: process() with {self.file_path} started ...')
        ratu = RatuConverter()
        ratu.LOCAL_FILE_NAME = self.file_name
        ratu.process()
        logger.info(f'{self.reg_name}: process() with {self.file_path} finished successfully.')

        self.log_obj.update_finish = timezone.now()
        self.log_obj.update_status = True
        self.log_obj.save()

        self.remove_file()

        logger.info(f'{self.reg_name}: Update finished successfully.')
