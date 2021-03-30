    # python -m unittest test

    # verbose
    # python -m unittest -v test

    """will search for any and all test files and run them"""
    # python -m unittest discover

    """you can provide the name of the directory instead by using the -s flag and the name of the directory"""
    # python -m unittest discover -s tests

    """Lastly, if your source code is not in the directory root and contained in a subdirectory, for example in a 
    folder called src/, you can tell unittest where to execute the tests so that it can import the modules correctly 
    with the -t flag: """
    # python -m unittest discover -s tests -t src

