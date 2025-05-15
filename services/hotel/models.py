from pydantic import BaseModel, EmailStr, field_validator, Field
from typing import Optional, Dict, List, Literal
import phonenumbers
from enum import Enum
from datetime import datetime, time


class PhoneNumberModel(BaseModel):
    """Модель для номера телефона с валидацией"""
    phone: str

    @field_validator('phone')
    def validate_phone(cls, v):
        try:
            parsed = phonenumbers.parse(v, "RU")
            if not phonenumbers.is_valid_number(parsed):
                raise ValueError("Invalid phone number")
        except phonenumbers.NumberParseException:
            raise ValueError("Invalid phone number format")
        return v

class ChildrenAgeInterval(BaseModel):
    """Модель для возрастных интервалов детей"""
    id: int
    min_age: int
    max_age: int
    beds_types: List[int]

class LogoModel(BaseModel):
    id: int
    name: str
    file_name: str
    mime_type: str
    size: int
    account_id: int
    url: str
    create_date: datetime
    update_date: datetime

class CurrencyModel(BaseModel):
    id: int
    iso_4217: str
    sign: str
    text: str
    create_date: Optional[str]
    update_date: Optional[str]

class ModuleSettingsModel(BaseModel):
    id: int
    account_id: int
    cart_position: int
    message_welcome_ru: Optional[str]
    message_welcome_en: Optional[str]
    message_rooms_unavailable_ru: Optional[str]
    message_rooms_unavailable_en: Optional[str]

class HotelType(str, Enum):
    hotel = "hotel"
    apartments = "apartments"
    hostel = "hostel"
    pension = "pension"
    recreational_center = "recreational center"
    sanatorium = "sanatorium"
    apart_hotel = "apart_hotel"
    glamping = "glamping"
    country_hotel = "country_hotel"
    motel = "motel"
    children_health_camp = "children_health_camp"
    other = "other"

class Account(BaseModel):
    """Модель Account"""
    id: int = Field(gt=0)
    name: str
    phone: str
    email: EmailStr
    address: Optional[str]
    address_eng: Optional[str]
    country: Optional[str]
    city: Optional[str]
    city_eng: Optional[str]
    enabled: Optional[int]
    checkin: time
    checkout: time
    logo_id: Optional[int]
    currency_id: Optional[int]
    timezone: Optional[str]
    uid: str
    language: Optional[str]
    compare_roomtypes_enabled: Optional[int]
    google_hotels_ads: Optional[int]
    geo_data: str
    yandex_metrika_counter_id: Optional[int]
    hotel_type: HotelType
    new_ui_enabled: Optional[int]
    offers: str
    logo: Optional[LogoModel]
    currency: CurrencyModel
    module_settings: ModuleSettingsModel
    fast_track_enabled: int
    map_link: str
    min_children_age: int
    children_ages: Dict[str, ChildrenAgeInterval]

class Hotel(BaseModel):
    account: Account





