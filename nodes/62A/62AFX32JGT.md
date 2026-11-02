---
tag: 62AFX32JGT
kind: concept
name: B-spline
msc: [41A15, 65D07, 65D17]
specializes: [84TJ8KQ926]
sources:
  - url: https://en.wikipedia.org/wiki/B-spline
same_as:
  wikidata: Q2083109
  wikipedia: B-spline
---

## Summary

A B-spline is a [[spline|84TJ8KQ926]] of given degree on a given knot sequence that is nonnegative and nonzero only on a few consecutive knot intervals.
The B-splines of degree $p$ on a knot sequence form a basis of the corresponding spline space.
So every such spline is a unique combination of them.
They are computed by a stable recursion, they sum to $1$, and each one is local.
This makes them the standard representation of splines in numerical work and in computer-aided design.
Curves built from them, including [[NURBS|Y8B2N9ERPE]], are evaluated with [[de Boor's algorithm|5JHFB384BF]].

## Explanations

### L1 human

A B-spline is a small smooth bump made of polynomial pieces.
Of degree $0$ it is a box, equal to $1$ on one interval and $0$ elsewhere.
Of degree $1$ it is a tent, rising from $0$ to $1$ and back down over two intervals.
Higher degrees give smoother and wider bumps.
Any spline is a weighted sum of such bumps, and changing one weight only changes the curve nearby.
The [[definition|8R4CVVV8WT]] gives the recursion.
