from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, EquipCategory, EquipBrand, User
#import psycopg2

databaseName = 'pvequipment'
engine = create_engine('postgresql+psycopg2://catalog:catalog@localhost/' + databaseName)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def addItem(entry):
	session.add(entry)
	session.commit()

# initial user data
user1 = User(name='Mark Purser', email='purser.mark@gmail.com', id=1)
addItem(user1)

# initial equipment category data
equipCat1 = EquipCategory(name="PV Panels", user_id=1, id=1)
addItem(equipCat1)

equipCat3 = EquipCategory(name="Inverters", user_id=1, id=2)
addItem(equipCat3)

equipCat2 = EquipCategory(name="Bracketing", user_id=1, id=3)
addItem(equipCat2)


# initial brand data
equipBrand1 = EquipBrand(name="Sunpower", category_id=1, description='Sunpower-made PV panels', user_id=1)
addItem(equipBrand1)

equipBrand2 = EquipBrand(name="LG", category_id=1, description='LG-made PV panels', user_id=1)
addItem(equipBrand2)

equipBrand3 = EquipBrand(name="Trina", category_id=1, description='Trina-made PV panels', user_id=1)
addItem(equipBrand3)

equipBrand4 = EquipBrand(name="Sunnyboy", category_id=2, description='Sunnyboy string inverters', user_id=1)
addItem(equipBrand4)

equipBrand5 = EquipBrand(name="Enphase", category_id=2, description='Enphase micro-inverters', user_id=1)
addItem(equipBrand5)

equipBrand6 = EquipBrand(name="LG", category_id=2, description='LG string inverters', user_id=1)
addItem(equipBrand6)

equipBrand7 = EquipBrand(name="Snap n rack", category_id=3, description='Sunrun-made rails', user_id=1)
addItem(equipBrand7)

equipBrand8 = EquipBrand(name="Zep", category_id=3, description='Solarcity-made rails', user_id=1)
addItem(equipBrand8)

equipBrand9 = EquipBrand(name="Railless", category_id=3, description='SunEdison-made railless system', user_id=1)
addItem(equipBrand9)

# unlike sqlite, postgresql seems to struggle with auto-incrementing the primary key.
# queries below are designed to address this.
sql = 'ALTER SEQUENCE users_id_seq RESTART WITH 2;'
engine.execute(sql)
sql = 'ALTER SEQUENCE equip_category_id_seq RESTART WITH 4;'
engine.execute(sql)
sql = 'ALTER SEQUENCE equip_brand_id_seq RESTART WITH 10;'
engine.execute(sql)

print("since empty, added initial equipment/brands!")