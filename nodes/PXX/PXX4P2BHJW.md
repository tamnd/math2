---
tag: PXX4P2BHJW
kind: definition
name: Morley rank
msc: [03C45]
defines: WN43DRPNBX
uses: [RMTZ5J64FX, CY1TXHF6KQ, HYJ10AF6RT, 0YSCSX5YZC, CGH8C8EA9N, MT8TDVPBXB, T7JW5QY6KR]
sources:
  - url: https://en.wikipedia.org/wiki/Morley_rank
---

## Definition

Let $M$ be an $L$-structure that is $\aleph_0$-[[saturated|RMTZ5J64FX]], and let $\varphi(\bar{x})$ be an $L$-[[formula|HYJ10AF6RT]] with parameters from $M$.
Write $\varphi(M)$ for the [[definable set|CY1TXHF6KQ]] of tuples of $M$ that satisfy $\varphi$.
For each [[ordinal|0YSCSX5YZC]] $\alpha$, the relation $\mathrm{RM}(\varphi) \ge \alpha$ is defined by induction on $\alpha$:

1. $\mathrm{RM}(\varphi) \ge 0$ if $\varphi(M)$ is nonempty;
2. $\mathrm{RM}(\varphi) \ge \alpha + 1$ if there are formulas $\psi_0, \psi_1, \dots$ with parameters from $M$ whose sets $\psi_i(M)$ are pairwise disjoint subsets of $\varphi(M)$ with $\mathrm{RM}(\psi_i) \ge \alpha$;
3. for a limit ordinal $\alpha$, $\mathrm{RM}(\varphi) \ge \alpha$ if $\mathrm{RM}(\varphi) \ge \beta$ for every $\beta < \alpha$.

The *Morley rank* $\mathrm{RM}(\varphi)$ is $-1$ if $\varphi(M)$ is empty.
Otherwise it is the largest ordinal $\alpha$ with $\mathrm{RM}(\varphi) \ge \alpha$ if one exists, and $\infty$ if $\mathrm{RM}(\varphi) \ge \alpha$ for every ordinal $\alpha$.
For an arbitrary $L$-structure $N$ and a formula with parameters from $N$, the Morley rank is computed in an $\aleph_0$-saturated [[elementary extension|CGH8C8EA9N]] of $N$.
It does not depend on the choice of the extension.

## Remarks

Example: in an [[algebraically closed field|MT8TDVPBXB]] $K$, the formula $x = x$ in one variable has Morley rank $1$.
The singletons $\set{a}$ for distinct $a \in K$ are infinitely many disjoint sets of rank $0$, so the rank is at least $1$.
By quantifier elimination every definable subset of $K$ is finite or cofinite, so no two disjoint definable subsets are both infinite.
A set of rank at least $1$ is infinite, so the rank of $x = x$ is not at least $2$.
More generally, in $K^n$ the Morley rank of an irreducible variety is its Krull dimension.

Non-example: in the theory of dense linear orders without endpoints, the formula $x = x$ has Morley rank $\infty$.
The rank of an open interval is at least $\alpha$ for every $\alpha$, by induction, since an interval contains infinitely many pairwise disjoint open intervals.

A complete theory $T$ in a countable signature is $\omega$-stable, a strong form of [[stability|T7JW5QY6KR]], if and only if every formula has Morley rank less than $\infty$.
