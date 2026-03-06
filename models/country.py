from sqlalchemy import Column, String, DateTime, Text
from core.database import Base

class Country(Base):
    __tablename__ = "countries"

    slug = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    alert_status = Column(String)
    entry_requirements_html = Column(Text)
    last_updated = Column(DateTime)
    gov_uk_last_updated = Column(DateTime)
