from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Union

class NamesPart(BaseModel):
    name_ru: Optional[str] = None
    name_en: Optional[str] = None
    name_zh: Optional[str] = None
    name_de: Optional[str] = None
    name_es: Optional[str] = None
    name_pl: Optional[str] = None
    name_fr: Optional[str] = None
    name_ja: Optional[str] = None
    name_it: Optional[str] = None
    name_ko: Optional[str] = None
    name_fi: Optional[str] = None
    name_lt: Optional[str] = None
    name_ro: Optional[str] = None
    name_lv: Optional[str] = None
    name_hy: Optional[str] = None
    name_uk: Optional[str] = None

class DescriptionsPart(BaseModel):
    description_ru: Optional[str] = None
    description_en: Optional[str] = None
    description_zh: Optional[str] = None
    description_de: Optional[str] = None
    description_es: Optional[str] = None
    description_pl: Optional[str] = None
    description_fr: Optional[str] = None
    description_ja: Optional[str] = None
    description_it: Optional[str] = None
    description_ko: Optional[str] = None
    description_fi: Optional[str] = None
    description_lt: Optional[str] = None
    description_ro: Optional[str] = None
    description_lv: Optional[str] = None
    description_hy: Optional[str] = None
    description_uk: Optional[str] = None

class Localization(DescriptionsPart, NamesPart):
    pass

class RoomType(BaseModel):
    id: int = Field(ge=0)
    account_id: int = Field(ge=0)
    parent_id: int = Field(ge=0)
    name: str
    description: Optional[str]
    adults: int = Field(ge=0)
    children: int = Field(ge=0)
    photos: Optional[List[Dict]]
    order: Optional[int]
    accommodation_type: int
    bed_variant: Optional[int]
    youtube_url: Optional[str]
    video_url: Optional[str]
    amenities: Union[List, Dict]
    extra_array: Optional[Dict]

class RoomTypeConstructor(RoomType, Localization):
    pass

class Rooms(BaseModel):
    rooms: List[RoomTypeConstructor]
