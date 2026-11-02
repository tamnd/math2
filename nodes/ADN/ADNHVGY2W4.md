---
tag: ADNHVGY2W4
kind: concept
name: Tautological one-form
msc: [53D05, 37J39]
specializes: [0E3G0GRPZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Tautological_one-form
same_as:
  wikidata: Q1014878
  wikipedia: Tautological one-form
---

## Summary

The tautological one-form is a canonical $1$-form on the cotangent bundle of any smooth manifold.
In coordinates $(q, p)$ it is $\sum_i p_i \, dq^i$, and it needs no choice of coordinates or metric.
Its exterior derivative gives the canonical [[symplectic form|CAN490EPRT]] of the cotangent bundle, which makes every cotangent bundle a symplectic manifold.
It is also called the Liouville form or the canonical one-form.

## Explanations

### L1 human

A point of the cotangent bundle is a pair: a position $q$ in the manifold and a covector $p$ at $q$, which in mechanics is a momentum.
The tautological form takes a small motion of such a pair, looks only at how the position moves, and feeds that motion to $p$.
So it uses the point itself as the instructions for what to measure, which is why it is called tautological.
On the cotangent bundle of the line, with coordinates $(q, p)$, it is $p \, dq$.
