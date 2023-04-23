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


class ODataDataModelRoleAssignments(object):
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
        'odata_context': 'str',
        'odata_count': 'int',
        'value': 'list[DataModelRoleAssignment]'
    }

    attribute_map = {
        'odata_context': '@odata.context',
        'odata_count': '@odata.count',
        'value': 'value'
    }

    def __init__(self, odata_context=None, odata_count=None, value=None, _configuration=None):  # noqa: E501
        """ODataDataModelRoleAssignments - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._odata_context = None
        self._odata_count = None
        self._value = None
        self.discriminator = None

        if odata_context is not None:
            self.odata_context = odata_context
        if odata_count is not None:
            self.odata_count = odata_count
        if value is not None:
            self.value = value

    @property
    def odata_context(self):
        """Gets the odata_context of this ODataDataModelRoleAssignments.  # noqa: E501


        :return: The odata_context of this ODataDataModelRoleAssignments.  # noqa: E501
        :rtype: str
        """
        return self._odata_context

    @odata_context.setter
    def odata_context(self, odata_context):
        """Sets the odata_context of this ODataDataModelRoleAssignments.


        :param odata_context: The odata_context of this ODataDataModelRoleAssignments.  # noqa: E501
        :type: str
        """

        self._odata_context = odata_context

    @property
    def odata_count(self):
        """Gets the odata_count of this ODataDataModelRoleAssignments.  # noqa: E501


        :return: The odata_count of this ODataDataModelRoleAssignments.  # noqa: E501
        :rtype: int
        """
        return self._odata_count

    @odata_count.setter
    def odata_count(self, odata_count):
        """Sets the odata_count of this ODataDataModelRoleAssignments.


        :param odata_count: The odata_count of this ODataDataModelRoleAssignments.  # noqa: E501
        :type: int
        """

        self._odata_count = odata_count

    @property
    def value(self):
        """Gets the value of this ODataDataModelRoleAssignments.  # noqa: E501


        :return: The value of this ODataDataModelRoleAssignments.  # noqa: E501
        :rtype: list[DataModelRoleAssignment]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ODataDataModelRoleAssignments.


        :param value: The value of this ODataDataModelRoleAssignments.  # noqa: E501
        :type: list[DataModelRoleAssignment]
        """

        self._value = value

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
        if issubclass(ODataDataModelRoleAssignments, dict):
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
        if not isinstance(other, ODataDataModelRoleAssignments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODataDataModelRoleAssignments):
            return True

        return self.to_dict() != other.to_dict()
