---
tag: DW5SBZXK6R
kind: concept
name: Loeb measure
msc: ["28E05", "26E35"]
specializes: [PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Loeb_space
same_as:
  wikidata: Q17103336
  wikipedia: Loeb space
---

## Summary

A Loeb measure is a genuine countably additive [[measure|PR11BZQQPG]] built from a finitely additive measure inside a nonstandard model of analysis.
One takes the standard part of the nonstandard measure and extends it to a σ-algebra.
Introduced by Peter Loeb, it lets hyperfinite objects, such as a finite set with an infinite number of points, serve as ordinary measure spaces.
It is the main tool of nonstandard measure theory and gives nonstandard constructions of Lebesgue measure and of Brownian motion.

## Explanations

### L1 human

In nonstandard analysis there are "finite" sets whose number of elements $N$ is an infinitely large hypernatural number.
On such a set one can give each point the infinitesimal weight $1/N$, as for a fair die with $N$ faces.
The resulting sizes are hyperreal numbers, so one rounds each of them to the nearest real number.
Loeb showed that the rounded sizes extend to a true probability measure.
For example, mapping the points $k/N$ for $k = 1, \ldots, N$ to their standard parts in $[0, 1]$ turns this uniform measure into Lebesgue measure on $[0, 1]$.
