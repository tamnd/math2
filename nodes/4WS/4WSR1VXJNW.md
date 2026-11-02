---
tag: 4WSR1VXJNW
kind: definition
name: Tate algebra
msc: [32P05, 14G22, 12J25]
defines: B1TEQ98JZD
uses: [1H5F1BP6XS, W168DS966V, 033WGN00BF, 9KYWN94QDN]
sources:
  - url: https://en.wikipedia.org/wiki/Restricted_power_series
---

## Definition

Let $K$ be a field that is complete with respect to a nontrivial [[non-archimedean absolute value|1H5F1BP6XS]] $\abs{\cdot}$, and let $n \ge 0$.
For a multi-index $\nu = (\nu_1, \dots, \nu_n) \in \N^n$ write $X^\nu = X_1^{\nu_1} \cdots X_n^{\nu_n}$ and $\abs{\nu} = \nu_1 + \cdots + \nu_n$.
The *Tate algebra* in $n$ variables over $K$ is the subring
$$T_n = K\langle X_1, \dots, X_n \rangle = \Big\{ \sum_{\nu \in \N^n} a_\nu X^\nu \in K[\![X_1, \dots, X_n]\!] : \abs{a_\nu} \to 0 \text{ as } \abs{\nu} \to \infty \Big\}$$
of the [[formal power series|033WGN00BF]] ring.
Its *Gauss norm* is $\norm{\sum a_\nu X^\nu} = \max_\nu \abs{a_\nu}$.

## Remarks

The maximum exists because $\abs{a_\nu} \to 0$.
$T_n$ is closed under multiplication, and the Gauss norm is multiplicative: $\norm{fg} = \norm{f} \norm{g}$.
With this norm $T_n$ is a [[Banach algebra|9KYWN94QDN]] over $K$, and the polynomial ring $K[X_1, \dots, X_n]$ is dense in it.
Let $\bar K$ be an algebraic closure of $K$ with the extended absolute value.
A formal power series lies in $T_n$ exactly when it converges at every point $x \in \bar K^n$ with all $\abs{x_i} \le 1$.
$T_n$ is Noetherian, regular and a unique factorization domain, and it satisfies a Noether normalization lemma.
The residue field of each maximal ideal of $T_n$ is a finite extension of $K$.

Example: over the [[completion|W168DS966V]] $\Q_p$ of $\Q$ for the $p$-adic absolute value, $f = \sum_{k \ge 0} p^k X^k$ lies in $T_1$, because $\abs{p^k}_p = p^{-k} \to 0$; its Gauss norm is $\abs{1}_p = 1$.

Non-example: $\sum_{k \ge 0} X^k$ has all coefficients of absolute value $1$, which do not tend to $0$, so it is not in $T_1$; it diverges at $X = 1$.
