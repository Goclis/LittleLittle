#!/usr/bin/env sh

cs=$(defaults read com.apple.finder AppleShowAllFiles)

case "$cs" in
    NO) defaults write com.apple.finder AppleShowAllFiles YES;;
    YES) defaults write com.apple.finder AppleShowAllFiles NO;;
esac
