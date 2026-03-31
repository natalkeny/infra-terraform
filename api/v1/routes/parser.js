import { promisify } from 'util';
import * as fs from 'fs';
import * as path from 'path';
import * as childProcess from 'child_process';
import * as console from 'console';

const exec = promisify(childProcess.exec);

const parseTfConfig = async (tfConfigPath) => {
  const tfConfigContent = fs.readFileSync(tfConfigPath, 'utf8');

  const tfConfig = JSON.parse(tfConfigContent);

  const resources = {};

  for (const resource in tfConfig) {
    if (Object.hasOwn(tfConfig, resource)) {
      const type = tfConfig[resource].type;
      const name = tfConfig[resource].name;

      if (!resources[type]) resources[type] = [];

      resources[type].push(name);
    }
  }

  return resources;
};

const getTfProviders = async (tfConfigPath) => {
  const tfConfigContent = fs.readFileSync(tfConfigPath, 'utf8');

  const tfConfig = JSON.parse(tfConfigContent);

  const providers = {};

  for (const provider in tfConfig.providers) {
    if (Object.hasOwn(tfConfig.providers, provider)) {
      const name = tfConfig.providers[provider].name;
      const version = tfConfig.providers[provider].version;

      providers[name] = version;
    }
  }

  return providers;
};

const terraformInit = async (workDir) => {
  const initCommand = `terraform init ${workDir}`;

  try {
    await exec(initCommand);
    console.log(`Terraform initialized successfully in ${workDir}`);
  } catch (error) {
    console.error(`Error executing terraform init in ${workDir}: ${error}`);
  }
};

export { parseTfConfig, getTfProviders, terraformInit };