---
tag: F1CCCF4V83
kind: statement
role: lemma
name: Rokhlin lemma
msc: [37A05, 28D05]
uses: [QDDRDW9PXS, 556WBDAHNP]
about: [556WBDAHNP]
sources:
  - url: https://en.wikipedia.org/wiki/Rokhlin_lemma
same_as:
  wikidata: Q21069246
  wikipedia: Rokhlin lemma
---

## Statement

Let $(X, \mathcal{B}, \mu)$ be a [[standard probability space|QDDRDW9PXS]] and let $T \colon X \to X$ be an invertible [[measure-preserving transformation|556WBDAHNP]] with measurable inverse.
Assume that $T$ is aperiodic: for every $n \ge 1$, the set $\set{x \in X : T^n x = x}$ has measure $0$.
Then for every integer $n \ge 1$ and every $\varepsilon > 0$ there is a set $B \in \mathcal{B}$ such that:

1. the sets $B, TB, T^2B, \dots, T^{n-1}B$ are pairwise disjoint, and
2. $\mu(B \cup TB \cup \cdots \cup T^{n-1}B) > 1 - \varepsilon$.

## Remarks

The sets $B, TB, \dots, T^{n-1}B$ form a Rokhlin tower of height $n$ with base $B$, and $T$ moves each level to the next one.
The proof for ergodic $T$ starts from a set $F$ of small positive measure and slices the space by the first return time to $F$.
Each column of height at least $n$ is cut into blocks of height $n$, and the leftover has measure at most about $n \mu(F)$.
Example at work: a tower gives a periodic approximation of $T$.
Define $P = T$ on $B \cup \cdots \cup T^{n-2}B$, let $P = T^{-(n-1)}$ on $T^{n-1}B$, and let $P$ be the identity elsewhere.
Then $P^n$ is the identity, $P$ preserves $\mu$, and $P$ agrees with $T$ outside a set of measure less than $\mu(B) + \varepsilon \le 1/n + \varepsilon$.
The aperiodicity hypothesis is necessary: if $T^2 = \mathrm{id}$ and $n = 3$, then $T^2 B = B$, so condition 1 forces $\mu(B) = 0$ and condition 2 fails.
The error $\varepsilon$ cannot be removed in general.
If a tower of height $n \ge 2$ covers $X$ up to a null set, then $T^n B = B$ up to a null set, and $f = \sum_{j=0}^{n-1} e^{2\pi i j/n} \mathbf{1}_{T^j B}$ satisfies $f \circ T = e^{2\pi i/n} f$.
So $f$ is a nonconstant eigenfunction, which is impossible when $T$ is weakly mixing, for example a Bernoulli scheme.

## Explanations

### L1 human

Any measure-preserving map without periodic behaviour can be pictured, up to a tiny leftover, as a tall stack of $n$ floors.
The map moves each floor up to the next one, and only at the top floor does something complicated happen.
The height $n$ can be as large as you like and the leftover as small as you like.

### L2 human

The lemma is the main tool for building approximations and codings in ergodic theory.
It shows that every aperiodic transformation can be approximated in the weak topology by periodic ones.
It is used in the proofs of Sinai's factor theorem and of Ornstein's isomorphism theorem.
It extends to free actions of $\Z^d$ and of countable amenable groups, where the role of intervals of times is played by Følner sets.
