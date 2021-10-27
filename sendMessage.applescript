on run {phoneNumber, textMessage}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy phoneNumber of targetService
        send textMessage to targetBuddy
    end tell
end run
