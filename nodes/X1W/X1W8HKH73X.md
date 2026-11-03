---
tag: X1W8HKH73X
kind: concept
name: Elliptic-curve cryptography
msc: [94A60, 14G50, 11T71]
specializes: [01E9MNJYEX]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic-curve_cryptography
same_as:
  wikidata: Q1048911
  wikipedia: Elliptic-curve cryptography
---

## Summary

Elliptic-curve cryptography is public-key cryptography in the group of points of an [[elliptic curve|427N6S6QQW]] over a [[finite field|0ZXZ82FTX2]].
Its security rests on the elliptic curve [[discrete logarithm|0HJHYMGN3C]] problem, for which no algorithm much faster than generic square-root methods is known on well-chosen curves.
So keys of about $256$ bits give a security level that needs keys of thousands of bits in RSA.
Neal Koblitz and Victor Miller proposed it independently in 1985.

## Explanations

### L1 human

The points of an elliptic curve over a finite field can be added.
Draw the line through two points, find the third point where it meets the curve, and reflect it.
Adding a point $P$ to itself $k$ times gives a point $kP$, and this is fast even for huge $k$ by repeated doubling.
Going back from $kP$ to $k$ seems very hard.
This easy-forward, hard-backward step plays the role that powers modulo a prime play in older systems such as the [[Diffie–Hellman key exchange|01TKKESHSB]].
