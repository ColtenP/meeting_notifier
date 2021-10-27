import threading
import subprocess


IS_IN_ZOOM = False
APP_NAME_TO_LOOK_FOR = 'cpthost.app/Contents/MacOS/CptHost'
NUMBER_TO_NOTIFY = ''


def check_zoom_status():
    global IS_IN_ZOOM
    threading.Timer(5.0, check_zoom_status).start()
    process = subprocess.Popen(f'''ps aux | grep '{APP_NAME_TO_LOOK_FOR}' | grep -v grep''', shell=True, stdout=subprocess.PIPE)
    process_return = process.stdout.read()
    is_in_zoom = len(process_return) > 0
    if not is_in_zoom == IS_IN_ZOOM:
        if is_in_zoom:
            message = "I am in a meeting xoxo"
        else:
            message = "I'm done with my meeting 🥰"
        
        IS_IN_ZOOM = is_in_zoom
        subprocess.Popen(f'''osascript sendMessage.applescript {NUMBER_TO_NOTIFY} "{message}"''', shell=True, stdout=subprocess.PIPE)
        

if __name__ == '__main__':
    check_zoom_status()
