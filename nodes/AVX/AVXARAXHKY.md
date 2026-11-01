---
tag: AVXARAXHKY
kind: statement
role: theorem
name: Tensor-hom adjunction
msc: [18A40, 13C05, 15A69]
uses: [0310REJJY8, 0NZ8JA25WK, 0NRYHJPQG2, F0HQXQ0HCD, JB7ZBFBA9C]
about: [F0HQXQ0HCD]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor%E2%80%93hom_adjunction
same_as:
  wikidata: Q16147769
  wikipedia: Tensor–hom adjunction
---

## Statement

Let $R$ be a [[commutative ring|0310REJJY8]] and let $M$, $N$, $P$ be [[$R$-modules|0NZ8JA25WK]].
Let $\Hom_R(N, P)$ be the $R$-module of $R$-[[linear maps|0NRYHJPQG2]] $N \to P$, with $(r\psi)(n) = r\psi(n)$.
Then the map
$$\Phi \colon \Hom_R(M \otimes_R N, P) \to \Hom_R(M, \Hom_R(N, P)), \qquad \Phi(\varphi)(m)(n) = \varphi(m \otimes n),$$
is an isomorphism of $R$-modules, natural in $M$, $N$ and $P$.
Thus the functor $- \otimes_R N$ is left adjoint to the hom functor $\Hom_R(N, -)$.

## Remarks

The inverse sends $\psi \colon M \to \Hom_R(N, P)$ to the linear map $M \otimes_R N \to P$ induced by the bilinear map $(m, n) \mapsto \psi(m)(n)$.
This is exactly the universal property of the [[tensor product|F0HQXQ0HCD]]: linear maps out of $M \otimes_R N$ are bilinear maps on $M \times N$.
In turn, a bilinear map is a linear map from $M$ to linear maps on $N$.

The adjunction has consequences for [[exact sequences|JB7ZBFBA9C]].
The functor $\Hom_R(N, -)$ is left exact: if $0 \to A \to B \to C$ is exact, then so is $0 \to \Hom_R(N, A) \to \Hom_R(N, B) \to \Hom_R(N, C)$.
As a left adjoint, $- \otimes_R N$ is right exact: if $A \to B \to C \to 0$ is exact, then so is $A \otimes_R N \to B \otimes_R N \to C \otimes_R N \to 0$.
Neither functor is exact in general.
For $N = \Z/2\Z$ over $\Z$, the surjection $\Z \to \Z/2\Z$ gives $\Hom(\Z/2\Z, \Z) = 0 \to \Hom(\Z/2\Z, \Z/2\Z) \cong \Z/2\Z$, which is not surjective; and the injection $\Z \xrightarrow{2} \Z$ becomes the zero map after $- \otimes_\Z \Z/2\Z$.

## Explanations

### L1 human

A function of two variables can be seen as a function of the first variable whose values are functions of the second.
The tensor-hom adjunction is this idea for linear algebra over a ring.
A linear map out of $M \otimes N$ is the same thing as a linear map from $M$ into the maps out of $N$.
It lets one move a factor from one side of $\Hom$ to the other.

### L2 human

This is the prototype of an adjunction, and it explains at once why tensor products are right exact and $\Hom$ is left exact.
The failure of exactness is measured by the derived functors $\operatorname{Tor}$ and $\operatorname{Ext}$.
[[Flat modules|73RYYEVDKA]] are those $N$ for which $- \otimes_R N$ is exact, and [[projective modules|BFFA03GE3V]] those for which $\Hom_R(N, -)$ is exact.
The same adjunction holds for bimodules over noncommutative rings, and for sheaves of modules.
