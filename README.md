# Python
small tools in python

1. class VCodeGenerator (use PIL) - to generate a verification code image
  # constructor
  # all three params optional, default:
  # fontPath='C:\Windows\Fonts\Arial.ttf',
  # numOfChars=4，
  # height=64
  VCodeGenerator(fontPath,numOfChar,height)
  
  # generate verification code image to current directory
  # return verification code
  string generate()
  
  
2. class PhoneExtracter (use urllib) - to extract phone numbers from webpage
  # constructor
  # all two params optional, default: 
  # urlAddress=["http://www.bilibili.com/html/contact.html", "https://www.mohawkcollege.ca/about-mohawk/contact-mohawk"],
  # phoneFormat=["\d{3}-\d{3}-\d{4}", "\(\d{3}\) *\d{3}-\d{4}"]
  PhoneExtracter(urlAddress,phoneFormat)
  
  # extract phone numbers from webpages
  # return list of phone numbers
  string{} extract()
