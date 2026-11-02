---
tag: TBNP6KYW4Z
kind: concept
name: Triebel–Lizorkin space
msc: ["46E35", 42B35]
sources:
  - url: https://en.wikipedia.org/wiki/Triebel%E2%80%93Lizorkin_space
same_as:
  wikidata: Q7841428
  wikipedia: Triebel–Lizorkin space
---

## Summary

A Triebel–Lizorkin space $F^s_{p,q}(\R^n)$ is a space of [[tempered distributions|AES2T5JPFP]] defined, like a [[Besov space|95QBBPRJ9E]], by splitting the [[Fourier transform|DPVM34ADZV]] into dyadic frequency shells.
The difference is the order of the norms.
One first takes an $\ell^q$ sum over the shells at each point, and then the $L^p$ norm in space.
The scale contains the [[Lp spaces|SASP14MA1Z]] for $1 < p < \infty$, the [[Sobolev spaces|M4CEZ5K9HP]] $W^{k,p}$ for $1 < p < \infty$, and the local Hardy spaces.
It gives one framework for many function spaces of harmonic analysis and partial differential equations.

## Explanations

### L1 human

Split a function into pieces of frequency about $2^j$ and weight the $j$-th piece by $2^{js}$.
A Besov norm measures each weighted piece in $L^p$ and then adds up the results.
A Triebel–Lizorkin norm adds up the weighted pieces at each point first, through a square sum when $q = 2$, and then measures the result in $L^p$.
For $q = 2$ this square function is the classical tool of Littlewood–Paley theory, and it recovers the $L^p$ and Sobolev norms.
