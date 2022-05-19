from datetime import date, datetime
from typing import Any  # noqa
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Country(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    subregion_id: "Optional[str]" = Field(None, alias="subregion_id")
    calling_code: "Optional[int]" = Field(None, alias="calling_code")
    name: "Optional[str]" = Field(None, alias="name")
    other_names: "Optional[str]" = Field(None, alias="other_names")
    motto: "Optional[str]" = Field(None, alias="motto")
    date_of_independence: "Optional[date]" = Field(None, alias="date_of_independence")
    introduction: "Optional[str]" = Field(None, alias="introduction")
    location: "Optional[str]" = Field(None, alias="location")
    neighbours: "Optional[str]" = Field(None, alias="neighbours")
    capital_city: "Optional[str]" = Field(None, alias="capital_city")
    population: "Optional[float]" = Field(None, alias="population")
    languages: "Optional[str]" = Field(None, alias="languages")
    facts_and_figures: "Optional[str]" = Field(None, alias="facts_and_figures")
    classification: "Optional[str]" = Field(None, alias="classification")
    life_expectancy: "Optional[float]" = Field(None, alias="life_expectancy")
    median_age: "Optional[float]" = Field(None, alias="median_age")
    average_children: "Optional[float]" = Field(None, alias="average_children")
    income_group: "Optional[str]" = Field(None, alias="income_group")
    employment_rate: "Optional[float]" = Field(None, alias="employment_rate")
    unemployment_rate: "Optional[float]" = Field(None, alias="unemployment_rate")
    contribution_men: "Optional[float]" = Field(None, alias="contribution_men")
    contribution_women: "Optional[float]" = Field(None, alias="contribution_women")
    gdp_2019: "Optional[float]" = Field(None, alias="gdp_2019")
    gdp_per_capita: "Optional[float]" = Field(None, alias="gdp_per_capita")
    growth_of_gdp: "Optional[float]" = Field(None, alias="growth_of_gdp")
    inflation: "Optional[float]" = Field(None, alias="inflation")
    investment: "Optional[float]" = Field(None, alias="investment")
    total_debt: "Optional[float]" = Field(None, alias="total_debt")
    gnp_per_capita: "Optional[float]" = Field(None, alias="gnp_per_capita")
    corruption_rank: "Optional[float]" = Field(None, alias="corruption_rank")
    credit_rank: "Optional[float]" = Field(None, alias="credit_rank")
    business_score: "Optional[float]" = Field(None, alias="business_score")
    key_sectors_growth: "Optional[str]" = Field(None, alias="key_sectors_growth")
    key_issues: "Optional[str]" = Field(None, alias="key_issues")


class CountryContact(BaseModel):
    country_id: "Optional[str]" = Field(None, alias="country_id")
    govt_contact: "Optional[str]" = Field(None, alias="govt_contact")
    economic_contact: "Optional[str]" = Field(None, alias="economic_contact")
    parliament_contact: "Optional[str]" = Field(None, alias="parliament_contact")
    judiciary_contact: "Optional[str]" = Field(None, alias="judiciary_contact")
    id: "int" = Field(..., alias="id")
    updated_at: "datetime" = Field(..., alias="updated_at")


class CountryContactCreate(BaseModel):
    country_id: "Optional[str]" = Field(None, alias="country_id")
    govt_contact: "Optional[str]" = Field(None, alias="govt_contact")
    economic_contact: "Optional[str]" = Field(None, alias="economic_contact")
    parliament_contact: "Optional[str]" = Field(None, alias="parliament_contact")
    judiciary_contact: "Optional[str]" = Field(None, alias="judiciary_contact")


class CountryContactUpdate(BaseModel):
    country_id: "Optional[str]" = Field(None, alias="country_id")
    govt_contact: "Optional[str]" = Field(None, alias="govt_contact")
    economic_contact: "Optional[str]" = Field(None, alias="economic_contact")
    parliament_contact: "Optional[str]" = Field(None, alias="parliament_contact")
    judiciary_contact: "Optional[str]" = Field(None, alias="judiciary_contact")


class CountryCreate(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    subregion_id: "Optional[str]" = Field(None, alias="subregion_id")
    calling_code: "Optional[int]" = Field(None, alias="calling_code")
    name: "Optional[str]" = Field(None, alias="name")
    other_names: "Optional[str]" = Field(None, alias="other_names")
    motto: "Optional[str]" = Field(None, alias="motto")
    date_of_independence: "Optional[date]" = Field(None, alias="date_of_independence")
    introduction: "Optional[str]" = Field(None, alias="introduction")
    location: "Optional[str]" = Field(None, alias="location")
    neighbours: "Optional[str]" = Field(None, alias="neighbours")
    capital_city: "Optional[str]" = Field(None, alias="capital_city")
    population: "Optional[float]" = Field(None, alias="population")
    languages: "Optional[str]" = Field(None, alias="languages")
    facts_and_figures: "Optional[str]" = Field(None, alias="facts_and_figures")
    classification: "Optional[str]" = Field(None, alias="classification")
    life_expectancy: "Optional[float]" = Field(None, alias="life_expectancy")
    median_age: "Optional[float]" = Field(None, alias="median_age")
    average_children: "Optional[float]" = Field(None, alias="average_children")
    income_group: "Optional[str]" = Field(None, alias="income_group")
    employment_rate: "Optional[float]" = Field(None, alias="employment_rate")
    unemployment_rate: "Optional[float]" = Field(None, alias="unemployment_rate")
    contribution_men: "Optional[float]" = Field(None, alias="contribution_men")
    contribution_women: "Optional[float]" = Field(None, alias="contribution_women")
    gdp_2019: "Optional[float]" = Field(None, alias="gdp_2019")
    gdp_per_capita: "Optional[float]" = Field(None, alias="gdp_per_capita")
    growth_of_gdp: "Optional[float]" = Field(None, alias="growth_of_gdp")
    inflation: "Optional[float]" = Field(None, alias="inflation")
    investment: "Optional[float]" = Field(None, alias="investment")
    total_debt: "Optional[float]" = Field(None, alias="total_debt")
    gnp_per_capita: "Optional[float]" = Field(None, alias="gnp_per_capita")
    corruption_rank: "Optional[float]" = Field(None, alias="corruption_rank")
    credit_rank: "Optional[float]" = Field(None, alias="credit_rank")
    business_score: "Optional[float]" = Field(None, alias="business_score")
    key_sectors_growth: "Optional[str]" = Field(None, alias="key_sectors_growth")
    key_issues: "Optional[str]" = Field(None, alias="key_issues")


class CountryDocument(BaseModel):
    id: "UUID" = Field(..., alias="id")
    country_id: "Optional[str]" = Field(None, alias="country_id")
    document_type: "Optional[str]" = Field(None, alias="document_type")
    name: "Optional[str]" = Field(None, alias="name")
    filetype: "Optional[str]" = Field(None, alias="filetype")
    filesize: "Optional[int]" = Field(None, alias="filesize")


class CountryDocumentCreate(BaseModel):
    id: "Optional[UUID]" = Field(None, alias="id")
    country_id: "Optional[str]" = Field(None, alias="country_id")
    document_type: "Optional[str]" = Field(None, alias="document_type")
    name: "Optional[str]" = Field(None, alias="name")
    filetype: "Optional[str]" = Field(None, alias="filetype")
    filesize: "Optional[int]" = Field(None, alias="filesize")


class CountryDocumentUpdate(BaseModel):
    id: "Optional[UUID]" = Field(None, alias="id")
    country_id: "Optional[str]" = Field(None, alias="country_id")
    document_type: "Optional[str]" = Field(None, alias="document_type")
    name: "Optional[str]" = Field(None, alias="name")
    filetype: "Optional[str]" = Field(None, alias="filetype")
    filesize: "Optional[int]" = Field(None, alias="filesize")


class CountryListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[Country]]" = Field(None, alias="data")


class CountryResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[Country]" = Field(None, alias="data")


class CountrySector(BaseModel):
    country_id: "Optional[str]" = Field(None, alias="country_id")
    sector_id: "Optional[str]" = Field(None, alias="sector_id")
    contribution_to_gdp: "Optional[float]" = Field(None, alias="contribution_to_gdp")
    growth_rate: "Optional[float]" = Field(None, alias="growth_rate")
    id: "int" = Field(..., alias="id")


class CountrySectorCreate(BaseModel):
    country_id: "Optional[str]" = Field(None, alias="country_id")
    sector_id: "Optional[str]" = Field(None, alias="sector_id")
    contribution_to_gdp: "Optional[float]" = Field(None, alias="contribution_to_gdp")
    growth_rate: "Optional[float]" = Field(None, alias="growth_rate")


class CountrySectorUpdate(BaseModel):
    country_id: "Optional[str]" = Field(None, alias="country_id")
    sector_id: "Optional[str]" = Field(None, alias="sector_id")
    contribution_to_gdp: "Optional[float]" = Field(None, alias="contribution_to_gdp")
    growth_rate: "Optional[float]" = Field(None, alias="growth_rate")


class CountryUpdate(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    subregion_id: "Optional[str]" = Field(None, alias="subregion_id")
    calling_code: "Optional[int]" = Field(None, alias="calling_code")
    name: "Optional[str]" = Field(None, alias="name")
    other_names: "Optional[str]" = Field(None, alias="other_names")
    motto: "Optional[str]" = Field(None, alias="motto")
    date_of_independence: "Optional[date]" = Field(None, alias="date_of_independence")
    introduction: "Optional[str]" = Field(None, alias="introduction")
    location: "Optional[str]" = Field(None, alias="location")
    neighbours: "Optional[str]" = Field(None, alias="neighbours")
    capital_city: "Optional[str]" = Field(None, alias="capital_city")
    population: "Optional[float]" = Field(None, alias="population")
    languages: "Optional[str]" = Field(None, alias="languages")
    facts_and_figures: "Optional[str]" = Field(None, alias="facts_and_figures")
    classification: "Optional[str]" = Field(None, alias="classification")
    life_expectancy: "Optional[float]" = Field(None, alias="life_expectancy")
    median_age: "Optional[float]" = Field(None, alias="median_age")
    average_children: "Optional[float]" = Field(None, alias="average_children")
    income_group: "Optional[str]" = Field(None, alias="income_group")
    employment_rate: "Optional[float]" = Field(None, alias="employment_rate")
    unemployment_rate: "Optional[float]" = Field(None, alias="unemployment_rate")
    contribution_men: "Optional[float]" = Field(None, alias="contribution_men")
    contribution_women: "Optional[float]" = Field(None, alias="contribution_women")
    gdp_2019: "Optional[float]" = Field(None, alias="gdp_2019")
    gdp_per_capita: "Optional[float]" = Field(None, alias="gdp_per_capita")
    growth_of_gdp: "Optional[float]" = Field(None, alias="growth_of_gdp")
    inflation: "Optional[float]" = Field(None, alias="inflation")
    investment: "Optional[float]" = Field(None, alias="investment")
    total_debt: "Optional[float]" = Field(None, alias="total_debt")
    gnp_per_capita: "Optional[float]" = Field(None, alias="gnp_per_capita")
    corruption_rank: "Optional[float]" = Field(None, alias="corruption_rank")
    credit_rank: "Optional[float]" = Field(None, alias="credit_rank")
    business_score: "Optional[float]" = Field(None, alias="business_score")
    key_sectors_growth: "Optional[str]" = Field(None, alias="key_sectors_growth")
    key_issues: "Optional[str]" = Field(None, alias="key_issues")


class Region(BaseModel):
    id: "str" = Field(..., alias="id")
    subregions: "List[SubRegion]" = Field(..., alias="subregions")


class RegionCreate(BaseModel):
    id: "str" = Field(..., alias="id")


class RegionUpdate(BaseModel):
    id: "str" = Field(..., alias="id")


class Sector(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    sector_group_id: "Optional[str]" = Field(None, alias="sector_group_id")
    name: "Optional[str]" = Field(None, alias="name")


class SectorCreate(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    sector_group_id: "Optional[str]" = Field(None, alias="sector_group_id")
    name: "Optional[str]" = Field(None, alias="name")


class SectorDivision(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    name: "str" = Field(..., alias="name")
    groups: "Optional[List[SectorGroup]]" = Field(None, alias="groups")


class SectorDivisionCreate(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    name: "str" = Field(..., alias="name")


class SectorDivisionListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[SectorDivision]]" = Field(None, alias="data")


class SectorDivisionResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[SectorDivision]" = Field(None, alias="data")


class SectorDivisionUpdate(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    name: "str" = Field(..., alias="name")


class SectorGroup(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    name: "str" = Field(..., alias="name")
    sectors: "Optional[List[Sector]]" = Field(None, alias="sectors")


class SectorGroupCreate(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    name: "str" = Field(..., alias="name")


class SectorGroupListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[SectorGroup]]" = Field(None, alias="data")


class SectorGroupResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[SectorGroup]" = Field(None, alias="data")


class SectorGroupUpdate(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    name: "str" = Field(..., alias="name")


class SectorIndustry(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    name: "str" = Field(..., alias="name")
    divisions: "Optional[List[SectorDivision]]" = Field(None, alias="divisions")


class SectorIndustryCreate(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    name: "str" = Field(..., alias="name")


class SectorIndustryListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[SectorIndustry]]" = Field(None, alias="data")


class SectorIndustryResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "SectorIndustry" = Field(..., alias="data")


class SectorIndustryUpdate(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    name: "str" = Field(..., alias="name")


class SectorListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[Sector]]" = Field(None, alias="data")


class SectorResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[Sector]" = Field(None, alias="data")


class SectorUpdate(BaseModel):
    id: "Optional[str]" = Field(None, alias="id")
    sector_group_id: "Optional[str]" = Field(None, alias="sector_group_id")
    name: "Optional[str]" = Field(None, alias="name")


class SubRegion(BaseModel):
    id: "str" = Field(..., alias="id")
    subregion_id: "str" = Field(..., alias="subregion_id")
    subregions: "List[Country]" = Field(..., alias="subregions")


class SubRegionCreate(BaseModel):
    id: "str" = Field(..., alias="id")
    subregion_id: "str" = Field(..., alias="subregion_id")


class SubRegionUpdate(BaseModel):
    id: "str" = Field(..., alias="id")
    subregion_id: "str" = Field(..., alias="subregion_id")
