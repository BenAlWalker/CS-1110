# Ben Walker, baw3hg
import re

nospace = re.compile(r'[\S]+')
quotation = re.compile(r'"\S+[^"]*\S+"')
twonum = re.compile(r'([-]?[0-9]+\.?[0-9]*)[,]? ?([-]?[0-9]+\.?[0-9]*)')
