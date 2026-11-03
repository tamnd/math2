---
tag: 9FPH2Z9DKR
kind: definition
name: Borda count
msc: [91B12, 91B14]
defines: V0EYM00JGK
uses: [JGP0Q56FRY, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Borda_count
---

## Definition

Let $N$ be a finite set of voters and $A$ a finite set of $m \ge 2$ candidates.
Each voter $i$ has a strict ranking $\succ_i$ of $A$, a [[linear order|0FRXBVVR03]].
The *Borda score* of a candidate $x$ in the ranking $\succ_i$ is the number of candidates ranked below $x$:
$$\beta_i(x) = \abs{\set{y \in A : x \succ_i y}}.$$
The *Borda score* of $x$ in the profile is $B(x) = \sum_{i \in N} \beta_i(x)$.
The *Borda count* is the voting rule that elects the candidates with the largest Borda score.

## Remarks

Equivalently, a candidate in position $k$ of a ranking receives $m - k$ points.
Another form: $B(x) = \sum_{y \ne x} n(x, y)$, where $n(x, y)$ is the number of voters ranking $x$ above $y$.

Example: with $A = \set{a, b, c}$, three voters with $a \succ b \succ c$ and two voters with $b \succ c \succ a$, the scores are $B(a) = 3 \cdot 2 + 2 \cdot 0 = 6$, $B(b) = 3 \cdot 1 + 2 \cdot 2 = 7$ and $B(c) = 0 + 2 \cdot 1 = 2$, so $b$ is elected.

Non-example: the plurality rule gives $1$ point for first place and $0$ for every other place.
Its points do not decrease by one at each position, so it is a different scoring rule; on the profile above it elects $a$.

The Borda count is a positional scoring rule; ties need a separate tie-breaking rule.
