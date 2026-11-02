---
tag: A2VXXBYX6A
kind: definition
name: CR manifold
msc: [32V05, 32V40]
defines: ZC78JKZX9S
uses: [F45VQ47GPV, WY6K3P4YCG, P4DZM975BV, 68FGQEBD6J]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] and let $T_\C M = TM \otimes_\R \C$ be its complexified [[tangent bundle|WY6K3P4YCG]].
A *CR structure* on $M$ is a complex [[vector subbundle|P4DZM975BV]] $L \subseteq T_\C M$ such that:

1. $L \cap \overline{L} = 0$, where $\overline{L}$ is the complex conjugate subbundle;
2. $L$ is involutive: for all smooth sections $X$, $Y$ of $L$, the [[Lie bracket|68FGQEBD6J]] $[X, Y]$ is a section of $L$.

A *CR manifold* is a smooth manifold with a CR structure.
The complex rank of $L$ is its *CR dimension*, and $\dim_\R M - 2 \operatorname{rank}_\C L$ is its *CR codimension*.

## Remarks

Example: let $M$ be a smooth real hypersurface of $\C^n$, and let $L_p = T^{1,0}_p \C^n \cap (T_p M \otimes \C)$ for $p \in M$, where $T^{1,0}\C^n$ is spanned by the $\partial / \partial z_j$.
This is a subbundle of rank $n - 1$.
Clause 1 holds because $T^{1,0} \C^n \cap T^{0,1} \C^n = 0$.
Clause 2 holds because $T^{1,0} \C^n$ is involutive and vector fields tangent to $M$ have brackets tangent to $M$.
So $M$ is a CR manifold of CR dimension $n - 1$ and CR codimension $1$.

Non-example: on $M = \R$, the complex line bundle $L$ spanned by $\partial / \partial x$ is involutive but satisfies $\overline{L} = L$, so clause 1 fails.

When $\operatorname{rank}_\C L = 1$, clause 2 holds automatically, since $[fX, gX] = (f \, Xg - g \, Xf) X$.
When $\dim_\R M = 2 \operatorname{rank}_\C L$, a CR structure is the same as an integrable almost complex structure, by the Newlander–Nirenberg theorem.
Some authors call a structure that satisfies only clause 1 an almost CR structure.
