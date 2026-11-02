---
tag: 1GHQMBR7DE
kind: concept
name: Multiresolution analysis
msc: [42C40, 65T60]
sources:
  - url: https://en.wikipedia.org/wiki/Multiresolution_analysis
same_as:
  wikidata: Q1952516
  wikipedia: Multiresolution analysis
---

## Summary

A multiresolution analysis of $L^2(\R)$ is a nested chain of closed subspaces $V_j$, one for each scale $2^{-j}$.
The spaces are related by dilation by $2$, and $V_0$ is spanned by the integer translates of one scaling function.
Stéphane Mallat and Yves Meyer introduced it as the framework in which orthonormal [[wavelets|4PZ35C0GV3]] are built.
The wavelet spaces are the orthogonal complements of $V_j$ in $V_{j+1}$, and the [[discrete wavelet transform|P3H4MMC4ZH]] moves between the levels with two filters.

## Explanations

### L1 human

Think of a photograph seen at several resolutions.
The space $V_j$ holds all the pictures that can be drawn with pixels of size $2^{-j}$.
Each finer space contains the coarser ones, and as the pixels shrink one can approximate any picture.
The detail that one gains by going from $V_j$ to $V_{j+1}$ is carried by the wavelets of scale $2^{-j}$.
In the simplest case $V_j$ consists of the functions that are constant on each interval $[k 2^{-j}, (k+1) 2^{-j})$.
