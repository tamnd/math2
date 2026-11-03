---
tag: 3WNSDAEMQQ
kind: statement
role: theorem
name: Master theorem
msc: [68W40, 68Q25]
uses: [0FYX44GP92, 0TGV80E6A4]
about: [G9NFJ55KCX, 2TSJFYVFS8]
sources:
  - url: https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)
same_as:
  wikidata: Q922367
  wikipedia: Master theorem (analysis of algorithms)
---

## Statement

Let $a \ge 1$ and $b > 1$ be constants.
Let $f$ map the positive integers to the nonnegative reals, and let $T$ map the positive integers to the positive reals.
Assume that, for all sufficiently large $n$,
$$T(n) = a\, T(n/b) + f(n),$$
where $n/b$ stands for $\floor{n/b}$ or $\ceil{n/b}$.
Let $c^* = \log_b a$.

1. If $f(n) = O(n^{c})$ for some constant $c < c^*$, then $T(n) = \Theta(n^{c^*})$.
2. If $f(n) = \Theta(n^{c^*} (\log n)^k)$ for some constant $k \ge 0$, then $T(n) = \Theta(n^{c^*} (\log n)^{k+1})$.
3. If $f(n) = \Omega(n^{c})$ for some constant $c > c^*$, and there are constants $\kappa < 1$ and $n_0$ with $a f(n/b) \le \kappa f(n)$ for all $n \ge n_0$, then $T(n) = \Theta(f(n))$.

## Remarks

The proof unrolls the [[recurrence|0FYX44GP92]] into a tree of depth about $\log_b n$ whose level $j$ has $a^j$ nodes of cost $f(n/b^j)$.
The leaves contribute $\Theta(a^{\log_b n}) = \Theta(n^{c^*})$.
In case 1 the level costs grow geometrically toward the leaves, and in case 3 they shrink geometrically from the root.
In case 2 all $\log_b n$ levels cost about the same.
The rounding of $n/b$ changes the argument only by bounded amounts.

Example: [[merge sort|GNGVP9EE8Y]] has $T(n) = 2T(n/2) + \Theta(n)$, so $a = b = 2$, $c^* = 1$, case 2 applies with $k = 0$, and $T(n) = \Theta(n \log n)$.
[[Binary search|V67H7YCQ17]] has $T(n) = T(n/2) + \Theta(1)$, so $c^* = 0$ and $T(n) = \Theta(\log n)$.
[[Karatsuba multiplication|CD5Y77KGYA]] has $T(n) = 3T(n/2) + \Theta(n)$, so case 1 gives $T(n) = \Theta(n^{\log_2 3})$.

The three cases do not cover every $f$.
For $T(n) = 2T(n/2) + n / \log n$, the term $f$ is smaller than $n^{c^*} = n$ only by a logarithmic factor, so neither case 1 nor case 2 applies; the [[Akra–Bazzi method|VZ1J7KM4QS]] gives $T(n) = \Theta(n \log\log n)$.

## Explanations

### L1 human

Many recursive algorithms split a problem of size $n$ into $a$ pieces of size $n/b$ and spend $f(n)$ extra work to split and combine.
The master theorem reads off the total running time from $a$, $b$ and $f$ alone.
It compares the extra work $f(n)$ with $n^{\log_b a}$, the number of smallest subproblems, and the larger one wins.

### L2 human

The theorem is the standard tool for [[divide-and-conquer algorithms|G9NFJ55KCX]] with equal-sized subproblems.
The regularity condition in case 3 holds for $f(n) = n^c$ with $c > c^*$, since then $a f(n/b) = (a/b^{c}) f(n)$ and $a/b^{c} < 1$.
When the subproblems have different sizes, as in $T(n) = T(n/3) + T(2n/3) + n$, use the Akra–Bazzi method or a direct recursion-tree argument.
