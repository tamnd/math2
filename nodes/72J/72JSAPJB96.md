---
tag: 72JSAPJB96
kind: definition
name: Fully invariant congruence
msc: [08A30, 08B05, 08A35]
defines: QKGW3Z9BHW
uses: [QJGPT2W0FT, DCSXXT4SER, KBXSZC6BV1]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Definition

Let $\mathbf{A}$ be an [[algebra|QJGPT2W0FT]] with universe $A$.
A [[congruence|DCSXXT4SER]] $\theta$ on $\mathbf{A}$ is *fully invariant* when, for every endomorphism $\varepsilon$ of $\mathbf{A}$ and all $a, b \in A$, $(a, b) \in \theta$ implies $(\varepsilon(a), \varepsilon(b)) \in \theta$.
Here an endomorphism is a [[homomorphism|KBXSZC6BV1]] from $\mathbf{A}$ to itself.

## Remarks

The congruences $\Delta_A$ and $\nabla_A$ are always fully invariant, and so is the intersection of any family of fully invariant congruences.

Example: on the group $\Z^2 = \Z \times \Z$, congruence modulo $2$ in both coordinates is fully invariant.
Every endomorphism of $\Z^2$ is given by an integer matrix $M$, and $a - b \in 2\Z^2$ implies $M a - M b = M(a - b) \in 2\Z^2$.

Non-example: on $\Z^2$, let $(a, b) \in \theta$ when the first coordinates of $a$ and $b$ are equal.
This is a congruence, but the swap $(x, y) \mapsto (y, x)$ is an endomorphism that sends the related pair $((0, 0), (0, 1))$ to the unrelated pair $((0, 0), (1, 0))$.

On the [[term algebra|3YYKGWJJND]] $\mathbf{T}(X)$ over a set of variables $X$, the endomorphisms are the substitutions.
So the fully invariant congruences on $\mathbf{T}(X)$ are the [[equational theories|F1M51B4MDG]] in the variables $X$.
