---
tag: 2XCR1B4MPS
kind: definition
name: Reduced K0
msc: [19A49, 13D15]
defines: GBJ1S3M5QV
uses: [0B1261B5ED, Q14JS2MA1C, 0KYX2N69J0]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity, and let $[R]$ be the class of the free module $R$ in [[$K_0(R)$|Q14JS2MA1C]].
The *reduced $K_0$* of $R$ is the [[quotient group|0KYX2N69J0]]
$$\tilde{K}_0(R) = K_0(R) / \Z [R],$$
the cokernel of the homomorphism $\Z \to K_0(R)$, $n \mapsto n[R]$.

## Remarks

A finitely generated projective module $P$ has class $0$ in $\tilde{K}_0(R)$ exactly when it is [[stably free|YMXJ4JTQPF]].
Indeed, if $[P] = n[R]$ with $n \in \Z$, then $P \oplus R^a \oplus Q \cong R^b \oplus Q$ for some $a, b \ge 0$ with $b - a = n$ and some finitely generated projective $Q$.
Adding a module $Q'$ with $Q \oplus Q' \cong R^k$ gives $P \oplus R^{a+k} \cong R^{b+k}$.
So $\tilde{K}_0(R) = 0$ exactly when every finitely generated projective $R$-module is stably free.

If $R$ is commutative and nonzero with $\mathrm{Spec}\, R$ connected, for instance an integral domain, the rank gives a split surjection $K_0(R) \to \Z$, and $\tilde{K}_0(R)$ is isomorphic to its kernel.
Then $K_0(R) \cong \Z \oplus \tilde{K}_0(R)$.

Example: for a field $F$, $K_0(F) = \Z [F]$, so $\tilde{K}_0(F) = 0$.

Non-example of vanishing: for $R = \Z/6\Z$, $K_0(R) \cong \Z^2$ with $[R] = (1, 1)$, so $\tilde{K}_0(R) \cong \Z$.
The generator is the class of $\Z/2\Z$, which is projective but not stably free.
