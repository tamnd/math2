---
tag: AYRX55XHZ6
kind: proof
name: Proof that the reals have the cardinality of the continuum
msc: ["03E10"]
proves: 075PM9FH7A
uses: [0STX0WRDNG, 0DS9KWFDK2, 01VG2A0BHW, 0PVG1CRAJN, 01FPXMTBX1, 0BC7KX51Z8, 05APWSX53S, 0FM6N4R0VB, 01BX15HSRR, 07XBM3A9J5, 0N32V0E3XJ, 0A9V6RKQG6, 0GPFKS96T7, 0WC28W9DNM, 0JTGRV4WT4, 08EJHHMB5R]
sources:
  - url: https://en.wikipedia.org/wiki/Cardinality_of_the_continuum
    locator: Cardinal equalities
---

## Proof

We give injections in both directions and apply the Schröder–Bernstein theorem.

1. Define $L \colon \R \to \mathcal{P}(\Q)$ by $L(x) = \{q \in \Q : q < x\}$, a subset of the [[power set|0BC7KX51Z8]] of $\Q$.
2. The map $L$ is [[injective|0PVG1CRAJN]]. Let $x \neq y$, say $x < y$. By the [[density of the rationals|0STX0WRDNG]], some $q \in \Q$ has $x < q < y$. Then $q \in L(y)$ and $q \notin L(x)$.
3. By [[the rationals are countable|0DS9KWFDK2]], there is a bijection $e \colon \N \to \Q$. Its inverse $e^{-1} \colon \Q \to \N$ is also a [[bijection|01VG2A0BHW]].
4. Define $E \colon \mathcal{P}(\Q) \to \mathcal{P}(\N)$ by $E(S) = e^{-1}(S)$. If $E(S) = E(T)$, then $S = e(e^{-1}(S)) = e(e^{-1}(T)) = T$. So $E$ is injective.
5. The composite $E \circ L \colon \R \to \mathcal{P}(\N)$ is [[injective|01FPXMTBX1]].
6. For $S \subseteq \N$ and $k \in \N$, let $s_k(S) = \sum_{n \in S,\ n < k} 10^{-(n+1)}$. The sequence $(s_k(S))_k$ is increasing, since each step adds a term $\ge 0$.
7. By the [[sum of a finite geometric series|05APWSX53S]], for $0 \le m \le M$ we have $\sum_{n=m}^{M} 10^{-(n+1)} = \frac{10^{-(m+1)}(1 - 10^{-(M-m+1)})}{1 - 1/10} < \frac{10^{-m}}{9}$.
8. By step 7 with $m = 0$, each $s_k(S) < 1/9$. By the [[monotone convergence theorem|0FM6N4R0VB]], $(s_k(S))_k$ converges. Let $F(S) \in \R$ be its limit.
9. We show that $F \colon \mathcal{P}(\N) \to \R$ is injective. Let $S \neq T$. By the [[well-ordering principle|01BX15HSRR]], there is a least $k$ in exactly one of $S$ and $T$. Say $k \in S$ and $k \notin T$.
10. Let $N > k + 1$. The sets $S$ and $T$ agree below $k$, so the terms with $n < k$ cancel in $s_N(S) - s_N(T)$. The term for $n = k$ is $10^{-(k+1)}$.
11. Each term with $k < n < N$ lies between $-10^{-(n+1)}$ and $10^{-(n+1)}$. So step 7 with $m = k + 1$ gives $s_N(S) - s_N(T) \ge 10^{-(k+1)} - \frac{10^{-(k+1)}}{9} = \frac{8}{9} \cdot 10^{-(k+1)}$.
12. By the [[algebra of limits|07XBM3A9J5]], $s_N(S) - s_N(T) \to F(S) - F(T)$. Since [[limits preserve non-strict inequalities|0N32V0E3XJ]], $F(S) - F(T) \ge \frac{8}{9} \cdot 10^{-(k+1)} > 0$. So $F(S) \neq F(T)$.
13. By the [[Schröder–Bernstein theorem|0A9V6RKQG6]], steps 5 and 12 give a bijection $\R \to \mathcal{P}(\N)$. So $\R$ and $\mathcal{P}(\N)$ are [[equinumerous|08EJHHMB5R]], and $|\R| = |\mathcal{P}(\N)|$ by the definition of [[cardinality|0JTGRV4WT4]].
14. By the [[cardinality of the power set|0GPFKS96T7]], $|\mathcal{P}(\N)| = 2^{|\N|} = 2^{\aleph_0}$, and this is the [[cardinality of the continuum|0WC28W9DNM]] $\mathfrak{c}$. Hence $|\R| = \mathfrak{c} = |\mathcal{P}(\N)|$.

## Idea

A real number is determined by the rationals below it, and there are only as many sets of rationals as sets of natural numbers. Conversely, a set $S$ of natural numbers gives the decimal $0.d_0 d_1 d_2 \ldots$ with $d_n = 1$ for $n \in S$ and $d_n = 0$ otherwise. Digits $0$ and $1$ never produce two expansions of the same number, so this map is injective.
