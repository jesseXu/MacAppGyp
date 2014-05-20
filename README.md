This mainly is a shell script with a few defaults template files. It can be used to generate a default mac project like xcode but using GYP to manage the project.

## Prerequisite: GYP
If you don't know it, you do not need this repo.

## How to use it

	./generate_mac targetDir targetName

## using gyp to generate xcode prject

	gyp xxx.gyp --depth=. -f xcode
