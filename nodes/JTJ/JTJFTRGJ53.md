---
tag: JTJFTRGJ53
kind: definition
name: Coherent risk measure
msc: [91G70, 91B05]
defines: YR1E91KSFA
uses: [0PNRKMRC55, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_risk_measure
---

## Definition

Let $\mathcal{L}$ be a vector space of real [[random variables|0PNRKMRC55]] on a probability space that contains the constants.
An element $L \in \mathcal{L}$ is read as the loss of a position.
A map $\rho \colon \mathcal{L} \to \R$ is a *coherent risk measure* if, for all $L, L_1, L_2 \in \mathcal{L}$:

1. (monotonicity) if $L_1 \le L_2$ almost surely, then $\rho(L_1) \le \rho(L_2)$;
2. (translation invariance) $\rho(L + m) = \rho(L) + m$ for every $m \in \R$;
3. (subadditivity) $\rho(L_1 + L_2) \le \rho(L_1) + \rho(L_2)$;
4. (positive homogeneity) $\rho(\lambda L) = \lambda \rho(L)$ for every $\lambda \ge 0$.

## Remarks

Example: $\rho(L) = E[L]$, the [[expected value|0WQNRCNY3M]], on integrable $L$, satisfies all four clauses by linearity and monotonicity of expectation.
Example: on bounded $L$, $\rho(L) = \operatorname{ess\,sup} L$, the worst-case loss, is coherent.
Non-example: $\rho(L) = E[L] + c \sqrt{\operatorname{Var}(L)}$ with $c > 0$ fails monotonicity.
For instance, if $L_1 = 0$ and $L_2 = -1$ or $0$ with probability $1/2$ each, then $L_2 \le L_1$ but $\rho(L_2) = -1/2 + c/2 > 0 = \rho(L_1)$ when $c > 1$.
Value at risk satisfies clauses 1, 2 and 4 but not 3.
Many authors work with the profit $X = -L$; then translation invariance reads $\rho(X + m) = \rho(X) - m$.
