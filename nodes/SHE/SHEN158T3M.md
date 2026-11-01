---
tag: SHEN158T3M
kind: concept
name: Local class field theory
msc: [11S31]
sources:
  - url: https://en.wikipedia.org/wiki/Local_class_field_theory
same_as:
  wikidata: Q3526829
  wikipedia: Local class field theory
---

## Summary

Local class field theory describes the abelian extensions of a non-Archimedean [[local field|J85FZEQG38]] $K$ in terms of the multiplicative group $K^\times$.
Its main result is the local reciprocity map $K^\times \to \Gal(K^{ab} / K)$, where $K^{ab}$ is the maximal abelian extension of $K$.
For each finite abelian extension $L / K$, it induces an isomorphism $K^\times / N_{L/K}(L^\times) \cong \Gal(L / K)$.
The finite abelian extensions of $K$ correspond to the open subgroups of finite index of $K^\times$, through their norm groups.

## Explanations

### L1 human

Class field theory says that the abelian extensions of a field are controlled by data inside the field itself.
Over a local field such as $\Q_p$ the data is simple: the group of nonzero elements $K^\times$.
Each abelian extension corresponds to a subgroup of $K^\times$ of finite index, namely the norms from the extension.
The Galois group of the extension is the quotient of $K^\times$ by this subgroup.
For example, take $K = \Q_p$ and its unramified extension of degree $n$.
It corresponds to the elements whose [[p-adic absolute value|WGN82TCEF2]] is an integer power of $p^n$.
It is the local half of [[class field theory|BEKCEYHCHX]]; the global theory glues the local ones together.
