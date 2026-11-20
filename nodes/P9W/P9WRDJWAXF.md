---
tag: P9WRDJWAXF
kind: example
name: FLew does not prove p to p times p
msc: ["03B47", "03F05"]
topics: [98QF5J4W16]
audience: research
not_instance_of:
  - target: V5XVVN16GS
    note: the sequent p to p times p is not derivable in FLew, since FLew has no contraction
uses: [Q47701D0E1, JSAH84Y9G2, VGS1GCM047]
sources:
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 1.4 Contraction
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - book: isbn:9780444521415
    note: Galatos, Jipsen, Kowalski and Ono, Residuated Lattices
---

## Example

Let $p$ be an atom.
The sequent $p \Rightarrow p \cdot p$ is not derivable in $\mathsf{FL}_{ew}$, the [[full Lambek calculus|Q47701D0E1]] with exchange and weakening.
So this sequent is not a theorem of the logic, although it is a theorem of intuitionistic logic.

1. By [[cut elimination|JSAH84Y9G2]], it suffices to show that there is no cut-free derivation.
2. The empty sequent $\Rightarrow$ has no cut-free derivation, since no axiom and no rule other than cut has it as conclusion.
3. $\Rightarrow p$ has no cut-free derivation: it is not an axiom, the only rule with this conclusion is right weakening, and its premise is the empty sequent.
4. $p \Rightarrow$ has no cut-free derivation: it is not an axiom, $p$ is an atom, and left weakening would need the empty sequent.
5. $\Rightarrow p \cdot p$ could come only from ${\cdot}\mathrm{R}$ with premises $\Rightarrow p$ and $\Rightarrow p$, or from right weakening of the empty sequent.
   Both fail by steps 2 and 3.
6. Now consider the last rule for $p \Rightarrow p \cdot p$.
   Exchange needs two formulas on the left, and $p$ is an atom, so no left logical rule applies.
7. Left weakening of $p$ needs $\Rightarrow p \cdot p$, which fails by step 5.
   Right weakening needs $p \Rightarrow$, which fails by step 4.
8. ${\cdot}\mathrm{R}$ splits the antecedent $p$ into two parts, one of them empty.
   So it needs $\Rightarrow p$, which fails by step 3.
9. No rule remains, so $p \Rightarrow p \cdot p$ is not derivable.

## Remarks

With left [[contraction|VGS1GCM047]] the sequent is derivable: ${\cdot}\mathrm{R}$ gives $p, p \Rightarrow p \cdot p$, and contraction gives $p \Rightarrow p \cdot p$.
An algebraic check gives the same result.
In the $\mathsf{FL}_{ew}$-algebra on $\set{0, \tfrac12, 1}$ with fusion $x \cdot y = \max(0, x + y - 1)$, the value $p = \tfrac12$ gives $p \cdot p = 0 < \tfrac12$.
By the soundness of $\mathsf{FL}_{ew}$ for its algebras, this also shows that the sequent is not derivable.

## Explanations

### L1 human

The sequent says "one copy of $p$ gives two copies of $p$".
Without the contraction rule, this is false: one coin does not give two coins.
The proof checks every rule that could end a derivation, and each one fails.

### L2 human

We check the algebra of the remarks.

1. The elements are $0$, $\tfrac12$ and $1$, ordered as numbers, and $1$ is the unit of fusion, since $\max(0, x + 1 - 1) = x$.
2. Fusion is commutative and monotone, and $x \leq 1$ and $0 \leq x$ for all $x$, so exchange and weakening are sound.
3. The residual is $x \backslash y = \min(1, 1 - x + y)$.
   For example, $\tfrac12 \backslash 0 = \tfrac12$, and indeed $\tfrac12 \cdot z \leq 0$ holds exactly for $z \leq \tfrac12$.
4. With $p = \tfrac12$, the sequent $p \Rightarrow p \cdot p$ says $\tfrac12 \leq 0$, which is false.

The typical use is to separate two logics by one sequent and one small algebra.
A trap: in this algebra $\tfrac12 \wedge \tfrac12 = \tfrac12$, so $p \Rightarrow p \wedge p$ is valid; only fusion fails to be idempotent.
