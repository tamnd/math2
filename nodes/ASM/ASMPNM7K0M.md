---
tag: ASMPNM7K0M
kind: concept
name: P-adic analysis
msc: [30G06, 11S80, "26E30"]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_analysis
same_as:
  wikidata: Q2845236
  wikipedia: P-adic analysis
---

## Summary

$p$-adic analysis is the analysis of functions of [[$p$-adic numbers|BT6T702C28]], where nearness is measured by the [[$p$-adic absolute value|WGN82TCEF2]] instead of the usual one.
This absolute value is ultrametric, which makes many things simpler than in real analysis: a series converges as soon as its terms tend to $0$.
Other things behave differently: the $p$-adic integers form a compact, totally disconnected space, and the exponential series converges only on a small disc.
The subject is a main tool of modern number theory, for example in $p$-adic $L$-functions and in the study of congruences.

## Explanations

### L1 human

In the $p$-adic world, a number is small when it is divisible by a high power of the prime $p$.
So $p, p^2, p^3, \ldots$ tend to $0$, and the series $1 + p + p^2 + \cdots$ converges, to $1/(1 - p)$.
One can then do calculus with limits, series, continuity and derivatives, as over the reals.
Much of it works the same way, but some facts change: for example, a function with derivative $0$ everywhere on $\Z_p$ need not be constant.
