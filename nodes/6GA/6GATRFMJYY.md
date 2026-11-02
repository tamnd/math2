---
tag: 6GATRFMJYY
kind: statement
role: theorem
name: Basu's theorem
msc: [62B05]
uses: [QNMR5F525C, PF4RHTZWXH, NR6MGAB5V0, 0XCE070V8B, 0YAMJRK04E]
about: [WP4TGXJQJG, DED6JFAV1K, VBW2A4H6TD]
sources:
  - url: https://en.wikipedia.org/wiki/Basu%27s_theorem
same_as:
  wikidata: Q791258
  wikipedia: Basu's theorem
---

## Statement

Let $\set{P_\theta : \theta \in \Theta}$ be a family of probability measures for the data $X$.
Let $T = T(X)$ be a [[sufficient|QNMR5F525C]] statistic that is boundedly [[complete|PF4RHTZWXH]], and let $V = V(X)$ be an [[ancillary|NR6MGAB5V0]] statistic.
Then, for every $\theta \in \Theta$, the statistics $T$ and $V$ are [[independent|0XCE070V8B]] under $P_\theta$.

## Remarks

Proof idea: fix a measurable set $B$ and let $q = P_\theta(V \in B)$, which does not depend on $\theta$ since $V$ is ancillary.
By sufficiency, the [[conditional probability|0YAMJRK04E]] $k(T) = P_\theta(V \in B \mid T)$ can be chosen free of $\theta$.
Then $k(T) - q$ is bounded and $E_\theta[k(T) - q] = 0$ for all $\theta$, so bounded completeness gives $k(T) = q$ almost surely; that is, $V \in B$ is independent of $T$.
Example: for $X_1, \dots, X_n$ i.i.d. $\mathcal{N}(\mu, \sigma^2)$ with $\sigma^2$ known and $\mu \in \R$, $\bar{X}$ is complete and sufficient for $\mu$, and the sample variance $S^2$ is ancillary; so $\bar{X}$ and $S^2$ are independent.
Since $\sigma^2$ was arbitrary, this proves the independence of $\bar{X}$ and $S^2$ for every normal sample.
Completeness cannot be dropped: for $n \ge 2$ the whole sample $T = (X_1, \dots, X_n)$ is sufficient, and $V = X_1 - X_2$ is ancillary, but $V$ is a non-constant function of $T$, so they are not independent.

## Explanations

### L1 human

A complete sufficient statistic holds all the information about the parameter, and an ancillary statistic holds none.
Basu's theorem says that two such statistics do not even influence each other: they are independent.
This gives quick proofs of independence results that are otherwise hard to compute.

### L2 human

The best-known use is the independence of the sample mean and the sample variance of a normal sample, which underlies the $t$-distribution of $\sqrt{n}(\bar{X} - \mu)/S$.
More generally, in an exponential family of full rank the natural sufficient statistic is complete, so it is independent of every ancillary statistic.
The theorem also allows one to compute $E_\theta[V \mid T]$ as $E_\theta[V]$ for an integrable ancillary $V$, which simplifies Rao–Blackwell computations.
