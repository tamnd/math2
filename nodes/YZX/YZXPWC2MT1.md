---
tag: YZXPWC2MT1
kind: definition
name: Arity
msc: [08A02, 03C07]
defines: MSXX2P86CY
uses: [0EPAT51DXQ, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Arity
---

## Definition

Let $A$ and $B$ be sets and let $n \ge 0$ be an integer.
Write $A^n$ for the [[Cartesian product|09CEDJYBKP]] of $n$ copies of $A$, the set of $n$-tuples of elements of $A$.
Here $A^0$ is the set whose only element is the empty tuple.

1. A [[function|0EPAT51DXQ]] $f \colon A^n \to B$ has *arity* $n$.
2. A relation $R \subseteq A^n$ has *arity* $n$.

A function or relation of arity $n$ is called $n$-ary.

## Remarks

Example: the map $(x, y, z) \mapsto x y + z$ from $\R^3$ to $\R$ has arity $3$, because its domain is $\R^3$.

Non-example: the map $\R \to \R^2$, $x \mapsto (x, x)$, has arity $1$ and not $2$, because the arity counts the factors of the domain, not of the codomain.

The arity of a function depends on how its domain is written as a power.
A map on $\R^2$ can be seen as a binary function on $\R$ or as a unary function on the set $\R^2$.
The words nullary, unary, binary and ternary are used for arities $0$, $1$, $2$ and $3$.
