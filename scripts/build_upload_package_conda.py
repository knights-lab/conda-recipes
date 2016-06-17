#!/usr/bin/env python

# This script will build a conda recipe and upload it and all systems packages to anaconda.org

import click
import os
import sys
import subprocess


def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    while process.poll() is None:
        sys.stdout.write(process.stdout.readline().decode())

@click.command()
@click.argument('recipe', type=click.Path(exists=True))
@click.option('--output_dir', type=click.Path(file_okay=False, writable=True), default=os.path.join(os.getcwd(), 'conda-blds'))
def build(recipe, output_dir):
    conda_build_cmd = ['conda', 'build', '-c', 'knights-lab', '--quiet', '--output', recipe]
    conda_build_sp = subprocess.Popen(conda_build_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    out, err = conda_build_sp.communicate()
    build_path = out.decode().rstrip()
    
    print(output_dir)
    conda_convert_cmd = ['conda', 'convert', '-f', '-p', 'all', '-o', output_dir, build_path]
    
    # conda_convert_sp = subprocess.Popen(conda_convert_cmd, stdout=subprocess.PIPE)
    # print_realtime(conda_convert_sp)
    # conda_convert_sp.communicate()
    run_command(conda_convert_cmd)
    
    conda_upload_cmd = ['anaconda', 'upload', '--user', 'knights-lab', '--force', '--label', 'dev']
    for dirpath, dirnames, filenames in os.walk(output_dir):
        for filename in filenames:
            upload_file = os.path.join(dirpath, filename)
            # conda_upload_sp = subprocess.Popen(conda_upload_cmd + [upload_file], stdout=subprocess.PIPE)
            # print_realtime(conda_upload_sp)
            # conda_upload_sp.communicate()
            run_command(conda_upload_cmd + [upload_file])



if __name__ == '__main__':
    build()