---
tag: CBNYG6QV03
kind: definition
name: Robust statistics
msc: [62F35, 62G35]
defines: J7410PG2DR
uses: [TASMEPWNA6, 0TTNRP5PFQ, 0AJN7WHBJZ, BRGGGZVQDS, EB2QJQNE5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_statistics
---

## Definition

*Robust statistics* is the study of statistical procedures that remain reliable when the true distribution of the data is only close to the assumed model.
The basic precise notion is Hampel's qualitative robustness.
Let $X_1, X_2, \dots$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with distribution $F$, and let $T_n = T_n(X_1, \dots, X_n)$, $n \ge 1$, be a sequence of [[estimators|0TTNRP5PFQ]].
Write $\mathcal{L}_F(T_n)$ for the law of $T_n$ when the $X_i$ have distribution $F$, and let $\pi$ be the [[Lévy–Prokhorov metric|TASMEPWNA6]] on probability distributions.
The sequence $(T_n)$ is *qualitatively robust* at $F$ if for every $\varepsilon > 0$ there is $\delta > 0$ such that for every distribution $G$ and every $n$,
$$\pi(F, G) < \delta \implies \pi\big(\mathcal{L}_F(T_n), \mathcal{L}_G(T_n)\big) < \varepsilon.$$

## Remarks

Qualitative robustness asks that the maps $G \mapsto \mathcal{L}_G(T_n)$ be continuous at $F$, uniformly in $n$.
Closeness in $\pi$ allows both small rounding of all data and a small fraction of arbitrary outliers.
The quantitative measures are the [[breakdown point|BRGGGZVQDS]] and the [[influence function|EB2QJQNE5Z]].

Example: if $F$ has a unique median $m$, the sample median is qualitatively robust at $F$.
A small fraction of outliers can shift it only to nearby order statistics, so its law changes little.

Non-example: the sample mean is not qualitatively robust at any $F$.
Let $0 < \eta < \delta$ and $G = (1 - \eta) F + \eta \, \delta_x$, with $\delta_x$ the point mass at $x$; then $\pi(F, G) \le \eta < \delta$.
For large $n$, with high probability about $n\eta$ observations equal $x$, and the mean moves by about $\eta x$, which is arbitrarily large for large $x$.
