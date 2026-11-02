---
tag: YHJHPRKQ6D
kind: concept
name: Poincaré–Lindstedt method
msc: ["34E10", 34C15]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Lindstedt_method
same_as:
  wikidata: Q7207873
  wikipedia: Poincaré–Lindstedt method
---

## Summary

The Poincaré–Lindstedt method finds approximate [[periodic solutions|FHNDX22WMK]] of weakly nonlinear oscillators.
It expands both the solution and its frequency in powers of the small parameter.
The frequency corrections are chosen to remove secular terms, which grow without bound in time and spoil a naive expansion.
The method shows how nonlinearity shifts the frequency of an oscillation with its amplitude.

## Explanations

### L1 human

A pendulum with a large swing has a slightly different period from one with a tiny swing.
If one expands the motion in a small parameter but keeps the old period, the error grows with time.
The method lets the period change too, and adjusts it so that the error stays bounded.
For $x'' + x + \varepsilon x^3 = 0$ with amplitude $a$, it gives the frequency $1 + \frac{3}{8} \varepsilon a^2$ up to $O(\varepsilon^2)$.
