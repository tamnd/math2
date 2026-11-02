---
tag: 1DHZ81S0YE
kind: statement
role: theorem
name: Krylov–Bogolyubov theorem
msc: [37A05, 37C40, 28A33]
uses: [B232EZ1FMB, 0TVJZYB6SH, 0VKD1TP7F3, 0X3WGX95FE, 059TJN0NZ1, DYR1QFNGNJ, MBW9JCGZC1, D6FMEQYA76]
about: [B232EZ1FMB]
sources:
  - url: https://en.wikipedia.org/wiki/Krylov–Bogolyubov_theorem
same_as:
  wikidata: Q1121027
  wikipedia: Krylov–Bogolyubov theorem
---

## Statement

Let $X$ be a [[compact|0TVJZYB6SH]] [[metric space|0VKD1TP7F3]], and let $T \colon X \to X$ be a [[continuous map|0X3WGX95FE]].
Then there is a Borel [[probability measure|059TJN0NZ1]] $\mu$ on $X$ that is [[$T$-invariant|B232EZ1FMB]], that is, $\mu(T^{-1}(A)) = \mu(A)$ for every Borel set $A \subseteq X$.

## Remarks

Fix $x \in X$ and let $\mu_n = \frac{1}{n} \sum_{k=0}^{n-1} \delta_{T^k(x)}$, where $\delta_y$ is the point mass at $y$.
Since $X$ is compact, the [[Borel probability measures|DYR1QFNGNJ]] on $X$ form a compact set for [[weak convergence|MBW9JCGZC1]], for instance by [[Prokhorov's theorem|D6FMEQYA76]].
So some subsequence $\mu_{n_j}$ converges weakly to a probability measure $\mu$.
For continuous $g \colon X \to \R$ one has $\int g \circ T \, d\mu_n - \int g \, d\mu_n = \frac{1}{n}\left(g(T^n(x)) - g(x)\right)$, which tends to $0$.
Passing to the limit gives $\int g \circ T \, d\mu = \int g \, d\mu$ for all continuous $g$, and this forces $T_* \mu = \mu$.
The same argument gives an invariant probability measure for a continuous flow on a compact metric space.

Compactness is needed: the translation $T(x) = x + 1$ on $\R$ has no invariant probability measure.
Indeed, invariance would give $\mu([k, k+1)) = \mu([0, 1))$ for every $k \in \Z$, and these countably many disjoint sets cover $\R$, so their measures cannot sum to $1$.

Example: for the rotation $x \mapsto x + \alpha \bmod 1$ of the circle, the theorem produces an invariant measure; when $\alpha$ is irrational, it is Lebesgue measure, which is the only invariant one.

## Explanations

### L1 human

Any continuous motion of a compact space has a way of spreading out mass that the motion leaves unchanged.
One finds it by following one orbit for a long time and recording how often it visits each region.
These visit frequencies settle down, at least along a subsequence, to an invariant measure.

### L2 human

The theorem makes ergodic theory available for every continuous map of a compact metric space: there is always at least one invariant probability measure to work with.
The set of invariant probability measures is a nonempty compact convex set, and its extreme points are the ergodic measures, so ergodic invariant measures exist as well.
When the invariant measure is unique, the map is called uniquely ergodic, and then Birkhoff averages of continuous functions converge uniformly.
The variational principle for topological entropy is a supremum over this set of invariant measures.
