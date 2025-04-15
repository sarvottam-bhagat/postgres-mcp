# PostgreSQL MCP Server

A FastMCP server that enables LLMs to connect and interact with PostgreSQL databases. This project allows Language Models to query and explore database schemas and tables through the Model Context Protocol (MCP).

## Features

- **Schema Exploration**: Retrieve metadata about database schemas
- **Table Inspection**: Get detailed information about table structures
- **Database Querying**: Execute SQL queries against the database
- **YAML Formatting**: Results are returned in YAML format for easy consumption by LLMs

## Resources

The server exposes the following MCP resources:

- `database://{schema}` - Get information about all tables in a schema
- `database://{schema}/tables/{table}` - Get detailed information about a specific table

## Tools

- `query_database` - Execute SQL queries against the database (SELECT queries only)

## Prompts

The server includes the following predefined prompts:

- `prompt_schema_description` - Ask for a description of a database schema
- `prompt_table_description` - Ask for a description of a specific table
- `prompt_query_database` - Ask for data from a specific table

## Prerequisites

- Python 3.12 or higher
- PostgreSQL database
- UV package manager (recommended)

## Installation

### Python Package Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/postgres-mcp.git
   cd postgres-mcp
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install UV (if not already installed):

   ```bash
   pip install uv
   ```

4. Install dependencies with UV:

   ```bash
   uv sync
   ```

### NPM Package Installation (Alternative)

You can also install the package globally via npm:

```bash
npm install -g postgres-mcp-server
```

## Configuration

The application is configured using environment variables:

| Variable    | Description              | Default            |
| ----------- | ------------------------ | ------------------ |
| APP_NAME    | Application name         | postgres-mcp-server|
| DB_HOST     | PostgreSQL host          | localhost          |
| DB_PORT     | PostgreSQL port          | 5432               |
| DB_USER     | PostgreSQL username      | postgres           |
| DB_PASSWORD | PostgreSQL password      | postgres-password  |
| DB_NAME     | PostgreSQL database name | postgres           |

## Usage

### Running the Server Directly

Start the FastMCP server:

```bash
python -m src.main
```

The server will be available for LLMs to connect to and query your PostgreSQL database.

### Client Configuration

#### VS Code

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

Replace the placeholders with your actual PostgreSQL database credentials.

#### Cursor

Add the following to your `.cursor/mcp.json` file:

```json
{
  "servers": {
    "postgres-mcp-server": {
      "command": "/path/to/your/venv/bin/mcp",
      "args": ["run", "/path/to/your/postgres-mcp/src/main.py"],
      "env": {
        "APP_NAME": "postgres-mcp-server",
        "DB_HOST": "your-database-host",
        "DB_PORT": "5432",
        "DB_USER": "your-database-username",
        "DB_PASSWORD": "your-database-password",
        "DB_NAME": "your-database-name"
      }
    }
  }
}
```

Be sure to replace the paths with the actual paths to your virtual environment and project directory, and update the environment variables to match your PostgreSQL configuration.

## Development

Install development dependencies with UV:

```bash
uv pip install -e ".[dev]"
```

Development tools included:

- JupyterLab for notebooks
- Pyright for type checking
- Ruff for linting

## Testing

### Testing Database Connection

You can test your database connection using the provided script:

```bash
python test_connection.py
```

### Testing MCP Server

Once the server is running, you can test it using the provided test script:

```bash
python test_mcp.py
```

## Example Usage

### Get Schema Information

```python
from mcp.client import get_client

client = get_client("http://localhost:3000")
schema_info = client.get_resource("database://public")
print(schema_info)
```

### Get Table Details

```python
table_info = client.get_resource("database://public/tables/users")
print(table_info)
```

### Execute a Query

```python
result = client.invoke_tool("query_database", {"query": "SELECT * FROM users LIMIT 10"})
print(result)
```

## Project Structure

```
.
├── bin/                    # Binary scripts
│   └── postgres-mcp-server.js  # Node.js wrapper script
├── src/                    # Source code
│   ├── __init__.py         # Package initialization
│   ├── main.py             # Main entry point
│   └── utils/              # Utility modules
│       ├── config.py       # Configuration handling
│       ├── db.py           # Database connection
│       └── types.py        # Type definitions
├── index.js                # Node.js entry point
├── package.json            # Node.js package configuration
├── pyproject.toml          # Python project configuration
├── template_mcp.json       # Template for MCP configuration
├── test_connection.py      # Database connection test
└── test_mcp.py             # MCP server test
```

## License

MIT
