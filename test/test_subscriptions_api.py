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
from swagger_client.api.subscriptions_api import SubscriptionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSubscriptionsApi(unittest.TestCase):
    """SubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.subscriptions_api.SubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_subscription(self):
        """Test case for add_subscription

        Creates new Subscription item  # noqa: E501
        """
        pass

    def test_delete_subscription(self):
        """Test case for delete_subscription

        Deletes the specified Subscription.  # noqa: E501
        """
        pass

    def test_disable_subscription(self):
        """Test case for disable_subscription

        Disables the Subscription specified by the Id.  # noqa: E501
        """
        pass

    def test_enable_subscription(self):
        """Test case for enable_subscription

        Enables a Subscription specified by the Id.  # noqa: E501
        """
        pass

    def test_execute_subscription(self):
        """Test case for execute_subscription

        Executes the Subscription specified by the Id.  # noqa: E501
        """
        pass

    def test_get_subscription(self):
        """Test case for get_subscription

        Get the specified Subscription.  # noqa: E501
        """
        pass

    def test_get_subscriptions(self):
        """Test case for get_subscriptions

        Gets an array of Subscriptions.  # noqa: E501
        """
        pass

    def test_set_subscription(self):
        """Test case for set_subscription

        Replaces the Subscription item using Id property as key.  # noqa: E501
        """
        pass

    def test_update_subscription(self):
        """Test case for update_subscription

        Updates the Subscription item using Id property as key.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
