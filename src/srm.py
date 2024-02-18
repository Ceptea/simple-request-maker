import requests
import argparse as ap
from rich import print

parser = ap.ArgumentParser("req", "-u <url> -d <data>", description="Make requests!")

parser.add_argument("-u", "-url")
parser.add_argument("-d", "-data")
parser.add_argument("-j", "-json")
parser.add_argument("-v", "-verbose", action="store_true")
args = parser.parse_args()
if not args.u:

    parser.print_usage()
    print("[red]You didnt provide a url.")
    exit()
try:

    if not args.u.startswith("http"):
        args.u = f"https://{args.u}"
    if args.d:
        response = requests.post(args.u, data=args.d)
    elif args.j:
        response = requests.post(args.u, data=args.d)
    else:
        response = requests.get(args.u)
except requests.exceptions.ConnectionError:
    print("[red]Failed to connect to that site, Does it exist?")

    exit(-1)


def getresponse(res):
    c = []
    try:
        c.append(res.json())
    except Exception:
        c.append(res.text)
    if args.v == True:
        c.append(f"[{res.status_code}]")
    if len(c) == 1:
        return c[0]
    else:
        return " ".join(c)


print(getresponse(response))
