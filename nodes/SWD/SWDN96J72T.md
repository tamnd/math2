---
tag: SWDN96J72T
kind: definition
name: Linearly disjoint extensions
msc: [12F05, 12F99]
defines: N6YZFG66YP
uses: [07QY5RPFBR, 0EVHJFTG9Z, 0G31VJ5YS5, X4ZZKC319Q]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_disjointness
---

## Definition

Let $\Omega$ be a field and let $K$, $E$ and $F$ be [[subfields|07QY5RPFBR]] of $\Omega$ with $K \subseteq E$ and $K \subseteq F$.
The fields $E$ and $F$ are *linearly disjoint over $K$* if the following holds.
Every finite family of elements of $E$ that is [[linearly independent|0EVHJFTG9Z]] over $K$ is linearly independent over $F$.

## Remarks

The definition is symmetric in $E$ and $F$.
It holds if and only if the $K$-linear map $E \otimes_K F \to \Omega$ with $x \otimes y \mapsto xy$ is injective, where $\otimes_K$ is the [[tensor product|0G31VJ5YS5]].
If $E/K$ is finite, it holds if and only if $[EF:F] = [E:K]$, where $EF$ is the [[compositum|X4ZZKC319Q]].
If $E/K$ is finite Galois, it holds if and only if $E \cap F = K$.

Example: $E = \Q(\sqrt{2})$ and $F = \Q(\sqrt{3})$ in $\C$ are linearly disjoint over $\Q$.
Check: $EF = \Q(\sqrt{2}, \sqrt{3})$ has degree $4$ over $\Q$, so $[EF:F] = 2 = [E:\Q]$.

Non-example: let $\omega = e^{2\pi i/3}$, $E = \Q(\sqrt[3]{2})$ and $F = \Q(\omega\sqrt[3]{2})$.
Then $E \cap F = \Q$, but $EF = \Q(\sqrt[3]{2}, \omega)$ has degree $6$, so $[EF:F] = 2 < 3 = [E:\Q]$.
Hence the $\Q$-basis $1, \sqrt[3]{2}, \sqrt[3]{4}$ of $E$ is linearly dependent over $F$.
