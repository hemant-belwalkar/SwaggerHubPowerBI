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


class CredentialsStoredInServer(object):
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
        'user_name': 'str',
        'password': 'str',
        'use_as_windows_credentials': 'bool',
        'impersonate_authenticated_user': 'bool'
    }

    attribute_map = {
        'user_name': 'UserName',
        'password': 'Password',
        'use_as_windows_credentials': 'UseAsWindowsCredentials',
        'impersonate_authenticated_user': 'ImpersonateAuthenticatedUser'
    }

    def __init__(self, user_name=None, password=None, use_as_windows_credentials=None, impersonate_authenticated_user=None, _configuration=None):  # noqa: E501
        """CredentialsStoredInServer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_name = None
        self._password = None
        self._use_as_windows_credentials = None
        self._impersonate_authenticated_user = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if use_as_windows_credentials is not None:
            self.use_as_windows_credentials = use_as_windows_credentials
        if impersonate_authenticated_user is not None:
            self.impersonate_authenticated_user = impersonate_authenticated_user

    @property
    def user_name(self):
        """Gets the user_name of this CredentialsStoredInServer.  # noqa: E501

        A string value that contains the user name to be used to connect to an external data source.  # noqa: E501

        :return: The user_name of this CredentialsStoredInServer.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CredentialsStoredInServer.

        A string value that contains the user name to be used to connect to an external data source.  # noqa: E501

        :param user_name: The user_name of this CredentialsStoredInServer.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this CredentialsStoredInServer.  # noqa: E501

        A string value that contains the password to be used to connect to an external data source.  # noqa: E501

        :return: The password of this CredentialsStoredInServer.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CredentialsStoredInServer.

        A string value that contains the password to be used to connect to an external data source.  # noqa: E501

        :param password: The password of this CredentialsStoredInServer.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def use_as_windows_credentials(self):
        """Gets the use_as_windows_credentials of this CredentialsStoredInServer.  # noqa: E501

        A boolean value that indicates whether the supplied credentials should be used as Windows credentials.  # noqa: E501

        :return: The use_as_windows_credentials of this CredentialsStoredInServer.  # noqa: E501
        :rtype: bool
        """
        return self._use_as_windows_credentials

    @use_as_windows_credentials.setter
    def use_as_windows_credentials(self, use_as_windows_credentials):
        """Sets the use_as_windows_credentials of this CredentialsStoredInServer.

        A boolean value that indicates whether the supplied credentials should be used as Windows credentials.  # noqa: E501

        :param use_as_windows_credentials: The use_as_windows_credentials of this CredentialsStoredInServer.  # noqa: E501
        :type: bool
        """

        self._use_as_windows_credentials = use_as_windows_credentials

    @property
    def impersonate_authenticated_user(self):
        """Gets the impersonate_authenticated_user of this CredentialsStoredInServer.  # noqa: E501

        A boolean value that indicates whether the session should impersonate the user for the supplied credentials.  # noqa: E501

        :return: The impersonate_authenticated_user of this CredentialsStoredInServer.  # noqa: E501
        :rtype: bool
        """
        return self._impersonate_authenticated_user

    @impersonate_authenticated_user.setter
    def impersonate_authenticated_user(self, impersonate_authenticated_user):
        """Sets the impersonate_authenticated_user of this CredentialsStoredInServer.

        A boolean value that indicates whether the session should impersonate the user for the supplied credentials.  # noqa: E501

        :param impersonate_authenticated_user: The impersonate_authenticated_user of this CredentialsStoredInServer.  # noqa: E501
        :type: bool
        """

        self._impersonate_authenticated_user = impersonate_authenticated_user

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
        if issubclass(CredentialsStoredInServer, dict):
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
        if not isinstance(other, CredentialsStoredInServer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CredentialsStoredInServer):
            return True

        return self.to_dict() != other.to_dict()