---
tag: ATHH5BY7MW
kind: definition
name: Kemeny–Young method
msc: [91B12, 91B14]
defines: ENTVWXCEBD
uses: [JGP0Q56FRY, 0FRXBVVR03, WZYEADV8E1, DYFY16SFHZ, V0EYM00JGK]
sources:
  - url: https://en.wikipedia.org/wiki/Kemeny_method
---

## Definition

Let $N$ be a finite set of voters and $A$ a finite set of candidates.
Each voter $i$ has a strict ranking $\succ_i$ of $A$, a [[linear order|0FRXBVVR03]].
For distinct $x, y \in A$, let $n(x, y)$ be the number of voters $i$ with $x \succ_i y$.
The *Kemeny score* of a linear order $\succ$ of $A$ is
$$K(\succ) = \sum_{x \succ y} n(x, y),$$
the sum over all pairs $(x, y)$ with $x$ ranked above $y$ in $\succ$.
The *Kemeny–Young method* selects the linear orders $\succ$ of $A$ with the largest Kemeny score, and elects the top candidate of such an order.

## Remarks

Equivalently, a Kemeny ranking minimizes $\sum_{i \in N} d(\succ, \succ_i)$, where $d$ is the Kendall tau distance.
This distance counts the pairs on which two rankings disagree, and it is related to the [[Kendall rank correlation coefficient|DYFY16SFHZ]].

Example: let $A = \set{a, b, c}$, three voters with $a \succ b \succ c$ and two with $b \succ c \succ a$.
Then $n(a, b) = 3$, $n(a, c) = 3$, $n(b, c) = 5$, $n(b, a) = 2$, $n(c, a) = 2$ and $n(c, b) = 0$.
The ranking $a \succ b \succ c$ has score $3 + 3 + 5 = 11$, and the other five rankings have scores $10, 9, 6, 5, 4$.
So the Kemeny ranking is $a \succ b \succ c$ and $a$ is elected; $a$ is also the Condorcet winner.

Non-example: on the same profile the [[Borda count|V0EYM00JGK]] ranks $b \succ a \succ c$, whose Kemeny score is $2 + 5 + 3 = 10 < 11$, so the Borda ranking is not a Kemeny ranking.

If a [[Condorcet winner|WZYEADV8E1]] $c$ exists, swapping $c$ with the candidate just above it replaces a term $n(y, c)$ by the larger $n(c, y)$.
So every ranking with $c$ below the top has a smaller score than some other ranking, every Kemeny ranking puts $c$ first, and the Kemeny–Young method is a Condorcet method.
