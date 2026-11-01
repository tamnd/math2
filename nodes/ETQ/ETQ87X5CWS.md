---
tag: ETQ87X5CWS
kind: definition
name: Jacobi sum
msc: [11T24, 11L05]
defines: 2767J23XHN
uses: [0ZXZ82FTX2, 0JYTG5K9Y4, EQ6A3ZN48K, 0JTC045NNZ]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_sum
---

## Definition

Let $F$ be a [[finite field|0ZXZ82FTX2]] with $q$ elements.
Let $\chi, \lambda \colon F^\times \to \C^\times$ be multiplicative characters, that is, [[group homomorphisms|0JYTG5K9Y4]], each extended to $F$ by the value $0$ at $0$.
The *Jacobi sum* of $\chi$ and $\lambda$ is
$$J(\chi, \lambda) = \sum_{a \in F} \chi(a) \lambda(1 - a).$$

## Remarks

Some books set the trivial character equal to $1$ at $0$; this changes $J$ only when $\chi$ or $\lambda$ is trivial.
If $\chi$, $\lambda$ and $\chi\lambda$ are nontrivial, then $J(\chi, \lambda) = g(\chi)g(\lambda)/g(\chi\lambda)$, where $g$ is the [[Gauss sum|EQ6A3ZN48K]] with a fixed nontrivial additive character, and so $\abs{J(\chi, \lambda)} = \sqrt{q}$.

Example: let $q = 5$ and $\chi = \lambda$ the [[Legendre symbol|0JTC045NNZ]] modulo $5$.
The terms with $a = 0$ and $a = 1$ vanish.
For $a = 2, 3, 4$ the products $\chi(a)\chi(1-a)$ are $(-1)(1) = -1$, $(-1)(-1) = 1$ and $(1)(-1) = -1$.
So $J(\chi, \chi) = -1$; here $\chi^2$ is trivial and the general rule gives $J(\chi, \chi^{-1}) = -\chi(-1) = -1$.

Non-example: the sum $\sum_{a} \chi(a) \lambda(a)$ is not a Jacobi sum, since the second argument is $a$ and not $1 - a$.
By orthogonality it equals $q - 1$ if $\chi\lambda$ is trivial and $0$ otherwise.
