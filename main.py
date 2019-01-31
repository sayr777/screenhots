import pyautogui, uuid

s_uuid = str(uuid.uuid4())

screen = pyautogui.screenshot(s_uuid + ".png")

print(screen)