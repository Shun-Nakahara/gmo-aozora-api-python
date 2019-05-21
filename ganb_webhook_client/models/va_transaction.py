# coding: utf-8

"""
    GMO Aozora Net Bank Open API

    <p>Ph2.5向けに作成したもの</p>   # noqa: E501

    OpenAPI spec version: 1.1.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VaTransaction(object):
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
        'va_id': 'str',
        'transaction_date': 'str',
        'value_date': 'str',
        'va_branch_code': 'str',
        'va_branch_name_kana': 'str',
        'va_account_number': 'str',
        'va_account_name_kana': 'str',
        'deposit_amount': 'str',
        'remitter_name_kana': 'str',
        'payment_bank_name': 'str',
        'payment_branch_name': 'str',
        'partner_name': 'str',
        'remarks': 'str',
        'item_key': 'str'
    }

    attribute_map = {
        'va_id': 'vaId',
        'transaction_date': 'transactionDate',
        'value_date': 'valueDate',
        'va_branch_code': 'vaBranchCode',
        'va_branch_name_kana': 'vaBranchNameKana',
        'va_account_number': 'vaAccountNumber',
        'va_account_name_kana': 'vaAccountNameKana',
        'deposit_amount': 'depositAmount',
        'remitter_name_kana': 'remitterNameKana',
        'payment_bank_name': 'paymentBankName',
        'payment_branch_name': 'paymentBranchName',
        'partner_name': 'partnerName',
        'remarks': 'remarks',
        'item_key': 'itemKey'
    }

    def __init__(self, va_id=None, transaction_date=None, value_date=None, va_branch_code=None, va_branch_name_kana=None, va_account_number=None, va_account_name_kana=None, deposit_amount=None, remitter_name_kana=None, payment_bank_name=None, payment_branch_name=None, partner_name=None, remarks=None, item_key=None):  # noqa: E501
        """VaTransaction - a model defined in Swagger"""  # noqa: E501

        self._va_id = None
        self._transaction_date = None
        self._value_date = None
        self._va_branch_code = None
        self._va_branch_name_kana = None
        self._va_account_number = None
        self._va_account_name_kana = None
        self._deposit_amount = None
        self._remitter_name_kana = None
        self._payment_bank_name = None
        self._payment_branch_name = None
        self._partner_name = None
        self._remarks = None
        self._item_key = None
        self.discriminator = None

        self.va_id = va_id
        self.transaction_date = transaction_date
        self.value_date = value_date
        self.va_branch_code = va_branch_code
        self.va_branch_name_kana = va_branch_name_kana
        self.va_account_number = va_account_number
        self.va_account_name_kana = va_account_name_kana
        self.deposit_amount = deposit_amount
        self.remitter_name_kana = remitter_name_kana
        self.payment_bank_name = payment_bank_name
        self.payment_branch_name = payment_branch_name
        self.partner_name = partner_name
        if remarks is not None:
            self.remarks = remarks
        self.item_key = item_key

    @property
    def va_id(self):
        """Gets the va_id of this VaTransaction.  # noqa: E501

        振込入金口座ID 半角数字 振込入金口座を識別するID   # noqa: E501

        :return: The va_id of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._va_id

    @va_id.setter
    def va_id(self, va_id):
        """Sets the va_id of this VaTransaction.

        振込入金口座ID 半角数字 振込入金口座を識別するID   # noqa: E501

        :param va_id: The va_id of this VaTransaction.  # noqa: E501
        :type: str
        """
        if va_id is None:
            raise ValueError("Invalid value for `va_id`, must not be `None`")  # noqa: E501
        if va_id is not None and len(va_id) > 10:
            raise ValueError("Invalid value for `va_id`, length must be less than or equal to `10`")  # noqa: E501
        if va_id is not None and len(va_id) < 10:
            raise ValueError("Invalid value for `va_id`, length must be greater than or equal to `10`")  # noqa: E501

        self._va_id = va_id

    @property
    def transaction_date(self):
        """Gets the transaction_date of this VaTransaction.  # noqa: E501

        取引日 半角文字 YYYY-MM-DD形式   # noqa: E501

        :return: The transaction_date of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this VaTransaction.

        取引日 半角文字 YYYY-MM-DD形式   # noqa: E501

        :param transaction_date: The transaction_date of this VaTransaction.  # noqa: E501
        :type: str
        """
        if transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501
        if transaction_date is not None and len(transaction_date) > 10:
            raise ValueError("Invalid value for `transaction_date`, length must be less than or equal to `10`")  # noqa: E501
        if transaction_date is not None and len(transaction_date) < 10:
            raise ValueError("Invalid value for `transaction_date`, length must be greater than or equal to `10`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def value_date(self):
        """Gets the value_date of this VaTransaction.  # noqa: E501

        起算日 半角文字 YYYY-MM-DD形式   # noqa: E501

        :return: The value_date of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._value_date

    @value_date.setter
    def value_date(self, value_date):
        """Sets the value_date of this VaTransaction.

        起算日 半角文字 YYYY-MM-DD形式   # noqa: E501

        :param value_date: The value_date of this VaTransaction.  # noqa: E501
        :type: str
        """
        if value_date is None:
            raise ValueError("Invalid value for `value_date`, must not be `None`")  # noqa: E501
        if value_date is not None and len(value_date) > 10:
            raise ValueError("Invalid value for `value_date`, length must be less than or equal to `10`")  # noqa: E501
        if value_date is not None and len(value_date) < 10:
            raise ValueError("Invalid value for `value_date`, length must be greater than or equal to `10`")  # noqa: E501

        self._value_date = value_date

    @property
    def va_branch_code(self):
        """Gets the va_branch_code of this VaTransaction.  # noqa: E501

        支店コード 半角数字   # noqa: E501

        :return: The va_branch_code of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._va_branch_code

    @va_branch_code.setter
    def va_branch_code(self, va_branch_code):
        """Sets the va_branch_code of this VaTransaction.

        支店コード 半角数字   # noqa: E501

        :param va_branch_code: The va_branch_code of this VaTransaction.  # noqa: E501
        :type: str
        """
        if va_branch_code is None:
            raise ValueError("Invalid value for `va_branch_code`, must not be `None`")  # noqa: E501
        if va_branch_code is not None and len(va_branch_code) > 3:
            raise ValueError("Invalid value for `va_branch_code`, length must be less than or equal to `3`")  # noqa: E501
        if va_branch_code is not None and len(va_branch_code) < 3:
            raise ValueError("Invalid value for `va_branch_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._va_branch_code = va_branch_code

    @property
    def va_branch_name_kana(self):
        """Gets the va_branch_name_kana of this VaTransaction.  # noqa: E501

        支店名カナ 半角文字   # noqa: E501

        :return: The va_branch_name_kana of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._va_branch_name_kana

    @va_branch_name_kana.setter
    def va_branch_name_kana(self, va_branch_name_kana):
        """Sets the va_branch_name_kana of this VaTransaction.

        支店名カナ 半角文字   # noqa: E501

        :param va_branch_name_kana: The va_branch_name_kana of this VaTransaction.  # noqa: E501
        :type: str
        """
        if va_branch_name_kana is None:
            raise ValueError("Invalid value for `va_branch_name_kana`, must not be `None`")  # noqa: E501
        if va_branch_name_kana is not None and len(va_branch_name_kana) > 15:
            raise ValueError("Invalid value for `va_branch_name_kana`, length must be less than or equal to `15`")  # noqa: E501
        if va_branch_name_kana is not None and len(va_branch_name_kana) < 1:
            raise ValueError("Invalid value for `va_branch_name_kana`, length must be greater than or equal to `1`")  # noqa: E501

        self._va_branch_name_kana = va_branch_name_kana

    @property
    def va_account_number(self):
        """Gets the va_account_number of this VaTransaction.  # noqa: E501

        口座番号 半角数字   # noqa: E501

        :return: The va_account_number of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._va_account_number

    @va_account_number.setter
    def va_account_number(self, va_account_number):
        """Sets the va_account_number of this VaTransaction.

        口座番号 半角数字   # noqa: E501

        :param va_account_number: The va_account_number of this VaTransaction.  # noqa: E501
        :type: str
        """
        if va_account_number is None:
            raise ValueError("Invalid value for `va_account_number`, must not be `None`")  # noqa: E501
        if va_account_number is not None and len(va_account_number) > 7:
            raise ValueError("Invalid value for `va_account_number`, length must be less than or equal to `7`")  # noqa: E501
        if va_account_number is not None and len(va_account_number) < 7:
            raise ValueError("Invalid value for `va_account_number`, length must be greater than or equal to `7`")  # noqa: E501

        self._va_account_number = va_account_number

    @property
    def va_account_name_kana(self):
        """Gets the va_account_name_kana of this VaTransaction.  # noqa: E501

        口座名義カナ 半角文字   # noqa: E501

        :return: The va_account_name_kana of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._va_account_name_kana

    @va_account_name_kana.setter
    def va_account_name_kana(self, va_account_name_kana):
        """Sets the va_account_name_kana of this VaTransaction.

        口座名義カナ 半角文字   # noqa: E501

        :param va_account_name_kana: The va_account_name_kana of this VaTransaction.  # noqa: E501
        :type: str
        """
        if va_account_name_kana is None:
            raise ValueError("Invalid value for `va_account_name_kana`, must not be `None`")  # noqa: E501
        if va_account_name_kana is not None and len(va_account_name_kana) > 40:
            raise ValueError("Invalid value for `va_account_name_kana`, length must be less than or equal to `40`")  # noqa: E501
        if va_account_name_kana is not None and len(va_account_name_kana) < 1:
            raise ValueError("Invalid value for `va_account_name_kana`, length must be greater than or equal to `1`")  # noqa: E501

        self._va_account_name_kana = va_account_name_kana

    @property
    def deposit_amount(self):
        """Gets the deposit_amount of this VaTransaction.  # noqa: E501

        入金金額 半角数字   # noqa: E501

        :return: The deposit_amount of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, deposit_amount):
        """Sets the deposit_amount of this VaTransaction.

        入金金額 半角数字   # noqa: E501

        :param deposit_amount: The deposit_amount of this VaTransaction.  # noqa: E501
        :type: str
        """
        if deposit_amount is None:
            raise ValueError("Invalid value for `deposit_amount`, must not be `None`")  # noqa: E501
        if deposit_amount is not None and len(deposit_amount) > 20:
            raise ValueError("Invalid value for `deposit_amount`, length must be less than or equal to `20`")  # noqa: E501
        if deposit_amount is not None and len(deposit_amount) < 1:
            raise ValueError("Invalid value for `deposit_amount`, length must be greater than or equal to `1`")  # noqa: E501

        self._deposit_amount = deposit_amount

    @property
    def remitter_name_kana(self):
        """Gets the remitter_name_kana of this VaTransaction.  # noqa: E501

        振込依頼人名カナ 半角文字   # noqa: E501

        :return: The remitter_name_kana of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._remitter_name_kana

    @remitter_name_kana.setter
    def remitter_name_kana(self, remitter_name_kana):
        """Sets the remitter_name_kana of this VaTransaction.

        振込依頼人名カナ 半角文字   # noqa: E501

        :param remitter_name_kana: The remitter_name_kana of this VaTransaction.  # noqa: E501
        :type: str
        """
        if remitter_name_kana is None:
            raise ValueError("Invalid value for `remitter_name_kana`, must not be `None`")  # noqa: E501
        if remitter_name_kana is not None and len(remitter_name_kana) > 48:
            raise ValueError("Invalid value for `remitter_name_kana`, length must be less than or equal to `48`")  # noqa: E501
        if remitter_name_kana is not None and len(remitter_name_kana) < 1:
            raise ValueError("Invalid value for `remitter_name_kana`, length must be greater than or equal to `1`")  # noqa: E501

        self._remitter_name_kana = remitter_name_kana

    @property
    def payment_bank_name(self):
        """Gets the payment_bank_name of this VaTransaction.  # noqa: E501

        仕向金融機関名カナ 半角文字   # noqa: E501

        :return: The payment_bank_name of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payment_bank_name

    @payment_bank_name.setter
    def payment_bank_name(self, payment_bank_name):
        """Sets the payment_bank_name of this VaTransaction.

        仕向金融機関名カナ 半角文字   # noqa: E501

        :param payment_bank_name: The payment_bank_name of this VaTransaction.  # noqa: E501
        :type: str
        """
        if payment_bank_name is None:
            raise ValueError("Invalid value for `payment_bank_name`, must not be `None`")  # noqa: E501
        if payment_bank_name is not None and len(payment_bank_name) > 30:
            raise ValueError("Invalid value for `payment_bank_name`, length must be less than or equal to `30`")  # noqa: E501
        if payment_bank_name is not None and len(payment_bank_name) < 1:
            raise ValueError("Invalid value for `payment_bank_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._payment_bank_name = payment_bank_name

    @property
    def payment_branch_name(self):
        """Gets the payment_branch_name of this VaTransaction.  # noqa: E501

        仕向支店名カナ 半角文字   # noqa: E501

        :return: The payment_branch_name of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payment_branch_name

    @payment_branch_name.setter
    def payment_branch_name(self, payment_branch_name):
        """Sets the payment_branch_name of this VaTransaction.

        仕向支店名カナ 半角文字   # noqa: E501

        :param payment_branch_name: The payment_branch_name of this VaTransaction.  # noqa: E501
        :type: str
        """
        if payment_branch_name is None:
            raise ValueError("Invalid value for `payment_branch_name`, must not be `None`")  # noqa: E501
        if payment_branch_name is not None and len(payment_branch_name) > 15:
            raise ValueError("Invalid value for `payment_branch_name`, length must be less than or equal to `15`")  # noqa: E501
        if payment_branch_name is not None and len(payment_branch_name) < 1:
            raise ValueError("Invalid value for `payment_branch_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._payment_branch_name = payment_branch_name

    @property
    def partner_name(self):
        """Gets the partner_name of this VaTransaction.  # noqa: E501

        サービス企業名 全角文字 振込入金口座契約サービス企業名   # noqa: E501

        :return: The partner_name of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._partner_name

    @partner_name.setter
    def partner_name(self, partner_name):
        """Sets the partner_name of this VaTransaction.

        サービス企業名 全角文字 振込入金口座契約サービス企業名   # noqa: E501

        :param partner_name: The partner_name of this VaTransaction.  # noqa: E501
        :type: str
        """
        if partner_name is None:
            raise ValueError("Invalid value for `partner_name`, must not be `None`")  # noqa: E501
        if partner_name is not None and len(partner_name) > 10:
            raise ValueError("Invalid value for `partner_name`, length must be less than or equal to `10`")  # noqa: E501
        if partner_name is not None and len(partner_name) < 1:
            raise ValueError("Invalid value for `partner_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._partner_name = partner_name

    @property
    def remarks(self):
        """Gets the remarks of this VaTransaction.  # noqa: E501

        摘要内容 全半角文字 該当データがない場合は項目自体を設定しません   # noqa: E501

        :return: The remarks of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this VaTransaction.

        摘要内容 全半角文字 該当データがない場合は項目自体を設定しません   # noqa: E501

        :param remarks: The remarks of this VaTransaction.  # noqa: E501
        :type: str
        """
        if remarks is not None and len(remarks) > 255:
            raise ValueError("Invalid value for `remarks`, length must be less than or equal to `255`")  # noqa: E501
        if remarks is not None and len(remarks) < 1:
            raise ValueError("Invalid value for `remarks`, length must be greater than or equal to `1`")  # noqa: E501

        self._remarks = remarks

    @property
    def item_key(self):
        """Gets the item_key of this VaTransaction.  # noqa: E501

        明細キー 半角数字 口座ID毎に設定される明細キー（明細データtimestamp（μs））  # noqa: E501

        :return: The item_key of this VaTransaction.  # noqa: E501
        :rtype: str
        """
        return self._item_key

    @item_key.setter
    def item_key(self, item_key):
        """Sets the item_key of this VaTransaction.

        明細キー 半角数字 口座ID毎に設定される明細キー（明細データtimestamp（μs））  # noqa: E501

        :param item_key: The item_key of this VaTransaction.  # noqa: E501
        :type: str
        """
        if item_key is None:
            raise ValueError("Invalid value for `item_key`, must not be `None`")  # noqa: E501
        if item_key is not None and len(item_key) > 24:
            raise ValueError("Invalid value for `item_key`, length must be less than or equal to `24`")  # noqa: E501
        if item_key is not None and len(item_key) < 1:
            raise ValueError("Invalid value for `item_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._item_key = item_key

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
        if issubclass(VaTransaction, dict):
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
        if not isinstance(other, VaTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other