# copyright 2017 jinyaoMa

from urllib import request as req
import re

class PhoneExtracter(object):
    __phoneRegex = []
    __url = ""

    '''
    # Initialize PhoneExtracter
    # @param urlAddress - web address e.g "http://www.bilibili.com/html/contact.html"
    # @param phoneFormat - list of regular expressions for phone number searching e.g ["\d{3}-\d{3}-\d{4}", "\(\d{3}\) *\d{3}-\d{4}"]
    '''
    def __init__(self, urlAddress="http://www.bilibili.com/html/contact.html", phoneFormat=["\d{3}-\d{3}-\d{4}", "\(\d{3}\) *\d{3}-\d{4}"]):
        self.__url = urlAddress
        self.__phoneRegex = phoneFormat

    '''
    # Extract a list of phone numbers that match the regex
    # @return listOfPhones - list of phone numbers
    '''
    def extract(self):
        cnt = req.Request(self.__url)
        listOfPhones = []
        page = req.urlopen(cnt)
        data = page.read().decode("utf-8")
        for phoneFormat in self.__phoneRegex:
            listOfPhones.extend(re.findall(phoneFormat, data))
        return listOfPhones
