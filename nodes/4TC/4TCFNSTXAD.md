---
tag: 4TCFNSTXAD
kind: definition
name: Nef line bundle
msc: [14C20, 14C17]
defines: RZ66X0NAM5
uses: [7JCF2TE3V5, 9537RKBZPP, XJM2MT4S3Y, RRK8P6TXG2]
sources:
  - url: https://en.wikipedia.org/wiki/Nef_line_bundle
---

## Definition

Let $X$ be a scheme that is [[proper|9537RKBZPP]] over a field $k$, and let $\mathcal{L}$ be an [[invertible sheaf|7JCF2TE3V5]] on $X$.
For a closed integral [[curve|XJM2MT4S3Y]] $C \subseteq X$, proper over $k$, let $\deg(\mathcal{L}|_C)$ be the degree of the restriction of $\mathcal{L}$ to $C$, also written $(\mathcal{L} \cdot C)$.
The sheaf $\mathcal{L}$ is *nef* if $(\mathcal{L} \cdot C) \ge 0$ for every closed integral curve $C \subseteq X$.

## Remarks

A Cartier divisor $D$ is nef when $\mathcal{O}_X(D)$ is nef, that is, $D \cdot C \ge 0$ for all curves $C$.

Example: every [[ample|RRK8P6TXG2]] $\mathcal{L}$ is nef.
Some power $\mathcal{L}^{\otimes m}$ is very ample, so $m \, (\mathcal{L} \cdot C)$ is the degree of $C$ in a projective embedding, which is positive.
The trivial bundle $\mathcal{O}_X$ is nef, with degree $0$ on every curve, and it is not ample when $\dim X \ge 1$ and $X$ is projective.

Non-example: on $\mathbb{P}^1_k$, $\mathcal{O}(-1)$ is not nef, since its degree on the curve $C = \mathbb{P}^1_k$ itself is $-1$.

On a projective scheme, Kleiman's criterion says that $\mathcal{L}$ is nef if and only if $(\mathcal{L}^{\dim V} \cdot V) \ge 0$ for every closed subvariety $V$.
It also says that the nef cone is the closure of the ample cone.
