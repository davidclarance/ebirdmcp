# ebirdmcp

MCP server for the [eBird API 2.0](https://documenter.getpostman.com/view/664302/S1ENwy59).

## Setup

1. Get an eBird API key at https://ebird.org/api/keygen
2. Install: `uv sync`

## Authentication

The server resolves the eBird API key in this order:

1. **`x-ebird-api-key` request header** — each user provides their own key (used for remote/hosted deployments)
2. **`EBIRD_API_KEY` environment variable** — fallback for local usage

This means hosted deployments don't need a shared key — each connecting client passes their own.

## Usage

### Local — with Claude Code (stdio)

Add to your MCP config:

```json
{
  "mcpServers": {
    "ebird": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/ebirdmcp", "ebirdmcp"],
      "env": {
        "EBIRD_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Remote — hosted for Claude web / shared use

Run with an HTTP transport:

```bash
uv run ebirdmcp --transport streamable-http --host 0.0.0.0 --port 8000
```

Clients connect to `https://your-host/mcp` and pass their eBird API key via the `x-ebird-api-key` header.

### Standalone

```bash
EBIRD_API_KEY=your-key uv run ebirdmcp
```

## Tools

### Observations
- `get_recent_observations` — Recent observations in a region
- `get_recent_notable_observations` — Recent rare/notable sightings in a region
- `get_recent_species_observations` — Recent observations of a species in a region
- `get_recent_nearby_observations` — Recent observations near coordinates
- `get_recent_nearby_species_observations` — Recent species observations near coordinates
- `get_nearest_species_observations` — Nearest observations of a species
- `get_recent_nearby_notable_observations` — Rare sightings near coordinates
- `get_historic_observations` — Observations on a specific past date

### Checklists & Statistics
- `get_recent_checklists` — Recent checklists in a region
- `get_top_100` — Top 100 contributors on a date
- `get_checklist_feed` — Checklist feed for a date
- `get_regional_statistics` — Birding stats for a region/date
- `get_species_list` — All species ever observed in a region
- `get_checklist` — View a specific checklist

### Hotspots
- `get_region_hotspots` — Hotspots in a region
- `get_nearby_hotspots` — Hotspots near coordinates
- `get_hotspot_info` — Details about a hotspot

### Taxonomy
- `get_taxonomy` — Full eBird taxonomy
- `get_taxonomic_forms` — Subspecies for a species
- `get_taxa_locale_codes` — Supported locale codes
- `get_taxonomy_versions` — Available taxonomy versions
- `get_taxonomic_groups` — Taxonomic groups

### Regions
- `get_region_info` — Region details
- `get_sub_region_list` — Sub-regions of a region
- `get_adjacent_regions` — Adjacent regions
