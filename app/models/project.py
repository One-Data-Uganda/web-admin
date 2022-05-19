# coding: utf-8
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_serializer import SerializerMixin

from app import db


class Capacity(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "capacity"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)

    def __str__(self):
        return id


class SponsorType(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "sponsor_type"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class DevelopmentType(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "development_type"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class DevelopmentModel(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "development_model"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class Project(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "project"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    type = db.Column(db.Text)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    size = db.Column(db.Float)
    investment = db.Column(db.Float)
    country_id = db.Column(db.Text)
    sector_industry_id = db.Column(db.Text)
    sector_group_id = db.Column(db.Text)
    sector_division_id = db.Column(db.Text)
    sector_id = db.Column(db.Text)
    technology = db.Column(db.Text)
    status = db.Column(db.Text)
    commencement_date = db.Column(db.Date)
    proposed_completion_date = db.Column(db.Date)
    current_stage = db.Column(db.Text)
    next_stages = db.Column(db.Text)
    estimated_cost = db.Column(db.Float)
    contact_information = db.Column(db.Text)
    contact_address = db.Column(db.Text)
    postal_address = db.Column(db.Text)
    telephone = db.Column(db.Text)
    email = db.Column(db.Text)
    website = db.Column(db.Text)
    completed_activities = db.Column(db.Text)
    current_activities = db.Column(db.Text)
    next_activities = db.Column(db.Text)
    outstanding_activities = db.Column(db.Text)
    status_id = db.Column(
        db.ForeignKey("status.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    sponsor_type_id = db.Column(
        db.ForeignKey("sponsor_type.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    reference_code = db.Column(db.Text)
    manager = db.Column(db.Text)
    development_type_id = db.Column(
        db.ForeignKey("development_type.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    development_model = db.Column(db.Text)
    percentage_public = db.Column(db.Float)
    percentage_private = db.Column(db.Float)
    location = db.Column(db.Text)
    nearest_town = db.Column(db.Text)
    distance = db.Column(db.Float)
    nearest_capital_country_id = db.Column(db.Text)
    nearest_capital = db.Column(db.Text)
    distance_capital = db.Column(db.Float)
    environmental_impact = db.Column(db.Text)
    social_impact = db.Column(db.Text)
    total_investment = db.Column(db.Float)
    equity_investment = db.Column(db.Float)
    debt_amount = db.Column(db.Float)
    grant_amount = db.Column(db.Float)
    outstanding_investment = db.Column(db.Float)
    related_projects = db.Column(db.Text)
    strategy = db.Column(db.Text)
    alliances = db.Column(db.Text)


class ProjectRegion(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "project_region"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(
        db.ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    region_id = db.Column(db.Text)


class ProjectCountry(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "project_country"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(
        db.ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    country_id = db.Column(db.Text)


class Status(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "status"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class Type(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "ptype"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class ProjectType(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "project_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(
        db.ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    type_id = db.Column(
        db.ForeignKey("ptype.id", ondelete="CASCADE", onupdate="CASCADE")
    )


class EnergyResource(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "energy_resource"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class TechnologyType(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "technology_type"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)
    technology_id = db.Column(
        db.ForeignKey("technology.id", ondelete="CASCADE", onupdate="CASCADE")
    )


class Technology(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "technology"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class OffTaker(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "off_taker"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class WaterService(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "water_service"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class PowerWaterService(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "power_water_service"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    power_id = db.Column(
        db.ForeignKey("power.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    water_service_id = db.Column(
        db.ForeignKey("water_service.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    is_primary = db.Column(db.Boolean, server_default=db.text("false"))


class PowerCustomer(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "power_customer"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class PowerPowerCustomer(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "power_power_customer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    power_id = db.Column(
        db.ForeignKey("power.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    power_customer_id = db.Column(
        db.ForeignKey("power_customer.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    is_primary = db.Column(db.Boolean, server_default=db.text("false"))


class PowerEnergyResource(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "power_energy_resource"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    power_id = db.Column(
        db.ForeignKey("power.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    energy_resource_id = db.Column(
        db.ForeignKey("energy_resource.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    is_primary = db.Column(db.Boolean, server_default=db.text("false"))


class PowerComponent(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "power_component"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)
    northings = db.Column(db.Text)
    eastings = db.Column(db.Text)


class PPAstatus(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "ppa_status"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)


class Unit(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "unit"

    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)


class Power(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "power"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    developer = db.Column(db.Text)
    notice = db.Column(db.Text)
    picture_source = db.Column(db.Text)
    sponsor_id = db.Column(UUID(as_uuid=True))
    sponsor_name = db.Column(db.Text)
    full_name = db.Column(db.Text)
    short_name = db.Column(db.Text)
    capacity_id = db.Column(
        db.ForeignKey("capacity.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    size = db.Column(db.Float)
    description = db.Column(db.Text)
    energy_resource_id = db.Column(
        db.ForeignKey("energy_resource.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    technology_id = db.Column(
        db.ForeignKey("technology.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    technology_type_id = db.Column(
        db.ForeignKey("technology_type.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    other_technologies = db.Column(db.Text)
    waterbody_names = db.Column(db.Text)
    scheme = db.Column(db.Text)
    design_components = db.Column(db.Text)
    unit_id = db.Column(
        db.ForeignKey("unit.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    average_length = db.Column(db.Float)
    average_width = db.Column(db.Float)
    off_taker_id = db.Column(
        db.ForeignKey("off_taker.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    statutory_permits = db.Column(db.Text)
    ppa_status_id = db.Column(
        db.ForeignKey("ppa_status.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    ppa_status_grid_id = db.Column(
        db.ForeignKey("ppa_status.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    data_shareable_public = db.Column(db.Boolean, server_default=db.text("false"))
    data_shareable_local = db.Column(db.Boolean, server_default=db.text("false"))

    capacity = db.relationship("Capacity")


class ProjectData(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "project_data"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    height = db.Column(db.Text)
    size_class = db.Column(db.Text)
    hazard_potential = db.Column(db.Text)
    type_of_dam = db.Column(db.Text)
    dam_length = db.Column(db.Float)
    crest_width = db.Column(db.Float)
    catchment_area = db.Column(db.Float)
    design_flow = db.Column(db.Float)
    maximum_flood = db.Column(db.Float)
    q100 = db.Column(db.Float)
    q200 = db.Column(db.Float)
    canal_length = db.Column(db.Float)
    canal_width = db.Column(db.Float)
    canal_velocity = db.Column(db.Float)
    spillway_type = db.Column(db.Text)
    spillway_length = db.Column(db.Float)
    spillway_free_board = db.Column(db.Float)
    spillway_discharge_capacity = db.Column(db.Float)
    penstocks_type = db.Column(db.Text)
    penstocks_diameter = db.Column(db.Float)
    penstocks_velocity = db.Column(db.Float)
    penstocks_thickness = db.Column(db.Float)
    penstocks_number = db.Column(db.Float)
    installation_method = db.Column(db.Text)
    upstream_control = db.Column(db.Text)
    inlet_control = db.Column(db.Text)
    outlet_control = db.Column(db.Text)
    overhead_crane = db.Column(db.Float)
    turbine_type = db.Column(db.Text)
    turbine_capacity_id = db.Column(
        db.ForeignKey("capacity.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    turbine_numbers = db.Column(db.Integer)
    turbine_capacity = db.Column(db.Float)
    turbine_efficiency = db.Column(db.Float)
    turbine_capacity_flow = db.Column(db.Float)
    alternator_power_output = db.Column(db.Float)
    alternator_number = db.Column(db.Integer)
    alternator_voltage = db.Column(db.Float)
    substation_power_output = db.Column(db.Float)
    substation_voltage = db.Column(db.Float)




class ProjectDocument(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "project_document"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    project_id = db.Column(
        db.ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    document_type = db.Column(db.Text)
    name = db.Column(db.Text)


class ProjectSponsorType(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "project_sponsor_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sponsor_id = db.Column(
        db.ForeignKey("sponsor.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    sponsor_type_id = db.Column(
        db.ForeignKey("sponsor_type.id", ondelete="CASCADE", onupdate="CASCADE")
    )


class SponsorCountry(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "sponsor_country"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sponsor_id = db.Column(
        db.ForeignKey("sponsor.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    country_id = db.Column(db.Text)


class SponsorSectorIndustry(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "sponsor_sector_industry"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sponsor_id = db.Column(
        db.ForeignKey("sponsor.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    sector_industry_id = db.Column(db.Text)
    is_primary = db.Column(db.Boolean, server_default=db.text("false"))


class SponsorDocument(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "sponsor_document"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    sponsor_id = db.Column(
        db.ForeignKey("sponsor.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    document_type = db.Column(db.Text)
    name = db.Column(db.Text)


class Sponsor(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "sponsor"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("gen_random_uuid()"))
    name = db.Column(db.Text)
    other_sponsors = db.Column(db.Text)
    shareholders = db.Column(db.Text)
    background = db.Column(db.Text)
    experience = db.Column(db.Text)
    ownership = db.Column(db.Text)
    percentage_public = db.Column(db.Float)
    percentage_private = db.Column(db.Float)
    percentage_academic = db.Column(db.Float)
    products = db.Column(db.Text)
    other_projects = db.Column(db.Text)
    compliance = db.Column(db.Text)
    partners = db.Column(db.Text)
    capital_statement = db.Column(db.Text)
    contact_person = db.Column(db.Text)
    contact_address = db.Column(db.Text)
    contact_postal = db.Column(db.Text)
    contact_email = db.Column(db.Text)
    contact_telephone = db.Column(db.Text)
    contact_website = db.Column(db.Text)


class ProjectTeam(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "project_team"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    manager = db.Column(db.Text)
    manager_background = db.Column(db.Text)
    has_board = db.Column(db.Boolean, server_default=db.text("false"))
    number_directors = db.Column(db.Integer)
    board_directors = db.Column(db.Text)
    management_oficers = db.Column(db.Text)
    technical_staff = db.Column(db.Text)
    management_targets = db.Column(db.Text)
    management_agreement = db.Column(db.Text)
    personnel_practices = db.Column(db.Text)
    manager_nin = db.Column(db.Text)
    nin_validate = db.Column(db.Boolean, server_default=db.text("false"))


class PowerSchedule(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "power_schedule"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    construction_schedule = db.Column(db.Text)
    startup_schedule = db.Column(db.Text)
    operations_schedule = db.Column(db.Text)
    expenditures = db.Column(db.Text)
    funding_schedule = db.Column(db.Text)
    regulatory_compliance = db.Column(db.Text)


class PowerImpact(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "power_impact"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    description_environment = db.Column(db.Text)
    description_social = db.Column(db.Text)
    description_environment_impact = db.Column(db.Text)
    description_social_impact = db.Column(db.Text)
    treatment_plans = db.Column(db.Text)
    occupational_hazards = db.Column(db.Text)
    local_regulations = db.Column(db.Text)
    sponsor_contribution = db.Column(db.Text)
    key_partners = db.Column(db.Text)
    environmental_concerns = db.Column(db.Text)
    esmp = db.Column(db.Text)


class ProjectMarket(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "project_market"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    overview = db.Column(db.Text)
    economic_issues = db.Column(db.Text)
    energy_sector = db.Column(db.Text)
    electricity_sector = db.Column(db.Text)
    sector_policies = db.Column(db.Text)
    laws = db.Column(db.Text)
    key_stakeholders = db.Column(db.Text)
    outlook = db.Column(db.Text)
    competition = db.Column(db.Text)
    main_competitors = db.Column(db.Text)
    competitive_advantage = db.Column(db.Text)
    strengths = db.Column(db.Text)
    weaknesses = db.Column(db.Text)
    opportunities = db.Column(db.Text)
    threats = db.Column(db.Text)


class ProjectInvestment(db.Model, SerializerMixin):
    __bind_key__ = 'project'
    __tablename__ = "project_investment"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    total_cost = db.Column(db.Float)
    required_investment = db.Column(db.Text)
    shareholder_structure = db.Column(db.Text)
    equity_investors = db.Column(db.Text)
    equity_partners = db.Column(db.Text)
    prospective_equity_amount = db.Column(db.Float)
    required_equity_amount = db.Column(db.Float)
    equity_mobilized = db.Column(db.Float)
    equity_needed = db.Column(db.Float)
    required_debt_amount = db.Column(db.Text)
    current_lenders = db.Column(db.Text)
    prospective_lenders = db.Column(db.Text)
    loan_type = db.Column(db.Text)
