// The World in One Day — Monday 23 November 2026 (news-image-20261123).
// A one-image news poster: 46 verified stories from a single UTC day,
// drawn in poster.html and rendered to entry.png with headless Chromium.
// This program only copies that image to the output directory.
// Node 22, standard library only; no network, no randomness, no writes
// other than the single output file. Both runs produce identical bytes.
//
// Run it outside the grader's container with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
