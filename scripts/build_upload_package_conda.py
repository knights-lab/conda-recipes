#!/usr/bin/env python

# This script will build a conda recipe and upload it and all systems packages to anaconda.org

import click
import os
import sys
import subprocess

def print_realtime(process):
    while True:
        out = process.stdout.read(1)
        if out and process.poll() != None:
            break
        else:
            sys.stdout.write(out.decode())
            sys.stdout.flush()


@click.command()
@click.argument('recipe', type=click.Path(exists=True))
@click.option('--output_dir', type=click.Path(file_okay=False, writable=True), default=os.path.join(os.getcwd(), 'conda-blds'))
def build(recipe, output_dir):
    conda_build_cmd = ['conda', 'build', '-c', 'knights-lab', '--quiet', '--output', recipe]
    conda_build_sp = subprocess.Popen(conda_build_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    out, err = conda_build_sp.communicate()
    build_path = out.decode().rstrip()
    
    print(output_dir)
    conda_convert_cmd = ['conda', 'convert', '-p', 'all', '-o', output_dir, build_path]
    
    conda_convert_sp = subprocess.Popen(conda_convert_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print_realtime(conda_convert_sp)
    
    conda_upload_cmd = ['anaconda', 'upload', '--user', 'knights-lab', '--label', 'dev']
    for dirpath, dirnames, filenames in os.walk(output_dir):
        for filename in filenames:
            upload_file = os.path.join(dirpath, filename)
            conda_upload_sp = subprocess.Popen(conda_upload_cmd + [upload_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print_realtime(conda_upload_sp)



if __name__ == '__main__':
    build()