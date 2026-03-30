from __future__ import annotations

from typing import Any

import httpx

BASE_URL = "https://api.ebird.org"


class EBirdClient:
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key
        self._client = httpx.AsyncClient(
            base_url=BASE_URL,
            headers={"x-ebirdapitoken": api_key},
            timeout=30.0,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def _get(
        self, path: str, params: dict[str, Any] | None = None
    ) -> Any:
        cleaned = {k: v for k, v in (params or {}).items() if v is not None}
        resp = await self._client.get(path, params=cleaned)
        resp.raise_for_status()
        return resp.json()

    async def _get_text(
        self, path: str, params: dict[str, Any] | None = None
    ) -> str:
        cleaned = {k: v for k, v in (params or {}).items() if v is not None}
        resp = await self._client.get(path, params=cleaned)
        resp.raise_for_status()
        return resp.text

    # ── Observations ──────────────────────────────────────────────

    async def get_recent_observations(
        self,
        region_code: str,
        back: int | None = None,
        cat: str | None = None,
        hotspot: bool | None = None,
        include_provisional: bool | None = None,
        max_results: int | None = None,
        r: str | None = None,
        spp_locale: str | None = None,
    ) -> list[dict]:
        return await self._get(
            f"/v2/data/obs/{region_code}/recent",
            {
                "back": back,
                "cat": cat,
                "hotspot": hotspot,
                "includeProvisional": include_provisional,
                "maxResults": max_results,
                "r": r,
                "sppLocale": spp_locale,
            },
        )

    async def get_recent_notable_observations(
        self,
        region_code: str,
        back: int | None = None,
        detail: str | None = None,
        hotspot: bool | None = None,
        max_results: int | None = None,
        r: str | None = None,
        spp_locale: str | None = None,
    ) -> list[dict]:
        return await self._get(
            f"/v2/data/obs/{region_code}/recent/notable",
            {
                "back": back,
                "detail": detail,
                "hotspot": hotspot,
                "maxResults": max_results,
                "r": r,
                "sppLocale": spp_locale,
            },
        )

    async def get_recent_species_observations(
        self,
        region_code: str,
        species_code: str,
        back: int | None = None,
        hotspot: bool | None = None,
        include_provisional: bool | None = None,
        max_results: int | None = None,
        r: str | None = None,
        spp_locale: str | None = None,
    ) -> list[dict]:
        return await self._get(
            f"/v2/data/obs/{region_code}/recent/{species_code}",
            {
                "back": back,
                "hotspot": hotspot,
                "includeProvisional": include_provisional,
                "maxResults": max_results,
                "r": r,
                "sppLocale": spp_locale,
            },
        )

    async def get_recent_nearby_observations(
        self,
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
    ) -> list[dict]:
        return await self._get(
            "/v2/data/obs/geo/recent",
            {
                "lat": lat,
                "lng": lng,
                "dist": dist,
                "back": back,
                "cat": cat,
                "hotspot": hotspot,
                "includeProvisional": include_provisional,
                "maxResults": max_results,
                "sort": sort,
                "sppLocale": spp_locale,
            },
        )

    async def get_recent_nearby_species_observations(
        self,
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
    ) -> list[dict]:
        return await self._get(
            f"/v2/data/obs/geo/recent/{species_code}",
            {
                "lat": lat,
                "lng": lng,
                "dist": dist,
                "back": back,
                "cat": cat,
                "hotspot": hotspot,
                "includeProvisional": include_provisional,
                "maxResults": max_results,
                "sort": sort,
                "sppLocale": spp_locale,
            },
        )

    async def get_nearest_species_observations(
        self,
        species_code: str,
        lat: float,
        lng: float,
        dist: int | None = None,
        back: int | None = None,
        hotspot: bool | None = None,
        include_provisional: bool | None = None,
        max_results: int | None = None,
        spp_locale: str | None = None,
    ) -> list[dict]:
        return await self._get(
            f"/v2/data/nearest/geo/recent/{species_code}",
            {
                "lat": lat,
                "lng": lng,
                "dist": dist,
                "back": back,
                "hotspot": hotspot,
                "includeProvisional": include_provisional,
                "maxResults": max_results,
                "sppLocale": spp_locale,
            },
        )

    async def get_recent_nearby_notable_observations(
        self,
        lat: float,
        lng: float,
        dist: int | None = None,
        back: int | None = None,
        detail: str | None = None,
        hotspot: bool | None = None,
        max_results: int | None = None,
        spp_locale: str | None = None,
    ) -> list[dict]:
        return await self._get(
            "/v2/data/obs/geo/recent/notable",
            {
                "lat": lat,
                "lng": lng,
                "dist": dist,
                "back": back,
                "detail": detail,
                "hotspot": hotspot,
                "maxResults": max_results,
                "sppLocale": spp_locale,
            },
        )

    async def get_historic_observations(
        self,
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
        r: str | None = None,
        spp_locale: str | None = None,
    ) -> list[dict]:
        return await self._get(
            f"/v2/data/obs/{region_code}/historic/{year}/{month}/{day}",
            {
                "cat": cat,
                "detail": detail,
                "hotspot": hotspot,
                "includeProvisional": include_provisional,
                "maxResults": max_results,
                "rank": rank,
                "r": r,
                "sppLocale": spp_locale,
            },
        )

    # ── Product / Checklists / Stats ──────────────────────────────

    async def get_recent_checklists(
        self,
        region_code: str,
        max_results: int | None = None,
    ) -> list[dict]:
        return await self._get(
            f"/v2/product/lists/{region_code}",
            {"maxResults": max_results},
        )

    async def get_top_100(
        self,
        region_code: str,
        year: int,
        month: int,
        day: int,
        ranked_by: str | None = None,
        max_results: int | None = None,
    ) -> list[dict]:
        return await self._get(
            f"/v2/product/top100/{region_code}/{year}/{month}/{day}",
            {"rankedBy": ranked_by, "maxResults": max_results},
        )

    async def get_checklist_feed(
        self,
        region_code: str,
        year: int,
        month: int,
        day: int,
        sort_key: str | None = None,
        max_results: int | None = None,
    ) -> list[dict]:
        return await self._get(
            f"/v2/product/lists/{region_code}/{year}/{month}/{day}",
            {"sortKey": sort_key, "maxResults": max_results},
        )

    async def get_regional_statistics(
        self,
        region_code: str,
        year: int,
        month: int,
        day: int,
    ) -> dict:
        return await self._get(
            f"/v2/product/stats/{region_code}/{year}/{month}/{day}"
        )

    async def get_species_list(
        self,
        region_code: str,
    ) -> list[str]:
        return await self._get(f"/v2/product/spplist/{region_code}")

    async def get_checklist(
        self,
        sub_id: str,
    ) -> dict:
        return await self._get(f"/v2/product/checklist/view/{sub_id}")

    # ── Hotspots ──────────────────────────────────────────────────

    async def get_region_hotspots(
        self,
        region_code: str,
        back: int | None = None,
        fmt: str | None = None,
    ) -> list[dict] | str:
        if fmt == "csv":
            return await self._get_text(
                f"/v2/ref/hotspot/{region_code}",
                {"back": back, "fmt": fmt},
            )
        return await self._get(
            f"/v2/ref/hotspot/{region_code}",
            {"back": back, "fmt": fmt},
        )

    async def get_nearby_hotspots(
        self,
        lat: float,
        lng: float,
        back: int | None = None,
        dist: int | None = None,
        fmt: str | None = None,
    ) -> list[dict] | str:
        if fmt == "csv":
            return await self._get_text(
                "/v2/ref/hotspot/geo",
                {"lat": lat, "lng": lng, "back": back, "dist": dist, "fmt": fmt},
            )
        return await self._get(
            "/v2/ref/hotspot/geo",
            {"lat": lat, "lng": lng, "back": back, "dist": dist, "fmt": fmt},
        )

    async def get_hotspot_info(
        self,
        loc_id: str,
    ) -> dict:
        return await self._get(f"/v2/ref/hotspot/info/{loc_id}")

    # ── Taxonomy ──────────────────────────────────────────────────

    async def get_taxonomy(
        self,
        cat: str | None = None,
        fmt: str | None = None,
        locale: str | None = None,
        species: str | None = None,
        version: str | None = None,
    ) -> list[dict] | str:
        if fmt == "csv":
            return await self._get_text(
                "/v2/ref/taxonomy/ebird",
                {
                    "cat": cat,
                    "fmt": fmt,
                    "locale": locale,
                    "species": species,
                    "version": version,
                },
            )
        return await self._get(
            "/v2/ref/taxonomy/ebird",
            {
                "cat": cat,
                "fmt": fmt,
                "locale": locale,
                "species": species,
                "version": version,
            },
        )

    async def get_taxonomic_forms(
        self,
        species_code: str,
    ) -> list[str]:
        return await self._get(f"/v2/ref/taxon/forms/{species_code}")

    async def get_taxa_locale_codes(self) -> list[dict]:
        return await self._get("/v2/ref/taxa-locales/ebird")

    async def get_taxonomy_versions(self) -> list[dict]:
        return await self._get("/v2/ref/taxonomy/versions")

    async def get_taxonomic_groups(
        self,
        species_grouping: str,
        group_name_locale: str | None = None,
    ) -> list[dict]:
        return await self._get(
            f"/v2/ref/sppgroup/{species_grouping}",
            {"groupNameLocale": group_name_locale},
        )

    # ── Regions ───────────────────────────────────────────────────

    async def get_region_info(
        self,
        region_code: str,
        region_name_format: str | None = None,
    ) -> dict:
        return await self._get(
            f"/v2/ref/region/info/{region_code}",
            {"regionNameFormat": region_name_format},
        )

    async def get_sub_region_list(
        self,
        region_type: str,
        region_code: str,
    ) -> list[dict]:
        return await self._get(
            f"/v2/ref/region/list/{region_type}/{region_code}"
        )

    async def get_adjacent_regions(
        self,
        region_code: str,
    ) -> list[dict]:
        return await self._get(f"/v2/ref/adjacent/{region_code}")
