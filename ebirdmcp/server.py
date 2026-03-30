from __future__ import annotations

import json
import os

from mcp.server.fastmcp import FastMCP

from ebirdmcp.client import EBirdClient

mcp = FastMCP(
    "ebirdmcp",
    instructions="MCP server for the eBird API 2.0 — bird observations, hotspots, taxonomy, and regions.",
)


def _get_client() -> EBirdClient:
    api_key = os.environ.get("EBIRD_API_KEY", "")
    if not api_key:
        raise RuntimeError(
            "EBIRD_API_KEY environment variable is required. "
            "Get one at https://ebird.org/api/keygen"
        )
    return EBirdClient(api_key)


def _format(data: object) -> str:
    return json.dumps(data, indent=2, default=str)


# ── Observations ──────────────────────────────────────────────────


@mcp.tool()
async def get_recent_observations(
    region_code: str,
    back: int | None = None,
    cat: str | None = None,
    hotspot: bool | None = None,
    include_provisional: bool | None = None,
    max_results: int | None = None,
    spp_locale: str | None = None,
) -> str:
    """Get recent bird observations in a region.

    Args:
        region_code: eBird region code (e.g. "US-NY", "US", "CA-ON")
        back: Number of days back to look (1-30, default 14)
        cat: Taxonomic category filter (e.g. "species", "slash", "hybrid")
        hotspot: Only return observations from hotspots
        include_provisional: Include unreviewed observations
        max_results: Max number of results
        spp_locale: Locale for species common names (e.g. "en", "es", "fr")
    """
    client = _get_client()
    try:
        data = await client.get_recent_observations(
            region_code, back=back, cat=cat, hotspot=hotspot,
            include_provisional=include_provisional,
            max_results=max_results, spp_locale=spp_locale,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_recent_notable_observations(
    region_code: str,
    back: int | None = None,
    detail: str | None = None,
    hotspot: bool | None = None,
    max_results: int | None = None,
    spp_locale: str | None = None,
) -> str:
    """Get recent notable (rare) bird observations in a region.

    Args:
        region_code: eBird region code (e.g. "US-NY", "US")
        back: Number of days back (1-30, default 14)
        detail: Detail level: "simple" or "full"
        hotspot: Only return hotspot observations
        max_results: Max number of results
        spp_locale: Locale for species common names
    """
    client = _get_client()
    try:
        data = await client.get_recent_notable_observations(
            region_code, back=back, detail=detail, hotspot=hotspot,
            max_results=max_results, spp_locale=spp_locale,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_recent_species_observations(
    region_code: str,
    species_code: str,
    back: int | None = None,
    hotspot: bool | None = None,
    include_provisional: bool | None = None,
    max_results: int | None = None,
    spp_locale: str | None = None,
) -> str:
    """Get recent observations of a specific species in a region.

    Args:
        region_code: eBird region code (e.g. "US-NY")
        species_code: eBird species code (e.g. "norcar" for Northern Cardinal)
        back: Number of days back (1-30, default 14)
        hotspot: Only return hotspot observations
        include_provisional: Include unreviewed observations
        max_results: Max number of results
        spp_locale: Locale for species common names
    """
    client = _get_client()
    try:
        data = await client.get_recent_species_observations(
            region_code, species_code, back=back, hotspot=hotspot,
            include_provisional=include_provisional,
            max_results=max_results, spp_locale=spp_locale,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_recent_nearby_observations(
    lat: float,
    lng: float,
    dist: int | None = None,
    back: int | None = None,
    cat: str | None = None,
    hotspot: bool | None = None,
    include_provisional: bool | None = None,
    max_results: int | None = None,
    sort: str | None = None,
    spp_locale: str | None = None,
) -> str:
    """Get recent bird observations near a location.

    Args:
        lat: Latitude (-90 to 90)
        lng: Longitude (-180 to 180)
        dist: Search radius in km (0-50, default 25)
        back: Number of days back (1-30, default 14)
        cat: Taxonomic category filter
        hotspot: Only return hotspot observations
        include_provisional: Include unreviewed observations
        max_results: Max number of results
        sort: Sort order: "date" or "species"
        spp_locale: Locale for species common names
    """
    client = _get_client()
    try:
        data = await client.get_recent_nearby_observations(
            lat, lng, dist=dist, back=back, cat=cat, hotspot=hotspot,
            include_provisional=include_provisional,
            max_results=max_results, sort=sort, spp_locale=spp_locale,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_recent_nearby_species_observations(
    species_code: str,
    lat: float,
    lng: float,
    dist: int | None = None,
    back: int | None = None,
    cat: str | None = None,
    hotspot: bool | None = None,
    include_provisional: bool | None = None,
    max_results: int | None = None,
    sort: str | None = None,
    spp_locale: str | None = None,
) -> str:
    """Get recent observations of a species near a location.

    Args:
        species_code: eBird species code (e.g. "norcar")
        lat: Latitude (-90 to 90)
        lng: Longitude (-180 to 180)
        dist: Search radius in km (0-50, default 25)
        back: Number of days back (1-30, default 14)
        cat: Taxonomic category filter
        hotspot: Only return hotspot observations
        include_provisional: Include unreviewed observations
        max_results: Max number of results
        sort: Sort order: "date" or "species"
        spp_locale: Locale for species common names
    """
    client = _get_client()
    try:
        data = await client.get_recent_nearby_species_observations(
            species_code, lat, lng, dist=dist, back=back, cat=cat,
            hotspot=hotspot, include_provisional=include_provisional,
            max_results=max_results, sort=sort, spp_locale=spp_locale,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_nearest_species_observations(
    species_code: str,
    lat: float,
    lng: float,
    dist: int | None = None,
    back: int | None = None,
    hotspot: bool | None = None,
    include_provisional: bool | None = None,
    max_results: int | None = None,
    spp_locale: str | None = None,
) -> str:
    """Find the nearest observations of a species to a location.

    Args:
        species_code: eBird species code (e.g. "norcar")
        lat: Latitude (-90 to 90)
        lng: Longitude (-180 to 180)
        dist: Search radius in km (0-500, default 50)
        back: Number of days back (1-30, default 14)
        hotspot: Only return hotspot observations
        include_provisional: Include unreviewed observations
        max_results: Max number of results
        spp_locale: Locale for species common names
    """
    client = _get_client()
    try:
        data = await client.get_nearest_species_observations(
            species_code, lat, lng, dist=dist, back=back, hotspot=hotspot,
            include_provisional=include_provisional,
            max_results=max_results, spp_locale=spp_locale,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_recent_nearby_notable_observations(
    lat: float,
    lng: float,
    dist: int | None = None,
    back: int | None = None,
    detail: str | None = None,
    hotspot: bool | None = None,
    max_results: int | None = None,
    spp_locale: str | None = None,
) -> str:
    """Get recent notable (rare) bird observations near a location.

    Args:
        lat: Latitude (-90 to 90)
        lng: Longitude (-180 to 180)
        dist: Search radius in km (0-50, default 25)
        back: Number of days back (1-30, default 14)
        detail: Detail level: "simple" or "full"
        hotspot: Only return hotspot observations
        max_results: Max number of results
        spp_locale: Locale for species common names
    """
    client = _get_client()
    try:
        data = await client.get_recent_nearby_notable_observations(
            lat, lng, dist=dist, back=back, detail=detail, hotspot=hotspot,
            max_results=max_results, spp_locale=spp_locale,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_historic_observations(
    region_code: str,
    year: int,
    month: int,
    day: int,
    cat: str | None = None,
    detail: str | None = None,
    hotspot: bool | None = None,
    include_provisional: bool | None = None,
    max_results: int | None = None,
    rank: str | None = None,
    spp_locale: str | None = None,
) -> str:
    """Get bird observations on a specific historical date in a region.

    Args:
        region_code: eBird region code (e.g. "US-NY")
        year: Year (e.g. 2024)
        month: Month (1-12)
        day: Day of month (1-31)
        cat: Taxonomic category filter
        detail: Detail level: "simple" or "full"
        hotspot: Only return hotspot observations
        include_provisional: Include unreviewed observations
        max_results: Max number of results
        rank: Rank by "mrec" (most recent) or "create" (creation date)
        spp_locale: Locale for species common names
    """
    client = _get_client()
    try:
        data = await client.get_historic_observations(
            region_code, year, month, day, cat=cat, detail=detail,
            hotspot=hotspot, include_provisional=include_provisional,
            max_results=max_results, rank=rank, spp_locale=spp_locale,
        )
        return _format(data)
    finally:
        await client.close()


# ── Products / Checklists / Statistics ────────────────────────────


@mcp.tool()
async def get_recent_checklists(
    region_code: str,
    max_results: int | None = None,
) -> str:
    """Get recent checklists submitted in a region.

    Args:
        region_code: eBird region code (e.g. "US-NY")
        max_results: Max number of results (default 10, max 200)
    """
    client = _get_client()
    try:
        data = await client.get_recent_checklists(region_code, max_results=max_results)
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_top_100(
    region_code: str,
    year: int,
    month: int,
    day: int,
    ranked_by: str | None = None,
    max_results: int | None = None,
) -> str:
    """Get the top 100 contributors for a region on a given date.

    Args:
        region_code: eBird region code (e.g. "US-NY")
        year: Year
        month: Month (1-12)
        day: Day (1-31)
        ranked_by: Rank by "spp" (species count) or "cl" (checklist count)
        max_results: Max number of results (default 100)
    """
    client = _get_client()
    try:
        data = await client.get_top_100(
            region_code, year, month, day,
            ranked_by=ranked_by, max_results=max_results,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_checklist_feed(
    region_code: str,
    year: int,
    month: int,
    day: int,
    sort_key: str | None = None,
    max_results: int | None = None,
) -> str:
    """Get a feed of checklists submitted on a date in a region.

    Args:
        region_code: eBird region code
        year: Year
        month: Month (1-12)
        day: Day (1-31)
        sort_key: Sort by "obs_dt" (observation date) or "creation_dt"
        max_results: Max number of results (default 10, max 200)
    """
    client = _get_client()
    try:
        data = await client.get_checklist_feed(
            region_code, year, month, day,
            sort_key=sort_key, max_results=max_results,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_regional_statistics(
    region_code: str,
    year: int,
    month: int,
    day: int,
) -> str:
    """Get birding statistics for a region on a given date.

    Returns species count, checklist count, and contributor count.

    Args:
        region_code: eBird region code (e.g. "US-NY")
        year: Year
        month: Month (1-12)
        day: Day (1-31)
    """
    client = _get_client()
    try:
        data = await client.get_regional_statistics(region_code, year, month, day)
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_species_list(
    region_code: str,
) -> str:
    """Get a list of all species ever observed in a region.

    Args:
        region_code: eBird region code (e.g. "US-NY")
    """
    client = _get_client()
    try:
        data = await client.get_species_list(region_code)
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_checklist(
    sub_id: str,
) -> str:
    """View a specific checklist by its submission ID.

    Args:
        sub_id: Checklist submission ID (e.g. "S12345678")
    """
    client = _get_client()
    try:
        data = await client.get_checklist(sub_id)
        return _format(data)
    finally:
        await client.close()


# ── Hotspots ──────────────────────────────────────────────────────


@mcp.tool()
async def get_region_hotspots(
    region_code: str,
    back: int | None = None,
) -> str:
    """Get birding hotspots in a region.

    Args:
        region_code: eBird region code (e.g. "US-NY", "US-NY-109")
        back: Only hotspots visited in the last N days (1-30)
    """
    client = _get_client()
    try:
        data = await client.get_region_hotspots(region_code, back=back)
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_nearby_hotspots(
    lat: float,
    lng: float,
    back: int | None = None,
    dist: int | None = None,
) -> str:
    """Find birding hotspots near a location.

    Args:
        lat: Latitude (-90 to 90)
        lng: Longitude (-180 to 180)
        back: Only hotspots visited in the last N days (1-30)
        dist: Search radius in km (0-500, default 25)
    """
    client = _get_client()
    try:
        data = await client.get_nearby_hotspots(lat, lng, back=back, dist=dist)
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_hotspot_info(
    loc_id: str,
) -> str:
    """Get details about a specific hotspot.

    Args:
        loc_id: Hotspot location ID (e.g. "L99381")
    """
    client = _get_client()
    try:
        data = await client.get_hotspot_info(loc_id)
        return _format(data)
    finally:
        await client.close()


# ── Taxonomy ──────────────────────────────────────────────────────


@mcp.tool()
async def get_taxonomy(
    cat: str | None = None,
    locale: str | None = None,
    species: str | None = None,
    version: str | None = None,
) -> str:
    """Get the eBird taxonomy (species list with scientific/common names).

    Args:
        cat: Taxonomic category filter (e.g. "species", "issf", "slash")
        locale: Locale for common names (e.g. "en", "es", "fr")
        species: Comma-separated species codes to filter (e.g. "norcar,baleag")
        version: Taxonomy version (e.g. "2024")
    """
    client = _get_client()
    try:
        data = await client.get_taxonomy(
            cat=cat, locale=locale, species=species, version=version,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_taxonomic_forms(
    species_code: str,
) -> str:
    """Get subspecies/forms for a given species.

    Args:
        species_code: eBird species code (e.g. "barswa")
    """
    client = _get_client()
    try:
        data = await client.get_taxonomic_forms(species_code)
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_taxa_locale_codes() -> str:
    """Get the list of supported locale codes for species common names."""
    client = _get_client()
    try:
        data = await client.get_taxa_locale_codes()
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_taxonomy_versions() -> str:
    """Get all available taxonomy versions."""
    client = _get_client()
    try:
        data = await client.get_taxonomy_versions()
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_taxonomic_groups(
    species_grouping: str,
    group_name_locale: str | None = None,
) -> str:
    """Get the list of taxonomic groups (e.g. birds, mammals).

    Args:
        species_grouping: Grouping type: "merlin" or "ebird"
        group_name_locale: Locale for group names (e.g. "en", "es")
    """
    client = _get_client()
    try:
        data = await client.get_taxonomic_groups(
            species_grouping, group_name_locale=group_name_locale,
        )
        return _format(data)
    finally:
        await client.close()


# ── Regions ───────────────────────────────────────────────────────


@mcp.tool()
async def get_region_info(
    region_code: str,
    region_name_format: str | None = None,
) -> str:
    """Get information about a region (name, coordinates, bounds).

    Args:
        region_code: eBird region code (e.g. "US-NY")
        region_name_format: Name format: "detailed", "detailednoqual", "full",
            "namequal", "nameonly", "revdetailed"
    """
    client = _get_client()
    try:
        data = await client.get_region_info(
            region_code, region_name_format=region_name_format,
        )
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_sub_region_list(
    region_type: str,
    region_code: str,
) -> str:
    """Get sub-regions of a given region.

    Args:
        region_type: Type of sub-regions: "country", "subnational1", or "subnational2"
        region_code: Parent region code (e.g. "world", "US", "US-NY")
    """
    client = _get_client()
    try:
        data = await client.get_sub_region_list(region_type, region_code)
        return _format(data)
    finally:
        await client.close()


@mcp.tool()
async def get_adjacent_regions(
    region_code: str,
) -> str:
    """Get regions adjacent to a given region.

    Args:
        region_code: eBird region code (e.g. "US-NY")
    """
    client = _get_client()
    try:
        data = await client.get_adjacent_regions(region_code)
        return _format(data)
    finally:
        await client.close()


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
