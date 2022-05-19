from datetime import date, datetime
from typing import Any  # noqa
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Account(BaseModel):
    kyc_id: "Optional[UUID]" = Field(None, alias="kyc_id")
    active: "Optional[bool]" = Field(None, alias="active")
    id: "UUID" = Field(..., alias="id")
    createdate: "datetime" = Field(..., alias="createdate")
    kyc: "KYC" = Field(..., alias="kyc")
    countries: "List[AccountCountry]" = Field(..., alias="countries")
    industries: "List[AccountIndustry]" = Field(..., alias="industries")


class AccountCountry(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    country_id: "str" = Field(..., alias="country_id")
    is_primary: "bool" = Field(..., alias="is_primary")
    id: "int" = Field(..., alias="id")


class AccountCountryCreate(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    country_id: "str" = Field(..., alias="country_id")
    is_primary: "bool" = Field(..., alias="is_primary")


class AccountCountryListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[AccountCountry]]" = Field(None, alias="data")


class AccountCountryResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[AccountCountry]" = Field(None, alias="data")


class AccountCountryUpdate(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    country_id: "str" = Field(..., alias="country_id")
    is_primary: "bool" = Field(..., alias="is_primary")


class AccountGroup(BaseModel):
    name: "str" = Field(..., alias="name")
    roles: "Optional[List[str]]" = Field(None, alias="roles")
    id: "Optional[int]" = Field(None, alias="id")
    account_id: "UUID" = Field(..., alias="account_id")
    account: "Optional[Account]" = Field(None, alias="account")


class AccountGroupCreate(BaseModel):
    name: "str" = Field(..., alias="name")
    roles: "Optional[List[str]]" = Field(None, alias="roles")
    account_id: "UUID" = Field(..., alias="account_id")


class AccountGroupListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "List[AccountGroup]" = Field(..., alias="data")


class AccountGroupResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "AccountGroup" = Field(..., alias="data")


class AccountGroupUpdate(BaseModel):
    name: "str" = Field(..., alias="name")
    roles: "Optional[List[str]]" = Field(None, alias="roles")


class AccountIndustry(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    industry_id: "str" = Field(..., alias="industry_id")
    is_primary: "bool" = Field(..., alias="is_primary")
    id: "int" = Field(..., alias="id")


class AccountIndustryCreate(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    industry_id: "str" = Field(..., alias="industry_id")
    is_primary: "bool" = Field(..., alias="is_primary")


class AccountIndustryListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[AccountIndustry]]" = Field(None, alias="data")


class AccountIndustryResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[AccountIndustry]" = Field(None, alias="data")


class AccountIndustryUpdate(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    industry_id: "str" = Field(..., alias="industry_id")
    is_primary: "bool" = Field(..., alias="is_primary")


class AccountListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[Account]]" = Field(None, alias="data")


class AccountResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[Account]" = Field(None, alias="data")


class AccountViewCreate(BaseModel):
    active: "Optional[bool]" = Field(None, alias="active")
    kyc_id: "Optional[UUID]" = Field(None, alias="kyc_id")
    is_company: "Optional[bool]" = Field(None, alias="is_company")
    business_name: "Optional[str]" = Field(None, alias="business_name")
    country_id: "str" = Field(..., alias="country_id")
    tin: "Optional[str]" = Field(None, alias="tin")
    document_type_id: "Optional[int]" = Field(None, alias="document_type_id")
    document_id: "Optional[str]" = Field(None, alias="document_id")
    document_file: "Optional[str]" = Field(None, alias="document_file")
    upline_id: "Optional[str]" = Field(None, alias="upline_id")
    address: "Optional[str]" = Field(None, alias="address")
    email_1: "Optional[str]" = Field(None, alias="email_1")
    email_2: "Optional[str]" = Field(None, alias="email_2")
    email_3: "Optional[str]" = Field(None, alias="email_3")
    msisdn_1: "Optional[str]" = Field(None, alias="msisdn_1")
    msisdn_2: "Optional[str]" = Field(None, alias="msisdn_2")
    msisdn_3: "Optional[str]" = Field(None, alias="msisdn_3")
    first_name: "Optional[str]" = Field(None, alias="first_name")
    last_name: "Optional[str]" = Field(None, alias="last_name")
    short_name: "Optional[str]" = Field(None, alias="short_name")
    website: "Optional[str]" = Field(None, alias="website")
    gender: "Optional[str]" = Field(None, alias="gender")
    dob: "Optional[date]" = Field(None, alias="dob")
    status: "Optional[int]" = Field(None, alias="status")
    statusdate: "Optional[datetime]" = Field(None, alias="statusdate")
    createdate: "Optional[datetime]" = Field(None, alias="createdate")
    reason: "Optional[str]" = Field(None, alias="reason")


class AccountViewUpdate(BaseModel):
    active: "Optional[bool]" = Field(None, alias="active")
    kyc_id: "Optional[UUID]" = Field(None, alias="kyc_id")
    is_company: "Optional[bool]" = Field(None, alias="is_company")
    business_name: "Optional[str]" = Field(None, alias="business_name")
    country_id: "Optional[str]" = Field(None, alias="country_id")
    tin: "Optional[str]" = Field(None, alias="tin")
    document_type_id: "Optional[int]" = Field(None, alias="document_type_id")
    document_id: "Optional[str]" = Field(None, alias="document_id")
    document_file: "Optional[str]" = Field(None, alias="document_file")
    upline_id: "Optional[str]" = Field(None, alias="upline_id")
    address: "Optional[str]" = Field(None, alias="address")
    email_1: "Optional[str]" = Field(None, alias="email_1")
    email_2: "Optional[str]" = Field(None, alias="email_2")
    email_3: "Optional[str]" = Field(None, alias="email_3")
    msisdn_1: "Optional[str]" = Field(None, alias="msisdn_1")
    msisdn_2: "Optional[str]" = Field(None, alias="msisdn_2")
    msisdn_3: "Optional[str]" = Field(None, alias="msisdn_3")
    first_name: "Optional[str]" = Field(None, alias="first_name")
    last_name: "Optional[str]" = Field(None, alias="last_name")
    short_name: "Optional[str]" = Field(None, alias="short_name")
    website: "Optional[str]" = Field(None, alias="website")
    gender: "Optional[str]" = Field(None, alias="gender")
    dob: "Optional[date]" = Field(None, alias="dob")
    status: "Optional[int]" = Field(None, alias="status")
    statusdate: "Optional[datetime]" = Field(None, alias="statusdate")
    createdate: "Optional[datetime]" = Field(None, alias="createdate")
    reason: "Optional[str]" = Field(None, alias="reason")


class Admin(BaseModel):
    first_name: "Optional[str]" = Field(None, alias="first_name")
    last_name: "Optional[str]" = Field(None, alias="last_name")
    gender: "Optional[str]" = Field(None, alias="gender")
    dob: "Optional[date]" = Field(None, alias="dob")
    msisdn: "Optional[str]" = Field(None, alias="msisdn")
    email: "Optional[str]" = Field(None, alias="email")
    document_type_id: "Optional[str]" = Field(None, alias="document_type_id")
    document_id_no: "Optional[str]" = Field(None, alias="document_id_no")
    status: "Optional[str]" = Field(None, alias="status")
    active: "Optional[bool]" = Field(None, alias="active")
    admin_group_id: "Optional[int]" = Field(None, alias="admin_group_id")
    id: "UUID" = Field(..., alias="id")
    createdate: "datetime" = Field(..., alias="createdate")
    failed_logins: "int" = Field(..., alias="failed_logins")
    group: "Optional[AdminGroup]" = Field(None, alias="group")
    prefs: "Optional[List[AdminPreference]]" = Field(None, alias="prefs")


class AdminCreate(BaseModel):
    first_name: "str" = Field(..., alias="first_name")
    last_name: "str" = Field(..., alias="last_name")
    gender: "str" = Field(..., alias="gender")
    dob: "date" = Field(..., alias="dob")
    msisdn: "str" = Field(..., alias="msisdn")
    email: "str" = Field(..., alias="email")
    document_type_id: "str" = Field(..., alias="document_type_id")
    document_id_no: "str" = Field(..., alias="document_id_no")
    status: "Optional[str]" = Field(None, alias="status")
    active: "Optional[bool]" = Field(None, alias="active")
    admin_group_id: "int" = Field(..., alias="admin_group_id")
    id: "Optional[UUID]" = Field(None, alias="id")
    password: "str" = Field(..., alias="password")


class AdminGroup(BaseModel):
    name: "str" = Field(..., alias="name")
    roles: "Optional[List[str]]" = Field(None, alias="roles")
    id: "int" = Field(..., alias="id")


class AdminGroupCreate(BaseModel):
    name: "str" = Field(..., alias="name")
    roles: "Optional[List[str]]" = Field(None, alias="roles")


class AdminGroupListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[AdminGroup]]" = Field(None, alias="data")


class AdminGroupResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[AdminGroup]" = Field(None, alias="data")


class AdminGroupUpdate(BaseModel):
    name: "str" = Field(..., alias="name")
    roles: "Optional[List[str]]" = Field(None, alias="roles")


class AdminListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[Admin]]" = Field(None, alias="data")


class AdminLogin(BaseModel):
    method: "str" = Field(..., alias="method")
    value: "str" = Field(..., alias="value")
    password: "str" = Field(..., alias="password")


class AdminPreference(BaseModel):
    admin_id: "UUID" = Field(..., alias="admin_id")
    name: "str" = Field(..., alias="name")
    value: "str" = Field(..., alias="value")
    id: "int" = Field(..., alias="id")


class AdminResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[Admin]" = Field(None, alias="data")


class AdminUpdate(BaseModel):
    first_name: "Optional[str]" = Field(None, alias="first_name")
    last_name: "Optional[str]" = Field(None, alias="last_name")
    gender: "Optional[str]" = Field(None, alias="gender")
    dob: "Optional[date]" = Field(None, alias="dob")
    msisdn: "Optional[str]" = Field(None, alias="msisdn")
    email: "Optional[str]" = Field(None, alias="email")
    document_type_id: "Optional[str]" = Field(None, alias="document_type_id")
    document_id_no: "Optional[str]" = Field(None, alias="document_id_no")
    status: "Optional[str]" = Field(None, alias="status")
    active: "Optional[bool]" = Field(None, alias="active")
    admin_group_id: "Optional[int]" = Field(None, alias="admin_group_id")
    password: "Optional[str]" = Field(None, alias="password")


class API(BaseModel):
    id: "Optional[UUID]" = Field(None, alias="id")
    secret: "Optional[UUID]" = Field(None, alias="secret")
    name: "Optional[str]" = Field(None, alias="name")
    account_id: "Optional[UUID]" = Field(None, alias="account_id")
    active: "Optional[bool]" = Field(None, alias="active")
    created_at: "datetime" = Field(..., alias="created_at")


class APIAuth(BaseModel):
    api: "API" = Field(..., alias="api")
    account: "Account" = Field(..., alias="account")


class APIAuthResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "APIAuth" = Field(..., alias="data")


class APICount(BaseModel):
    count: "int" = Field(..., alias="count")


class APICountResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "APICount" = Field(..., alias="data")


class APIListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "List[API]" = Field(..., alias="data")


class APILogin(BaseModel):
    id: "UUID" = Field(..., alias="id")
    secret: "UUID" = Field(..., alias="secret")


class APINew(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    name: "str" = Field(..., alias="name")
    active: "Optional[bool]" = Field(None, alias="active")


class APIResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "API" = Field(..., alias="data")


class BodyAddKycDocumentV1KycKycIdDocumentPost(BaseModel):
    name: "str" = Field(..., alias="name")
    document_type_id: "str" = Field(..., alias="document_type_id")
    uploaded_file: "IO[Any]" = Field(..., alias="uploaded_file")


class BodyUpdateKycDocumentV1KycIdDocumentPut(BaseModel):
    uploaded_file: "IO[Any]" = Field(..., alias="uploaded_file")


class ContactPerson(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    kyc_id: "UUID" = Field(..., alias="kyc_id")
    position: "str" = Field(..., alias="position")
    id: "UUID" = Field(..., alias="id")


class ContactPersonCreate(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    kyc_id: "UUID" = Field(..., alias="kyc_id")
    position: "str" = Field(..., alias="position")


class ContactPersonListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[ContactPerson]]" = Field(None, alias="data")


class ContactPersonResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[ContactPerson]" = Field(None, alias="data")


class ContactPersonUpdate(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    kyc_id: "UUID" = Field(..., alias="kyc_id")
    position: "str" = Field(..., alias="position")


class Country(BaseModel):
    name: "str" = Field(..., alias="name")
    calling_code: "int" = Field(..., alias="calling_code")
    id: "str" = Field(..., alias="id")


class CountryCreate(BaseModel):
    name: "str" = Field(..., alias="name")
    calling_code: "int" = Field(..., alias="calling_code")
    id: "str" = Field(..., alias="id")


class CountryListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "List[Country]" = Field(..., alias="data")


class CountryResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Country" = Field(..., alias="data")


class CountryUpdate(BaseModel):
    name: "str" = Field(..., alias="name")
    calling_code: "int" = Field(..., alias="calling_code")


class DocumentType(BaseModel):
    name: "str" = Field(..., alias="name")
    is_company: "bool" = Field(..., alias="is_company")
    kyc_level: "int" = Field(..., alias="kyc_level")
    id: "str" = Field(..., alias="id")


class DocumentTypeCreate(BaseModel):
    name: "str" = Field(..., alias="name")
    is_company: "bool" = Field(..., alias="is_company")
    kyc_level: "int" = Field(..., alias="kyc_level")
    id: "str" = Field(..., alias="id")


class DocumentTypeListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "List[DocumentType]" = Field(..., alias="data")


class DocumentTypeResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "DocumentType" = Field(..., alias="data")


class DocumentTypeUpdate(BaseModel):
    name: "str" = Field(..., alias="name")
    is_company: "bool" = Field(..., alias="is_company")
    kyc_level: "int" = Field(..., alias="kyc_level")


class EmailModel(BaseModel):
    email: "str" = Field(..., alias="email")


class FailureResponseModel(BaseModel):
    success: "bool" = Field(..., alias="success")
    message: "str" = Field(..., alias="message")


class KYC(BaseModel):
    is_company: "Optional[bool]" = Field(None, alias="is_company")
    business_name: "Optional[str]" = Field(None, alias="business_name")
    country_id: "Optional[str]" = Field(None, alias="country_id")
    tin: "Optional[str]" = Field(None, alias="tin")
    address: "Optional[str]" = Field(None, alias="address")
    first_name: "Optional[str]" = Field(None, alias="first_name")
    last_name: "Optional[str]" = Field(None, alias="last_name")
    gender: "Optional[str]" = Field(None, alias="gender")
    dob: "Optional[date]" = Field(None, alias="dob")
    short_name: "Optional[str]" = Field(None, alias="short_name")
    website: "Optional[str]" = Field(None, alias="website")
    status: "Optional[int]" = Field(None, alias="status")
    statusdate: "Optional[datetime]" = Field(None, alias="statusdate")
    createdate: "Optional[datetime]" = Field(None, alias="createdate")
    reason: "Optional[str]" = Field(None, alias="reason")
    id: "UUID" = Field(..., alias="id")
    emails: "List[KYCEmail]" = Field(..., alias="emails")
    msisdns: "List[KYCMSISDN]" = Field(..., alias="msisdns")
    documents: "Optional[List[KYCDocument]]" = Field(None, alias="documents")


class KYCCreate(BaseModel):
    is_company: "Optional[bool]" = Field(None, alias="is_company")
    business_name: "Optional[str]" = Field(None, alias="business_name")
    country_id: "Optional[str]" = Field(None, alias="country_id")
    tin: "Optional[str]" = Field(None, alias="tin")
    address: "Optional[str]" = Field(None, alias="address")
    first_name: "Optional[str]" = Field(None, alias="first_name")
    last_name: "Optional[str]" = Field(None, alias="last_name")
    gender: "Optional[str]" = Field(None, alias="gender")
    dob: "Optional[date]" = Field(None, alias="dob")
    short_name: "Optional[str]" = Field(None, alias="short_name")
    website: "Optional[str]" = Field(None, alias="website")
    status: "Optional[int]" = Field(None, alias="status")
    statusdate: "Optional[datetime]" = Field(None, alias="statusdate")
    createdate: "Optional[datetime]" = Field(None, alias="createdate")
    reason: "Optional[str]" = Field(None, alias="reason")
    id: "Optional[UUID]" = Field(None, alias="id")


class KYCDocument(BaseModel):
    kyc_id: "UUID" = Field(..., alias="kyc_id")
    name: "str" = Field(..., alias="name")
    document_type_id: "str" = Field(..., alias="document_type_id")
    id: "UUID" = Field(..., alias="id")
    created_at: "datetime" = Field(..., alias="created_at")
    document_type: "DocumentType" = Field(..., alias="document_type")


class KYCDocumentResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "KYCDocument" = Field(..., alias="data")


class KYCEmail(BaseModel):
    id: "str" = Field(..., alias="id")
    is_primary: "bool" = Field(..., alias="is_primary")


class KYCResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[KYC]" = Field(None, alias="data")


class KYCUpdate(BaseModel):
    is_company: "Optional[bool]" = Field(None, alias="is_company")
    business_name: "Optional[str]" = Field(None, alias="business_name")
    country_id: "Optional[str]" = Field(None, alias="country_id")
    tin: "Optional[str]" = Field(None, alias="tin")
    address: "Optional[str]" = Field(None, alias="address")
    first_name: "Optional[str]" = Field(None, alias="first_name")
    last_name: "Optional[str]" = Field(None, alias="last_name")
    gender: "Optional[str]" = Field(None, alias="gender")
    dob: "Optional[date]" = Field(None, alias="dob")
    short_name: "Optional[str]" = Field(None, alias="short_name")
    website: "Optional[str]" = Field(None, alias="website")
    status: "Optional[int]" = Field(None, alias="status")
    statusdate: "Optional[datetime]" = Field(None, alias="statusdate")
    createdate: "Optional[datetime]" = Field(None, alias="createdate")
    reason: "Optional[str]" = Field(None, alias="reason")


class KYCMSISDN(BaseModel):
    id: "str" = Field(..., alias="id")
    is_primary: "bool" = Field(..., alias="is_primary")


class MSISDNModel(BaseModel):
    msisdn: "str" = Field(..., alias="msisdn")


class PasswordModel(BaseModel):
    password: "str" = Field(..., alias="password")


class Role(BaseModel):
    id: "str" = Field(..., alias="id")
    name: "str" = Field(..., alias="name")


class RoleCreate(BaseModel):
    id: "str" = Field(..., alias="id")
    name: "str" = Field(..., alias="name")


class RoleListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "List[Role]" = Field(..., alias="data")


class RoleResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Role" = Field(..., alias="data")


class RoleUpdate(BaseModel):
    name: "str" = Field(..., alias="name")


class User(BaseModel):
    kyc_id: "Optional[UUID]" = Field(None, alias="kyc_id")
    account_group_id: "Optional[int]" = Field(None, alias="account_group_id")
    active: "Optional[bool]" = Field(None, alias="active")
    hotp_secret: "Optional[str]" = Field(None, alias="hotp_secret")
    totp_secret: "Optional[str]" = Field(None, alias="totp_secret")
    id: "UUID" = Field(..., alias="id")
    createdate: "datetime" = Field(..., alias="createdate")
    failed_logins: "int" = Field(..., alias="failed_logins")
    password: "str" = Field(..., alias="password")
    kyc: "KYC" = Field(..., alias="kyc")
    account_group: "AccountGroup" = Field(..., alias="account_group")
    prefs: "Optional[List[UserPreference]]" = Field(None, alias="prefs")


class UserCreate(BaseModel):
    kyc_id: "Optional[UUID]" = Field(None, alias="kyc_id")
    account_group_id: "Optional[int]" = Field(None, alias="account_group_id")
    active: "Optional[bool]" = Field(None, alias="active")
    hotp_secret: "Optional[str]" = Field(None, alias="hotp_secret")
    totp_secret: "Optional[str]" = Field(None, alias="totp_secret")
    id: "Optional[UUID]" = Field(None, alias="id")
    password: "str" = Field(..., alias="password")


class UserLogin(BaseModel):
    method: "str" = Field(..., alias="method")
    value: "str" = Field(..., alias="value")
    password: "str" = Field(..., alias="password")


class UserPreference(BaseModel):
    user_id: "UUID" = Field(..., alias="user_id")
    name: "str" = Field(..., alias="name")
    value: "str" = Field(..., alias="value")
    id: "int" = Field(..., alias="id")


class UserPreferenceCreate(BaseModel):
    user_id: "UUID" = Field(..., alias="user_id")
    name: "str" = Field(..., alias="name")
    value: "str" = Field(..., alias="value")


class UserPreferenceListResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[List[UserPreference]]" = Field(None, alias="data")


class UserPreferenceResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[UserPreference]" = Field(None, alias="data")


class UserResponse(BaseModel):
    success: "bool" = Field(..., alias="success")
    data: "Optional[User]" = Field(None, alias="data")


class UserViewCreate(BaseModel):
    first_name: "Optional[str]" = Field(None, alias="first_name")
    last_name: "Optional[str]" = Field(None, alias="last_name")
    address: "Optional[str]" = Field(None, alias="address")
    website: "Optional[str]" = Field(None, alias="website")
    email_1: "str" = Field(..., alias="email_1")
    email_2: "Optional[str]" = Field(None, alias="email_2")
    email_3: "Optional[str]" = Field(None, alias="email_3")
    msisdn_1: "str" = Field(..., alias="msisdn_1")
    msisdn_2: "Optional[str]" = Field(None, alias="msisdn_2")
    msisdn_3: "Optional[str]" = Field(None, alias="msisdn_3")
    password: "Optional[str]" = Field(None, alias="password")
    dob: "Optional[date]" = Field(None, alias="dob")
    gender: "Optional[str]" = Field(None, alias="gender")
    kyc_id: "Optional[UUID]" = Field(None, alias="kyc_id")
    country_id: "Optional[str]" = Field(None, alias="country_id")
    status: "Optional[int]" = Field(None, alias="status")
    reason: "Optional[str]" = Field(None, alias="reason")
    active: "Optional[bool]" = Field(None, alias="active")
    is_company: "Optional[bool]" = Field(None, alias="is_company")
    account_group_id: "int" = Field(..., alias="account_group_id")
    hotp_secret: "Optional[str]" = Field(None, alias="hotp_secret")
    totp_secret: "Optional[str]" = Field(None, alias="totp_secret")


class UserViewUpdate(BaseModel):
    first_name: "Optional[str]" = Field(None, alias="first_name")
    last_name: "Optional[str]" = Field(None, alias="last_name")
    address: "Optional[str]" = Field(None, alias="address")
    website: "Optional[str]" = Field(None, alias="website")
    email_1: "Optional[str]" = Field(None, alias="email_1")
    email_2: "Optional[str]" = Field(None, alias="email_2")
    email_3: "Optional[str]" = Field(None, alias="email_3")
    msisdn_1: "Optional[str]" = Field(None, alias="msisdn_1")
    msisdn_2: "Optional[str]" = Field(None, alias="msisdn_2")
    msisdn_3: "Optional[str]" = Field(None, alias="msisdn_3")
    password: "Optional[str]" = Field(None, alias="password")
    dob: "Optional[date]" = Field(None, alias="dob")
    gender: "Optional[str]" = Field(None, alias="gender")
    kyc_id: "Optional[UUID]" = Field(None, alias="kyc_id")
    country_id: "Optional[str]" = Field(None, alias="country_id")
    status: "Optional[int]" = Field(None, alias="status")
    reason: "Optional[str]" = Field(None, alias="reason")
    active: "Optional[bool]" = Field(None, alias="active")
    is_company: "Optional[bool]" = Field(None, alias="is_company")
    account_group_id: "Optional[int]" = Field(None, alias="account_group_id")
    hotp_secret: "Optional[str]" = Field(None, alias="hotp_secret")
    totp_secret: "Optional[str]" = Field(None, alias="totp_secret")
