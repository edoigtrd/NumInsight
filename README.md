[![Windows](https://badgen.net/badge/icon/windows?icon=windows&label)](https://microsoft.com/windows/) ![Linux](https://img.shields.io/badge/Linux-FCC624.svg?style=for-the-badge&logo=Linux&logoColor=black) ![Issues](https://img.shields.io/github/issues/edoigtrd/NumInsight.svg) ![Action](https://github.com/edoigtrd/NumInsight/actions/workflows/main.yml/badge.svg
)


# NumInsight

Numinsight is a HoleHe like project to query information about a phone number.

## Usage

You can run the script from the command line with the following syntax:

    ```bash
    python3 main.py [options]
    ```

Options:

- `-h, --help`: Show this help message and exit
- `-n NUBER, --nuber NUBER`: Phone number to check
- `-H, --head`: Headless mode
- `--driver DRIVER`: Driver to use (chrome, firefox)
- `--json`: Output as json

## Scripting 

NumInsight aims to allow lua scripting to automate the process of querying phone numbers.

To add a script, create a file in the `scripts` directory with the following syntax:

A one line json header should be created to define the script name :


```lua
{"meta_name":"Amazon"}

browseto("https://www.amazon.fr/")
clickon("#nav-link-accountList-nav-line-1")
fill("#ap_email", meta_get("number"))
clickon("#continue")

if checkfor("#auth-error-message-box > div > h4") then
    meta_return(false)
else
    meta_return(true)
end
```
*This scipt is the litteral translation of the amazon app script*

Lua API has access to all highlenium functions, and some additional functions:
* `meta_get(key)` : get a meta value
* `meta_return(value)` : return a value to the main script

