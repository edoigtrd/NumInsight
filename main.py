import argparse
import highlenium
from apps import apps
import colorama
import json

def print_result(apps) :
    colorama.init()
    for i in apps :
        if type(apps[i]) == bool :
            if apps[i] :
                print(f"{colorama.Fore.GREEN}[✓] : {i}")
            else :
                print(f"{colorama.Fore.RED}[𐄂] : {i}")
        else :
            print(f"{colorama.Fore.MAGENTA}[!] : {i}")

def get_result_json(results) :
    r = {}
    for k,v in results.items():
        if type(v) == bool :
            r[k] = v
        else :
            r[k] = "Exception"
    return json.dumps(r, indent=4)

if __name__ == "__main__" :
    ap = argparse.ArgumentParser()
    ap.add_argument("-n","--nuber", type=str, default="", help="Phone nuumber to check")
    ap.add_argument("-H", "--head", action="store_true", default=False, help="Headless mode")
    ap.add_argument("--driver", type=str, default="chrome", help="Driver to use (chrome, firefox)")
    ap.add_argument("--json", action="store_true", default=False, help="Output as json")
    args = vars(ap.parse_args())

    params = {
        "number": args["nuber"]
    }

    highlenium.get_driver(args["driver"])
    apps.set_params(params)
    results = apps.run()
    if not args["json"] :
        print_result(results)
    else :
        print(get_result_json(results))



    