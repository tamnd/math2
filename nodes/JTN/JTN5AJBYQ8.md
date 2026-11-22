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

We define $Sw$ for each $w$ with the Riesz theorem, then we check uniqueness and linearity, and last we compute $Sw$ in an orthonormal basis.

1. Let $V$, $W$ and $T$ be as in the statement. Fix $w \in W$, and define $f_w \colon V \to \mathbb{K}$ by $f_w(v) = \ip{Tv}{w}$.
2. The map $f_w$ is a [[linear form|0RT96J4D3H]], because $T$ is linear and the [[inner product|0VGSYBWHV2]] is linear in the first slot. So $f_w(av + bv') = a f_w(v) + b f_w(v')$.
3. The space $V$ is a finite-dimensional [[inner product space|01EK923SKP]]. By the [[Riesz representation theorem|04GYPXDXNH]], exactly one vector $u_w \in V$ satisfies $f_w(v) = \ip{v}{u_w}$ for all $v \in V$.
4. Define $S \colon W \to V$ by $S w = u_w$. By steps 1 and 3, $\ip{Tv}{w} = \ip{v}{Sw}$ for all $v \in V$ and $w \in W$, so a map with the property exists.
5. For uniqueness, let $S' \colon W \to V$ also satisfy $\ip{Tv}{w} = \ip{v}{S' w}$ for all $v$ and $w$, and fix $w$. Then $S' w$ also represents $f_w$, so the uniqueness part of the Riesz theorem gives $S' w = u_w = S w$. As $w$ is arbitrary, $S' = S$.
6. For linearity, let $w, w' \in W$ and $a, b \in \mathbb{K}$, and let $v \in V$. The inner product is conjugate linear in the second slot, and step 4 applies to $w$ and to $w'$, so
$$\ip{Tv}{aw + bw'} = \overline{a} \ip{Tv}{w} + \overline{b} \ip{Tv}{w'} = \overline{a} \ip{v}{Sw} + \overline{b} \ip{v}{Sw'} = \ip{v}{a Sw + b Sw'}.$$
7. So the vector $a Sw + b Sw'$ represents the form $f_{aw + bw'}$. The uniqueness in step 3 gives $S(aw + bw') = a Sw + b Sw'$, so $S$ is linear.
8. For the formula, let $e_1, \dots, e_n$ be an orthonormal basis of $V$. Every vector $x$ of $V$ satisfies $x = \sum_j \ip{x}{e_j} e_j$, so $S w = \sum_j \ip{Sw}{e_j} e_j$.
9. By conjugate symmetry and step 4, $\ip{Sw}{e_j} = \overline{\ip{e_j}{Sw}} = \overline{\ip{T e_j}{w}} = \ip{w}{T e_j}$. So $T^* w = S w = \sum_j \ip{w}{T e_j} e_j$, and this proves the statement.

## Idea

For a fixed $w$, the number $\ip{Tv}{w}$ depends linearly on $v$.
The Riesz theorem turns this linear form into a vector, and that vector is $T^* w$.
Uniqueness in the Riesz theorem then does two jobs: it makes $T^*$ unique, and it forces $T^*$ to be linear, because both sides of each linearity identity represent the same form.

## Variants

With an orthonormal basis $e_1, \dots, e_n$ of $V$, we can start from the formula and define $Sw = \sum_j \ip{w}{T e_j} e_j$.
Then we check the identity for $v = e_k$, which reads $\ip{T e_k}{w} = \overline{\ip{w}{T e_k}}$, and extend it to all $v$ by linearity in the first slot.
With matrices, we choose orthonormal bases, let $A$ be the matrix of $T$, and let $S$ be the map with the matrix $A^*$.
The identity then reads $y^* A x = (A^* y)^* x$, which is the rule $(MN)^* = N^* M^*$ for matrices.
