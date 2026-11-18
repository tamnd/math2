---
tag: MT0CNMDT3R
kind: definition
name: Modal logic S5
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
defines: VC3A2VWXND
uses: [JS8W7PA6JK, FDFQFWPM4X, YHGXV3SQDP, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/S5_(modal_logic)
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Definition

The logic $\mathsf{S5} = \mathsf{KT5}$ is the smallest [[normal modal logic|JS8W7PA6JK]] that contains the axioms
$$\mathrm{T}: \square p \to p \qquad \text{and} \qquad \mathrm{5}: \lozenge p \to \square\lozenge p.$$
An $\mathsf{S5}$-frame is a frame $(W, R)$ whose relation is an [[equivalence relation|0G8VEZ3WTK]].
A frame is universal when $R = W \times W$.

## Notation

The name comes from the fifth system of Lewis and Langford (1932).
Equivalent axiomatizations are $\mathsf{KTB4}$, $\mathsf{KT45}$ and $\mathsf{KTB5}$, see [[the axioms of S5|ECYRK9C2ZT]].
On a universal frame, $\square\varphi$ means "$\varphi$ holds at every world", so the accessibility relation is often omitted and a model is a pair $(W, V)$.

## Remarks

1. By [[common modal axiom schemata|FDFQFWPM4X]], a frame validates $\mathsf{S5}$ if and only if its relation is reflexive and Euclidean. That is, the relation is an equivalence relation, as in [[the accessibility relation|YHGXV3SQDP]].
2. $\mathsf{S5}$ is complete for equivalence relations and also for universal frames, see [[the completeness theorem|FXTCKYR3AQ]].
3. The full discussion, with modalities and complexity, is in [[modal logic S5|VC3A2VWXND]].

## Explanations

### L1 human

The logic $\mathsf{S5}$ treats "necessary" as "true in every possible world", with no world left out.
Then a statement is either necessary everywhere or nowhere, and the same holds for "possible".
For example, if it is possible that it rains, then it is necessary that it is possible that it rains.

### L2 human

We check axiom $\mathrm{5}$ on the universal frame $W = \set{1, 2}$ with $V(p) = \set{2}$.

1. $\lozenge p$ is true at 1 and at 2, since both see world 2, where $p$ holds.
2. $\square\lozenge p$ is true at 1 and at 2, since $\lozenge p$ holds at every world.
3. So $\lozenge p \to \square\lozenge p$ holds at both worlds.

The typical use of universal frames is to evaluate $\mathsf{S5}$ formulas: boxes and diamonds become "all worlds" and "some world".
A trap: $\mathsf{S5}$ is not the logic of one world; the trivial logic $\square p \leftrightarrow p$ is that.

### L3 human

Read on universal frames, $\square$ is the universal quantifier of one-variable first-order logic, and $\mathsf{S5}$ is that logic in modal notation.
