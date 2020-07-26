from argparse import ArgumentParser


def get_tools_options():
    argparser = ArgumentParser()
    argparser.add_argument("filepath", type=str,
                            help="Specify the path of the uasset file whose number of bytes you want to change")
    argparser.add_argument("size", type=int,
                            help="Specifies the byte size to change")

    args = argparser.parse_args()
    return args
