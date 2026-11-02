---
tag: F2W20ZNWC7
kind: definition
name: Delta functor
msc: [18G10]
defines: 32ZHMZMACN
uses: [Y9CZ3MTNF1, KAN07YC9T2, KJKNJMGKZZ, JB7ZBFBA9C, KYCPCC57FT]
sources:
  - url: https://en.wikipedia.org/wiki/Delta-functor
---

## Definition

Let $\mathcal{A}$ and $\mathcal{B}$ be [[abelian categories|Y9CZ3MTNF1]].
A *cohomological $\delta$-functor* from $\mathcal{A}$ to $\mathcal{B}$ consists of [[additive functors|KAN07YC9T2]] $T^n \colon \mathcal{A} \to \mathcal{B}$ for $n \ge 0$ and of connecting morphisms.
For every [[short exact sequence|KJKNJMGKZZ]] $0 \to A' \to A \to A'' \to 0$ in $\mathcal{A}$ and every $n \ge 0$, there is a morphism $\delta^n \colon T^n(A'') \to T^{n+1}(A')$.
These data must satisfy:

1. for every short exact sequence, the sequence
$$0 \to T^0(A') \to T^0(A) \to T^0(A'') \xrightarrow{\delta^0} T^1(A') \to T^1(A) \to T^1(A'') \xrightarrow{\delta^1} T^2(A') \to \cdots$$
is [[exact|JB7ZBFBA9C]];
2. the maps $\delta^n$ are natural. Let a morphism from $0 \to A' \to A \to A'' \to 0$ to $0 \to B' \to B \to B'' \to 0$ have components $f' \colon A' \to B'$ and $f'' \colon A'' \to B''$. Then $\delta^n \circ T^n(f'') = T^{n+1}(f') \circ \delta^n$.

A $\delta$-functor $(T^n)$ is *universal* if the following holds for every $\delta$-functor $(S^n)$ and every [[natural transformation|KYCPCC57FT]] $T^0 \to S^0$.
There is a unique family of natural transformations $T^n \to S^n$ extending it and commuting with the maps $\delta^n$.

## Remarks

Example: for an $R$-module $M$, the functors $T^n = \operatorname{Ext}^n_R(M, -)$ with their connecting maps form a $\delta$-functor, since Ext has the long exact sequence in the second variable, and it is natural.
Non-example: on abelian groups, put $T^0 = \Hom_\Z(\Z/2\Z, -)$ and $T^n = 0$ for $n \ge 1$.
For $0 \to \Z \xrightarrow{\cdot 2} \Z \to \Z/2\Z \to 0$ the sequence in clause 1 starts $0 \to 0 \to 0 \to \Z/2\Z \to 0$, which is not exact, so clause 1 fails.
A theorem of Grothendieck says that a $\delta$-functor is universal when each $T^n$ with $n \ge 1$ is effaceable, meaning that every object $A$ embeds by a monomorphism $u$ with $T^n(u) = 0$.
Hence the right derived functors of a left exact functor form a universal $\delta$-functor.
Homological $\delta$-functors $(T_n)$ are defined in the same way with the arrows $\delta_n \colon T_n(A'') \to T_{n-1}(A')$.
