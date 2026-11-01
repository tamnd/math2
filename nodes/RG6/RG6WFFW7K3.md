---
tag: RG6WFFW7K3
kind: definition
name: Kähler differentials
msc: [13N05, 13N15]
defines: 7HCFARHG7D
uses: [0310REJJY8, DPBJ04JMH8, 0NZ8JA25WK, 3J89REV9WQ, 0SDC934R52, 0EGN1E1JPB, 1735VGRT2P]
sources:
  - url: https://en.wikipedia.org/wiki/Kähler_differential
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $A$ be a commutative [[$R$-algebra|DPBJ04JMH8]].
For an $A$-[[module|0NZ8JA25WK]] $M$, an *$R$-derivation* $D \colon A \to M$ is an $R$-linear map with $D(ab) = a \, D(b) + b \, D(a)$ for all $a, b \in A$; see [[derivation|3J89REV9WQ]].
The *module of Kähler differentials* $\Omega_{A/R}$ is the $A$-module with one generator $da$ for each $a \in A$ and the following relations, for all $a, b \in A$ and $r \in R$:

1. $d(a + b) = da + db$.
2. $d(ab) = a \, db + b \, da$.
3. $d(r \cdot 1) = 0$.

The map $d \colon A \to \Omega_{A/R}$, $a \mapsto da$, is the *universal derivation*.

## Remarks

The map $d$ is an $R$-derivation, and it is universal: for each $R$-derivation $D \colon A \to M$ there is a unique $A$-linear map $\varphi \colon \Omega_{A/R} \to M$ with $D = \varphi \circ d$.
An equivalent form: if $I$ is the kernel of the multiplication map $A \otimes_R A \to A$ (see [[tensor product of algebras|1735VGRT2P]]), then $\Omega_{A/R} \cong I/I^2$, with $da$ corresponding to the class of $a \otimes 1 - 1 \otimes a$.

Example: for the [[polynomial ring|0SDC934R52]] $A = R[x_1, \ldots, x_n]$, the module $\Omega_{A/R}$ is free with basis $dx_1, \ldots, dx_n$, and $df = \sum_i \frac{\partial f}{\partial x_i} \, dx_i$, with [[formal partial derivatives|0EGN1E1JPB]].
For a quotient $A = R[x]/(f)$, the module $\Omega_{A/R}$ is $A \, dx / (f'(x) \, dx) \cong A/(f'(x))$.
So $\Omega_{\Q(\sqrt 2)/\Q} = 0$, because $f = x^2 - 2$ and $f'(\sqrt 2) = 2\sqrt 2$ is a unit.
For $A = \F_p(t^{1/p})$ over $R = \F_p(t)$, with $f = x^p - t$, one has $f' = 0$, so $\Omega_{A/R} \cong A \ne 0$.

Non-example: the identity map $A \to A$ is not a derivation when $A \ne 0$, because it gives $1 = D(1 \cdot 1) = 2 \cdot D(1) = 2$, which fails in $A$ unless $1 = 0$.
