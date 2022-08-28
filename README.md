# track_app_icon_click
This app records the time for running windows on the operating system!
## How to add run the start.py script at startup in Ubuntu
run this command

 crontab -e
- and then add

@reboot /usr/bin/python /path/to/yourpythonscript
save and quit,then your python script will automatically run after you reboot
