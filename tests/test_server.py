from __future__ import annotations

import json
from unittest.mock import AsyncMock, patch

import pytest

from ebirdmcp.server import (
    get_adjacent_regions,
    get_checklist,
    get_checklist_feed,
    get_historic_observations,
    get_hotspot_info,
    get_nearby_hotspots,
    get_nearest_species_observations,
    get_recent_checklists,
    get_recent_nearby_notable_observations,
    get_recent_nearby_observations,
    get_recent_nearby_species_observations,
    get_recent_notable_observations,
    get_recent_observations,
    get_recent_species_observations,
    get_region_hotspots,
    get_region_info,
    get_regional_statistics,
    get_species_list,
    get_sub_region_list,
    get_taxa_locale_codes,
    get_taxonomic_forms,
    get_taxonomic_groups,
    get_taxonomy,
    get_taxonomy_versions,
    get_top_100,
)


def _mock_client(method_name: str, return_value: object):
    mock = AsyncMock()
    mock.close = AsyncMock()
    setattr(mock, method_name, AsyncMock(return_value=return_value))
    return patch("ebirdmcp.server._get_client", return_value=mock)


@pytest.mark.asyncio
async def test_get_recent_observations():
    data = [{"speciesCode": "norcar", "comName": "Northern Cardinal"}]
    with _mock_client("get_recent_observations", data):
        result = await get_recent_observations("US-NY")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_recent_notable_observations():
    data = [{"speciesCode": "snogoo", "comName": "Snow Goose"}]
    with _mock_client("get_recent_notable_observations", data):
        result = await get_recent_notable_observations("US-NY")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_recent_species_observations():
    data = [{"speciesCode": "norcar", "locName": "Central Park"}]
    with _mock_client("get_recent_species_observations", data):
        result = await get_recent_species_observations("US-NY", "norcar")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_recent_nearby_observations():
    data = [{"speciesCode": "baleag", "lat": 40.7}]
    with _mock_client("get_recent_nearby_observations", data):
        result = await get_recent_nearby_observations(40.7, -73.9)
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_recent_nearby_species_observations():
    data = [{"speciesCode": "norcar"}]
    with _mock_client("get_recent_nearby_species_observations", data):
        result = await get_recent_nearby_species_observations("norcar", 40.7, -73.9)
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_nearest_species_observations():
    data = [{"speciesCode": "norcar", "locName": "Prospect Park"}]
    with _mock_client("get_nearest_species_observations", data):
        result = await get_nearest_species_observations("norcar", 40.7, -73.9)
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_recent_nearby_notable_observations():
    data = [{"speciesCode": "snogoo"}]
    with _mock_client("get_recent_nearby_notable_observations", data):
        result = await get_recent_nearby_notable_observations(40.7, -73.9)
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_historic_observations():
    data = [{"speciesCode": "norcar", "obsDt": "2024-01-15"}]
    with _mock_client("get_historic_observations", data):
        result = await get_historic_observations("US-NY", 2024, 1, 15)
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_recent_checklists():
    data = [{"subId": "S12345", "loc": {"name": "Central Park"}}]
    with _mock_client("get_recent_checklists", data):
        result = await get_recent_checklists("US-NY")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_top_100():
    data = [{"userDisplayName": "birder1", "numSpecies": 50}]
    with _mock_client("get_top_100", data):
        result = await get_top_100("US-NY", 2024, 5, 10)
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_checklist_feed():
    data = [{"subId": "S12345"}]
    with _mock_client("get_checklist_feed", data):
        result = await get_checklist_feed("US-NY", 2024, 5, 10)
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_regional_statistics():
    data = {"numSpecies": 150, "numChecklists": 200}
    with _mock_client("get_regional_statistics", data):
        result = await get_regional_statistics("US-NY", 2024, 5, 10)
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_species_list():
    data = ["norcar", "baleag", "amecro"]
    with _mock_client("get_species_list", data):
        result = await get_species_list("US-NY")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_checklist():
    data = {"subId": "S12345", "obs": []}
    with _mock_client("get_checklist", data):
        result = await get_checklist("S12345")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_region_hotspots():
    data = [{"locId": "L99381", "locName": "Central Park"}]
    with _mock_client("get_region_hotspots", data):
        result = await get_region_hotspots("US-NY")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_nearby_hotspots():
    data = [{"locId": "L99381", "locName": "Central Park"}]
    with _mock_client("get_nearby_hotspots", data):
        result = await get_nearby_hotspots(40.7, -73.9)
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_hotspot_info():
    data = {"locId": "L99381", "locName": "Central Park", "lat": 40.78}
    with _mock_client("get_hotspot_info", data):
        result = await get_hotspot_info("L99381")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_taxonomy():
    data = [{"speciesCode": "norcar", "comName": "Northern Cardinal"}]
    with _mock_client("get_taxonomy", data):
        result = await get_taxonomy()
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_taxonomic_forms():
    data = ["barswa1", "barswa2"]
    with _mock_client("get_taxonomic_forms", data):
        result = await get_taxonomic_forms("barswa")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_taxa_locale_codes():
    data = [{"code": "en", "name": "English"}]
    with _mock_client("get_taxa_locale_codes", data):
        result = await get_taxa_locale_codes()
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_taxonomy_versions():
    data = [{"authorityVer": 2024, "latest": True}]
    with _mock_client("get_taxonomy_versions", data):
        result = await get_taxonomy_versions()
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_taxonomic_groups():
    data = [{"groupName": "Birds", "groupOrder": 1}]
    with _mock_client("get_taxonomic_groups", data):
        result = await get_taxonomic_groups("ebird")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_region_info():
    data = {"result": "New York", "bounds": {}}
    with _mock_client("get_region_info", data):
        result = await get_region_info("US-NY")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_sub_region_list():
    data = [{"code": "US-NY-061", "name": "New York County"}]
    with _mock_client("get_sub_region_list", data):
        result = await get_sub_region_list("subnational2", "US-NY")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_get_adjacent_regions():
    data = [{"code": "US-CT", "name": "Connecticut"}]
    with _mock_client("get_adjacent_regions", data):
        result = await get_adjacent_regions("US-NY")
    assert json.loads(result) == data


@pytest.mark.asyncio
async def test_missing_api_key():
    with patch.dict("os.environ", {}, clear=True):
        with pytest.raises(RuntimeError, match="EBIRD_API_KEY"):
            from ebirdmcp.server import _get_client
            _get_client()
