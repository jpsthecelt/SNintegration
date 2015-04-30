
# AUTHOR: Created by John Singer, 4.13.15
# Any usage must include giving credit to the above author,
# but there is no warranty, express or implied for the use of this code.
#
#  If problems are encountered, your 'best bet' is to ask for help
# on the bigfix forum (http://forum.bigfix.com).
#
import sys
import requests
from argparse import ArgumentParser

usage = """sNowIncidentGetMultiple.py [options]

Get ServiceNow Incident information, based on commandline

Options:
  --user USERNAME             IEM console-login USERNAME
                               (no default)
  --password PASSWORD         IEM console-login PASSWORD for above user
                               (no default)
  -h, --help                   Print this help message and exit


Examples:

    sNowIncidentGetMultiple -u Admin -p Password

"""
el = ''

if __name__ == '__main__':
    try:
        parser = ArgumentParser(add_help=False, usage=usage)

        parser.add_argument('-u', '--user')
        parser.add_argument('-p', '--password')

        if '-h' in sys.argv or '--help' in sys.argv:
          print(usage)
          exit()

        args = parser.parse_args()

        if args.user: user = args.user
        if args.password: password = args.password

# Now, try 'tapping into' the ServiceNow instance
        snUrlBase = 'https://mjones1.service-now.com'

        headers = {"Accept":"application/json"}
        r = requests.get(snUrlBase+'/api/now/table/incident?sysparm_limit=10',auth=(user,password),headers=headers)

        if r.status_code != 200:
            print('sNowIncidentGetinfo ERROR -- Status: ', r.status_code, 'Headers:', r.headers, 'Error Response:', r.json())
            exit()

        else:
            print('Status:', r.status_code, 'Headers:', r.headers, 'Response:', r.json())
            print('Cookies:', r.cookies)
            print('\nAnd now; the first 10 ServciceNow records...')
            for record in r.json()['result']:
                print ('\n', record)

# Handle any exceptions, printing out error code
    except SystemExit:
        pass
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        print("\n")

