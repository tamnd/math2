---
tag: 14DWEDXWCC
kind: concept
name: Tarski's axioms
msc: [51M05, 03B30, 03B25]
sources:
  - url: https://en.wikipedia.org/wiki/Tarski%27s_axioms
same_as:
  wikidata: Q7686757
  wikipedia: Tarski's axioms
---

## Summary

Tarski's axioms are an axiom system for plane [[Euclidean geometry|KRZD96GSVC]] in first-order logic, due to Alfred Tarski.
They speak only of points and of two relations: [[betweenness|CE8GX6ADZS]] of three points and congruence of two segments.
Tarski proved that the resulting [[theory|92SWXST1ZM]] is [[complete|655K8Y7VS8]] and decidable: an algorithm decides, for each sentence, whether it is a theorem.

## Explanations

### L1 human

Tarski's axioms describe plane geometry with only points, no lines or circles as basic objects.
Two relations are enough: "$y$ is between $x$ and $z$" and "the segment $xy$ is as long as the segment $zw$".
A line, for example, is the set of points $y$ such that one of $x$, $y$, $z$ is between the other two, for two fixed points $x \ne z$.
Because the theory is decidable, every elementary question about the plane can be decided by a computer in principle.
