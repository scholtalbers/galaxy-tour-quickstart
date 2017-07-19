#!/usr/bin/env python

import re
import argparse

parser = argparse.ArgumentParser(description="""
Convert uirecorder spec file to a Galaxy Tour yaml file (stdout). The generated yaml file is not a complete Galaxy Tour
and you will want to modify its content.""")

parser.add_argument('-i', dest="input", metavar='uirecorder spec file',
                    type=argparse.FileType('rt'))
parser.add_argument('-n', dest="name", default="Galaxy Tour")
parser.add_argument('-d', dest="description", default="")
parser.add_argument('-t', dest="title", default="")
args = parser.parse_args()

print("""
name: {name}
description: {description}
title_default: "{title}"
steps:""".format(name=args.name, description=args.description, title=args.title))

step_number = 0
for line in args.input:
    # it('click: Workflow ( #workflow a, 31, 22, 0 )', async function(){
    match = re.search(r'it\(\'(\w+):\s([A-Za-z- ]*\s*?)\s*\(*\s*(\#*.+?),.+? async.+', line)
    if match:
        step_number += 1
        title = match.group(2) if match.group(2) != "" else "Step {}".format(step_number)
        step = """
    - title: {title}
      element: '{element}'
      intro: """.format(title=title, element=match.group(3))
        if match.group(1) == "click":
            step += """
      postclick:
        - '{element}'""".format(element=match.group(3))
        print(step)
