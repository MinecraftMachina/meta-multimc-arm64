# ManyMC Meta Package for arm64

## Supported platforms

Currently, only macOS arm64 (M1) is supported.

## Introduction

This is the meta package used for [ManyMC](https://github.com/MinecraftMachina/ManyMC). It holds metadata that points ManyMC to all available versions of Minecraft, its dependencies and mod loaders. The idea is that this package can be updated at any time and all versions of ManyMC will use the new data - no update necessary.

## Changes from PolyMC meta package

- [lwjgl3-mmachina](https://github.com/MinecraftMachina/lwjgl3) replaces LWJGL3, bringing upstream arm64 support and containing a patch to fix crash on boot on Minecraft 1.17 and before.
- [lwjgl2-mmachina](https://github.com/MinecraftMachina/lwjgl) replaces LWJGL2, containing patches for MacOS on arm64.
- text2speech 1.11.3 has been forced on Minecraft 1.12-1.13 to fix a crash on boot.
- [java-objc-bridge-mmachina](https://github.com/MinecraftMachina/Java-Objective-C-Bridge) replaces Java-Objective-C-Bridge, fixing fullscreen.

This repo is hooked to the upstream meta, so updates will be instant.

## Development

If you update any of the assets manually, use the provided script [fix-assets.py](fix-assets.py) to update their checksums and sizes.
