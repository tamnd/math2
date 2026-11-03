---
tag: E1GGS48ZFE
kind: statement
role: theorem
name: Wendel's theorem on multipliers of L1(G)
msc: [43A22, 43A20, 43A10]
uses: [AHV05ZBCYW, 6GD25S53ND, 8E2CDA2WSV, TSVMMGZ716]
about: [6GD25S53ND, 8E2CDA2WSV]
sources:
  - url: https://en.wikipedia.org/wiki/Group_algebra_of_a_locally_compact_group
---

## Statement

Let $G$ be a [[locally compact group|AHV05ZBCYW]], let $L^1(G)$ be its [[group algebra|6GD25S53ND]] and let $M(G)$ be its [[measure algebra|8E2CDA2WSV]].
Let $T \colon L^1(G) \to L^1(G)$ be a bounded linear operator.
Then $T(f * g) = (Tf) * g$ for all $f, g \in L^1(G)$ if and only if there is a measure $\mu \in M(G)$ with
$$Tf = \mu * f \quad \text{for every } f \in L^1(G).$$
In this case $\mu$ is unique and $\norm{T} = \norm{\mu}$.

## Remarks

If $Tf = \mu * f$, the condition $T(f * g) = (Tf) * g$ is associativity of convolution in $M(G)$.
For the converse, apply $T$ to a [[bounded approximate identity|TSVMMGZ716]] $(e_U)$ of $L^1(G)$.
The measures $T e_U$ have norm at most $\norm{T}$, so they have a weak-$*$ limit point $\mu$ in $M(G) = C_0(G)^*$.
Then $Tf = \lim_U T(e_U * f) = \lim_U (Te_U) * f$, and this limit is identified with $\mu * f$.

Example: for $y \in G$, the left translation $L_y f(x) = f(y^{-1}x)$ satisfies $L_y(f * g) = (L_y f) * g$.
The measure given by the theorem is the point mass $\delta_y$, since $\delta_y * f = L_y f$, and $\norm{L_y} = \norm{\delta_y} = 1$.

The boundedness of $T$ is a hypothesis of the theorem; the operators $f \mapsto \mu * f$ with $\mu \in M(G)$ are bounded, with $\norm{\mu * f}_1 \le \norm{\mu} \norm{f}_1$.

## Explanations

### L1 human

Some operations on functions on a group commute with convolution from one side, for example shifts and averages of shifts.
Wendel's theorem says that every such bounded operation on $L^1(G)$ is a weighted average of shifts, given by convolution with a finite measure.
So the measure algebra describes exactly these operations, and nothing more is needed.

### L2 human

In the language of Banach algebras, $M(G)$ is the left multiplier algebra, or algebra of left centralizers, of $L^1(G)$.
For abelian $G$, combined with the Fourier transform, this says that the bounded translation-invariant operators on $L^1(G)$ correspond to multiplication of Fourier transforms by Fourier–Stieltjes transforms of measures.
This contrasts with $L^2(G)$, where the multipliers for abelian $G$ are all bounded measurable functions on the dual group.
Wendel used the result to show that if $L^1(G_1)$ and $L^1(G_2)$ are isometrically isomorphic Banach algebras, then $G_1$ and $G_2$ are isomorphic topological groups.
