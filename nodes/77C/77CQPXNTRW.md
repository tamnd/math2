---
tag: 77CQPXNTRW
kind: definition
name: Universally measurable set
msc: [28A05, 28C15]
defines: GSFXAV0VD7
uses: [N4KDT83V3S, 0VGMEBVW1M, KJNSKV75VQ]
sources:
  - url: https://en.wikipedia.org/wiki/Universally_measurable_set
---

## Definition

Let $(X, \Sigma)$ be a [[measurable space|N4KDT83V3S]].
For a [[probability measure|0VGMEBVW1M]] $\mu$ on $(X, \Sigma)$, let $\Sigma_\mu$ be the σ-algebra of the [[completion|KJNSKV75VQ]] of $\mu$.
A subset $A \subseteq X$ is *universally measurable* if $A \in \Sigma_\mu$ for every probability measure $\mu$ on $(X, \Sigma)$.

## Remarks

Every $A \in \Sigma$ is universally measurable, since $\Sigma \subseteq \Sigma_\mu$ for every $\mu$.
The universally measurable sets form a σ-algebra, the intersection of all the $\Sigma_\mu$.
Let $X = [0, 1]$ with its Borel σ-algebra, and let $\lambda$ be Lebesgue measure on it.
Then $\Sigma_\lambda$ is the σ-algebra of Lebesgue measurable subsets of $[0, 1]$, and a Vitali set $V \subseteq [0, 1]$ is not in it.
So $V$ is not universally measurable.
The definition is usually applied when $X$ is a Polish space and $\Sigma$ is its Borel σ-algebra; then every analytic set is universally measurable.
Replacing probability measures by σ-finite measures gives the same family of sets.
