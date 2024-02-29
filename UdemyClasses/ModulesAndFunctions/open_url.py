import webbrowser

# webbrowser.open('https://docs.python.org/3.10/library/webbrowser')

# chrome = webbrowser.get(using='google-chrome')
# chrome = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s')  # noqa
chrome = webbrowser.get('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/chrome.exe %s')  # noqa
chrome.open('https://learningprogramming.academy/courses')
