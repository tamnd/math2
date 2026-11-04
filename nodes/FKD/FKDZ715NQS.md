---
tag: FKDZ715NQS
kind: proof
name: Proof of the absorption laws in a lattice
msc: [06B05]
proves: 0ZKZBJPG2J
uses: [X8WD0ABG07, F7YV441H6R, 0QV2JS9RJ3]
sources:
  - url: https://proofwiki.org/wiki/Join_Absorbs_Meet
  - url: https://proofwiki.org/wiki/Meet_Absorbs_Join
---

## Proof

We use the description of the join and the meet as least upper and greatest lower bounds.

1. If the [[lattice|X8WD0ABG07]] $L$ is given in algebraic form, the two absorption laws are among its axioms, and there is nothing to prove.
2. So let $L$ be a [[partially ordered set|0QV2JS9RJ3]] $(L, \le)$ in which every two elements have a [[join and a meet|F7YV441H6R]]. Let $a, b \in L$, and put $c = a \wedge b$.
3. The meet $c$ is a lower bound of $\set{a, b}$, so $c \le a$.
4. The element $a$ is an upper bound of $\set{a, c}$, since $a \le a$ by reflexivity and $c \le a$ by Step 3.
5. Every upper bound $z$ of $\set{a, c}$ satisfies $a \le z$, by the definition of an upper bound.
6. By Steps 4 and 5, $a$ is the least upper bound of $\set{a, c}$. The least upper bound is unique by antisymmetry, so $a \vee (a \wedge b) = a \vee c = a$.
7. Now put $d = a \vee b$. The join $d$ is an upper bound of $\set{a, b}$, so $a \le d$.
8. The element $a$ is a lower bound of $\set{a, d}$, since $a \le a$ and $a \le d$.
9. Every lower bound $z$ of $\set{a, d}$ satisfies $z \le a$.
10. By Steps 8 and 9, $a$ is the greatest lower bound of $\set{a, d}$, which is unique by antisymmetry. So $a \wedge (a \vee b) = a \wedge d = a$.

## Idea

The element $a \wedge b$ lies below $a$, so joining it with $a$ adds nothing: $a$ is already the smallest element above both. Dually, $a \vee b$ lies above $a$, so meeting it with $a$ gives back $a$.
