---
tag: XP5JC1VXKZ
kind: concept
name: Branch point
msc: [30B40, 30F10]
sources:
  - url: https://en.wikipedia.org/wiki/Branch_point
same_as:
  wikidata: Q2625091
  wikipedia: Branch point
---

## Summary

A branch point of a [[multivalued function|03CPD1HGF3]] is a point with this property: going once around it along a small loop changes the value.
See the [[definition|XDNRXKH3KT]].
The square root has branch points at $0$ and $\infty$, and so does the [[complex logarithm|02QGGD5G87]].
Branch points are the reason for [[branch cuts|0W8QHVSN95]].
When the function is made single-valued on a [[Riemann surface|5K0N8QMV6Q]], they become the ramification points of a [[branched covering|YARENZRXTD]].

## Explanations

### L1 human

Follow $\sqrt{z}$ continuously while $z$ walks once around the circle $\abs{z} = 1$, starting at $z = 1$ with $\sqrt{1} = 1$.
When $z = e^{it}$ goes from $t = 0$ to $t = 2\pi$, the chosen root $e^{it/2}$ goes from $1$ to $-1$.
So you come back to the same $z$ with a different value of the root.
The point $0$ that you walked around is a branch point.
For $1/z$ nothing like this happens, because $1/z$ has only one value at each point.
