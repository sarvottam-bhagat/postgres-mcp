# PostgreSQL MCP Server

A FastMCP server that enables LLMs to connect and interact with PostgreSQL databases.

## Quick Start

### Installation

```bash
npm install -g postgres-mcp-server
```

### Configuration in VS Code

Add the following to your `.vscode/mcp.json` file:

```json
{
  "servers": {
    "postgres-mcp-server": {
      "type": "stdio",
      "command": "postgres-mcp-server",
      "args": [
        "DB_HOST=your-database-host",
        "DB_USER=your-database-username",
        "DB_PASSWORD=your-database-password",
        "DB_PORT=5432",
        "DB_NAME=your-database-name"
      ]
    }
  }
}
```

Replace the placeholders with your actual PostgreSQL database credentials:
- `your-database-host`: Your PostgreSQL server hostname or IP address
- `your-database-username`: Your PostgreSQL username
- `your-database-password`: Your PostgreSQL password
- `5432`: Your PostgreSQL port (default is 5432)
- `your-database-name`: Your PostgreSQL database name

### Usage

1. Open VS Code
2. Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P)
3. Select "MCP: Start Server"
4. Choose "postgres-mcp-server"

You can now interact with your PostgreSQL database through the MCP interface.

## Features

- **Schema Exploration**: Retrieve metadata about database schemas
- **Table Inspection**: Get detailed information about table structures
- **Database Querying**: Execute SQL queries against the database

## Resources

The server exposes the following MCP resources:

- `database://{schema}` - Get information about all tables in a schema
- `database://{schema}/tables/{table}` - Get detailed information about a specific table

## Tools

- `query_database` - Execute SQL queries against the database (SELECT queries only)

## Example Usage

### Get Schema Information

```
database://public
```

### Get Table Details

```
database://public/tables/users
```

### Execute a Query

```
SELECT * FROM users LIMIT 10
```

## Troubleshooting

If you encounter connection issues:

1. Verify that your database credentials are correct
2. Ensure that your database is accessible from your machine
3. Check if any firewalls or network restrictions are blocking the connection
4. Verify that the PostgreSQL port (default: 5432) is open
