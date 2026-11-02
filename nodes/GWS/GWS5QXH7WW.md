---
tag: GWS5QXH7WW
kind: definition
name: Club set
msc: ["03E05", "03E10"]
defines: YW8YSCFPG5
uses: [0RDJK7EQYY, 0BTMQ04556, NTE5C260S1]
sources:
  - url: https://en.wikipedia.org/wiki/Club_set
---

## Definition

Let $\kappa$ be a limit [[ordinal|0RDJK7EQYY]] of uncountable [[cofinality|NTE5C260S1]], and let $C \subseteq \kappa$.
The set $C$ is a club set in $\kappa$ if both conditions hold:

1. $C$ is closed: for each nonzero limit ordinal $\alpha < \kappa$, if $\sup(C \cap \alpha) = \alpha$, then $\alpha \in C$.
2. $C$ is unbounded: for each $\beta < \kappa$ there is $\gamma \in C$ with $\gamma \ge \beta$.

Here $\sup$ is the [[supremum|0BTMQ04556]] of a set of ordinals.

## Remarks

Example: the set $C$ of limit ordinals below $\omega_1$ is club in $\omega_1$.
It is unbounded, since $\beta + \omega \in C$ for each $\beta < \omega_1$.
It is closed, since a limit of limit ordinals is a limit ordinal.
Non-example: the set of successor ordinals below $\omega_1$ is unbounded but not closed.
Indeed the successor ordinals below $\omega$ have supremum $\omega$, which is not a successor.
Condition 1 says that $C$ is closed in the order topology of $\kappa$.
If $\kappa$ is a regular uncountable cardinal, the intersection of fewer than $\kappa$ club sets in $\kappa$ is club.
For such $\kappa$, the diagonal intersection $\set{\alpha < \kappa : \alpha \in \bigcap_{\xi < \alpha} C_\xi}$ of a sequence $(C_\xi)_{\xi < \kappa}$ of club sets is club.
For such $\kappa$, the range of a [[normal function|PXTF18X433]] from $\kappa$ to $\kappa$ is club, and so is its set of fixed points.
