---
tag: YGP3Q2EF31
kind: definition
name: Bonferroni correction
msc: [62J15]
defines: 8GRD2TMJRR
uses: [GQCY1N8JZT, 0EHYZFZ4PK, 0EGSEE9J9R]
sources:
  - url: https://en.wikipedia.org/wiki/Bonferroni_correction
---

## Definition

Let $H_1, \dots, H_m$ be null hypotheses with [[p-values|0EHYZFZ4PK]] $p_1, \dots, p_m$, and let $\alpha \in (0, 1)$.
The *Bonferroni correction* at level $\alpha$ is the procedure that rejects $H_i$ exactly when $p_i \le \alpha/m$.

## Remarks

Assume each p-value is valid: if $H_i$ is true, then $P(p_i \le u) \le u$ for all $u \in [0, 1]$.
Let $I_0$ be the set of true null hypotheses and $m_0$ its size.
By [[Boole's inequality|0EGSEE9J9R]], $P(\text{some } H_i \text{ with } i \in I_0 \text{ is rejected}) \le \sum_{i \in I_0} P(p_i \le \alpha/m) \le m_0 \alpha/m \le \alpha$.
So the correction controls the [[family-wise error rate|GQCY1N8JZT]] strongly at level $\alpha$, with no assumption on the joint law of the p-values.
Example: with $m = 10$ and $\alpha = 0.05$, a hypothesis is rejected when its p-value is at most $0.005$.
Non-example: rejecting when $p_i \le \alpha$ is not the correction, and with $m$ independent true nulls its FWER is $1 - (1 - \alpha)^m > \alpha$.
Equivalently, one rejects $H_i$ when the adjusted p-value $\min(1, m p_i)$ is at most $\alpha$.
