---
tag: NRP019D9AE
kind: definition
name: Uniform module
msc: [16D10, 16P60]
defines: YXEVE39Q31
uses: [09VDS2W1E8, 0RGZ10DFPG, 8MS51FASMX, E2P29GCD9T]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_module
---

## Definition

Let $R$ be a ring and let $M$ be a left [[$R$-module|09VDS2W1E8]].
The module $M$ is *uniform* if:

1. $M \ne 0$;
2. $N_1 \cap N_2 \ne 0$ for all nonzero [[submodules|0RGZ10DFPG]] $N_1, N_2$ of $M$.

## Remarks

Equivalently, $M \ne 0$ and every nonzero submodule of $M$ is [[essential|8MS51FASMX]] in $M$.
Example: the $\Z$-module $\Z$ is uniform.
The check: nonzero submodules $a\Z$ and $b\Z$ both contain $ab \ne 0$.
Example: $\Z/p^n\Z$, for $p$ prime and $n \ge 1$, is uniform, since its subgroups form a chain.
Non-example: $\Z \oplus \Z$ fails clause 2, since $\Z \oplus 0$ and $0 \oplus \Z$ meet only in $0$.
Every uniform module is [[indecomposable|E2P29GCD9T]].
The converse fails: let $K$ be a field and $A = K[x, y]/(x^2, xy, y^2)$.
As a module over itself, $A$ is indecomposable, because $A$ is a commutative local ring and so has no idempotents other than $0$ and $1$.
It is not uniform, since its submodules $Ax = Kx$ and $Ay = Ky$ meet only in $0$.
