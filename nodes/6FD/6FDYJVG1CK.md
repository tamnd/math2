---
tag: 6FDYJVG1CK
kind: definition
name: Stationary set
msc: ["03E05", "03E10"]
defines: YE6WZR46RQ
uses: [GWS5QXH7WW, ZCE333FAWC]
sources:
  - url: https://en.wikipedia.org/wiki/Stationary_set
---

## Definition

Let $\kappa$ be an uncountable [[regular cardinal|ZCE333FAWC]], and let $S \subseteq \kappa$.
The set $S$ is stationary in $\kappa$ if $S \cap C \ne \varnothing$ for each [[club set|GWS5QXH7WW]] $C$ in $\kappa$.

## Remarks

Example: each club set $D$ in $\kappa$ is stationary.
Check: for each club $C$, the intersection $C \cap D$ is club, hence unbounded, hence nonempty.
Example: the set $\set{\alpha < \omega_2 : \operatorname{cf}(\alpha) = \omega}$ is stationary in $\omega_2$.
Check: each club $C$ in $\omega_2$ contains the supremum of its first $\omega$ elements, and this supremum has cofinality $\omega$.
Non-example: a bounded set $S \subseteq \kappa$, with $S \subseteq \beta$ for some $\beta < \kappa$, misses the club set $\set{\alpha : \beta \le \alpha < \kappa}$.
The sets that are not stationary form a $\kappa$-complete ideal, the nonstationary ideal; it is closed under diagonal unions.
The same definition is used for a limit ordinal of uncountable cofinality in place of $\kappa$.
By a theorem of Solovay, each stationary subset of $\kappa$ is the union of $\kappa$ pairwise disjoint stationary sets.
