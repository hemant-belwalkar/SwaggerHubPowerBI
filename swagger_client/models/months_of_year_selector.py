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


class MonthsOfYearSelector(object):
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
        'january': 'bool',
        'february': 'bool',
        'march': 'bool',
        'april': 'bool',
        'may': 'bool',
        'june': 'bool',
        'july': 'bool',
        'august': 'bool',
        'september': 'bool',
        'october': 'bool',
        'november': 'bool',
        'december': 'bool'
    }

    attribute_map = {
        'january': 'January',
        'february': 'February',
        'march': 'March',
        'april': 'April',
        'may': 'May',
        'june': 'June',
        'july': 'July',
        'august': 'August',
        'september': 'September',
        'october': 'October',
        'november': 'November',
        'december': 'December'
    }

    def __init__(self, january=None, february=None, march=None, april=None, may=None, june=None, july=None, august=None, september=None, october=None, november=None, december=None, _configuration=None):  # noqa: E501
        """MonthsOfYearSelector - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._january = None
        self._february = None
        self._march = None
        self._april = None
        self._may = None
        self._june = None
        self._july = None
        self._august = None
        self._september = None
        self._october = None
        self._november = None
        self._december = None
        self.discriminator = None

        if january is not None:
            self.january = january
        if february is not None:
            self.february = february
        if march is not None:
            self.march = march
        if april is not None:
            self.april = april
        if may is not None:
            self.may = may
        if june is not None:
            self.june = june
        if july is not None:
            self.july = july
        if august is not None:
            self.august = august
        if september is not None:
            self.september = september
        if october is not None:
            self.october = october
        if november is not None:
            self.november = november
        if december is not None:
            self.december = december

    @property
    def january(self):
        """Gets the january of this MonthsOfYearSelector.  # noqa: E501


        :return: The january of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._january

    @january.setter
    def january(self, january):
        """Sets the january of this MonthsOfYearSelector.


        :param january: The january of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._january = january

    @property
    def february(self):
        """Gets the february of this MonthsOfYearSelector.  # noqa: E501


        :return: The february of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._february

    @february.setter
    def february(self, february):
        """Sets the february of this MonthsOfYearSelector.


        :param february: The february of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._february = february

    @property
    def march(self):
        """Gets the march of this MonthsOfYearSelector.  # noqa: E501


        :return: The march of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._march

    @march.setter
    def march(self, march):
        """Sets the march of this MonthsOfYearSelector.


        :param march: The march of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._march = march

    @property
    def april(self):
        """Gets the april of this MonthsOfYearSelector.  # noqa: E501


        :return: The april of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._april

    @april.setter
    def april(self, april):
        """Sets the april of this MonthsOfYearSelector.


        :param april: The april of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._april = april

    @property
    def may(self):
        """Gets the may of this MonthsOfYearSelector.  # noqa: E501


        :return: The may of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._may

    @may.setter
    def may(self, may):
        """Sets the may of this MonthsOfYearSelector.


        :param may: The may of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._may = may

    @property
    def june(self):
        """Gets the june of this MonthsOfYearSelector.  # noqa: E501


        :return: The june of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._june

    @june.setter
    def june(self, june):
        """Sets the june of this MonthsOfYearSelector.


        :param june: The june of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._june = june

    @property
    def july(self):
        """Gets the july of this MonthsOfYearSelector.  # noqa: E501


        :return: The july of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._july

    @july.setter
    def july(self, july):
        """Sets the july of this MonthsOfYearSelector.


        :param july: The july of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._july = july

    @property
    def august(self):
        """Gets the august of this MonthsOfYearSelector.  # noqa: E501


        :return: The august of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._august

    @august.setter
    def august(self, august):
        """Sets the august of this MonthsOfYearSelector.


        :param august: The august of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._august = august

    @property
    def september(self):
        """Gets the september of this MonthsOfYearSelector.  # noqa: E501


        :return: The september of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._september

    @september.setter
    def september(self, september):
        """Sets the september of this MonthsOfYearSelector.


        :param september: The september of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._september = september

    @property
    def october(self):
        """Gets the october of this MonthsOfYearSelector.  # noqa: E501


        :return: The october of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._october

    @october.setter
    def october(self, october):
        """Sets the october of this MonthsOfYearSelector.


        :param october: The october of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._october = october

    @property
    def november(self):
        """Gets the november of this MonthsOfYearSelector.  # noqa: E501


        :return: The november of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._november

    @november.setter
    def november(self, november):
        """Sets the november of this MonthsOfYearSelector.


        :param november: The november of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._november = november

    @property
    def december(self):
        """Gets the december of this MonthsOfYearSelector.  # noqa: E501


        :return: The december of this MonthsOfYearSelector.  # noqa: E501
        :rtype: bool
        """
        return self._december

    @december.setter
    def december(self, december):
        """Sets the december of this MonthsOfYearSelector.


        :param december: The december of this MonthsOfYearSelector.  # noqa: E501
        :type: bool
        """

        self._december = december

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
        if issubclass(MonthsOfYearSelector, dict):
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
        if not isinstance(other, MonthsOfYearSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MonthsOfYearSelector):
            return True

        return self.to_dict() != other.to_dict()
