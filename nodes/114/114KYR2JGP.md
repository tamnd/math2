---
tag: 114KYR2JGP
kind: definition
name: Median algebra
msc: [06D99, 08A99, 05C12]
defines: DN7VSSDYPQ
uses: [0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Median_algebra
---

## Definition

Let $X$ be a set and let $\langle \cdot, \cdot, \cdot \rangle \colon X \times X \times X \to X$ be a ternary operation.
The pair $(X, \langle \cdot, \cdot, \cdot \rangle)$ is a *median algebra* if for all $x, y, z, w \in X$:

1. $\langle x, y, y \rangle = y$;
2. $\langle x, y, z \rangle = \langle z, x, y \rangle$;
3. $\langle x, y, z \rangle = \langle x, z, y \rangle$;
4. $\langle \langle x, w, y \rangle, w, z \rangle = \langle x, w, \langle y, w, z \rangle \rangle$.

## Remarks

Clauses 2 and 3 together say that $\langle x, y, z \rangle$ does not change under any permutation of $x, y, z$.
Clause 4 says that for fixed $w$, the binary operation $(x, y) \mapsto \langle x, w, y \rangle$ is associative.

Example: $X = \R$ with $\langle x, y, z \rangle$ the median of $x, y, z$, which equals $\max(\min(x, y), \min(y, z), \min(z, x))$.
More generally, every [[distributive lattice|0HM0HQCK6N]] is a median algebra with $\langle x, y, z \rangle = (x \wedge y) \vee (y \wedge z) \vee (z \wedge x)$.
For clause 1, $(x \wedge y) \vee y \vee (y \wedge x) = y$.

Non-example: a set $X$ with at least two elements and $\langle x, y, z \rangle = x$.
Clause 1 fails: for $x \ne y$, $\langle x, y, y \rangle = x \ne y$.
