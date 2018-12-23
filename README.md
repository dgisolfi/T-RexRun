# T-RexRun

A recreation of the T-Rex Run game found on Google Chrome. Written instead in PyGame.

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## Running the Game

To run the latest release of the game you can either download the latest release on GitHub or follow the steps below to create a new build. In either case to run on windows run the RunRex Executable found in the build path, to run on OSX open the T-Rex Run app found in the build path as well.

## Developing

To test and develop the T-RexRun Game, with python 3 installed run the following in a terminal:

`python -m pip install -r requirements.txt `

This will install all required dependencies of the game. Once complete the code can be altered and then tested by running the main script: `python3 RexRun.py`

## Creating a new Build

After changes have been made and are ready to be released the executables must be re-built. To do this there is a `setup.py`  file located in the root of the repository that can be used. In a terminal navigate to the root of the directory and run the following if on windows: `python3 setup.py build` If on OSX run: `python setup.py bdist_dmg`. This will result in the build program being placed in the `build` folder.

## Troubleshooting

There is an error currently when running PyGame on OSX, the error causes the FPS to drop drastically. if this occurs follow these steps to resolve the issue:

1. Run the T-RexRun program(RexRun.py)
2. In your dock, you will see the PyGame Icon(snake with a controller in his mouth). Right-Click on it.
3. Go to Options and click "Show in Finder"
4. Finder will open and you will see the python application. (Rocket Icon)
5. Right-click the python application and click "Get Info".
6. Check the box "Open in Low Resolution" and it should now run at around 60fps.