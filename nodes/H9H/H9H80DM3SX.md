---
tag: H9H80DM3SX
kind: concept
name: Wiener amalgam space
msc: [42B35, "46E30"]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_amalgam_space
same_as:
  wikidata: Q7999135
  wikipedia: Wiener amalgam space
---

## Summary

A Wiener amalgam space measures a function with one norm locally and another norm globally.
The basic example $W(L^p, \ell^q)$ takes the $L^p$ norm of the function on each unit cube and then the $\ell^q$ norm of the resulting sequence.
Such spaces separate the local regularity of a function from its decay at infinity.
They go back to Norbert Wiener, were developed in general by Hans Feichtinger, and are used in [[time–frequency analysis|GQFPVXEWK1]] and sampling theory.

## Explanations

### L1 human

Cut the line or the space into unit cubes.
On each cube, measure the function with one ruler, for instance its largest value.
Then add up these local sizes over all cubes with a second ruler.
A function with tall but narrow spikes can fail the local test, and a function with slow decay can fail the global test.
For example, $1/(1 + \abs{x})$ on the line has local maxima about $1/\abs{k}$ on the cube near $k$, so its sizes have finite sum of squares but infinite plain sum.
