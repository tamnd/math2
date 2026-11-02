---
tag: A8WVA43YXS
kind: definition
name: Separable algebra
msc: [16H05]
defines: X8H7A98Q55
uses: [3CTW1P4HBP, M8Q24XB0AF, EM7FHAFD3N, 1735VGRT2P, NY25HXA478, 0WCX7NB4N7]
sources:
  - url: https://en.wikipedia.org/wiki/Separable_algebra
---

## Definition

Let $K$ be a commutative ring and let $A$ be an [[associative algebra|3CTW1P4HBP]] over $K$.
Let $A^{\mathrm{op}}$ be the [[opposite ring|M8Q24XB0AF]] of $A$ and let $A^e = A \otimes_K A^{\mathrm{op}}$ be the [[tensor product of algebras|1735VGRT2P]].
An $A$-[[bimodule|EM7FHAFD3N]] is the same as a left $A^e$-module, and $A$ itself is one.
Let $\mu \colon A^e \to A$ be the map $a \otimes b \mapsto ab$, which is a homomorphism of $A^e$-modules.
The algebra $A$ is *separable* over $K$ if there is a homomorphism of $A^e$-modules $s \colon A \to A^e$ with $\mu \circ s = \id_A$.

## Remarks

Equivalently, $A$ is a projective $A^e$-module.
Equivalently, there is a *separability idempotent*: an element $e = \sum_i x_i \otimes y_i$ of $A^e$ with $\sum_i x_i y_i = 1$ and $\sum_i a x_i \otimes y_i = \sum_i x_i \otimes y_i a$ for all $a \in A$; take $e = s(1)$.

Example: $A = M_n(K)$ is separable over $K$.
With matrix units $E_{ij}$, the element $e = \sum_{i} E_{i1} \otimes E_{1i}$ satisfies $\sum_i E_{i1} E_{1i} = \sum_i E_{ii} = 1$, and for all $k, l$ the sums $\sum_i E_{kl} E_{i1} \otimes E_{1i}$ and $\sum_i E_{i1} \otimes E_{1i} E_{kl}$ both equal $E_{k1} \otimes E_{1l}$.

Non-example: let $K = \F_p(t)$ and $A = K(t^{1/p})$, a purely inseparable field extension of degree $p$.
Then $A \otimes_K A \cong A[x]/(x - t^{1/p})^p$ has nonzero nilpotent elements, so it is not semisimple, and $A$ is not separable over $K$.

When $K$ is a field, a finite-dimensional algebra $A$ is separable if and only if $A \otimes_K L$ is [[semisimple|NY25HXA478]] for every field extension $L$ of $K$.
Equivalently, $A$ is semisimple and the center of each simple factor of $A$ is a [[separable field extension|0WCX7NB4N7]] of $K$.
A finite field extension $L/K$ is a separable algebra exactly when it is a separable extension.
