---
tag: NX8RE9B72A
kind: concept
name: Total variation diminishing scheme
msc: [65M08, 65M12, 35L65]
sources:
  - url: https://en.wikipedia.org/wiki/Total_variation_diminishing
same_as:
  wikidata: Q7828154
  wikipedia: Total variation diminishing
---

## Summary

A total variation diminishing (TVD) scheme is a numerical scheme for a scalar [[conservation law|8RA7AMWSAF]] in one space dimension.
Its discrete [[total variation|8QA5DEWNYD]] never increases from one time step to the next.
This copies a property of the exact entropy solutions, and it rules out the creation of new local extrema.
So the scheme gives no spurious oscillations near shocks.
The notion was introduced by Harten in 1983, and it is the design principle of the high-resolution schemes built with flux limiters.

## Explanations

### L1 human

The total variation of a list of numbers is the sum of the sizes of the jumps between neighbours: it measures how much the profile goes up and down.
Wiggles near a shock increase this sum.
A TVD scheme guarantees that the sum never grows, so wiggles cannot appear.
For example, a step from $1$ to $0$ has total variation $1$, and a TVD scheme can smear the step but never turn it into an overshoot such as $1, 1.1, 0.4, 0$.
