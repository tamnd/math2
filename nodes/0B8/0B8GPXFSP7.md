---
tag: 0B8GPXFSP7
kind: statement
role: proposition
name: Continuity via closed sets
msc: [54C05]
uses: [0SY9ECQ19Q, 0G5AV9Q4RR, 0K67Q60Z8P, 0FGCFY1AZX]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Closure operator and interior operator definitions
---

## Statement

Let $X$ and $Y$ be [[topological spaces|0CNQXVBHCX]] and let $f \colon X \to Y$ be a function.
Then $f$ is [[continuous|0SY9ECQ19Q]] if and only if for each [[closed set|0G5AV9Q4RR]] $F$ of $Y$, the [[preimage|0FGCFY1AZX]] $f^{-1}(F)$ is closed in $X$.

## Remarks

Proof: preimages commute with complements, that is, $f^{-1}(Y \setminus A) = X \setminus f^{-1}(A)$ for each $A \subseteq Y$. Then use that the [[complements of open sets are closed|0K67Q60Z8P]].
For example, for a continuous $f \colon \mathbb{R} \to \mathbb{R}$, the set of zeros $f^{-1}(\{0\})$ is closed.

## Explanations

### L1 human

Continuity can be tested with closed sets as well as with open sets.
This form is useful to show that a set given by an equation, such as $\{x : f(x) = 0\}$, is closed.
