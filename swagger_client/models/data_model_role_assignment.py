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


class DataModelRoleAssignment(object):
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
        'group_user_name': 'str',
        'data_model_roles': 'list[str]'
    }

    attribute_map = {
        'group_user_name': 'GroupUserName',
        'data_model_roles': 'DataModelRoles'
    }

    def __init__(self, group_user_name=None, data_model_roles=None, _configuration=None):  # noqa: E501
        """DataModelRoleAssignment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._group_user_name = None
        self._data_model_roles = None
        self.discriminator = None

        if group_user_name is not None:
            self.group_user_name = group_user_name
        if data_model_roles is not None:
            self.data_model_roles = data_model_roles

    @property
    def group_user_name(self):
        """Gets the group_user_name of this DataModelRoleAssignment.  # noqa: E501

        A string value that specifies the name of the user or group to which the role assignment applies.  # noqa: E501

        :return: The group_user_name of this DataModelRoleAssignment.  # noqa: E501
        :rtype: str
        """
        return self._group_user_name

    @group_user_name.setter
    def group_user_name(self, group_user_name):
        """Sets the group_user_name of this DataModelRoleAssignment.

        A string value that specifies the name of the user or group to which the role assignment applies.  # noqa: E501

        :param group_user_name: The group_user_name of this DataModelRoleAssignment.  # noqa: E501
        :type: str
        """

        self._group_user_name = group_user_name

    @property
    def data_model_roles(self):
        """Gets the data_model_roles of this DataModelRoleAssignment.  # noqa: E501

        An array of unique UUID values that specify the identifiers of assigned data model roles.  # noqa: E501

        :return: The data_model_roles of this DataModelRoleAssignment.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_model_roles

    @data_model_roles.setter
    def data_model_roles(self, data_model_roles):
        """Sets the data_model_roles of this DataModelRoleAssignment.

        An array of unique UUID values that specify the identifiers of assigned data model roles.  # noqa: E501

        :param data_model_roles: The data_model_roles of this DataModelRoleAssignment.  # noqa: E501
        :type: list[str]
        """

        self._data_model_roles = data_model_roles

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
        if issubclass(DataModelRoleAssignment, dict):
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
        if not isinstance(other, DataModelRoleAssignment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataModelRoleAssignment):
            return True

        return self.to_dict() != other.to_dict()
