---
tag: EMAR4X3W8D
kind: concept
name: Hasse principle
msc: [11D09, "11E12", 11G05]
sources:
  - url: https://en.wikipedia.org/wiki/Hasse_principle
same_as:
  wikidata: Q2115578
  wikipedia: Hasse principle
---

## Summary

The Hasse principle, or local-global principle, concerns polynomial equations with rational coefficients.
It says that such an equation should have a rational solution when it has a real solution and a [[p-adic|BT6T702C28]] solution for each prime $p$.
Local solvability is easy to test, so when the principle holds it turns a hard question into finitely many checks.
The [[Hasse–Minkowski theorem|R8HCWA981S]] shows that it holds for quadratic forms.
It fails for some cubic equations, and the failures are measured by objects such as the [[Tate–Shafarevich group|BK9WBMF56G]].

## Explanations

### L1 human

A solution in rational numbers gives a solution modulo every power of every prime, and a real solution.
These "local" solutions are necessary conditions, and they can be checked by finite computations.
The Hasse principle asks whether the necessary conditions are also enough.
For $x^2 + y^2 = 3z^2$ there is no solution modulo $9$ with $x$, $y$, $z$ not all divisible by $3$, so there is no nonzero rational solution either.
For quadratic equations, the local conditions are always enough; for the cubic $3x^3 + 4y^3 + 5z^3 = 0$ they are not.
