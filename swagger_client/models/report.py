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


class Report(object):
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
        'has_data_sources': 'bool',
        'has_shared_data_sets': 'bool',
        'has_parameters': 'bool'
    }

    attribute_map = {
        'has_data_sources': 'HasDataSources',
        'has_shared_data_sets': 'HasSharedDataSets',
        'has_parameters': 'HasParameters'
    }

    def __init__(self, has_data_sources=None, has_shared_data_sets=None, has_parameters=None, _configuration=None):  # noqa: E501
        """Report - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._has_data_sources = None
        self._has_shared_data_sets = None
        self._has_parameters = None
        self.discriminator = None

        if has_data_sources is not None:
            self.has_data_sources = has_data_sources
        if has_shared_data_sets is not None:
            self.has_shared_data_sets = has_shared_data_sets
        if has_parameters is not None:
            self.has_parameters = has_parameters

    @property
    def has_data_sources(self):
        """Gets the has_data_sources of this Report.  # noqa: E501

        A boolean value that indicates whether the Report has DataSources associated with it.  # noqa: E501

        :return: The has_data_sources of this Report.  # noqa: E501
        :rtype: bool
        """
        return self._has_data_sources

    @has_data_sources.setter
    def has_data_sources(self, has_data_sources):
        """Sets the has_data_sources of this Report.

        A boolean value that indicates whether the Report has DataSources associated with it.  # noqa: E501

        :param has_data_sources: The has_data_sources of this Report.  # noqa: E501
        :type: bool
        """

        self._has_data_sources = has_data_sources

    @property
    def has_shared_data_sets(self):
        """Gets the has_shared_data_sets of this Report.  # noqa: E501

        A boolean value that indicates whether the Report has shared DataSets associated with it.  # noqa: E501

        :return: The has_shared_data_sets of this Report.  # noqa: E501
        :rtype: bool
        """
        return self._has_shared_data_sets

    @has_shared_data_sets.setter
    def has_shared_data_sets(self, has_shared_data_sets):
        """Sets the has_shared_data_sets of this Report.

        A boolean value that indicates whether the Report has shared DataSets associated with it.  # noqa: E501

        :param has_shared_data_sets: The has_shared_data_sets of this Report.  # noqa: E501
        :type: bool
        """

        self._has_shared_data_sets = has_shared_data_sets

    @property
    def has_parameters(self):
        """Gets the has_parameters of this Report.  # noqa: E501

        A boolean value that indicates whether the Report has parameters.  # noqa: E501

        :return: The has_parameters of this Report.  # noqa: E501
        :rtype: bool
        """
        return self._has_parameters

    @has_parameters.setter
    def has_parameters(self, has_parameters):
        """Sets the has_parameters of this Report.

        A boolean value that indicates whether the Report has parameters.  # noqa: E501

        :param has_parameters: The has_parameters of this Report.  # noqa: E501
        :type: bool
        """

        self._has_parameters = has_parameters

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
        if issubclass(Report, dict):
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
        if not isinstance(other, Report):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Report):
            return True

        return self.to_dict() != other.to_dict()
