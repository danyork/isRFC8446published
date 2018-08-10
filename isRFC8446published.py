#!/usr/bin/env python

# Incredibly basic script to test if an RFC has been published yet and display the associated HTML code.

import urllib2

try:
    response = urllib2.urlopen('https://www.rfc-editor.org/rfc/rfc8446.txt')
    print "got the site"
    print """
<html>
<head>
<title>Is RFC 8446 Published?</title>
</head>
<body style="background:green;">
<p style="font-size:200pt;text-align:center;padding-top:50px;"><a href="https://www.rfc-editor.org/rfc/rfc8446.txt">YES!</a></p>
</body>
</html>
"""
except:
    print """
<html>
<head>
<title>Is RFC 8446 Published?</title>
</head>
<body style="background:red;">
<p style="font-size:200pt;text-align:center;padding-top:50px;">NO</p>
<p style="text-align:center;"><a href="https://www.rfc-editor.org/auth48/rfc8446">See current status</a></p>
</body>
</html>
"""
