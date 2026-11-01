---
tag: VZ1G9CYQSK
kind: definition
name: Transfer homomorphism
msc: [20D20, 20J06]
defines: 3R2Y906QAQ
uses: [G5S1M9, 0X1JXT47GA, 0DTXBQPA2S, 03DEH43F4H, 0ASGSTXSBW, 0AQZV0905N, 0JYTG5K9Y4, 0053CQE9Y2, 0YGN3VAA0D, 0DZ93493VN]
sources:
  - url: https://en.wikipedia.org/wiki/Transfer_(group_theory)
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of finite [[index|0DTXBQPA2S]] $n$.
Let $H'$ be the [[commutator subgroup|0ASGSTXSBW]] of $H$, so that $H/H'$ is the [[abelianisation|0AQZV0905N]] of $H$.
Choose elements $t_1, \dots, t_n$ of $G$ such that $G$ is the disjoint union of the [[left cosets|03DEH43F4H]] $t_1 H, \dots, t_n H$.
For $g \in G$ and each $i$, there are a unique index $\sigma_g(i)$ and a unique $h_i(g) \in H$ with $g t_i = t_{\sigma_g(i)} h_i(g)$.
The *transfer* is the map $V \colon G \to H/H'$ given by
$$V(g) = h_1(g) h_2(g) \cdots h_n(g) \, H'.$$

## Remarks

The product is taken in the abelian group $H/H'$, so its order does not matter.
One proves that $V$ is a [[group homomorphism|0JYTG5K9Y4]] and that it does not depend on the choice of $t_1, \dots, t_n$.

Example: if $G$ is abelian, then $H' = \set{e}$ and $h_i(g) = t_{\sigma_g(i)}^{-1} g t_i$.
Since $\sigma_g$ permutes $\set{1, \dots, n}$, the factors $t_i$ cancel, and $V(g) = g^n$.
For $G = \Z$ and $H = n\Z$, the transfer is $V(k) = nk$.

Non-example: take the product $h_1(g) \cdots h_n(g)$ in $H$ itself, without passing to $H/H'$.
In general it depends on the order of the factors and on the choice of the $t_i$, so it does not give a well-defined homomorphism to $H$.

A main application is Burnside's normal $p$-complement theorem.
Let $P$ be a [[Sylow $p$-subgroup|0053CQE9Y2]] of a finite group $G$ that lies in the [[centre|0DZ93493VN]] of its [[normaliser|0YGN3VAA0D]].
Then $G$ has a normal subgroup $K$ with $G = KP$ and $K \cap P = \set{e}$.
