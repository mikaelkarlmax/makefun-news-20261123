# Render poster.html to entry.png with headless Chromium (Playwright).
# Local dev tool only -- the grader never runs this; main.ts just copies
# the rendered PNG. Run from the repo root:
#   /tmp/pw-venv/bin/python render.py
# (Python Playwright is used because the venv is already set up for it;
# the render is deterministic: fixed viewport, no network, no animations.)

import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1024, "height": 1024})
        await page.goto(ROOT.joinpath("poster.html").as_uri())
        await page.wait_for_timeout(400)
        await page.screenshot(path=str(ROOT / "entry.png"))
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
    print("rendered entry.png")
