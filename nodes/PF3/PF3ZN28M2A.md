---
tag: PF3ZN28M2A
kind: statement
role: theorem
name: Connes–Thom isomorphism
msc: [46L80, 46L55, 19K99]
uses: [8HG8TS46A6, BP86XQRZD2, 7NTVTHC7CG, 2VHFR8XFWK]
about: [8HG8TS46A6, BP86XQRZD2, 7NTVTHC7CG]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
---

## Statement

Let $A$ be a C*-algebra and let $\alpha$ be a strongly continuous action of the additive group $\R$ on $A$ by automorphisms.
Let $A \rtimes_\alpha \R$ be the [[crossed product|8HG8TS46A6]].
Then for $i = 0, 1$ there are isomorphisms
$$K_i(A \rtimes_\alpha \R) \cong K_{1-i}(A),$$
where $K_0$ and $K_1$ are the groups of [[K0|BP86XQRZD2]] and [[K1|7NTVTHC7CG]].

## Remarks

Connes proved the theorem in 1981.
The isomorphisms are natural with respect to equivariant $*$-homomorphisms.
Example: for the trivial action, $A \rtimes \R \cong C_0(\R) \otimes A = SA$, and the theorem reduces to $K_i(SA) \cong K_{1-i}(A)$, which is [[Bott periodicity|2VHFR8XFWK]] together with $K_1(A) \cong K_0(SA)$.
So the theorem says that, for K-theory, every action of $\R$ behaves like the trivial action.
The name refers to the analogy with the Thom isomorphism of topological K-theory.

## Explanations

### L1 human

Crossing a C*-algebra with a flow, an action of the real line, gives a new algebra.
Whatever the flow is, the K-groups of the new algebra are those of the old one with $K_0$ and $K_1$ swapped.
So a flow can change the algebra a lot without changing its K-theory beyond this shift.

### L2 human

The result is used to compute the K-theory of crossed products by $\R$, such as algebras of foliations and flows.
Combined with Takai duality, it shows again that crossing twice by $\R$ gives back $K_*(A)$, consistent with $A \rtimes \R \rtimes \hat{\R} \cong A \otimes \mathcal{K}$.
In KK-theory, the isomorphism is given by an invertible element of $KK^1(A, A \rtimes_\alpha \R)$.
