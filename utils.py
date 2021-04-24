import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, required=True, help='Target url.')
    parser.add_argument('-o', '--output', type=str, required=False, help='Output file.', default='output.json')
    return parser.parse_args()
