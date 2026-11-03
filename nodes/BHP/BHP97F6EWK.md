---
tag: BHP97F6EWK
kind: definition
name: Condorcet method
msc: [91B12, 91B14]
defines: WZYEADV8E1
uses: [JGP0Q56FRY, 0FRXBVVR03, V0EYM00JGK]
sources:
  - url: https://en.wikipedia.org/wiki/Condorcet_method
---

## Definition

Let $N$ be a finite set of voters and $A$ a finite set of candidates.
Each voter $i$ has a strict ranking $\succ_i$ of $A$, a [[linear order|0FRXBVVR03]].
For distinct $x, y \in A$, let $n(x, y)$ be the number of voters $i$ with $x \succ_i y$.
A candidate $c \in A$ is a *Condorcet winner* of the profile if $n(c, y) > n(y, c)$ for every $y \in A$ with $y \ne c$.
A *voting rule* assigns a winning candidate, or a set of winners, to each profile.
A *Condorcet method* is a voting rule that selects exactly the Condorcet winner whenever the profile has one.

## Remarks

A profile has at most one Condorcet winner: two of them would each beat the other.

Example: Copeland's method gives each candidate one point for each candidate it beats in pairwise majority, and elects the candidates with the most points.
A Condorcet winner beats all $\abs{A} - 1$ others, while any other candidate loses at least to the Condorcet winner, so Copeland's method is a Condorcet method.

Non-example: the [[Borda count|V0EYM00JGK]] is not a Condorcet method.
Take $A = \set{a, b, c}$, three voters with $a \succ b \succ c$ and two voters with $b \succ c \succ a$.
Then $a$ beats $b$ and $c$ by $3$ to $2$, so $a$ is the Condorcet winner.
The Borda scores (2 points for first place, 1 for second) are $a: 6$, $b: 7$, $c: 2$, so Borda elects $b$.
