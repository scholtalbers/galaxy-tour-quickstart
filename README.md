# Galaxy Tour Quick Start

Writing galaxy tours can be tedious as one needs to figure out the html elements clicked. 
One way to overcome this is to use test frameworks that can record your steps.

Here we use [UI Recorder](http://uirecorder.com) to record our steps and subsequently convert
the spec file to a Galaxy Tour compatible format.

**The generated yaml format is not a finished Galaxy Tour and you will want to modify its content.**


## How to

1. Get this repo
2. Get & Setup UIrecorder
    ```
    npm install
    node_modules/uirecorder/bin/uirecorder init
    ```

3. Start UIrecorder and record your steps

    ``node_modules/uirecorder/bin/uirecorder``
4. Convert the spec file
    
    ``python convert-to-yaml.py -i galaxy.spec.js -n "My first Galaxy Tour" -d "From recording" -t "StepTitle" > build_workflow.yaml``
