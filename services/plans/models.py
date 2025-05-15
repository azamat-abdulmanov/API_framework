from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Union


class BookingGuaranteeDescriptionPart(BaseModel):
    booking_guarantee_description_ru: Optional[str] = None
    booking_guarantee_description_en: Optional[str] = None
    booking_guarantee_description_de: Optional[str] = None
    booking_guarantee_description_zh: Optional[str] = None
    booking_guarantee_description_es: Optional[str] = None
    booking_guarantee_description_fr: Optional[str] = None
    booking_guarantee_description_ja: Optional[str] = None
    booking_guarantee_description_it: Optional[str] = None
    booking_guarantee_description_ko: Optional[str] = None
    booking_guarantee_description_pl: Optional[str] = None
    booking_guarantee_description_fi: Optional[str] = None
    booking_guarantee_description_lt: Optional[str] = None
    booking_guarantee_description_ro: Optional[str] = None
    booking_guarantee_description_lv: Optional[str] = None
    booking_guarantee_description_hy: Optional[str] = None
    booking_guarantee_description_uk: Optional[str] = None

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

class CancellationRulesPart(BaseModel):
    cancellation_rules_ru: Optional[str] = None
    cancellation_rules_en: Optional[str] = None
    cancellation_rules_de: Optional[str] = None
    cancellation_rules_zh: Optional[str] = None
    cancellation_rules_es: Optional[str] = None
    cancellation_rules_pl: Optional[str] = None
    cancellation_rules_fr: Optional[str] = None
    cancellation_rules_ja: Optional[str] = None
    cancellation_rules_it: Optional[str] = None
    cancellation_rules_ko: Optional[str] = None
    cancellation_rules_fi: Optional[str] = None
    cancellation_rules_lt: Optional[str] = None
    cancellation_rules_ro: Optional[str] = None
    cancellation_rules_lv: Optional[str] = None
    cancellation_rules_hy: Optional[str] = None
    cancellation_rules_uk: Optional[str] = None

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

class Localization(BookingGuaranteeDescriptionPart, DescriptionsPart, CancellationRulesPart, NamesPart):
    pass

class PlanCancellations(BaseModel):
    id: int
    account_id: int
    plan_id: int
    date_from: datetime
    date_to: datetime
    deadline: int
    fine: int
    fine_amount: int

class BookingGuaranteePart(BaseModel):
    booking_guarantee_sum: str
    booking_guarantee_unit: str
    booking_guarantee_percentage_from: str
    booking_guarantee_link: Optional[str]
    booking_guarantee_services: int = 0
    booking_guarantee_till_hours_after: Optional[int] = None

class Plan(BaseModel):
    id: int = Field(gt=0)
    name: str
    account_id: int = Field(gt=0)
    description: Optional[str] = None
    cancellation_rules: Optional[str] = None
    booking_guarantee_description: Optional[str] = None
    create_date: datetime
    update_date: datetime
    default: int
    delete_date: Optional[datetime]
    enabled: int
    restriction_plan_id: Optional[int]
    nutrition: str
    order: Optional[int]
    legal_entity_id: Optional[int]
    for_promo_code: int
    enabled_ota: int
    warranty_type: str = 'no'
    warranty_card_card_types: str = ''
    warranty_card_need_cvv: bool = True
    payment_systems: Optional[str] = '[]'
    board_from_services: int = 0
    payment_system_ids: Optional[str] = None
    extra: Optional[str]
    enabled_yandex: int = 0
    cancellation_rule: int = 0
    additional_services_ids: Union[List, Dict[int, int]]
    plan_cancellations: List[PlanCancellations] = []

class PlanConstructor(Plan, BookingGuaranteePart, Localization):
    pass

class Plans(BaseModel):
    plans: List[PlanConstructor]