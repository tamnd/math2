---
tag: 4CSMQFTGD8
kind: concept
name: Tate module
msc: [14K15, 11G10]
sources:
  - url: https://en.wikipedia.org/wiki/Tate_module
same_as:
  wikidata: Q7687981
  wikipedia: Tate module
---

## Summary

Fix a prime $\ell$.
The $\ell$-adic Tate module of an abelian group collects its elements of $\ell$-power order into one module over the [[$\ell$-adic integers|V6TJAFZ4MD]].
Let $A$ be an [[abelian variety|R7W03TXRS9]] of dimension $g$ over a field $k$ whose characteristic is not $\ell$.
Then the Tate module of $A$ is free of rank $2g$.
The [[absolute Galois group|PGKWBJDTKX]] of $k$ acts on it, which gives an $\ell$-adic [[Galois representation|JQEYEQJY2G]].
These representations carry much of the arithmetic of $A$.

## Explanations

### L1 human

On an elliptic curve over $\C$ there are $\ell^{2n}$ points that give zero when added to themselves $\ell^n$ times.
These torsion points form a tower as $n$ grows, each level mapping onto the one below by multiplication by $\ell$.
The Tate module is the limit of this tower.
It behaves like a lattice $\Z_\ell^2$, an $\ell$-adic version of the lattice that defines the curve as a quotient of $\C$.
Over a number field, the Galois group permutes the torsion points, and so it acts on the Tate module.
