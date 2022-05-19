# coding: utf-8
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_serializer import SerializerMixin

from app import db


class Region(db.Model, SerializerMixin):
    __bind_key__ = 'information'
    __tablename__ = "region"

    id = db.Column(db.Text, primary_key=True)

    subregions = db.relationship("SubRegion")


class SubRegion(db.Model, SerializerMixin):
    __bind_key__ = 'information'
    __tablename__ = "sub_region"

    id = db.Column(db.Text, primary_key=True)
    region_id = db.Column(db.
        ForeignKey("region.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    countries = db.relationship("Country")
    region = db.relationship("Region", back_populates="subregions")


class Country(db.Model, SerializerMixin):
    __bind_key__ = 'information'
    __tablename__ = "country"

    id = db.Column(db.CHAR(2), primary_key=True)
    subregion_id = db.Column(db.
        ForeignKey("sub_region.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    calling_code = db.Column(db.Integer)
    name = db.Column(db.Text)
    other_names = db.Column(db.Text)
    motto = db.Column(db.Text)
    date_of_independence = db.Column(db.Date)
    description = db.Column(db.Text)
    political_system = db.Column(db.Text)
    location = db.Column(db.Text)
    neighbours = db.Column(db.Text)
    capital_city = db.Column(db.Text)
    population = db.Column(db.Float(53))
    languages = db.Column(db.Text)
    facts_and_figures = db.Column(db.Text)
    classification = db.Column(db.Text)
    life_expectancy = db.Column(db.Float)
    median_age = db.Column(db.Float)
    average_children = db.Column(db.Float)
    income_group = db.Column(db.Text)
    employment_rate = db.Column(db.Float)
    unemployment_rate = db.Column(db.Float)
    contribution_men = db.Column(db.Float)
    contribution_women = db.Column(db.Float)
    gdp_2019 = db.Column(db.Float(53))
    gdp_per_capita = db.Column(db.Float)
    growth_of_gdp = db.Column(db.Float)
    inflation = db.Column(db.Float)
    investment = db.Column(db.Float)
    total_debt = db.Column(db.Float)
    gnp_per_capita = db.Column(db.Float)
    corruption_rank = db.Column(db.Float)
    credit_rank = db.Column(db.Float)
    business_score = db.Column(db.Float)
    key_sectors_growth = db.Column(db.Text)
    key_issues = db.Column(db.Text)

    contacts = db.relationship("CountryContact")
    documents = db.relationship("CountryDocument")
    sectors = db.relationship("CountrySector")

    sub_region = db.relationship("SubRegion", back_populates="countries")


class CountryContact(db.Model, SerializerMixin):
    __bind_key__ = 'information'
    __tablename__ = "country_contact"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_id = db.Column(db.
        ForeignKey("country.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    updated_at = db.Column(db.DateTime)
    govt_contact = db.Column(db.Text)
    economic_contact = db.Column(db.Text)
    parliament_contact = db.Column(db.Text)
    judiciary_contact = db.Column(db.Text)


class CountryDocument(db.Model, SerializerMixin):
    __bind_key__ = 'information'
    __tablename__ = "country_document"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    country_id = db.Column(db.
        ForeignKey("country.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    document_type = db.Column(db.Text)
    name = db.Column(db.Text)
    filesize = db.Column(db.Integer)
    filetype = db.Column(db.Text)


class CountrySector(db.Model, SerializerMixin):
    __bind_key__ = 'information'
    __tablename__ = "country_sector"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_id = db.Column(db.
        ForeignKey("country.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    sector_id = db.Column(db.ForeignKey("sector.id", ondelete="CASCADE", onupdate="CASCADE"))
    contribution_to_gdp = db.Column(db.Float)
    growth_rate = db.Column(db.Float)

    sector = db.relationship("Sector")


class SectorIndustry(db.Model, SerializerMixin):
    __bind_key__ = 'information'
    __tablename__ = "sector_industry"

    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)

    divisions = db.relationship("SectorDivision")


class SectorDivision(db.Model, SerializerMixin):
    __bind_key__ = 'information'
    __tablename__ = "sector_division"

    id = db.Column(db.Text, primary_key=True)
    sector_industry_id = db.Column(db.
        ForeignKey("sector_industry.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    name = db.Column(db.Text)

    groups = db.relationship("SectorGroup")
    sector_industry = db.relationship("SectorIndustry", back_populates="divisions")


class SectorGroup(db.Model, SerializerMixin):
    __bind_key__ = 'information'
    __tablename__ = "sector_group"

    id = db.Column(db.Text, primary_key=True)
    sector_division_id = db.Column(db.
        ForeignKey("sector_division.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    name = db.Column(db.Text)

    sectors = db.relationship("Sector")
    sector_division = db.relationship("SectorDivision", back_populates="groups")


class Sector(db.Model, SerializerMixin):
    __bind_key__ = 'information'
    __tablename__ = "sector"

    id = db.Column(db.Text, primary_key=True)
    sector_group_id = db.Column(db.
        ForeignKey("sector_group.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    name = db.Column(db.Text)

    sector_group = db.relationship("SectorGroup", back_populates="sectors")
