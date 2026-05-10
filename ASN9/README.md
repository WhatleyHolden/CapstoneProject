# Simple MVC PySide6 Calculator

## Student
Holden Whatley

## Description
A simple calculator app that completes addition and subtract problems.

## MVC Overview
- Model : Handles input validation and calculation logic. It does not import PySide6 or depend on GUI widgets.
- View : Contains the GUI layout created for Qt Designer. It includes input boxes, labels, and buttons.
- Controller : Connects button clicks to the model methods and updates the GUI result label.
- Entry Point : Starts the PySide6 application and displays the window.

## Files Included
- main.py
- model.py
- controller.py
- view.ui
- view.py
- README.md

## How to Run
1. Install PySide6 if needed:

2. Run the application:

## Testing
Try these inputs:
- 10 and 5, then click Add. Expected result: 15.000
- 10 and 5, then click Subtract. Expected result: 5.000
- Empty input, then click Add or Subtract. Expected: warning message.
- ABC in either input box. Expected: warning message.
- Decimal inputs such as 5.5 and 2.25. Expected: result rounded to three decimal places.

## Attributions
https://doc.qt.io/qtforpython-6/
https://doc.qt.io/qt-6/qtdesigner-manual.html


## Issues Encountered
None while testing.
