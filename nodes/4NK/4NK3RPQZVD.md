---
tag: 4NK3RPQZVD
kind: definition
name: Euclidean Jordan algebra
msc: [17C20, 17C36, 17C90]
defines: N184N4TVZ2
uses: [6C2MCVB8C7, 0QVNCJXRY3, WYE4E80T43]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_algebra
---

## Definition

A *Euclidean Jordan algebra* is a finite-dimensional [[Jordan algebra|6C2MCVB8C7]] $J$ over $\R$, with product $(x, y) \mapsto xy$, together with an inner product $\ip{\cdot}{\cdot}$ on $J$, such that:

1. $J$ has a unit element $e$, that is, $ex = x$ for all $x \in J$;
2. $\ip{\cdot}{\cdot}$ makes $J$ a real [[inner product space|0QVNCJXRY3]];
3. $\ip{xy}{z} = \ip{y}{xz}$ for all $x, y, z \in J$.

## Remarks

Example: the real symmetric $n \times n$ matrices with $X \circ Y = \frac{1}{2}(XY + YX)$ and $\ip{X}{Y} = \tr(XY)$.
The unit is the identity matrix, and $\tr(X^2) = \sum_{i, j} X_{ij}^2 > 0$ for $X \ne 0$.
Clause 3 follows from $\tr(ABC) = \tr(BCA)$: both $\tr((X \circ Y) Z)$ and $\tr(Y (X \circ Z))$ equal $\frac{1}{2}\tr(XYZ + YXZ)$.

Non-example: $\R[\varepsilon]/(\varepsilon^2)$ is a unital Jordan algebra, but no inner product satisfies clause 3.
Indeed clause 3 would give $\ip{\varepsilon}{\varepsilon} = \ip{\varepsilon e}{\varepsilon} = \ip{e}{\varepsilon^2} = 0$, so the inner product would not be positive definite.

A finite-dimensional real Jordan algebra admits such an inner product exactly when it is [[formally real|WYE4E80T43]] and unital; formally real finite-dimensional Jordan algebras are automatically unital.
