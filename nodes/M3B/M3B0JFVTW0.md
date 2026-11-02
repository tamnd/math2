---
tag: M3B0JFVTW0
kind: definition
name: Family-wise error rate
msc: [62J15]
defines: GQCY1N8JZT
uses: [087P03NEND, 0R41PVFA39]
sources:
  - url: https://en.wikipedia.org/wiki/Family-wise_error_rate
---

## Definition

Let $H_1, \dots, H_m$ be null hypotheses about the law $P$ of the data, tested by a procedure that rejects a random subset of them.
Let $I_0(P) \subseteq \set{1, \dots, m}$ be the set of indices $i$ such that $H_i$ is true under $P$.
Let $V$ be the number of rejected $H_i$ with $i \in I_0(P)$, the number of [[type I errors|0R41PVFA39]].
The *family-wise error rate* is $\mathrm{FWER} = P(V \ge 1)$.
The procedure controls the FWER *strongly* at level $\alpha$ if $P(V \ge 1) \le \alpha$ for every $P$ in the model.
It controls the FWER *weakly* at level $\alpha$ if this holds for every $P$ under which all $H_i$ are true.

## Remarks

Strong control implies weak control.
Example: if $m$ tests of exact level $\alpha$ are independent and all null hypotheses are true, then $\mathrm{FWER} = 1 - (1 - \alpha)^m$.
So testing each hypothesis at level $\alpha$ does not control the FWER at level $\alpha$ for $m \ge 2$; this is the non-example.
The [[Bonferroni correction|8GRD2TMJRR]] tests each hypothesis at level $\alpha/m$ and gives strong control.
