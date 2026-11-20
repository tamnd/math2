---
tag: JTN5AJBYQ8
kind: proof
name: Proof of the existence and uniqueness of the adjoint
msc: ["15A04", "47A05"]
topics: [3YM9EK6VMB]
audience: ug1
proves: E0KFAXMTC2
uses: [01EK923SKP, 0VGSYBWHV2, 0RT96J4D3H, 04GYPXDXNH]
methods: [01XM7JEKHY, GQHHNV79PA]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_representation_theorem
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Proof

We define $S w$ for each $w$ with the Riesz theorem, and then we check uniqueness and linearity.

1. Let $V$, $W$ and $T$ be as in the statement. Fix $w \in W$, and define $f_w \colon V \to \mathbb{K}$ by $f_w(v) = \ip{Tv}{w}$.
2. The map $f_w$ is a [[linear form|0RT96J4D3H]]. The reason: $T$ is linear, and the [[inner product|0VGSYBWHV2]] is linear in the first slot, so $f_w(av + bv') = a f_w(v) + b f_w(v')$.
3. The space $V$ is a finite-dimensional [[inner product space|01EK923SKP]]. By the [[Riesz representation theorem|04GYPXDXNH]], there is exactly one vector $u_w \in V$ with $f_w(v) = \ip{v}{u_w}$ for all $v \in V$.
4. Define $S \colon W \to V$ by $S w = u_w$. By steps 1 and 3, $\ip{Tv}{w} = \ip{v}{Sw}$ for all $v \in V$ and $w \in W$. So a map with the property exists.
5. Uniqueness. Let $S' \colon W \to V$ be a second map with $\ip{Tv}{w} = \ip{v}{S' w}$ for all $v$ and $w$. Fix $w$.
6. Then $S' w$ also represents $f_w$. By the uniqueness part of the Riesz theorem, $S' w = u_w = S w$. As $w$ is arbitrary, $S' = S$.
7. Linearity. Let $w, w' \in W$ and $a, b \in \mathbb{K}$. For each $v \in V$, the inner product is conjugate linear in the second slot. So $\ip{Tv}{aw + bw'} = \overline{a} \ip{Tv}{w} + \overline{b} \ip{Tv}{w'}$.
8. By step 4, the right side of step 7 is $\overline{a} \ip{v}{Sw} + \overline{b} \ip{v}{Sw'}$. By conjugate linearity in the second slot again, this is $\ip{v}{a Sw + b Sw'}$.
9. So the vector $a Sw + b Sw'$ represents the form $f_{aw + bw'}$. By the uniqueness in step 3, $S(aw + bw') = a Sw + b Sw'$.
10. Hence $S$ is linear, and $S$ is the only map with the property. This proves the statement.

## Idea

For each fixed $w$, the number $\ip{Tv}{w}$ depends linearly on $v$.
The Riesz theorem turns this linear form into a vector, and that vector is $T^* w$.
Uniqueness in the Riesz theorem gives uniqueness of $T^*$, and also forces $T^*$ to be linear.

## Variants

- With an orthonormal basis $e_1, \dots, e_n$ of $V$, one can define $S w = \sum_{j} \ip{w}{T e_j} e_j$ directly. Then one checks the identity on the basis vectors $v = e_k$ and extends by linearity in $v$.
- With matrices: choose orthonormal bases, let $A$ be the matrix of $T$, and let $S$ be the map with the matrix $A^*$. The identity then reads $y^* A x = (A^* y)^* x$, which is the rule $(MN)^* = N^* M^*$ for matrices.
