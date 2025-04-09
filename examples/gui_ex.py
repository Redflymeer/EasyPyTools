from easy_python.gui import EasyWindow

window = EasyWindow("EasyWindow")
window.add_label("Hello")
window.add_button("OK", lambda: print("Ready!"))
window.run()