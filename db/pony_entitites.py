from db.pony_config import *
from datetime import date

#création de la base de donnée
class User(db.Entity):
    _table_ = "t_user"
    email = Required(str, unique=True)
    password = Required(str)
    firstname = Optional(str)
    lastname = Optional(str)
    token = Required(str, unique=True)
    role = Set("Role")

class Role(db.Entity):
    _table_ = "t_role"
    tag = Required(str)
    user = Set(User)

class Customer(db.Entity):
    _table_ = "t_customer"
    email = Required(str)
    address = Set("Address")
    order = Optional("Order")

class Address(db.Entity):
    _table_ = "t_address"
    number = Required(str)
    street = Required(str)
    additional = Required(str)
    customer = Set(Customer)
    city = Set("City")

class City(db.Entity):
    _table_ = "t_city"
    zipCode = Required(str)
    name = Required(str)
    department = Required(str)
    address = Set(Address)

class Order(db.Entity):
    _table_ = "t_order"
    date = Required(date)
    stampCustomer = Required(float)
    stampCode = Required(float)
    numberPackage = Required(int)
    check = Required(float)
    conditioning = Required("Conditioning")
    customer = Required(Customer)
    detailOrder = Required("DetailOrder")

class Conditioning(db.Entity):
    _table_ = "t_conditioning"
    tag = Required(str)
    weightTag = Required("WeightTag")
    price = Required(float)
    order = Set(Order)
    object = Set("Object")

class DetailOrder(db.Entity):
    _table_ = "t_detail_order"
    quantity = Required(int)
    order = Optional(Order)
    object = Set("Object")

class Object(db.Entity):
    _table_ = "t_object"
    name = Required(str)
    height = Required(int)
    weight = Required("Weight")
    description = Required(str)
    detailOrder = Set(DetailOrder)
    price = Required("Price")
    update = Set("Update")
    stockLine = Required("StockLine")
    shop = Required("Shop")
    conditioning = Required(Conditioning)

class Update(db.Entity):
    _table_ = "t_update"
    quantity = Required(int)
    date = Required(date)
    object = Set(Object)

class Price(db.Entity):
    _table_ = "t_price"
    price = Required(float)
    object = Optional(Object)

class StockLine(db.Entity):
    _table_ = "t_stock_line"
    quantity = Required(int)
    object = Set(Object)
    stock = Required("Stock")
    
class Stock(db.Entity):
    _table_ = "t_stock"
    name = Required(str)
    stockLine = Set(StockLine)
    
class Shop(db.Entity):
    _table_ = "t_shop"
    name = Required(str)
    date = Required(date)
    object = Set(Object)
    
class Weight(db.Entity):
    _table_ = "t_weight"
    w_val = Required(float)
    object = Set(Object)

class WeightTag(db.Entity):
    _table_ = "t_weight_tag"
    tagValues = Required(float)
    conditioning = Set(Conditioning)

db.generate_mapping(create_tables=True)
