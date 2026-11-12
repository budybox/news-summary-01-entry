#!/usr/bin/env python3
"""
Photo geolocation agent skeleton for make.fun bounty `photo-geolocator-01`.
Receives street-level photos and answers latitude/longitude.
Placeholder implementation: answers (0, 0) for every photo until you add
real geolocation logic (vision model via gateway, image fingerprinting, etc.).
"""

import json
import sys
import os


def geolocate_photo(photo_bytes: bytes) -> dict:
    """
    Given a street-level photo (raw bytes), return {"lat": float, "lon": float}.

    Replace this stub with real logic:
      - Call make.fun vision gateway (allowlisted model) with base64 image
      - Or use image fingerprinting / model-free heuristics
    """
    return {"lat": 0.0, "lon": 0.0}


def main():
    """
    Agent entry point. The make.fun harness calls this per photo.
    Expected input: JSON on stdin with {"photo_base64": "..."} or similar
    Expected output: JSON on stdout {"lat": ..., "lon": ...}
    """
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw else {}
    except Exception:
        payload = {}

    # Accept either base64 or raw path – adapt to harness contract in kit
    photo_b64 = payload.get("photo_base64") or payload.get("image") or ""
    photo_id = payload.get("photo_id") or payload.get("id") or "unknown"

    result = geolocate_photo(photo_b64.encode() if isinstance(photo_b64, str) else b"")

    out = {
        "photo_id": photo_id,
        "lat": float(result.get("lat", 0.0)),
        "lon": float(result.get("lon", 0.0)),
    }
    print(json.dumps(out))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
