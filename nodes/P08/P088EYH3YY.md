---
tag: P088EYH3YY
kind: definition
name: P/poly
msc: [68Q15, 68Q06]
defines: P0A5DVRYDW
uses: [SQXNFGVADX, 5MFZ4VNY6D, ESPYW94XGR]
sources:
  - url: https://en.wikipedia.org/wiki/P/poly
---

## Definition

A language $L \subseteq \set{0,1}^*$ is in *P/poly* if there are a polynomial $p$ and a sequence $(C_n)_{n \ge 1}$ of [[Boolean circuits|SQXNFGVADX]] such that, for every $n$:

1. $C_n$ has $n$ inputs and at most $p(n)$ gates;
2. for every $x \in \set{0,1}^n$, $C_n(x) = 1$ if and only if $x \in L$.

## Remarks

No algorithm is required to produce $C_n$ from $n$.

Example: every unary language $L \subseteq \set{1}^*$ is in P/poly.
For each $n$ let $C_n$ compute $x_1 \wedge \cdots \wedge x_n$ if $1^n \in L$ and the constant $0$ otherwise; both have at most $n + 1$ gates, the constant $0$ being $x_1 \wedge \neg x_1$.
This holds even when $L$ is undecidable, as for $\set{1^n : \text{the } n \text{th Turing machine halts on the empty input}}$.

Non-example: a language whose indicator function on $\set{0,1}^n$ has [[circuit complexity|4PGX7PHJCK]] at least $2^n / (10 n)$ for every large enough $n$ fails clause 1 for every polynomial $p$.
Such languages exist by [[Shannon's counting argument|2R30KR3Z5G]].

Equivalent form: $L \in \mathrm{P/poly}$ if and only if there are a deterministic polynomial-time machine $M$, a polynomial $q$ and strings $a_n$ of length $q(n)$, the advice, such that $x \in L \iff M(x, a_{\abs{x}}) = 1$.
Every language in P is in P/poly, and Adleman showed $\mathrm{BPP} \subseteq \mathrm{P/poly}$.
