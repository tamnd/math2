---
tag: 8XH5R0NXXQ
kind: conjecture
name: Bass–Quillen conjecture
msc: [19A13, 13C10]
uses: [0670T59HGE, 63XXTF6B5M, 0SDC934R52, HQA9YHDSH5, F0HQXQ0HCD]
about: [HQA9YHDSH5, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Bass%E2%80%93Quillen_conjecture
same_as:
  wikidata: Q28455751
  wikipedia: Bass–Quillen conjecture
history:
  posed_by: "Hyman Bass and Daniel Quillen"
  first_stated: "1973"
---

## Statement

Let $A$ be a commutative [[Noetherian ring|0670T59HGE]] that is regular, that is, its localization at every prime ideal is a [[regular local ring|63XXTF6B5M]].
Let $n \ge 1$ and let $A[t_1, \ldots, t_n]$ be the [[polynomial ring|0SDC934R52]] over $A$.
Conjecture: every [[finitely generated projective|HQA9YHDSH5]] $A[t_1, \ldots, t_n]$-module $P$ is extended from $A$, that is, $P \cong A[t_1, \ldots, t_n] \otimes_A Q$ for some finitely generated projective $A$-module $Q$.

## Remarks

The conjecture is open in general.
For a field $A$, every finitely generated projective $A$-module is free, and the conjecture becomes the [[Quillen–Suslin theorem|7N50GA46W1]].
Quillen's proof also gives the case where $A$ is a Dedekind domain.
Lindel proved the conjecture when $A$ is essentially of finite type over a field, and with Popescu's approximation theorem this extends to regular rings that contain a field.
The regularity hypothesis cannot be dropped: over a non-regular ring there can be projective modules over $A[t]$ that are not extended from $A$.

## Explanations

### L1 human

The Quillen–Suslin theorem says that projective modules over a polynomial ring over a field are free.
The Bass–Quillen conjecture asks for the same rigidity over a polynomial ring over a more general, "smooth" base ring.
Adding polynomial variables should not create new projective modules: each one should come from a module over the base ring.
