# AUTHOR: Created by John Singer, 4.13.15
# Any usage must include giving credit to the above author,
# but there is no warranty, express or implied for the use of this code.
#
#  If problems are encountered, your 'best bet' is to ask for help
# on the bigfix forum (http://forum.bigfix.com).
#

import sys
import json
import requests
from argparse import ArgumentParser

usage = """sNowIncidentCreate.py "problem description" [options]

Options:
  --user USERNAME             IEM console-login USERNAME
                               (no default)
  --password PASSWORD         IEM console-login PASSWORD for above user
                               (no default)
  -h, --help                   Print this help message and exit

Examples:
  Creates a new incident with the problem-description indicated on the command-line;
        outputs sys_id of the created incident

  uses indicated service-now username & password

    sNowIncidentCreate "problem description" -u adminMO -p adminmo

"""

# When invoked as the main program, take the command-line parameters & create a new ServiceNow Incident-Record
if __name__ == '__main__':
    try:
        parser = ArgumentParser(add_help=False, usage=usage)

        parser.add_argument('incident_desc')
        parser.add_argument('-u', '--user')
        parser.add_argument('-p', '--password')


        if '-h' in sys.argv or '--help' in sys.argv:
          print(usage)
          exit()

        args = parser.parse_args()

        if args.incident_desc == None:
            exit(status=0)
        incident_desc = args.incident_desc

        if args.user: user = args.user
        if args.password: password = args.password


# Now, try 'tapping into' the ServiceNow instance
        snUrlBase = 'https://mjones1.service-now.com'

        headers = {"Content-Type":"application/json", "Accept":"application/json"}
        description = '{"short_description":"'+incident_desc+'"}'
        r = requests.post(snUrlBase+'/api/now/v1/table/incident',auth=(user,password),headers=headers, data=description)

        if r.status_code != 201:
            print('sNowIncidentGetinfo ERROR -- Status: ', r.status_code, 'Headers:', r.headers, 'Error Response:', r.json())
            exit()
        else:
#            print('Status:', r.status_code, 'Headers:', r.headers, 'Response:', r.json())
#            print('Cookies:', r.cookies)
            dct = json.loads(r.text)
            print "\nCreated Incident-Record {0} with SysID: {1}".format(dct['result']['number'], dct['result']['sys_id'])
            print "\n (referencable URL is: %s)" % dct['result']['opened_by']['link']


# Handle any exceptions, printing out error code
    except SystemExit:
        pass
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        print("\n")
