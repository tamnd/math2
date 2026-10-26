---
tag: ~cbaece73
kind: statement
role: proposition
name: Monotonicity of probability
msc: [60A05]
uses: [~ae896b89, ~ff25e688, 0FE8Q5S42Y]
sources:
  - url: https://en.wikipedia.org/wiki/Probability_axioms
    locator: Elementary consequences
---

## Statement

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|~ae896b89]] and let $A, B \in \mathcal{F}$ be [[events|~ff25e688]] with $A \subseteq B$.
Then $P(A) \le P(B)$.
More precisely, $P(B \setminus A) = P(B) - P(A)$.

## Remarks

The proof: $B$ is the disjoint union of $A$ and $B \setminus A$, so $P(B) = P(A) + P(B \setminus A)$, and $P(B \setminus A) \ge 0$.
With $B = \Omega$, monotonicity gives $P(A) \le 1$ for each event $A$.
If $A$ implies $B$, then $B$ is at least as likely as $A$. For example, "the die shows $6$" is at most as likely as "the die shows an even number".

## Explanations

### L1 human

A bigger event contains more outcomes, so it cannot be less likely.
The chance to draw a heart from a deck is at most the chance to draw a red card, because every heart is red.
