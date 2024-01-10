---
layout: default
title: Welcome to NumInsight!
---

# Welcome to NumInsight!

NumInsight is a powerful tool that allows you to query phone numbers. It's easy to use and highly customizable.

## Usage

To use NumInsight, simply run the following command:

```bash
python3 main.py [options]
```

Here are the options you can use:

- `-h, --help`: Show this help message and exit
- `-n NUBER, --nuber NUBER`: Phone number to check
- `-H, --head`: Headless mode
- `--driver DRIVER`: Driver to use (chrome, firefox)
- `--json`: Output as json

## Scripting with NumInsight

NumInsight allows for Lua scripting to automate the process of querying phone numbers. You can create a script in the `scripts` directory with the following syntax:

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

The Lua API has access to all highlenium functions, and some additional functions:
* `meta_get(key)` : get a meta value
* `meta_return(value)` : return a value to the main script

We hope you enjoy using NumInsight!
