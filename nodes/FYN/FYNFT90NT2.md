---
tag: FYNFT90NT2
kind: statement
role: lemma
name: Frostman lemma
msc: [28A78, 28A80]
uses: [Q1TGZK8RN6, SSNFTHZ6YJ, HZNEQQBCW4, FQTXV6BQZG, 0R6EWFKRCF]
about: [Q1TGZK8RN6, SSNFTHZ6YJ]
sources:
  - url: https://en.wikipedia.org/wiki/Frostman_lemma
same_as:
  wikidata: Q5506220
  wikipedia: Frostman lemma
---

## Statement

Let $A \subseteq \R^n$ be a Borel set and let $s \ge 0$.
Let $\mathcal{H}^s$ be the $s$-dimensional [[Hausdorff measure|Q1TGZK8RN6]], and let $B(x, r)$ be the closed ball of centre $x$ and radius $r$.
Then $\mathcal{H}^s(A) > 0$ if and only if there is a nonzero [[Radon measure|HZNEQQBCW4]] $\mu$ on $\R^n$ with these two properties:

1. The [[support|FQTXV6BQZG]] of $\mu$ is a [[compact set|0R6EWFKRCF]] contained in $A$.
2. $\mu(B(x, r)) \le r^s$ for every $x \in \R^n$ and every $r > 0$.

## Remarks

The direction from $\mu$ to $\mathcal{H}^s(A) > 0$ is the mass distribution principle.
If $A \subseteq \bigcup_i U_i$, each nonempty $U_i$ lies in a closed ball of radius $\operatorname{diam} U_i$ centred at a point of $U_i$.
So $0 < \mu(A) \le \sum_i \mu(U_i) \le \sum_i (\operatorname{diam} U_i)^s$, and the infimum over covers is at least $\mu(A)$.
For the other direction, with $A$ compact, one builds $\mu$ on dyadic cubes from the finest scale upwards, cutting the mass wherever the bound fails, and takes a weak limit.
The Borel case reduces to the compact case, since a Borel set with $\mathcal{H}^s(A) > 0$ contains a compact set with positive $\mathcal{H}^s$ measure.

As a consequence, $\dim_H A = \sup \set{ s \ge 0 : \text{a measure as above exists} }$ for every Borel set $A$, where $\dim_H$ is the [[Hausdorff dimension|SSNFTHZ6YJ]].

Example: for $A = [0, 1] \subseteq \R$ and $s = 1$, Lebesgue measure restricted to $[0, 1]$ works, since an interval of radius $r$ has length $2r$.
After scaling by $\frac12$, it satisfies $\mu(B(x, r)) \le r$.

## Explanations

### L1 human

A set is at least $s$-dimensional in the sense of Hausdorff measure exactly when one can spread a positive amount of mass on it that is never too concentrated.
Here "not too concentrated" means that a ball of radius $r$ carries at most $r^s$ of the mass.
This turns a question about all covers of the set into the search for one good measure.

### L2 human

Lower bounds for Hausdorff dimension are usually proved by constructing a Frostman measure, since upper bounds come from explicit covers.
The lemma leads to the energy method: if $A$ carries a nonzero measure with finite $t$-energy, then $\dim_H A \ge t$.
It is a standard tool in projection theorems and in the study of Kakeya sets.
It also links Hausdorff dimension to capacity in potential theory.
