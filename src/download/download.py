#!/usr/bin/env python3

import argparse
import asyncio

from torrentp import TorrentDownloader


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        metavar="FILE",
        help="path to the input .torrent file",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        metavar="PATH",
        help="path to output file or directory",
    )
    args = parser.parse_args()

    torrent_file = TorrentDownloader(args.input, args.output)
    asyncio.run(torrent_file.start_download())


if __name__ == "__main__":
    main()
