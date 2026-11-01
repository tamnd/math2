---
tag: CFRN0G7GDB
kind: statement
role: theorem
name: Continuous mapping theorem
msc: [60F05, 60B10]
uses: [0FQ968YKA1, 0SRYJGXKR4, 0QA1HBD9Z4, 0AAXWGT5TD, 0VKD1TP7F3, 0X3WGX95FE]
about: [0FQ968YKA1]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_mapping_theorem
same_as:
  wikidata: Q5165492
  wikipedia: Continuous mapping theorem
---

## Statement

Let $(S, d)$ and $(S', d')$ be [[metric spaces|0VKD1TP7F3]] with their Borel $\sigma$-algebras.
Let $X, X_1, X_2, \dots$ be random elements of $S$.
Let $g \colon S \to S'$ be a measurable map, and let $D_g$ be the set of points of $S$ at which $g$ is not [[continuous|0X3WGX95FE]].
Assume that $P(X \in D_g) = 0$.

1. If $X_n \to X$ [[in distribution|0SRYJGXKR4]], then $g(X_n) \to g(X)$ in distribution.
2. If the $X_n$ and $X$ are defined on one probability space and $X_n \to X$ [[in probability|0QA1HBD9Z4]], then $g(X_n) \to g(X)$ in probability.
3. If the $X_n$ and $X$ are defined on one probability space and $X_n \to X$ [[almost surely|0AAXWGT5TD]], then $g(X_n) \to g(X)$ almost surely.

## Remarks

Part 3 is direct: on the event where $X_n \to X$ and $X \notin D_g$, the continuity of $g$ at $X$ gives $g(X_n) \to g(X)$, and this event has probability $1$.
Part 1 follows from the portmanteau theorem: for a closed set $F \subseteq S'$, the closure of $g^{-1}(F)$ lies in $g^{-1}(F) \cup D_g$.
Part 2 follows from part 3 applied along subsequences, since convergence in probability holds exactly when every subsequence has a further subsequence that converges almost surely.

Example: if $X_n \to Z$ in distribution with $Z$ standard normal, then $X_n^2$ converges in distribution to a chi-squared variable with one degree of freedom.

The hypothesis $P(X \in D_g) = 0$ cannot be dropped.
Take $X_n = 1/n$, $X = 0$ and $g = \mathbf{1}_{(0, \infty)}$.
Then $X_n \to X$ surely, but $g(X_n) = 1$ for all $n$ while $g(X) = 0$.
Here $D_g = \set{0}$ and $P(X \in D_g) = 1$.

## Explanations

### L1 human

If random quantities settle down to a limit, then any continuous function of them settles down to the same function of the limit.
This holds for each of the three usual kinds of convergence.
The function may even jump at some points, as long as the limit almost never lands on such a point.

### L2 human

The theorem is the main tool to move limit results from one statistic to another.
With [[Slutsky's theorem|GCV10B5HES]] and the [[central limit theorem|0EPZC4Z1FC]], it gives the limit laws of sums, products, quotients and squares of asymptotically normal statistics.
It also underlies the delta method, where $g$ is a differentiable function.
For random paths, applied with $g$ the supremum map, it turns [[Donsker's theorem|818832PMSV]] into a limit law for the maximum of a random walk.
