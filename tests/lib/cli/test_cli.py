import frrtest


class TestCli(frrtest.TestRefOut):
    program = "./test_cli"
    built_refout = True
