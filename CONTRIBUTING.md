## Contributing to raylib-python-cffi

Hello contributors! Welcome to **raylib-python-cffi** AKA **pyray**! 

Do you enjoy pyray and want to contribute? Nice! You can help with the following points:

- `Python programming` - Can you write/review/test/improve the code? 
- `Documentation/Tutorials/Example` - Can you write some tutorial/example?
- `Porting Examples from C to Python` - Can you port the raylib examples in c to python?
- `Build For Web` - Can you help [the issue](https://github.com/electronstudio/raylib-python-cffi/issues/58)?
- `Testing` - Can you find some bugs in pyray?

This document contains a set of guidelines to contribute to the project. These are mostly guidelines, not rules. 
Use your best judgement, and feel free to propose changes to this document in a pull request.

### raylib philosophy

 - raylib is a tool to **ENJOY** videogames programming, every function in raylib is designed as a mini-tutorial on itself.
 - raylib is **SIMPLE** and **EASY-TO-USE**, I tried to keep it compact with a small set of functions, if a function is too complex, better not including it.
 - raylib is open source and free; educators and institutions can use this tool to **TEACH** videogames programming completely for free.
 - raylib is collaborative; contribution of tutorials / code examples / bug fixes / code comments are highly appreciated.
 - raylib's license (and its external libs respective licenses) allow using raylib on commercial projects.

### raylib python coding conventions

Despite being written in C, pyray is a python bindings for raylib. so the conventions are also python independent
look at [Python API Coding Style Conventions](https://github.com/raysan5/raylib/wiki/raylib-coding-conventions), 

Source code is extensively commented for that purpose, raylib primary learning method is:

 > `Learn by reading code and examples`

### Opening new Issues

To open new issue for raylib (bug, enhancement, discussion...), just try to follow these rules:

 - Make sure the issue has not already been reported before by searching on GitHub under Issues.
 - If you're unable to find an open issue addressing the problem, open a new one. Be sure to include a 
 title and clear description, as much relevant information as possible, and a code sample demonstrating the unexpected behavior.
 - If applies, attach some screenshot of the issue and a .zip file with the code sample and required resources.
 - On issue description, add a brackets tag about the raylib module that relates to this issue. 
 If don't know which module, just report the issue, I will review it.
 - You can check other issues to see how is being done!

### Sending a Pull-Request

 - Make sure the PR description clearly describes the problem and solution. Include the relevant issue number if applicable.
 - Don't send big pull requests (lots of changelists), they are difficult to review. It's better to send small pull requests, one at a time.
 - Verify that changes don't break the build (at least on Windows platform). As many platforms where you can test it, the better, but don't worry
 if you cannot test all the platforms.

Thank you very much for your time! :)
