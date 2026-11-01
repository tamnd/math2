---
tag: GTGFXW37YM
kind: definition
name: Normal closure
msc: [12F05, 12F10]
defines: 6XM4CCVTKE
uses: [0PTBM7K0R2, 0CBRFQ7DVZ, 0KXQKX9P63, 0GK1WB9R98]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_extension
---

## Definition

Let $L/K$ be an [[algebraic extension|0PTBM7K0R2]].
A *normal closure* of $L/K$ is a field extension $M/L$ such that:

1. $M/K$ is a [[normal extension|0CBRFQ7DVZ]];
2. no proper subfield of $M$ that contains $L$ is normal over $K$.

## Remarks

A normal closure exists and is unique up to an isomorphism of fields that is the identity on $L$.
Let $L = K(\alpha_1, \ldots, \alpha_n)$ be finite over $K$, and let $f_i$ be the [[minimal polynomial|0GK1WB9R98]] of $\alpha_i$ over $K$.
Then a normal closure is the [[splitting field|0KXQKX9P63]] of $f_1 \cdots f_n$ over $L$, and it is again finite over $K$.
Let $N$ be a normal extension of $K$ that contains $L$.
Inside $N$, the normal closure is the compositum of the fields $\tau(L)$, for all embeddings $\tau \colon L \to N$ over $K$.

Example: for $L = \Q(\sqrt[3]{2})$ over $\Q$, let $M = \Q(\sqrt[3]{2}, \omega)$ with $\omega = e^{2\pi i/3}$.
Check: $M$ is the splitting field of $x^3 - 2$ over $\Q$, so it is normal over $\Q$.
A normal subfield containing $\sqrt[3]{2}$ contains all roots $\sqrt[3]{2}, \omega\sqrt[3]{2}, \omega^2\sqrt[3]{2}$ of its minimal polynomial, hence contains $M$.

Non-example: an algebraic closure $\overline{\Q}$ of $\Q$ contains $L$ and is normal over $\Q$, but it fails clause 2, since $M$ is a proper normal subfield containing $L$.
