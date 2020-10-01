import argparse
import logging
import os
from pi_pir_webthing.motionsensor_webthing import run_server
from pi_pir_webthing.unit import register, deregister, printlog

PACKAGENAME = 'pi_pir_webthing'
ENTRY_POINT = "pir"
DESCRIPTION = "A web connected PIR motion sensor detecting movement running on Raspberry Pi"


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--command', metavar='command', required=True, type=str, help='the command. Supported commands are: listen (run the webthing service), register (register and starts the webthing service as a systemd unit, deregister (deregisters the systemd unit), log (prints the log)')
    parser.add_argument('--port', metavar='port', required=True, type=int, help='the port of the webthing serivce')
    parser.add_argument('--gpio', metavar='gpio', required=False, type=int, help='the gpio number wired to the device')
    args = parser.parse_args()

    if args.command == 'listen':
        print("running " + PACKAGENAME + " on port " + str(args.port) + "/gpio " + str(args.gpio))
        run_server(int(args.port), int(args.gpio), DESCRIPTION)
    elif args.command == 'register':
        print("register " + PACKAGENAME + " on port " + str(args.port) + "/gpio " + str(args.gpio) + " and starting it")
        register(PACKAGENAME, ENTRY_POINT, int(args.port), int(args.gpio))
    elif args.command == 'deregister':
        deregister(PACKAGENAME, int(args.port))
    elif args.command == 'log':
        printlog(PACKAGENAME, int(args.port))
    else:
        print("usage " + ENTRY_POINT + " --help")


if __name__ == '__main__':
    log_level = os.environ.get("LOGLEVEL", "INFO")
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.getLevelName(log_level), datefmt='%Y-%m-%d %H:%M:%S')

    main()
