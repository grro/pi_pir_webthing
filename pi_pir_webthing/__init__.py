import logging
from string import Template
from pi_pir_webthing.app import App
from pi_pir_webthing.motionsensor_webthing import run_server

PACKAGENAME = 'pi_pir_webthing'
ENTRY_POINT = "pir"
DESCRIPTION = "A web connected PIR motion sensor detecting movement running on Raspberry Pi"



UNIT_TEMPLATE = Template('''
[Unit]
Description=$packagename
After=syslog.target network.target

[Service]
Type=simple
ExecStart=$entrypoint --command listen --verbose $verbose --port $port --gpio $gpio --name $name
SyslogIdentifier=$packagename
StandardOutput=syslog
StandardError=syslog
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
''')



class PirApp(App):

    def do_add_argument(self, parser):
        parser.add_argument('--gpio', metavar='gpio', required=False, type=int, help='the gpio number wired to the device')
        parser.add_argument('--name', metavar='name', required=False, default='Motion Sensor', type=str, help='the name of the sensor')


    def do_additional_listen_example_params(self):
        return "--gpio 14"

    def do_process_command(self, command:str, port: int, verbose: bool, args) -> bool:
        if command == 'listen' and (args. gpio is not None):
            print("running " + self.packagename + "/" + args.name + " on port " + str(port) + " (gpio " + str(args.gpio) + ")")
            run_server(port, int(args.gpio), args.name, self.description)
            return True
        elif args.command == 'register' and (args.gpio is not None):
            print("register " + self.packagename + "/" + args.name  + " on port " + str(port) + " (gpio " + str(args.gpio) + ") and starting it")
            unit = UNIT_TEMPLATE.substitute(packagename=self.packagename, entrypoint=self.entrypoint, port=port, verbose=verbose, gpio=args.gpio, name=args.name)
            self.unit.register(port, unit)
            return True
        else:
            return False


def main():
    PirApp(PACKAGENAME, ENTRY_POINT, DESCRIPTION).handle_command()


if __name__ == '__main__':
    main()

