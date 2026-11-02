---
tag: SC3MSJRJ3S
kind: definition
name: Supercompact cardinal
msc: ["03E55"]
defines: 91GE4C1BC5
uses: [0EBACQFAZW, CGH8C8EA9N, 0YSCSX5YZC]
sources:
  - url: https://en.wikipedia.org/wiki/Supercompact_cardinal
---

## Definition

Let $\kappa$ be a [[cardinal|0EBACQFAZW]], and let $\lambda \ge \kappa$ be an [[ordinal|0YSCSX5YZC]].
The cardinal $\kappa$ is *$\lambda$-supercompact* if there is an [[elementary embedding|CGH8C8EA9N]] $j \colon V \to M$, with $M$ a transitive class, such that:

1. The critical point of $j$ is $\kappa$, that is, $j(\alpha) = \alpha$ for $\alpha < \kappa$ and $j(\kappa) > \kappa$.
2. $j(\kappa) > \lambda$.
3. $M$ is closed under $\lambda$-sequences: every function from $\lambda$ to $M$ is an element of $M$.

The cardinal $\kappa$ is *supercompact* if it is $\lambda$-supercompact for every ordinal $\lambda \ge \kappa$.

## Remarks

A cardinal is $\kappa$-supercompact if and only if it is measurable: the ultrapower embedding by a $\kappa$-complete nonprincipal ultrafilter on $\kappa$ satisfies the three clauses with $\lambda = \kappa$.
So the least measurable cardinal is $\kappa$-supercompact, but it is not supercompact, since a supercompact cardinal has measurable cardinals below it.
An equivalent form uses ultrafilters on the set $P_\kappa(\lambda)$ of subsets of $\lambda$ of size less than $\kappa$.
The cardinal $\kappa$ is $\lambda$-supercompact if and only if there is a fine normal $\kappa$-complete ultrafilter on $P_\kappa(\lambda)$.
Every supercompact cardinal is a Woodin cardinal.
