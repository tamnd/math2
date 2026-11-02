---
tag: D3BN7MBKTR
kind: concept
name: Path space fibration
msc: [55R05, 55P35]
sources:
  - url: https://en.wikipedia.org/wiki/Path_space_fibration
same_as:
  wikidata: Q25100552
  wikipedia: Path space fibration
---

## Summary

Let $(X, x_0)$ be a [[pointed space|T9DG8DDE75]] and $PX$ the space of paths that start at $x_0$.
The path space fibration is the map $PX \to X$ that sends each path to its end point.
It is a fibration, its total space $PX$ is contractible, and its fiber over $x_0$ is the [[loop space|2JFF5F3EGF]] $\Omega X$.
From its [[long exact sequence of homotopy groups|E0RV5D1GQ0]] one gets $\pi_n(\Omega X) \cong \pi_{n+1}(X)$.
It plays the role of a universal bundle for loops and is the basic input of the Serre spectral sequence computations of loop spaces.

## Explanations

### L1 human

Fix a home point $x_0$ in $X$.
A point of the path space is a walk in $X$ that starts at home, and the map records where the walk ends.
All walks can be shrunk back to the walk that stays at home, so the path space has no shape of its own.
The walks that end at home are the loops, so the loops form the fiber over $x_0$.
