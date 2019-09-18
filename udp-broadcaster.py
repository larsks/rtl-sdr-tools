#!/usr/bin/python3

import click
import socket
import sys

BUFFER_SIZE = 8192
UDP_PORT = 7355
UDP_ADDRESS = '0.0.0.0'
DEFAULT_LISTEN_ADDRESS = '{}:{}'.format(UDP_ADDRESS, UDP_PORT)


def parse_address(addr, template=None):
    if ':' in addr:
        host, port = addr.split(':')
        port = int(port)
    elif template:
        host = template[0]
        port = int(addr)
    else:
        raise ValueError('expecting <host:port>')

    return (host, port)


@click.command()
@click.option('-l', '--listen-address', default=DEFAULT_LISTEN_ADDRESS)
@click.argument('addresses', nargs=-1)
def main(listen_address, addresses):
    if not addresses:
        raise click.ClickException(
            'There must be at least one rebroadcast address')

    listen_address = parse_address(listen_address)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(listen_address)

    targets = []
    for addr in addresses:
        targets.append(parse_address(addr, template=listen_address))

    while True:
        data, address = sock.recvfrom(BUFFER_SIZE)
        for target in targets:
            sock.sendto(data, target)


if __name__ == '__main__':
    main(sys.argv[1:])
