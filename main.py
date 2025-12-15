import os
import argparse
from infra_terraform.terraform_typer import TerraformTyper

def main():
    parser = argparse.ArgumentParser(description='Run Terraform infrastructure provisioning.')
    parser.add_argument('--project', required=True, help='Project directory')
    parser.add_argument('--action', required=True, choices=['init', 'apply', 'destroy'], help='Terraform action')
    parser.add_argument('--config', help='Path to Terraform configuration file')
    parser.add_argument('--vars', help='Path to Terraform variables file')
    args = parser.parse_args()

    if not os.path.exists(args.project):
        raise Exception(f"Project directory '{args.project}' does not exist")

    terraform = TerraformTyper(args.project)
    action = args.action
    config = args.config
    variables = args.vars

    if action == 'init':
        terraform.configure()
    elif action == 'apply':
        terraform.apply(config, variables)
    elif action == 'destroy':
        terraform.destroy()

if __name__ == '__main__':
    main()