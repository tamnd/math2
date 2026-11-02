---
tag: 9V11N8VVTP
kind: concept
name: Handle decomposition
msc: [57R65, 57N99]
sources:
  - url: https://en.wikipedia.org/wiki/Handle_decomposition
same_as:
  wikidata: Q2852446
  wikipedia: Handle decomposition
---

## Summary

A handle decomposition builds a manifold from a ball, or from a given boundary, by attaching handles $D^k \times D^{n-k}$ one after another.
Each handle is glued along part of its boundary.
It is the smooth analogue of a CW structure: a $k$-handle plays the role of a $k$-cell, thickened to full dimension.
Every compact smooth manifold has a handle decomposition, obtained from a [[Morse function|KPQ96640ZJ]], with one $k$-handle for each critical point of index $k$.
Handle decompositions are the main tool in the proof of the h-cobordism theorem and in surgery theory.
In dimensions $3$ and $4$ they underlie Kirby calculus.

## Explanations

### L1 human

Build a surface out of clay: start with a disc, glue on flat strips along their two ends, and cap off with more discs.
The discs at the start are $0$-handles, the strips are $1$-handles, and the final caps are $2$-handles.
A torus can be built from one disc, two strips and one cap.
In higher dimensions the pieces are thickened discs of the same dimension as the manifold, glued along part of their boundary.
