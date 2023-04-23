# coding: utf-8

"""
    Power BI Report Server REST API

    The Power BI Report Server REST API provides programmatic access to the report server catalog.  For example, basic CRUD operations can be done on folders, reports, KPIs, data sources, datasets, refresh plans, subscriptions, etc.     The REST API can also be used to provide more advanced functionality, such as: * Navigate the folder hierarchy * Discover the contents of a folder * Download a report definition * Modify default report parameters * Change or execute a refresh plan * A whole lot more  The REST API is a RESTful successor to the legacy [SOAP API](https://msdn.microsoft.com/library/reportservice2010.reportingservice2010.aspx).  Since Power BI Report Server is a superset of SQL Server Reporting Services, the Power BI Report Server REST API is a superset of the  [SQL Server Reporting Services REST API](https://app.swaggerhub.com/apis/microsoft-rs/SSRS/2.0).  __Power BI Report Server API Additions__ * October 2020 Release   * /PowerBIReports({Id})/DataModelParameters(GET & POST)  * January 2019 Release   * /PowerBIReports({Id})/DataModelRoles (GET)   * /PowerBIReports({Id})/DataModelRoleAssignments (GET & PUT)  Happy coding!  __API samples:__ https://github.com/Microsoft/Reporting-Services  __Developer documentation:__ https://powerbi.microsoft.com/documentation/reportserver-developer-handbook-overview/  __Team Blog:__  https://powerbi.microsoft.com/blog/  __Support forums:__  https://community.powerbi.com/t5/Report-Server/bd-p/ReportServer   # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class MobileReportManifest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'resources': 'list[ResourceGroup]',
        'data_sets': 'list[DataSetItem]',
        'thumbnails': 'list[ThumbnailItem]'
    }

    attribute_map = {
        'resources': 'Resources',
        'data_sets': 'DataSets',
        'thumbnails': 'Thumbnails'
    }

    def __init__(self, resources=None, data_sets=None, thumbnails=None, _configuration=None):  # noqa: E501
        """MobileReportManifest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resources = None
        self._data_sets = None
        self._thumbnails = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if data_sets is not None:
            self.data_sets = data_sets
        if thumbnails is not None:
            self.thumbnails = thumbnails

    @property
    def resources(self):
        """Gets the resources of this MobileReportManifest.  # noqa: E501

        An array of items of type ResourceGroup that specify the resources referenced in this MobileReport. A Resource is a generalized object and its content type is undefined.  A client must be able to understand the content returned in the Resource.  # noqa: E501

        :return: The resources of this MobileReportManifest.  # noqa: E501
        :rtype: list[ResourceGroup]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this MobileReportManifest.

        An array of items of type ResourceGroup that specify the resources referenced in this MobileReport. A Resource is a generalized object and its content type is undefined.  A client must be able to understand the content returned in the Resource.  # noqa: E501

        :param resources: The resources of this MobileReportManifest.  # noqa: E501
        :type: list[ResourceGroup]
        """

        self._resources = resources

    @property
    def data_sets(self):
        """Gets the data_sets of this MobileReportManifest.  # noqa: E501

        An array of objects of type DataSetItem that specifies the DataSets referenced in this MobileReport.  # noqa: E501

        :return: The data_sets of this MobileReportManifest.  # noqa: E501
        :rtype: list[DataSetItem]
        """
        return self._data_sets

    @data_sets.setter
    def data_sets(self, data_sets):
        """Sets the data_sets of this MobileReportManifest.

        An array of objects of type DataSetItem that specifies the DataSets referenced in this MobileReport.  # noqa: E501

        :param data_sets: The data_sets of this MobileReportManifest.  # noqa: E501
        :type: list[DataSetItem]
        """

        self._data_sets = data_sets

    @property
    def thumbnails(self):
        """Gets the thumbnails of this MobileReportManifest.  # noqa: E501

        An array of items of type ThumbnailItem that contains the Thumbnails associated with the MobileReport.  # noqa: E501

        :return: The thumbnails of this MobileReportManifest.  # noqa: E501
        :rtype: list[ThumbnailItem]
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """Sets the thumbnails of this MobileReportManifest.

        An array of items of type ThumbnailItem that contains the Thumbnails associated with the MobileReport.  # noqa: E501

        :param thumbnails: The thumbnails of this MobileReportManifest.  # noqa: E501
        :type: list[ThumbnailItem]
        """

        self._thumbnails = thumbnails

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MobileReportManifest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MobileReportManifest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MobileReportManifest):
            return True

        return self.to_dict() != other.to_dict()
