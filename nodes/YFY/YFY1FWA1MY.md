---
tag: YFY1FWA1MY
kind: concept
name: (∞,1)-category
msc: [18N60]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-category
---

## Summary

An $(\infty,1)$-category is a higher category with $k$-morphisms for every $k \ge 1$, in which all $k$-morphisms with $k \ge 2$ are invertible.
It behaves like a [[category|A2DE66937D]] whose hom-sets are replaced by spaces, taken up to homotopy.
Several precise models exist, such as [[quasi-categories|9328WEVJEK]], categories enriched in Kan complexes, and complete Segal spaces, and these models are known to be equivalent.
$(\infty,1)$-categories are the natural setting for homotopy theory, derived algebraic geometry and stable homotopy theory.

## Explanations

### L1 human

In topology, two maps can be homotopic, two homotopies can be homotopic, and so on.
An $(\infty,1)$-category keeps all of this information instead of collapsing homotopic maps to a single class.
The "$1$" means that only the ordinary morphisms may fail to be invertible; everything above them is a kind of homotopy, which can be reversed.
For example, topological spaces with continuous maps, homotopies between maps and homotopies between homotopies form an $(\infty,1)$-category.
