---
tag: 83DSSH4HZY
kind: definition
name: Fuzzy measure
msc: ["28E10"]
defines: CRFQEGJDA9
uses: [PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Fuzzy_measure_theory
    locator: Definitions
---

## Definition

Let $X$ be a set and let $\mathcal{C}$ be a family of subsets of $X$ with $\emptyset \in \mathcal{C}$.
A *fuzzy measure* on $(X, \mathcal{C})$ is a map $g \colon \mathcal{C} \to [0, \infty]$ such that:

1. $g(\emptyset) = 0$.
2. If $E, F \in \mathcal{C}$ and $E \subseteq F$, then $g(E) \le g(F)$.

If $X \in \mathcal{C}$ and $g(X) = 1$, the fuzzy measure is *normalised*.

## Remarks

Often $\mathcal{C}$ is a $\sigma$-algebra or the set of all subsets of a finite set $X$.
Example: let $\mu$ be a probability measure on a $\sigma$-algebra $\mathcal{C}$ and $g(E) = \mu(E)^2$.
Then $g(\emptyset) = 0$, and $g$ is monotone because $\mu$ is monotone and squaring is increasing on $[0, 1]$.
It is not additive: if $\mu(E) = \mu(F) = 1/2$ with $E \cap F = \emptyset$, then $g(E) + g(F) = 1/2$ but $g(E \cup F) = 1$.
Non-example: $g(E) = \mu(E) - \mu(E)^2$ vanishes on $\emptyset$, but it is not monotone: $g(E) = 1/4$ for $\mu(E) = 1/2$, while $g(X) = 0$.
Every [[measure|PR11BZQQPG]] is a fuzzy measure.
