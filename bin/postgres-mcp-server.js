#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');

// Create a temporary configuration file with user's database credentials
function createConfigFile(credentials) {
  const configDir = path.join(os.homedir(), '.postgres-mcp');
  
  if (!fs.existsSync(configDir)) {
    fs.mkdirSync(configDir, { recursive: true });
  }
  
  const configPath = path.join(configDir, 'config.env');
  
  let configContent = '';
  for (const [key, value] of Object.entries(credentials)) {
    configContent += `${key}=${value}\n`;
  }
  
  fs.writeFileSync(configPath, configContent);
  return configPath;
}

// Parse command line arguments
const args = process.argv.slice(2);
const credentials = {};

// Default values
credentials.APP_NAME = 'mcp-demo';
credentials.DB_PORT = '5432';
credentials.DB_NAME = 'postgres';

// Parse arguments in the format key=value
for (const arg of args) {
  if (arg.includes('=')) {
    const [key, value] = arg.split('=');
    if (key.startsWith('DB_')) {
      credentials[key] = value;
    }
  }
}

// Check for required credentials
const requiredCredentials = ['DB_HOST', 'DB_USER', 'DB_PASSWORD'];
const missingCredentials = requiredCredentials.filter(cred => !credentials[cred]);

if (missingCredentials.length > 0) {
  console.error(`Error: Missing required database credentials: ${missingCredentials.join(', ')}`);
  console.error('Usage: postgres-mcp-server DB_HOST=your-host DB_USER=your-user DB_PASSWORD=your-password [DB_PORT=5432] [DB_NAME=postgres]');
  process.exit(1);
}

// Create config file
const configPath = createConfigFile(credentials);

// Find the Python executable
const pythonPath = 'python3'; // Assuming python3 is in the PATH

// Find the main.py script
const scriptPath = path.join(__dirname, '..', 'src', 'main.py');

// Run the Python script with the config file
const pythonProcess = spawn(pythonPath, [scriptPath], {
  env: {
    ...process.env,
    ...credentials
  },
  stdio: 'inherit'
});

pythonProcess.on('close', (code) => {
  console.log(`PostgreSQL MCP server exited with code ${code}`);
});

// Handle termination signals
process.on('SIGINT', () => {
  pythonProcess.kill('SIGINT');
});

process.on('SIGTERM', () => {
  pythonProcess.kill('SIGTERM');
});
