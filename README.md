# SSRFHunter

## Overview

This is a simple tool designed to help test and identify potential SSRF (Server-Side Request Forgery) vulnerabilities. It works by testing the target application for any URLs that may be vulnerable to SSRF attacks. By detecting these vulnerabilities, the tool can assist developers and security researchers in identifying and mitigating potential threats to the target application.


## Contribution
Please feel free to contribute as it will be highly appreciated

## Install prerequisites

This tool requires Python 3 to run. If you don't have Python 3 installed on your system, you can download it from the official Python website:  https://www.python.org/downloads/
 
## Clone the repo
    git clone https://github.com/not1cyyy/SSRFHunter.git

## Run the package
Change current directory into the SSRFHunter directory : 

    cd SSRFHunter

Then use the tool with :

    python3 main.py [flag]


| **Flag** | Description|
| -------------------------------------- | ---------------------------------------------- |
| **-u**  | Used to specify the target **URL** for scanning. The tool will use the given URL as the starting point to search for potential SSRF vulnerabilities. |
| **-m**  | Used to define the **HTTP method** to use for the request being sent to the target URL. Examples to be entered are POST and GET ...  |
| **-t**  | Used to set the number of **threads** to use when scanning the target URL (parallel processing or concurrency). The input should be a number.  |
| **-c**  | Used to specify **CUSTOM_PAYLOADS** to be injected into the target URL to test for potential SSRF vulnerabilities.  |


