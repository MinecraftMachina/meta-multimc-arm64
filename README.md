# MultiMC Meta Package for arm64

> ### ⚠️ This is an UNOFFICIAL project. DO NOT report any issues to the MultiMC team. ONLY raise issues in THIS repository.

## Supported platforms

Currently, only macOS arm64 (M1) is supported.

## Introduction

This is an alternative meta package for MultiMC. It holds metadata that points MultiMC to all available versions of Minecraft, its dependencies and mod loaders. The idea is that this package can be updated at any time and all versions of MultiMC will use the new data - no update necessary.

Why alternative? Because it supports arm64 platforms, such as the new MacBook M1. Check out [ManyMC](https://github.com/MinecraftMachina/ManyMC), which uses this package by default.

How? LWJGL 3 is forcefully pinned to 3.3.0-mmachina, which is the official arm64 release, but with a patch to fix a crash on boot on Minecraft 1.17 and before.
LWJGL 2 is forcefully pinned to 2.9.4-nightly-20150209-mmachina, which has been manually built for arm64 by [Tanmay Bakshi](https://gist.github.com/tanmayb123).
Minecraft 1.12-1.13 have been forced to use text2speech 1.11.3 to fix a crash on boot.
All versions of Minecraft have been forced to use java-objc-bridge 1.1.0-mmachina, which is manually built for arm64, fixing fullscreen.

This package is set up to automatically synchronize with the original package, thanks to the [pull app](https://wei.github.io/pull/), so any new Minecraft and mod loader versions should be instantly supported.

## Building

To make MultiMC use this meta package, you need to compile it with a special flag, like so:

```bash
cmake -DLauncher_META_URL="https://minecraftmachina.github.io/meta-multimc-arm64/" ...
```

If you update any of the assets manually, use the provided script [fix-assets.py](fix-assets.py) to update their checksums and sizes.
