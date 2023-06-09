# coding: utf-8

"""
    Power BI Report Server REST API

    The Power BI Report Server REST API provides programmatic access to the report server catalog.  For example, basic CRUD operations can be done on folders, reports, KPIs, data sources, datasets, refresh plans, subscriptions, etc.     The REST API can also be used to provide more advanced functionality, such as: * Navigate the folder hierarchy * Discover the contents of a folder * Download a report definition * Modify default report parameters * Change or execute a refresh plan * A whole lot more  The REST API is a RESTful successor to the legacy [SOAP API](https://msdn.microsoft.com/library/reportservice2010.reportingservice2010.aspx).  Since Power BI Report Server is a superset of SQL Server Reporting Services, the Power BI Report Server REST API is a superset of the  [SQL Server Reporting Services REST API](https://app.swaggerhub.com/apis/microsoft-rs/SSRS/2.0).  __Power BI Report Server API Additions__ * October 2020 Release   * /PowerBIReports({Id})/DataModelParameters(GET & POST)  * January 2019 Release   * /PowerBIReports({Id})/DataModelRoles (GET)   * /PowerBIReports({Id})/DataModelRoleAssignments (GET & PUT)  Happy coding!  __API samples:__ https://github.com/Microsoft/Reporting-Services  __Developer documentation:__ https://powerbi.microsoft.com/documentation/reportserver-developer-handbook-overview/  __Team Blog:__  https://powerbi.microsoft.com/blog/  __Support forums:__  https://community.powerbi.com/t5/Report-Server/bd-p/ReportServer   # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.power_bi_reports_api import PowerBIReportsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPowerBIReportsApi(unittest.TestCase):
    """PowerBIReportsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.power_bi_reports_api.PowerBIReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_power_bi_report(self):
        """Test case for add_power_bi_report

        Creates a new PowerBIReport CatalogItem.  # noqa: E501
        """
        pass

    def test_add_power_bi_report_comment(self):
        """Test case for add_power_bi_report_comment

        Creates a new Comment associated to the specified PowerBIReport.  # noqa: E501
        """
        pass

    def test_check_power_bi_report_data_source_connection(self):
        """Test case for check_power_bi_report_data_source_connection

        Checks the status of the specified DataSource connection.  # noqa: E501
        """
        pass

    def test_delete_power_bi_report(self):
        """Test case for delete_power_bi_report

        Deletes the specified PowerBIReport.  # noqa: E501
        """
        pass

    def test_delete_power_bi_report_comment(self):
        """Test case for delete_power_bi_report_comment

        Deletes the specified Comment associated to the PowerBIReport.  # noqa: E501
        """
        pass

    def test_get_power_bi_cache_refresh_plans(self):
        """Test case for get_power_bi_cache_refresh_plans

        Gets the CacheRefreshPlans for a given Power BI Report.  # noqa: E501
        """
        pass

    def test_get_power_bi_report(self):
        """Test case for get_power_bi_report

        Gets a PowerBIReport CatalogItem specified by the Id.  # noqa: E501
        """
        pass

    def test_get_power_bi_report_allowed_actions(self):
        """Test case for get_power_bi_report_allowed_actions

        Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.  # noqa: E501
        """
        pass

    def test_get_power_bi_report_comments(self):
        """Test case for get_power_bi_report_comments

        Gets the Comments for a PowerBIReport specified by the Id.  # noqa: E501
        """
        pass

    def test_get_power_bi_report_content(self):
        """Test case for get_power_bi_report_content

        Gets the content of the specified PowerBIReport CatalogItem.  # noqa: E501
        """
        pass

    def test_get_power_bi_report_data_model_parameters(self):
        """Test case for get_power_bi_report_data_model_parameters

        Gets the data model parameters that are associated with the specified PowerBIReport.  # noqa: E501
        """
        pass

    def test_get_power_bi_report_data_model_role_assignments(self):
        """Test case for get_power_bi_report_data_model_role_assignments

        Gets the data model role assignments that are associated with the specified PowerBIReport.  # noqa: E501
        """
        pass

    def test_get_power_bi_report_data_model_roles(self):
        """Test case for get_power_bi_report_data_model_roles

        Gets the data model roles that are associated with the specified PowerBIReport.  # noqa: E501
        """
        pass

    def test_get_power_bi_report_data_sources(self):
        """Test case for get_power_bi_report_data_sources

        Gets the DataSources that are associated with the specified PowerBIReport.  # noqa: E501
        """
        pass

    def test_get_power_bi_report_policies(self):
        """Test case for get_power_bi_report_policies

        Gets ItemPolicies associated with the specified PowerBIReport CatalogItem.  # noqa: E501
        """
        pass

    def test_get_power_bi_report_properties(self):
        """Test case for get_power_bi_report_properties

        Gets PowerBIReports Properties (takes list of Property names to retrieve the values)  # noqa: E501
        """
        pass

    def test_get_power_bi_reports(self):
        """Test case for get_power_bi_reports

        Gets an array of PowerBIReport CatalogItems.  # noqa: E501
        """
        pass

    def test_replace_power_bi_report_data_model_role_assignments(self):
        """Test case for replace_power_bi_report_data_model_role_assignments

        Replaces the data model role assignments that are associated with the specified PowerBIReport.  # noqa: E501
        """
        pass

    def test_set_power_bi_report_policies(self):
        """Test case for set_power_bi_report_policies

        Replaces ItemPolicies associated with the specified PowerBIReport item.  # noqa: E501
        """
        pass

    def test_update_power_bi_report(self):
        """Test case for update_power_bi_report

        Updates the specified PowerBIReport CatalogItem using the provided definition.  # noqa: E501
        """
        pass

    def test_update_power_bi_report_comment(self):
        """Test case for update_power_bi_report_comment

        Updates the Comment specified by CommentId in the associated PowerBIReport.  # noqa: E501
        """
        pass

    def test_update_power_bi_report_data_model_parameters(self):
        """Test case for update_power_bi_report_data_model_parameters

        Updates the data model parameters that are associated with the specified PowerBIReport. If any datasources are updated based on parameters, they can be fetched with DataSources api.  # noqa: E501
        """
        pass

    def test_update_power_bi_report_data_source(self):
        """Test case for update_power_bi_report_data_source

        Updates the DataSource definition associated with the PowerBIReport specified by the Id.  # noqa: E501
        """
        pass

    def test_update_power_bi_report_properties(self):
        """Test case for update_power_bi_report_properties

        Updates the PowerBIReport Properties included in the given list.  # noqa: E501
        """
        pass

    def test_upload_power_bi_report(self):
        """Test case for upload_power_bi_report

        Does an efficient binary upload of a new or existing PowerBIReport CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
