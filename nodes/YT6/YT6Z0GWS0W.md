---
tag: YT6Z0GWS0W
kind: concept
name: Nevanlinna characteristic
msc: ["30D35"]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna_theory
---

## Summary

The Nevanlinna characteristic $T(r, f)$ of a [[meromorphic function|0NSD1TPHR0]] $f$ on $\C$ measures its growth on the disc of radius $r$.
It adds a term for the size of $f$ on the circle $\abs{z} = r$ and a term that counts the poles inside.
For entire functions it plays the role of $\log M(r)$, and for meromorphic functions it replaces the degree of a rational function.
It is the central quantity of [[Nevanlinna theory|1EHH63VNAD]].

## Explanations

### L1 human

For an entire function, growth is measured by the maximum of $\abs{f}$ on circles.
A meromorphic function has poles, where it is infinite, so the maximum is useless.
Nevanlinna's idea is to average $\log \abs{f}$ where it is large on the circle and to add a logarithmic count of the poles inside.
For a rational function of degree $d$, $T(r, f)$ is about $d \log r$.
For $e^z$, $T(r, f) = r/\pi$.
