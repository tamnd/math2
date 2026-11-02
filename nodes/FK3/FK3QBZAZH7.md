---
tag: FK3QBZAZH7
kind: concept
name: Lebesgue–Stieltjes integration
msc: [26A42, 28A25]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue%E2%80%93Stieltjes_integration
same_as:
  wikidata: Q3799278
  wikipedia: Lebesgue–Stieltjes integration
---

## Summary

Lebesgue–Stieltjes integration integrates a function $f$ against a non-decreasing function $g$ on the real line, written $\int f \, dg$.
It is the Lebesgue integral with respect to the Lebesgue–Stieltjes measure of $g$, which gives each interval $(a, b]$ the mass $g(b) - g(a)$.
It extends the Riemann–Stieltjes integral to all measurable functions, and to functions $g$ of bounded variation by splitting $g$ into monotone parts.
It is the language of probability distributions on the line, where $g$ is a cumulative distribution function.

## Explanations

### L1 human

In an ordinary integral each small piece of the line counts with its length.
In a Stieltjes integral it counts with the increase of a given function $g$ over that piece.
Where $g$ is flat, nothing is counted; where $g$ jumps, the point of the jump gets a mass equal to the jump.
For example, if $g$ jumps from $0$ to $1$ at $0$ and is constant elsewhere, then $\int f \, dg = f(0)$.
