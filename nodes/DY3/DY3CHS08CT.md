---
tag: DY3CHS08CT
kind: concept
name: Algebraic geometry code
msc: [94B27, 14G50]
specializes: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_geometry_code
same_as:
  wikidata: Q2981471
  wikipedia: Algebraic geometry code
---

## Summary

An algebraic geometry code, or Goppa geometric code, is a [[linear code|E85KREWV60]] built from an [[algebraic curve|XJM2MT4S3Y]] over a finite field.
Its codewords are the values of the functions of a Riemann–Roch space at some [[rational points|SWJYG87QQH]] of the curve.
For the projective line it gives back the [[Reed–Solomon codes|5VBWJ7EFTX]].
The [[Riemann–Roch theorem|WMVAT9MBZ1]] controls the dimension, and the [[genus|6W8TDV9VVN]] $g$ of the curve measures how far the code is from the [[Singleton bound|RAKXDDYNAM]]: $k + d \ge n + 1 - g$.
Curves with many points compared to their genus give long codes over a fixed alphabet that beat the [[Gilbert–Varshamov bound|1NYCGYDNTX]], by the [[Tsfasman–Vlăduț–Zink bound|NS4N2EAKJ1]].

## Explanations

### L1 human

A Reed–Solomon code evaluates polynomials at points of a line, and the number of points is limited by the size of the field.
An algebraic geometry code evaluates functions on a curve instead, which can have many more points.
The functions allowed are those whose poles are controlled by a fixed divisor $G$, so that they behave like polynomials of bounded degree.
A nonzero such function has at most $\deg G$ zeros, so its list of values has many nonzero entries, as for Reed–Solomon codes.
