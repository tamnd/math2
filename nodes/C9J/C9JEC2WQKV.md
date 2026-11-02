---
tag: C9JEC2WQKV
kind: concept
name: Quasi-isomorphism
msc: [18G35, 18G80]
specializes: [HTK9WQZJ1G]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-isomorphism
same_as:
  wikidata: Q3413378
  wikipedia: Quasi-isomorphism
---

## Summary

A quasi-isomorphism is a [[chain map|HTK9WQZJ1G]] that induces an isomorphism on [[homology|2J4JJJYP22]] in every degree.
Every chain homotopy equivalence is a quasi-isomorphism, but not conversely.
The [[derived category|5ST7NVJFSM]] is obtained by formally inverting the quasi-isomorphisms, so that complexes with "the same homology in a coherent way" become isomorphic.

## Explanations

### L1 human

Homology is the information one usually wants from a chain complex.
A quasi-isomorphism is a map between two complexes that matches their homology exactly, even if the complexes themselves look very different.
For example, the complex $0 \to \Z \xrightarrow{2} \Z \to 0$ and the single group $\Z/2\Z$ both have homology $\Z/2\Z$ in degree $0$ and nothing else.
The reduction map from the first to the second is a quasi-isomorphism.
This is how a resolution replaces a module by a nicer complex with the same homology.
