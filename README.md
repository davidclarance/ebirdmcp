# ebirdmcp

MCP server for the [eBird API 2.0](https://documenter.getpostman.com/view/664302/S1ENwy59).

## Setup

1. Get an eBird API key at https://ebird.org/api/keygen
2. Set the `EBIRD_API_KEY` environment variable

## Install

```bash
uv sync
```

## Usage

### With Claude Code

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
