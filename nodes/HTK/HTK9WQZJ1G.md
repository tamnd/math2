---
tag: HTK9WQZJ1G
kind: concept
name: Chain map
msc: [18G35]
specializes: [859F0TFVA3]
sources:
  - url: https://en.wikipedia.org/wiki/Chain_complex
---

## Summary

A chain map is a morphism between two [[chain complexes|WQ82C0M3QB]]: a family of maps $f_n \colon C_n \to D_n$, one in each degree, that commute with the differentials.
Chain complexes and chain maps form a category, which is abelian when the underlying category is abelian.
Every chain map induces maps on [[homology|2J4JJJYP22]], and continuous maps of spaces induce chain maps of singular chains.

## Explanations

### L1 human

A chain complex is a row of objects with downward maps.
A chain map from one such row to another is a ladder of vertical maps such that every square in the ladder commutes.
Going down then across gives the same result as going across then down.
For example, multiplication by $2$ in every degree is a chain map from any complex of abelian groups to itself.
Because the squares commute, a chain map sends cycles to cycles and boundaries to boundaries.
