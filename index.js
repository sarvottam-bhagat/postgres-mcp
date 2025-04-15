#!/usr/bin/env node

const { execSync } = require('child_process');
const path = require('path');

// This file is just a simple wrapper that calls the main script
require('./bin/postgres-mcp-server');
