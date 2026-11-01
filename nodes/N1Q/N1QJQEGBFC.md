---
tag: N1QJQEGBFC
kind: concept
name: Cohen–Macaulay ring
msc: [13H10, 13C14]
sources:
  - url: https://en.wikipedia.org/wiki/Cohen–Macaulay_ring
same_as:
  wikidata: Q2893695
  wikipedia: Cohen–Macaulay ring
---

## Summary

A Cohen–Macaulay ring is a Noetherian ring whose local rings have [[depth|M2RADBFW99]] equal to their [[Krull dimension|MVGBS3J1P7]].
This class contains [[regular local rings|63XXTF6B5M]], [[complete intersection rings|EPM2HKGMZS]] and [[Gorenstein rings|T6HCX959PJ]].
Cohen–Macaulay rings are the setting where dimension theory works best, since systems of parameters are regular sequences.
They also have a good duality theory through the [[canonical module|W5ECXPM6FW]].

## Explanations

### L1 human

The dimension of a ring counts its independent directions, and the depth counts how many independent equations can be imposed one after the other without hitting a zero divisor.
In a Cohen–Macaulay ring these two counts agree at every point.
Polynomial rings over a field are Cohen–Macaulay, and so is the ring of the two coordinate axes $K[x,y]/(xy)$.
The ring $K[x,y]/(x^2, xy)$, a line with an extra "fuzzy" point at the origin, is not.
