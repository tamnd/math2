---
tag: PW2TVRD47Y
kind: definition
name: Small cancellation theory
msc: ["20F06", "20F05"]
defines: 3A1D37TVF6
uses: [0KTW26C80J, 0JGEQXQ4AC]
sources:
  - url: https://en.wikipedia.org/wiki/Small_cancellation_theory
---

## Definition

Let $F(S)$ be the [[free group|0KTW26C80J]] on a set $S$, with elements written as freely reduced words.
Let $\abs{w}$ be the length of a word $w$.
A set $R$ of cyclically reduced words in $F(S)$ is *symmetrized* if it is closed under taking inverses and cyclic permutations.
Let $R$ be symmetrized.
A *piece* relative to $R$ is a nonempty word $u$ such that two distinct elements $r_1 \ne r_2$ of $R$ both begin with $u$.
That is, $r_1 = u v_1$ and $r_2 = u v_2$ with no cancellation.

1. Let $\lambda$ be a real number with $0 < \lambda < 1$. Then $R$ satisfies the *condition $C'(\lambda)$* if $\abs{u} < \lambda \abs{r}$ whenever $r \in R$ and $r = u v$ with $u$ a piece.
2. For an integer $p \ge 2$, $R$ satisfies the *condition $C(p)$* if no element of $R$ is a product of fewer than $p$ pieces.

A [[presentation|0JGEQXQ4AC]] $\langle S \mid R_0 \rangle$ is a *small cancellation presentation* of type $C'(\lambda)$ or $C(p)$ if the symmetrized closure of $R_0$ satisfies the condition.
*Small cancellation theory* is the study of groups with such presentations.

## Remarks

The condition $C'(\lambda)$ implies $C(p)$ for $p$ with $\lambda \le 1/(p-1)$; in particular $C'(1/6)$ implies $C(7)$.
Greendlinger's lemma: if $R$ satisfies $C'(1/6)$ and a nontrivial reduced word $w$ equals $1$ in $\langle S \mid R \rangle$, then $w$ contains a subword of some $r \in R$ of length greater than $\abs{r}/2$.

Example: let $S = \set{a, b, c, d}$ and $r = a b a^{-1} b^{-1} c d c^{-1} d^{-1}$.
In $r$ and its cyclic permutations each two-letter subword occurs once, and no two-letter subword of $r^{-1}$ or of its cyclic permutations occurs in $r$.
So all pieces have length $1$, and $1 < \frac{1}{6} \cdot 8$, so the presentation satisfies $C'(1/6)$.

Non-example: $\langle a, b \mid a b a^{-1} b^{-1} \rangle$, a presentation of $\Z^2$, does not satisfy $C'(1/6)$.
Each letter is a piece, but the relator has length $4$ and $1 \ge \frac{1}{6} \cdot 4$.
