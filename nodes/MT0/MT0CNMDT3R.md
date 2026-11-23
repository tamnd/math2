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

The logic $\mathsf{S5}$ adds to $\mathsf{K}$ the laws "what is necessary is true" and "what is possible is necessarily possible".
Exactly, $\mathsf{S5} = \mathsf{KT5}$ is the smallest [[normal modal logic|JS8W7PA6JK]] that contains these axioms:
$$\mathrm{T}\colon \square p \to p, \qquad \mathrm{5}\colon \lozenge p \to \square\lozenge p.$$
An $\mathsf{S5}$-frame is a frame $(W, R)$ whose relation is an [[equivalence relation|0G8VEZ3WTK]].
A frame is *universal* when $R = W \times W$.

## Notation

The name is the fifth of the systems $\mathsf{S1}$ to $\mathsf{S5}$ of Lewis and Langford (1932).
Other axiom sets for the same logic are $\mathsf{KTB4}$, $\mathsf{KT45}$ and $\mathsf{KTB5}$, by [[the axioms of S5|ECYRK9C2ZT]].
On a universal frame, $\square\varphi$ means "$\varphi$ holds at every world", so the relation is often left out and a model is a pair $(W, V)$.

## Remarks

Each axiom is there for one property of the [[accessibility relation|YHGXV3SQDP]].
By the [[common modal axiom schemata|FDFQFWPM4X]], $\mathrm{T}$ is valid on a frame exactly when the frame is reflexive, and $\mathrm{5}$ exactly when it is Euclidean.
A reflexive Euclidean relation is an equivalence relation.
For symmetry, $x R y$ and $x R x$ give $y R x$ by the Euclidean law.
For transitivity, $x R y$ and $y R z$ give $y R x$ by symmetry, and then $y R x$ and $y R z$ give $x R z$ by the Euclidean law.

The two classes of frames are worth keeping apart.
On the equivalence relation with classes $\{ 1, 2 \}$ and $\{ 3 \}$, put $p$ at $1$ and $2$.
Then $\square p$ is true at $1$ and $2$ and false at $3$, so a boxed formula can change value across classes.
On a universal frame the value of a boxed formula is the same at every world.
Both classes give the logic $\mathsf{S5}$, by [[the completeness theorem|FXTCKYR3AQ]], because truth at a world depends only on its own class.

Without $\mathrm{T}$ the frames change: the frame with arrows $a R b$ and $b R b$ is Euclidean but not reflexive, and $\mathrm{T}$ fails at $a$ when $V(p) = \{ b \}$.
The concept page [[modal logic S5|VC3A2VWXND]] covers modalities and complexity.

## Explanations

### L1 human

The logic $\mathsf{S5}$ treats "necessary" as "true in every possible world", with no world left out.
Then a statement is either necessary everywhere or nowhere, and the same holds for "possible".
For example, if it is possible that it rains, then it is necessary that it is possible that it rains.

### L2 human

We check axiom $\mathrm{5}$ on the universal frame $W = \{ 1, 2 \}$ with $V(p) = \{ 2 \}$.
Both worlds see world $2$, where $p$ holds, so $\lozenge p$ is true at $1$ and at $2$.
Then $\lozenge p$ holds at every world, so $\square\lozenge p$ is true at $1$ and at $2$.
So $\lozenge p \to \square\lozenge p$ holds at both worlds.
This is how you evaluate $\mathsf{S5}$ formulas on a universal frame: boxes become "all worlds" and diamonds become "some world".
Watch out: $\mathsf{S5}$ is not the logic of one world, since one world with a loop validates $\square p \leftrightarrow p$, which $\mathsf{S5}$ does not prove.

### L3 human

Read on universal frames, $\square$ is the universal quantifier of one-variable first-order logic, and $\mathsf{S5}$ is that logic written in modal notation.
