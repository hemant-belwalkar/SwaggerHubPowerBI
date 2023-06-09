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


class Comment(object):
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
        'id': 'str',
        'item_id': 'str',
        'user_name': 'str',
        'thread_id': 'str',
        'attachment_path': 'str',
        'text': 'str',
        'created_date': 'datetime',
        'modified_date': 'datetime'
    }

    attribute_map = {
        'id': 'Id',
        'item_id': 'ItemId',
        'user_name': 'UserName',
        'thread_id': 'ThreadId',
        'attachment_path': 'AttachmentPath',
        'text': 'Text',
        'created_date': 'CreatedDate',
        'modified_date': 'ModifiedDate'
    }

    def __init__(self, id=None, item_id=None, user_name=None, thread_id=None, attachment_path=None, text=None, created_date=None, modified_date=None, _configuration=None):  # noqa: E501
        """Comment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._item_id = None
        self._user_name = None
        self._thread_id = None
        self._attachment_path = None
        self._text = None
        self._created_date = None
        self._modified_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if item_id is not None:
            self.item_id = item_id
        if user_name is not None:
            self.user_name = user_name
        if thread_id is not None:
            self.thread_id = thread_id
        if attachment_path is not None:
            self.attachment_path = attachment_path
        if text is not None:
            self.text = text
        if created_date is not None:
            self.created_date = created_date
        if modified_date is not None:
            self.modified_date = modified_date

    @property
    def id(self):
        """Gets the id of this Comment.  # noqa: E501

        A unique UUID value that specifies the identifier of the comment.  # noqa: E501

        :return: The id of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comment.

        A unique UUID value that specifies the identifier of the comment.  # noqa: E501

        :param id: The id of this Comment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def item_id(self):
        """Gets the item_id of this Comment.  # noqa: E501

        A unique UUID value that specifies the identifier of the CatalogItem item to which the comment is attached.  # noqa: E501

        :return: The item_id of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this Comment.

        A unique UUID value that specifies the identifier of the CatalogItem item to which the comment is attached.  # noqa: E501

        :param item_id: The item_id of this Comment.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def user_name(self):
        """Gets the user_name of this Comment.  # noqa: E501

         A string value that represents the user who created the comment item.  # noqa: E501

        :return: The user_name of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this Comment.

         A string value that represents the user who created the comment item.  # noqa: E501

        :param user_name: The user_name of this Comment.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def thread_id(self):
        """Gets the thread_id of this Comment.  # noqa: E501

        A unique UUID value that specifies the identifier of the thread of the comment. A comment thread can be used to group comments that are a response to one another in one grouping.  # noqa: E501

        :return: The thread_id of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        """Sets the thread_id of this Comment.

        A unique UUID value that specifies the identifier of the thread of the comment. A comment thread can be used to group comments that are a response to one another in one grouping.  # noqa: E501

        :param thread_id: The thread_id of this Comment.  # noqa: E501
        :type: str
        """

        self._thread_id = thread_id

    @property
    def attachment_path(self):
        """Gets the attachment_path of this Comment.  # noqa: E501

        A string value that specifies the server path to an attachment that is part of the comment.  # noqa: E501

        :return: The attachment_path of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._attachment_path

    @attachment_path.setter
    def attachment_path(self, attachment_path):
        """Sets the attachment_path of this Comment.

        A string value that specifies the server path to an attachment that is part of the comment.  # noqa: E501

        :param attachment_path: The attachment_path of this Comment.  # noqa: E501
        :type: str
        """

        self._attachment_path = attachment_path

    @property
    def text(self):
        """Gets the text of this Comment.  # noqa: E501

        A string value that contains the text of the comment.  # noqa: E501

        :return: The text of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Comment.

        A string value that contains the text of the comment.  # noqa: E501

        :param text: The text of this Comment.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def created_date(self):
        """Gets the created_date of this Comment.  # noqa: E501

        A string that contains the date-time of the creation of the comment.  # noqa: E501

        :return: The created_date of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Comment.

        A string that contains the date-time of the creation of the comment.  # noqa: E501

        :param created_date: The created_date of this Comment.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def modified_date(self):
        """Gets the modified_date of this Comment.  # noqa: E501

        A string value that contains the date-time of the last modification to the comment.  # noqa: E501

        :return: The modified_date of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this Comment.

        A string value that contains the date-time of the last modification to the comment.  # noqa: E501

        :param modified_date: The modified_date of this Comment.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

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
        if issubclass(Comment, dict):
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
        if not isinstance(other, Comment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Comment):
            return True

        return self.to_dict() != other.to_dict()
