#!/usr/bin/env bash
ce2fs -i $(find ./dist -name 'DS3_TGA_v*.CT') "$@"
