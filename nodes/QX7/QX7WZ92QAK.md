---
tag: QX7WZ92QAK
kind: concept
name: Modular lattice
msc: [06C05, 06B05]
specializes: [WH4SFAACAS]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_lattice
same_as:
  wikidata: Q1538614
  wikipedia: Modular lattice
---

## Summary

A modular lattice is a [[lattice|WH4SFAACAS]] that satisfies the modular law: if $a \le b$, then $a \vee (x \wedge b) = (a \vee x) \wedge b$ for every $x$.
The lattices of subspaces of a vector space, of submodules of a module and of normal subgroups of a group are modular.
Every [[distributive lattice|0HM0HQCK6N]] is modular, but not conversely.
Modularity is what makes dimension and length behave well, as in the [[Jordan–Hölder theorem for modular lattices|BCG5KM83AP]].

## Explanations

### L1 human

Take subspaces $A \subseteq B$ of a vector space and any subspace $X$.
One can add $X$ to $A$ and then cut down to $B$, or cut $X$ down to $B$ and then add $A$; the result is the same.
The modular law asks for this rule in an abstract lattice.
It is a weak form of the distributive law, which only has to hold when two of the elements are comparable.
The smallest lattice that breaks it is the [[pentagon lattice N5|DHC8TZXGYS]].
