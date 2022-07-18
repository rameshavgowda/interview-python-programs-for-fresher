def print_msg(msg):
    def printer():
        print(msg)
    return printer

other= print_msg("Ramesha")
other()