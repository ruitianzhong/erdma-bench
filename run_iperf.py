#!/bin/python

import argparse
import subprocess


def run_client(args):
    cmd = f"iperf3 --client {args.server_ip} -B {args.client_ip} --parallel 5 --port 10086"
    # server = subprocess.run(cmd.split())
    print(cmd)


def run_server(args):
    cmd = f"iperf3 -B {args.server_ip} --port 10086 --server"
    # subprocess.run(cmd)
    print(cmd)


def main():
    parser = argparse.ArgumentParser(description="iperf runner")
    parser.add_argument("--server", action="store_true", help="server side")
    parser.add_argument("--server-ip", '-sip', type=str, default="0.0.0.0")

    #
    parser.add_argument("--client", action="store_true", help="client side")
    parser.add_argument("--client-ip", '-cip', type=str, default="0.0.0.0")
    parser.add_argument("--zerocopy", "-Z", action="store_true")

    args = parser.parse_args()

    if args.server:
        run_server(args)

    if args.client:
        run_client(args)


if __name__ == "__main__":
    print("hello")
    main()
