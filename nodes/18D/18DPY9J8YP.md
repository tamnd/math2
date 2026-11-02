---
tag: 18DPY9J8YP
kind: definition
name: Kolmogorov complexity
msc: [68Q30, 03D32]
defines: 8PY3K6NCKF
uses: [TC69PEHAX7, KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_complexity
---

## Definition

Let $\set{0,1}^*$ be the set of finite binary strings, and let $\abs{p}$ denote the length of a string $p$.
For a partial [[computable function|KZSB5E471K]] $\varphi \colon \set{0,1}^* \to \set{0,1}^*$ and a string $x$, let
$$C_\varphi(x) = \min \set{\abs{p} : \varphi(p) = x},$$
with $C_\varphi(x) = \infty$ if no such $p$ exists.
Fix a partial computable function $U$, given by a [[universal Turing machine|TC69PEHAX7]], with this property.
For every partial computable $\varphi$ there is a string $q_\varphi$ with $U(q_\varphi p) = \varphi(p)$ for all $p$, where $q_\varphi p$ is the concatenation.
The (plain) *Kolmogorov complexity* of $x$ is $C(x) = C_U(x)$.

## Remarks

Invariance theorem: for every partial computable $\varphi$ and every $x$, $C(x) \le C_\varphi(x) + \abs{q_\varphi}$.
So two choices of $U$ give complexities that differ by at most a constant.

Example: there is a constant $c$ with $C(x) \le \abs{x} + c$ for all $x$, by taking $\varphi$ the identity, which has $C_\varphi(x) = \abs{x}$.
For the string $0^n$ of $n$ zeros, $C(0^n) \le \log_2 n + c'$ for a constant $c'$, because a program can read $n$ in binary and print $n$ zeros.

Non-example: $C_{\mathrm{id}}(x) = \abs{x}$, the complexity for the identity function, is not the Kolmogorov complexity.
The identity is not universal, and $C_{\mathrm{id}}(0^n) = n$ exceeds $C(0^n)$ by more than any constant.

For each $n$ there is a string $x$ of length $n$ with $C(x) \ge n$, since there are $2^n$ such strings but only $2^n - 1$ strings of length less than $n$.
The function $C$ is not computable.
A variant, the prefix-free complexity $K$, uses a universal machine whose domain is a prefix-free set.
