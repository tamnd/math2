---
tag: RASDTDEKP7
kind: concept
name: Self-similar process
msc: [60G18]
specializes: [0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Self-similar_process
same_as:
  wikidata: Q7448216
  wikipedia: Self-similar process
---

## Summary

A self-similar process is a [[stochastic process|0QH5ENKZM1]] whose law is unchanged when time is scaled by $a$ and space by $a^H$.
The number $H$ is the Hurst index.
The [[Wiener process|22735FGJV6]] and [[fractional Brownian motion|VC6R7XSKRQ]] are the main examples.
Self-similar processes model random signals that look alike at every scale, in physics, hydrology, networks and finance.

## Explanations

### L1 human

Zoom into the graph of a self-similar process and rescale the vertical axis in the right way: the picture you get is statistically the same as the original.
The vertical rescaling is a power $a^H$ of the horizontal zoom $a$.
For Brownian motion $H = 1/2$: watch it for four times as long and its typical size doubles.
A straight line $t \mapsto t$ is self-similar with $H = 1$ in a trivial, non-random way.
