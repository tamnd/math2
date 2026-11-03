---
tag: 3RFH3GS3AK
kind: definition
name: Capital asset pricing model
msc: [91G10, 91G30]
defines: 3T10Q8A736
uses: [ZBDA8W9D6V, SCTRT97C2R, 0WQNRCNY3M, 0477R9PYAE, 0KBFAWYRTE]
sources:
  - url: https://en.wikipedia.org/wiki/Capital_asset_pricing_model
---

## Definition

Consider a single-period market with a riskless asset of return $r_f$ and risky assets with returns $R_1, \dots, R_n$.
Let $R_M$ be the return of the market portfolio, which holds every risky asset in proportion to its total market value, and assume $\operatorname{Var}(R_M) > 0$.
The *beta* of asset $i$ is
$$\beta_i = \frac{\operatorname{Cov}(R_i, R_M)}{\operatorname{Var}(R_M)},$$
with [[covariance|0KBFAWYRTE]] and [[variance|0477R9PYAE]].
The *capital asset pricing model* is the assertion that, for every $i$,
$$\mathbb{E}[R_i] = r_f + \beta_i \left( \mathbb{E}[R_M] - r_f \right).$$
The line $\beta \mapsto r_f + \beta (\mathbb{E}[R_M] - r_f)$ is the *security market line*.

## Remarks

The relation holds in equilibrium when all investors choose [[mean–variance efficient|SCTRT97C2R]] portfolios, share the same beliefs about means and covariances, and can borrow and lend at $r_f$.
Then everyone holds the same tangency portfolio, which must be the market portfolio.

Example: with $r_f = 0.02$, $\mathbb{E}[R_M] = 0.08$ and $\beta_i = 1.5$, the model gives $\mathbb{E}[R_i] = 0.02 + 1.5 \cdot 0.06 = 0.11$.
The market itself has $\beta_M = 1$, and the riskless asset has $\beta = 0$.

Non-example: an asset with $\beta_i = 0$ and $\mathbb{E}[R_i] = 0.05$ when $r_f = 0.02$ does not satisfy the model, since the model requires $\mathbb{E}[R_i] = r_f$.

Writing $R_i - r_f = \beta_i (R_M - r_f) + \varepsilon_i$ with $\operatorname{Cov}(\varepsilon_i, R_M) = 0$ splits the variance of $R_i$ into a systematic part $\beta_i^2 \operatorname{Var}(R_M)$ and an idiosyncratic part $\operatorname{Var}(\varepsilon_i)$.
Only the systematic part is priced.
