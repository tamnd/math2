---
tag: 2PKHANZ8JS
kind: statement
role: theorem
name: Hahn decomposition theorem
msc: [28A10]
uses: [VG2P7R91Z7, N4KDT83V3S]
about: [VG2P7R91Z7]
sources:
  - url: https://en.wikipedia.org/wiki/Hahn_decomposition_theorem
same_as:
  wikidata: Q1568811
  wikipedia: Hahn decomposition theorem
---

## Statement

Let $(X, \Sigma)$ be a [[measurable space|N4KDT83V3S]] and let $\nu$ be a [[signed measure|VG2P7R91Z7]] on it.
A set $A \in \Sigma$ is *positive* for $\nu$ if $\nu(E) \ge 0$ for every $E \in \Sigma$ with $E \subseteq A$, and *negative* if $\nu(E) \le 0$ for all such $E$.
Then there are disjoint sets $P, N \in \Sigma$ with $P \cup N = X$ such that $P$ is positive and $N$ is negative for $\nu$.
If $P', N'$ is another such pair, then $P \triangle P' = N \triangle N'$ is null for $\nu$: every measurable subset of it has $\nu$-measure $0$.

## Remarks

Assume $\nu$ does not take the value $+\infty$; otherwise apply the argument to $-\nu$.
Let $s$ be the supremum of $\nu(A)$ over positive sets $A$.
A maximising sequence of positive sets has a positive union $P$ with $\nu(P) = s$.
Suppose $N = X \setminus P$ contained a set of strictly positive measure.
Then a lemma gives a positive subset of $N$ of strictly positive measure, and adding it to $P$ contradicts maximality.

Example: let $\nu(E) = \int_E f \, d\mu$ with $f \in L^1(\mu)$ real.
Then $P = \set{f \ge 0}$ and $N = \set{f < 0}$ is a Hahn decomposition.
The set $\set{f = 0}$ can be put into either part, which shows that the decomposition is unique only up to null sets.

## Explanations

### L1 human

A signed measure has regions where it is positive and regions where it is negative.
The theorem says that one can split the whole space into two measurable pieces, one on which every part counts positively and one on which every part counts negatively.
The cut is not unique, but the possible cuts differ only by sets that do not matter for $\nu$.

### L2 human

The Hahn decomposition is the first step towards the [[Jordan decomposition|WAGJVK2NWE]] $\nu = \nu^+ - \nu^-$, which reduces questions about signed measures to questions about measures.
It is also used in the proof of the [[Radon–Nikodym theorem|1ZSZS5G1Q4]], applied to signed measures of the form $\nu - c \mu$.
