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


class MonthlyDOWRecurrence(object):
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
        'which_week': 'WeekNumberEnum',
        'which_week_specified': 'bool',
        'days_of_week': 'DaysOfWeekSelector',
        'months_of_year': 'MonthsOfYearSelector'
    }

    attribute_map = {
        'which_week': 'WhichWeek',
        'which_week_specified': 'WhichWeekSpecified',
        'days_of_week': 'DaysOfWeek',
        'months_of_year': 'MonthsOfYear'
    }

    def __init__(self, which_week=None, which_week_specified=None, days_of_week=None, months_of_year=None, _configuration=None):  # noqa: E501
        """MonthlyDOWRecurrence - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._which_week = None
        self._which_week_specified = None
        self._days_of_week = None
        self._months_of_year = None
        self.discriminator = None

        if which_week is not None:
            self.which_week = which_week
        if which_week_specified is not None:
            self.which_week_specified = which_week_specified
        if days_of_week is not None:
            self.days_of_week = days_of_week
        if months_of_year is not None:
            self.months_of_year = months_of_year

    @property
    def which_week(self):
        """Gets the which_week of this MonthlyDOWRecurrence.  # noqa: E501


        :return: The which_week of this MonthlyDOWRecurrence.  # noqa: E501
        :rtype: WeekNumberEnum
        """
        return self._which_week

    @which_week.setter
    def which_week(self, which_week):
        """Sets the which_week of this MonthlyDOWRecurrence.


        :param which_week: The which_week of this MonthlyDOWRecurrence.  # noqa: E501
        :type: WeekNumberEnum
        """

        self._which_week = which_week

    @property
    def which_week_specified(self):
        """Gets the which_week_specified of this MonthlyDOWRecurrence.  # noqa: E501

        Specifies whether week is specified  # noqa: E501

        :return: The which_week_specified of this MonthlyDOWRecurrence.  # noqa: E501
        :rtype: bool
        """
        return self._which_week_specified

    @which_week_specified.setter
    def which_week_specified(self, which_week_specified):
        """Sets the which_week_specified of this MonthlyDOWRecurrence.

        Specifies whether week is specified  # noqa: E501

        :param which_week_specified: The which_week_specified of this MonthlyDOWRecurrence.  # noqa: E501
        :type: bool
        """

        self._which_week_specified = which_week_specified

    @property
    def days_of_week(self):
        """Gets the days_of_week of this MonthlyDOWRecurrence.  # noqa: E501


        :return: The days_of_week of this MonthlyDOWRecurrence.  # noqa: E501
        :rtype: DaysOfWeekSelector
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        """Sets the days_of_week of this MonthlyDOWRecurrence.


        :param days_of_week: The days_of_week of this MonthlyDOWRecurrence.  # noqa: E501
        :type: DaysOfWeekSelector
        """

        self._days_of_week = days_of_week

    @property
    def months_of_year(self):
        """Gets the months_of_year of this MonthlyDOWRecurrence.  # noqa: E501


        :return: The months_of_year of this MonthlyDOWRecurrence.  # noqa: E501
        :rtype: MonthsOfYearSelector
        """
        return self._months_of_year

    @months_of_year.setter
    def months_of_year(self, months_of_year):
        """Sets the months_of_year of this MonthlyDOWRecurrence.


        :param months_of_year: The months_of_year of this MonthlyDOWRecurrence.  # noqa: E501
        :type: MonthsOfYearSelector
        """

        self._months_of_year = months_of_year

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
        if issubclass(MonthlyDOWRecurrence, dict):
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
        if not isinstance(other, MonthlyDOWRecurrence):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MonthlyDOWRecurrence):
            return True

        return self.to_dict() != other.to_dict()
