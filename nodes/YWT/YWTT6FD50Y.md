---
tag: YWTT6FD50Y
kind: definition
name: Oriented matroid
msc: [52C40, 05B35, 52B40]
defines: R5EB9NKQ5M
uses: [PX31ZNYS3Z, 0CRMGPAH83]
sources:
  - url: https://en.wikipedia.org/wiki/Oriented_matroid
---

## Definition

Let $E$ be a finite set.
A *signed subset* of $E$ is a pair $X = (X^+, X^-)$ of disjoint subsets of $E$; its support is $\underline{X} = X^+ \cup X^-$, and $-X = (X^-, X^+)$.
An *oriented matroid* on $E$, given by its signed circuits, is a set $\mathcal{C}$ of signed subsets of $E$ such that:

1. $(\emptyset, \emptyset) \notin \mathcal{C}$.
2. If $X \in \mathcal{C}$, then $-X \in \mathcal{C}$.
3. If $X, Y \in \mathcal{C}$ and $\underline{X} \subseteq \underline{Y}$, then $X = Y$ or $X = -Y$.
4. If $X, Y \in \mathcal{C}$, $X \ne -Y$, and $e \in X^+ \cap Y^-$, then there is $Z \in \mathcal{C}$ with $Z^+ \subseteq (X^+ \cup Y^+) \setminus \set{e}$ and $Z^- \subseteq (X^- \cup Y^-) \setminus \set{e}$.

## Remarks

The supports of the signed circuits are the circuits of a [[matroid|PX31ZNYS3Z]] on $E$, the underlying matroid.
Axiom 4 is the signed form of circuit elimination.
There are equivalent axiom systems in terms of covectors, of vectors and of chirotopes, which are signed versions of the bases.

Example: let $v_1, \dots, v_n$ be vectors in $\R^r$ and $E = \set{1, \dots, n}$.
For each linear dependence $\sum_i \lambda_i v_i = 0$ whose support $\set{i : \lambda_i \ne 0}$ is minimal and nonempty, put $X^+ = \set{i : \lambda_i > 0}$ and $X^- = \set{i : \lambda_i < 0}$.
These signed sets satisfy the axioms; such oriented matroids are called realizable.
For $v_1 = e_1$, $v_2 = e_2$, $v_3 = e_1 + e_2$ in $\R^2$, the only minimal dependence up to scaling is $v_1 + v_2 - v_3 = 0$, so $\mathcal{C} = \set{(\set{1,2}, \set{3}), (\set{3}, \set{1,2})}$.

Non-example: on $E = \set{1, 2}$, the set $\mathcal{C} = \set{(\set{1}, \set{2}), (\set{1,2}, \emptyset), (\set{2}, \set{1}), (\emptyset, \set{1,2})}$ fails axiom 3, since all four sets have the same support but $(\set{1}, \set{2}) \ne \pm (\set{1,2}, \emptyset)$.
