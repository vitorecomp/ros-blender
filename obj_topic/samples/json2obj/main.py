def start():
    pass


if name == "main":
    #get the arguments from the command line
    args = sys.argv[1:]
    #check if there is any argument
    if len(args) == 0:
        throw("No arguments given. please use -h for help.")

    #check if the first argument is help option
    if args[0] == "-h":
        print(help)
        exit(0)
    #check if the first argument is a valid file
    if not os.path.isfile(args[0]):
        throw("The input file file is not valid.")
        
    start()