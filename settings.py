import cx_Freeze

executables = [cx_Freeze.Executable("myGame.py")]

cx_Freeze.setup(

    name = "Laspeed Dodger",
    options ={"built_exe": {"packages":["pygame"],"include_files":["carpy.png"]}},
    executables = executables
)