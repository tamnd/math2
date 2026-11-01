---
tag: B1YJM6EENP
kind: definition
name: Monad in nonstandard topology
msc: [54J05, "26E35", "03H05"]
defines: RAGJSF4V9V
uses: [0CQHFPGJ45, 02BH3MCBQB, 0S1FJ8VEX9, 0TVJZYB6SH, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(nonstandard_analysis)
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let ${}^*X$ be its extension in a model of nonstandard analysis that is an enlargement.
For an [[open set|02BH3MCBQB]] $U \subseteq X$, write ${}^*U \subseteq {}^*X$ for its extension.
The *monad* of a point $x \in X$ is
$$\mu(x) = \bigcap \set{{}^*U : U \subseteq X \text{ open}, \ x \in U}.$$
A point $y \in {}^*X$ is *infinitely close* to $x$ if $y \in \mu(x)$.

## Remarks

Example: for $X = \R$ with the usual topology, ${}^*X$ is the field of hyperreal numbers.
A hyperreal $y$ lies in $\mu(x)$ exactly when $\abs{y - x} < 1/n$ for every positive integer $n$, that is, when $y - x$ is infinitesimal; so $x + \varepsilon \in \mu(x)$ for every infinitesimal $\varepsilon$.
Non-example: for $x = 0$ and a positive infinitesimal $\varepsilon$, the hyperreal $1 + \varepsilon$ is not in $\mu(0)$, since it is not in ${}^*(-1/2, 1/2)$.
The standard part of a finite hyperreal $y$ is the unique real $x$ with $y \in \mu(x)$.
Standard characterizations in an enlargement: $X$ is [[Hausdorff|0S1FJ8VEX9]] if and only if distinct points have disjoint monads.
$X$ is [[compact|0TVJZYB6SH]] if and only if every point of ${}^*X$ lies in the monad of some point of $X$.
A map $f \colon X \to Y$ is [[continuous|0X3WGX95FE]] at $x$ if and only if ${}^*f(\mu(x)) \subseteq \mu(f(x))$.
