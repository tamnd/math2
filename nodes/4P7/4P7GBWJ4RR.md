---
tag: 4P7GBWJ4RR
kind: concept
name: Ext functor
msc: [13D07, 18G15]
sources:
  - url: https://en.wikipedia.org/wiki/Ext_functor
same_as:
  wikidata: Q1384902
  wikipedia: Ext functor
---

## Summary

The Ext functors $\operatorname{Ext}^n_R(M, N)$ are the right derived functors of $\Hom_R(-, N)$.
They measure how far $\Hom$ is from being exact.
The group $\operatorname{Ext}^1_R(M, N)$ classifies the extensions of $M$ by $N$, and the vanishing of Ext detects [[projective modules|BFFA03GE3V]], injective modules and the [[projective dimension|MR9QCH1PNA]].

## Explanations

### L1 human

Applying $\Hom(-, N)$ to a short exact sequence loses exactness on the right.
The Ext groups record exactly what is lost, in a long sequence of correction terms.
To compute them, replace $M$ by a [[projective resolution|HK2AA1YSQ2]], apply $\Hom(-, N)$, and take cohomology.
For example, $\operatorname{Ext}^1_\Z(\Z/n\Z, \Z) \cong \Z/n\Z$, which reflects the extension $0 \to \Z \xrightarrow{n} \Z \to \Z/n\Z \to 0$ that does not split.
