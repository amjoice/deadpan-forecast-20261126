#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist, in one line.

Siltmere sits in fog so thick its lighthouse needs guiding, and the
ferry waits until it can find the dock. Pure stdlib, deterministic,
no network, no secrets; writes a single line of at most 160 characters
to /output/entry.txt with no trailing newline.
"""
import os

# The forecast, assembled from its parts so the wording stays in one place.
_CITY = "Siltmere today:"
_CONDITION = "fog so thick the lighthouse is guiding itself, high 58, visibility 40 feet."
_ADVICE = "Ferry leaves when it can find the dock."


def build_forecast():
    """Return the full one-line forecast, exactly 131 characters."""
    return " ".join((_CITY, _CONDITION, _ADVICE))


def main():
    forecast = build_forecast()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(forecast)


if __name__ == "__main__":
    main()
