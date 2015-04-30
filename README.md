# Some ReST examples with Service Now
#
# Notice that you'll need to have a ServiceNow instance, against which to test.  Mine was generously loaned by ServiceNow's
#        MJones (Thank you; thank you).
#
# I used a library called requests (see import requests), but this will also work with urllib3 (contained in Python 2.7 onward)
# The files included are:
# 1 - SNowIncidentGetMultiple.py, gets the first 10 incidents
# 2 - sNowIncidentCreate.py, puts the Text from the commandline into an unassigned incident-record.  
# 3 - Given the sysid from the incident created in #2, above, get and display that information.
#
