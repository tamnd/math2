---
tag: F12A5QKW8Z
kind: concept
name: Walsh function
msc: [42C10]
sources:
  - url: https://en.wikipedia.org/wiki/Walsh_function
same_as:
  wikidata: Q1934233
  wikipedia: Walsh function
---

## Summary

The Walsh functions are functions on $[0, 1)$ that take only the values $1$ and $-1$.
They are the finite products of [[Rademacher functions|51GRFQ4WY6]], and together they form a complete orthonormal system of $L^2([0, 1))$.
They are a digital analogue of the trigonometric system, and they lead to the [[Walsh–Hadamard transform|K784BA2WHV]].

## Explanations

### L1 human

Think of a square wave that jumps between $+1$ and $-1$.
The Rademacher functions are square waves that flip sign faster and faster, one for each binary digit.
A Walsh function multiplies some of these square waves together, chosen by the binary digits of an index $n$.
For example, $w_3 = r_1 r_2$ equals $1$ on $[0, \tfrac14)$, $-1$ on $[\tfrac14, \tfrac34)$, and $1$ on $[\tfrac34, 1)$.
Every square-integrable function on $[0, 1)$ can be expanded in Walsh functions, much as in a Fourier series.
