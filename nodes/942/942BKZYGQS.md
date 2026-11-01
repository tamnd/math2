---
tag: 942BKZYGQS
kind: definition
name: P-adic analysis
msc: [30G06, 11S80, "26E30"]
defines: ASMPNM7K0M
uses: [BT6T702C28, WGN82TCEF2, 03HDF50VN4, V6TJAFZ4MD]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_analysis
---

## Definition

Let $p$ be a prime number.
Let $\Q_p$ be the field of [[$p$-adic numbers|BT6T702C28]], the completion of $\Q$ for the [[$p$-adic absolute value|WGN82TCEF2]] $\abs{x}_p = p^{-v_p(x)}$, where $v_p$ is the [[$p$-adic valuation|03HDF50VN4]].
*$p$-adic analysis* is the study of functions defined on subsets of $\Q_p$ or of a complete field extension of $\Q_p$.
The values lie in such a field or in $\R$ or $\C$.
It treats limits, series, continuity, differentiability, power series and integration for the topology given by $\abs{\cdot}_p$.

## Remarks

The absolute value $\abs{\cdot}_p$ satisfies the strong triangle inequality $\abs{x + y}_p \le \max(\abs{x}_p, \abs{y}_p)$.
Hence a series $\sum_n a_n$ in $\Q_p$ converges if and only if $a_n \to 0$.

Example: $\abs{p^n}_p = p^{-n} \to 0$, so $\sum_{n \ge 0} p^n$ converges in $\Q_p$, and its sum is $\frac{1}{1 - p}$, since $(1 - p) \sum_{n=0}^{N} p^n = 1 - p^{N+1} \to 1$.

Non-example: the same series $\sum_{n \ge 0} p^n$ diverges for the usual absolute value on $\R$; its study is part of real analysis, not of $p$-adic analysis.

Two typical facts.
The ring $\Z_p$ of [[$p$-adic integers|V6TJAFZ4MD]] is compact and totally disconnected.
The exponential series $\sum_n x^n / n!$ converges in $\Q_p$ exactly when $\abs{x}_p < p^{-1/(p-1)}$.
