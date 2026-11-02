---
tag: W8DZQZQTJA
kind: definition
name: False discovery rate and the Benjamini–Hochberg procedure
msc: [62J15]
defines: 6CHHCTGQ18
uses: [0EHYZFZ4PK, GQCY1N8JZT, 087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/False_discovery_rate
    locator: Benjamini–Hochberg procedure
---

## Definition

Let $H_1, \dots, H_m$ be null hypotheses tested by a procedure that rejects $R$ of them.
Let $V$ be the number of rejected hypotheses that are true.
The *false discovery proportion* is $Q = V/R$ if $R \ge 1$ and $Q = 0$ if $R = 0$.
The *false discovery rate* is $\mathrm{FDR} = E[Q]$.

Let $p_1, \dots, p_m$ be [[p-values|0EHYZFZ4PK]] for the $H_i$, ordered as $p_{(1)} \le \dots \le p_{(m)}$ with hypotheses $H_{(1)}, \dots, H_{(m)}$, and let $q \in (0, 1)$.
The *Benjamini–Hochberg procedure* at level $q$ lets $k$ be the largest $i$ with $p_{(i)} \le i q/m$.
It rejects $H_{(1)}, \dots, H_{(k)}$, and it rejects nothing if no such $i$ exists.

## Remarks

Benjamini and Hochberg proved the following in 1995.
If the p-values of the $m_0$ true nulls are independent, uniform on $[0, 1]$, and independent of the other p-values, then the procedure has $\mathrm{FDR} \le m_0 q/m \le q$.
Benjamini and Yekutieli later extended the bound to a form of positive dependence.
If all null hypotheses are true, then $Q = 1$ whenever $R \ge 1$, so $\mathrm{FDR} = P(R \ge 1)$ is the [[family-wise error rate|GQCY1N8JZT]].
In general $\mathrm{FDR} \le \mathrm{FWER}$, since $Q \le 1$ and $Q = 0$ when $V = 0$.
Example: with $m = 4$, $q = 0.05$ and p-values $0.001, 0.02, 0.03, 0.5$, the thresholds are $0.0125, 0.025, 0.0375, 0.05$.
The first three p-values are below their thresholds, so $k = 3$ and $H_{(1)}, H_{(2)}, H_{(3)}$ are rejected.
Non-example: the rule "reject $H_{(i)}$ when $p_{(i)} \le q/m$" is the Bonferroni rule, not the Benjamini–Hochberg procedure; here it rejects only $H_{(1)}$.
