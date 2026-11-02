---
tag: D4TYZN7BRH
kind: definition
name: Socle of a module
msc: [16D60, 16D70]
defines: S2KXCAH5MM
uses: [0NZ8JA25WK, 05WDSN597C, G00C22AEDH]
sources:
  - url: https://en.wikipedia.org/wiki/Socle_(mathematics)
---

## Definition

Let $R$ be a ring and let $M$ be a left [[module|0NZ8JA25WK]] over $R$.
The *socle* of $M$, written $\operatorname{soc}(M)$, is the sum of all [[simple submodules|G00C22AEDH]] of $M$.
If $M$ has no simple [[submodule|05WDSN597C]], then $\operatorname{soc}(M) = 0$.

## Remarks

Example: let $M = \Z/12\Z$ as a $\Z$-module.
A submodule is simple exactly when it has prime order, so the simple submodules are $6\Z/12\Z$ and $4\Z/12\Z$, of orders $2$ and $3$.
Their sum is $2\Z/12\Z$, so $\operatorname{soc}(\Z/12\Z) = 2\Z/12\Z$.

Non-example of a nonzero socle: the $\Z$-module $\Z$ has socle $0$.
Each nonzero submodule $n\Z$ contains the proper nonzero submodule $2n\Z$, so no submodule of $\Z$ is simple.

The socle is a semisimple module, and it contains every semisimple submodule of $M$.
It also equals the intersection of all essential submodules of $M$.
The socle of the left module ${}_R R$ is a two-sided ideal of $R$.
