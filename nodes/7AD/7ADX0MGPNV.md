---
tag: 7ADX0MGPNV
kind: definition
name: Weak dimension
msc: ["16E10", 16D40]
defines: 5MEKEETGDA
uses: [0B1261B5ED, 0NZ8JA25WK, 73RYYEVDKA, JB7ZBFBA9C, DDQRERAQCV]
sources:
  - url: https://en.wikipedia.org/wiki/Flat_module
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $M$ be a left $R$-[[module|0NZ8JA25WK]].
A *flat resolution* of length $n$ of $M$ is an [[exact sequence|JB7ZBFBA9C]]
$$0 \to F_n \to F_{n-1} \to \cdots \to F_0 \to M \to 0$$
in which every $F_i$ is a [[flat|73RYYEVDKA]] left $R$-module.
The *weak dimension* (or *flat dimension*) $\operatorname{wd}(M)$ is the least $n \ge 0$ such that $M$ has a flat resolution of length $n$.
If there is no such $n$, then $\operatorname{wd}(M) = \infty$.
The *weak global dimension* of $R$ is the supremum of $\operatorname{wd}(M)$ over all left $R$-modules $M$.

## Remarks

Equivalently, $\operatorname{wd}(M) \le n$ if and only if $\operatorname{Tor}^R_{n+1}(N, M) = 0$ for every right $R$-module $N$, with [[Tor|DDQRERAQCV]] the derived functors of the tensor product.
So the weak global dimension of $R$ is the supremum of the $n$ with $\operatorname{Tor}^R_n(N, M) \ne 0$ for some right module $N$ and left module $M$.
It is the same for left and right modules.
Example: over $R = \Z$, the module $\Z/2$ has weak dimension $1$.
The sequence $0 \to \Z \xrightarrow{2} \Z \to \Z/2 \to 0$ is a flat resolution of length $1$.
The module $\Z/2$ is not flat, since tensoring the injective map $\Z \xrightarrow{2} \Z$ with $\Z/2$ gives the zero map on $\Z/2$, which is not injective.
Non-example of finite dimension: over $R = \Z/4$, the module $\Z/2$ has infinite weak dimension.
Its resolution $\cdots \to \Z/4 \xrightarrow{2} \Z/4 \xrightarrow{2} \Z/4 \to \Z/2 \to 0$ gives $\operatorname{Tor}^R_n(\Z/2, \Z/2) \cong \Z/2 \ne 0$ for every $n \ge 1$.
The weak dimension of a module is at most its [[projective dimension|MR9QCH1PNA]], so the weak global dimension is at most the left and the right [[global dimension|GWA0T1WKCN]].
For a left Noetherian ring it equals the left global dimension.
A ring has weak global dimension $0$ if and only if it is von Neumann regular.
