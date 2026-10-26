---
tag: 0HJ4DTW6FN
kind: statement
role: theorem
name: Second isomorphism theorem for rings
msc: [16D25]
uses: [0VFW4Y69BT, 0859D58WPD, 0B6QC0C0G1]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem B (rings)
---

## Statement

Let $R$ be a [[ring|0894J980RK]], let $S$ be a [[subring|0859D58WPD]] of $R$ and let $I$ be a two-sided ideal of $R$.
Then $S + I = \{s + x : s \in S, x \in I\}$ is a subring of $R$, and $I$ is a two-sided ideal of $S + I$.
The intersection $S \cap I$ is a two-sided ideal of $S$.
The map $S/(S \cap I) \to (S + I)/I$, $s + (S \cap I) \mapsto s + I$, is a [[ring isomorphism|0B6QC0C0G1]].

## Remarks

The proof applies the [[first isomorphism theorem|0ZMYX7GMH0]] to the map $S \to (S + I)/I$, $s \mapsto s + I$. It is surjective, and its kernel is $S \cap I$.
The theorem is also called the diamond theorem, after the picture of the four rings $S \cap I$, $S$, $I$ and $S + I$.

## Explanations

### L1 human

The theorem compares two quotients.
Divide the subring $S$ by its part inside $I$, or divide the larger ring $S + I$ by $I$.
The two quotients are the same ring.
