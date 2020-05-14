#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.test import TestCase
from workflow.models import (
    Organization, Program, Country, Province, ProjectAgreement, Sector,
    ProjectComplete, ProjectType, SiteProfile, Office, Budget,
    Documentation, Checklist, ProjectStatus
)

class ProjectStatusTestCase(TestCase):


    def setUp(self):
        new_project_status = ProjectStatus.objects.create(name="project status")

    def test_project_status_creation(self):
        """Check for ProjectStatus Object creation"""
        get_project_status = ProjectStatus.objects.get(name="project status")
        self.assertIsInstance(get_project_status, ProjectStatus)
        self.assertIn(get_project_status.name, get_project_status.__str__())
        self.assertEqual(ProjectStatus.objects.filter(
            name=get_project_status.name).count(), 1)
        

class DocumentationTestCase(TestCase):


    def setUp(self):
        new_documentation = Documentation.objects.create(name="document created", description="documentation test")

    def test_documenation_creation(self):
        """Check Documentation Object creation"""
        get_documentation =Documentation.objects.get(name="document created")
        self.assertIsInstance(get_documentation, Documentation)
        self.assertIn(get_documentation.name, get_documentation.__str__() )
        self.assertEqual(Documentation.objects.filter(
            name=get_documentation.name).count(), 1)

class ChecklistTestCase(TestCase):


    fixtures = ['fixtures/sectors.json', 'fixtures/projecttype.json']
    def setUp(self):   
        # load from fixtures
        get_project_type = ProjectType.objects.get(id='1')
        get_sector = Sector.objects.get(id='2')
        new_organization = Organization.objects.create(name="Activity")
        get_organization = Organization.objects.get(name="Activity")
        new_country = Country.objects.create(
            country="testcountry", organization=get_organization)
        get_country = Country.objects.get(country="testcountry")
        new_province = Province.objects.create(
            name="testprovince", country=get_country)
        get_province = Province.objects.get(name="testprovince")
        new_office = Office.objects.create(
            name="testoffice", province=get_province)
        get_office = Office.objects.get(name="testoffice")
        new_program = Program.objects.create(name="testprogram")
        new_program.country.add(get_country)
        get_program = Program.objects.get(name="testprogram")
        new_agreement = ProjectAgreement.objects.create(
            program=get_program,
            project_name="testproject",
            project_type=get_project_type, activity_code="111222",
            office=get_office, sector=get_sector)
        get_agreement = ProjectAgreement.objects.get(project_name="testproject")
        new_checklist = Checklist.objects.create(name="test checklist created", country=get_country, agreement=get_agreement)
        new_sector = Sector.objects.create(sector="new sector", create_date=None)

    def test_sector_creation(self):
        """Test sector creation with null create_date"""
        get_sector = Sector.objects.get(sector="new sector")
        self.assertIsInstance(get_sector, Sector)
        self.assertIn(get_sector.sector, get_sector.__str__())
        self.assertEqual(Sector.objects.filter(
            sector=get_sector.sector).count(), 1)


    def test_checklist_creation(self):
        """Check for Checklist Object creation"""
        get_checklist =Checklist.objects.get(name="test checklist created")
        self.assertIsInstance(get_checklist, Checklist)
        self.assertEqual(get_checklist.agreement, get_checklist.__str__())
        self.assertEqual(Checklist.objects.filter(
            name=get_checklist.name).count(), 1)


class SiteProfileTestCase(TestCase):


    fixtures = ['fixtures/organization.json', 'fixtures/profiletypes.json']

    def setUp(self):
        new_organization = Organization.objects.create(name="Activity")
        get_organization = Organization.objects.get(name="Activity")
        new_country = Country.objects.create(
            country="testcountry", organization=get_organization)
        get_country = Country.objects.get(country="testcountry")
        new_province = Province.objects.create(
            name="testprovince", country=get_country)
        get_province = Province.objects.get(name="testprovince")
        new_office = Office.objects.create(
            name="testoffice", province=new_province)
        get_office = Office.objects.get(name="testoffice")
        new_community = SiteProfile.objects.create(
            name="testcommunity", country=get_country, office=get_office,
            province=get_province)

    def test_community_creation(self):
        """Test if SiteProfile Object is created"""
        get_community = SiteProfile.objects.get(name="testcommunity")
        self.assertIsInstance(get_community, SiteProfile)
        self.assertIn(get_community.name, get_community.__str__())
        self.assertEqual(SiteProfile.objects.filter(
            name=get_community.name).count(), 1)


class AgreementTestCase(TestCase):


    fixtures = ['fixtures/projecttype.json', 'fixtures/sectors.json']

    def setUp(self):
        new_organization = Organization.objects.create(name="Activity")
        get_organization = Organization.objects.get(name="Activity")
        new_country = Country.objects.create(
            country="testcountry", organization=get_organization)
        get_country = Country.objects.get(country="testcountry")
        new_program = Program.objects.create(name="testprogram")
        new_program.country.add(get_country)
        get_program = Program.objects.get(name="testprogram")
        new_province = Province.objects.create(
            name="testprovince", country=get_country)
        get_province = Province.objects.get(name="testprovince")
        new_office = Office.objects.create(
            name="testoffice", province=new_province)
        get_office = Office.objects.get(name="testoffice")
        new_community = SiteProfile.objects.create(
            name="testcommunity", country=get_country, office=get_office,
            province=get_province)
        get_community = SiteProfile.objects.get(name="testcommunity")
        # load from fixtures
        get_project_type = ProjectType.objects.get(id='1')
        get_sector = Sector.objects.get(id='2')
        new_agreement = ProjectAgreement.objects.create(
            program=get_program,
            project_name="testproject",
            project_type=get_project_type, activity_code="111222",
            office=get_office, sector=get_sector)
        new_agreement.site.add(get_community)

        new_budget = Budget.objects.create(
            contributor="testbudget",
            description_of_contribution="new_province", proposed_value="24",
            agreement=new_agreement)


    def test_Agreement_creation(self):
        """Test if Agreement Object is created"""
        get_agreement = ProjectAgreement.objects.get(
            project_name="testproject")
        self.assertIsInstance(get_agreement, ProjectAgreement)
        self.assertIn(get_agreement.project_name, get_agreement.__str__())
        self.assertEqual(ProjectAgreement.objects.filter(
            project_name=get_agreement.project_name).count(), 1)

    def test_Budget_creation(self):
        """Test if Budget Object is created"""
        get_budget = Budget.objects.get(contributor="testbudget")
        self.assertIsInstance(get_budget, Budget)
        self.assertIn(get_budget.contributor, get_budget.__str__())
        self.assertEqual(Budget.objects.filter(id=get_budget.id).count(), 1)

class CompleteTestCase(TestCase):


    fixtures = ['fixtures/projecttype.json', 'fixtures/sectors.json']

    def setUp(self):
        new_organization = Organization.objects.create(name="Activity")
        get_organization = Organization.objects.get(name="Activity")
        new_country = Country.objects.create(
            country="testcountry", organization=get_organization)
        get_country = Country.objects.get(country="testcountry")
        new_program = Program.objects.create(name="testprogram")
        new_program.country.add(get_country)
        get_program = Program.objects.get(name="testprogram")
        new_province = Province.objects.create(
            name="testprovince", country=get_country)
        get_province = Province.objects.get(name="testprovince")
        new_office = Office.objects.create(
            name="testoffice", province=new_province)
        get_office = Office.objects.get(name="testoffice")
        new_community = SiteProfile.objects.create(
            name="testcommunity", country=get_country, office=get_office,
            province=get_province)
        get_community = SiteProfile.objects.get(name="testcommunity")
        # load from fixtures
        get_project_type = ProjectType.objects.get(id='1')
        get_sector = Sector.objects.get(id='2')
        new_agreement = ProjectAgreement.objects.create(
            program=get_program,
            project_name="testproject",
            project_type=get_project_type, activity_code="111222",
            office=get_office, sector=get_sector)
        new_agreement2 = ProjectAgreement.objects.create(
            program=get_program,
            project_name="testproject2",
            project_type=get_project_type, activity_code="111222",
            office=get_office, sector=get_sector,
            total_estimated_budget = None,
            mc_estimated_budget = None,
            local_total_estimated_budget = None,
            local_mc_estimated_budget = None
            )
        new_agreement2.site.add(get_community)
        new_agreement.site.add(get_community)
        get_agreement = ProjectAgreement.objects.get(
            project_name="testproject")
        get_agreement2 = ProjectAgreement.objects.get(
            project_name="testproject2")
        new_complete = ProjectComplete.objects.create(
            program=get_program, project_name="testproject",
            activity_code="111222", office=get_office, on_time=True,
            community_handover=1, project_agreement=get_agreement,
            estimated_budget = None, actual_budget = None, total_cost = None,
            agency_cost = None, local_total_cost = None, local_agency_cost = None
            )
        new_complete2 = ProjectComplete.objects.create(
            program=get_program, project_name="testproject2",
            activity_code="111222", office=get_office, on_time=True,
            community_handover=1, project_agreement=get_agreement2)

    def test_complete_creation(self):
        """Test if ProjectComplete Object is created with defaults set to None"""
        get_complete = ProjectComplete.objects.get(project_name="testproject")
        self.assertIsInstance(get_complete, ProjectComplete)
        self.assertIn(get_complete.project_name, get_complete.__str__())
        self.assertEqual(ProjectComplete.objects.filter(project_name=get_complete.project_name).count(), 1)

    def test_complete_creation_with_defaults_for_project_agreement(self):
        """Test if ProjectComplete Object with defaults for ProjectAgreement Object is created"""
        get_complete2 = ProjectComplete.objects.get(project_name="testproject2")
        self.assertIn(get_complete2.project_name, get_complete2.__str__())
        self.assertIsInstance(get_complete2, ProjectComplete)

    def test_complete_exists(self):
        """Check for Complete object"""
        get_complete = ProjectComplete.objects.get(project_name="testproject")
        self.assertEqual(ProjectComplete.objects.filter(
            id=get_complete.id).count(), 1)
