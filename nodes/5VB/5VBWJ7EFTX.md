---
tag: 5VBWJ7EFTX
kind: concept
name: Reed–Solomon code
msc: [94B05, 94B15]
specializes: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction
same_as:
  wikidata: Q1061598
  wikipedia: Reed–Solomon error correction
---

## Summary

A Reed–Solomon code is a [[linear code|E85KREWV60]] over a [[finite field|0ZXZ82FTX2]].
Its codewords are the lists of values of the low-degree polynomials at fixed distinct points.
A nonzero polynomial of degree less than $k$ has fewer than $k$ roots, so two codewords differ in at least $n - k + 1$ places.
This meets the [[Singleton bound|RAKXDDYNAM]], so Reed–Solomon codes are [[maximum distance separable|3H9XZA1SR5]].
They have fast decoders and are used in storage media, QR codes and deep-space communication.

## Explanations

### L1 human

Pick a polynomial of degree less than $k$ that encodes the message through its coefficients.
Send its values at $n$ distinct points, with $n \ge k$.
Any $k$ correct values determine the polynomial by [[interpolation|SS1YMS2NPC]], so the extra $n - k$ values are redundancy.
For example, over $\F_5$ with $k = 2$, the message $(1, 2)$ gives the line $f(x) = 1 + 2x$, and its values at $0, 1, 2, 3, 4$ are $(1, 3, 0, 2, 4)$.
Two different lines agree in at most one point, so two codewords differ in at least $4$ places.
