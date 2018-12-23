import cx_Freeze

executables = [cx_Freeze.Executable("./src/RexRun.py")]

cx_Freeze.setup(
    name="T-Rex Run",
    options = {
        "build_exe": {
        "packages":["pygame"],
        "include_files":[
            "./src/ObstacleClass.py",
            "./src/PlayerClass.py",
            "./src/settings.py",
            "./src/imgs/dino.png",
            "./src/imgs/dino_left_foot_up.png",
            "./src/imgs/dino_right_foot_up.png",
            ]
        }
    },
    executables = executables
)