from PyZest.gui import EasyWindow

window = EasyWindow("EasyWindow")
window.add_label("Hello")
window.add_button("OK", lambda: print("Ready!"))
window.run()
