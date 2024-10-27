A python and bash script that explains basic file handling and cronjobs on a Debian based system.

Generates a file with data from an external list and sum up specific data from that file that was generated. Time the execution of scripts with the cronjob service daemon.

The value this this tool should put out is an EXAMPLE on how a beginner can turn an idea in his head to materialized functioning code. The script might seem simple, but for a beginner like me that learns from the web it means quit a lot. Let me show you how!

- At the beginning of my journey in IT I had so much frustration, because I just could not see any results or proof that I actually understood what I was trying to learn. No I can see the light at the end of the tunnel and I feel much more MOTIVATION.

- About 3 month into python and Linux I head a thought in my head, that I could not write down or even verbalize, but now that thought became a real script. That thought is now MATERIALIZED.

- The potential of python and it's modules (e. g. pandas for data analyses) seems now so clear to me. 
Collecting data, processing data, data comparison, machine learning and building neural nets are a fantastic way to improve the efficiency of a company or their resources in action.

- Now that I made this simple little script work, a whole new real of imagination and realization has opened up it's gates in front of me and I can see how much is possible with automation and scripting in combination with MEANINGFUL data.

Visualization / diagram / video will follow

This tool is written on Debian and should work with other Linux distributions as well. But not yet tested.

To install just copy the folder shop_report to your drive make the bash (daily_income_report) and py (generate_order.py) files executable and run them timed with crontab.

Set up crontab with terminal:
"crontab -e" runs the cronjob editor. If you never ran crontab before, you will be asked to chose a editor to edit your crontab daemon. Basically a service running in the background. You can check it's activity state with "systemctl status cron". Might be crontab instead of cron on other distributions. "man crontab" and "man 5 crontab" especially man 5 give you very detailed information about the service and how to set the timer. Also try "man cron".
 
The lines for running these files with cron could look like this:
"*/15 * * * * /usr/bin/python3 /home/user/path/to/file/generate_order.py"
to generate an order every 15 minutes
"15 12 * * * /usr/bin/env bash /home/user/path/to/file/daily_income_report" no quotes ;)
To sum up the 'income' daily. Instead of the 5-digit syntax it is possible to just wright "@daily".

generate_order.py:
Generates a txt-file that randomly assembles the order picking a list entry from product_list.py
The content looks like this (order_2024-10-27_18-59-38.txt):
productname: T-Shirt
price: 20
date_recieved: 2024-10-27_18-59-38

daily_income_report(bashfile):
This greps the word after price: with a for loop, creating list of all the product prices of that day as a txt-file called "price_sum_2024-10-18-12-15-00.txt". After that it sums them up and writes them to another txt-file, called "daily_income_2024-10-18-12-15-00.txt"

After trying the scripts, remember to comment out the commands in the crontab or deactivate the daemon.
Otherwise it keeps writing data to your drive. 

There is also an alternative product_list.py that handles the access of the list items a bit more smoothly, but
my next script (csv_report) is the actual 'gamechanger'^^ LOL

How to tweak this project for your own uses?
Since this is an example project, I'd encourage you to clone and rename it to use it for you own purpose.

Found a bug?
The code is not debugged, because the script is not used in the wild, but I might consider working on common errors that might occur. If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to submit a PR with a fix, reference the issue you created!

Known issues:
If there are no files to process the correct prompt "No files to process" comes up, but the sum will still be written with 0. Of course it would be better to not wright any file at all.

End of README.md
