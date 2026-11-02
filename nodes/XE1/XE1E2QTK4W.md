---
tag: XE1E2QTK4W
kind: definition
name: Lebesgue–Stieltjes measure
msc: [28A12, 26A42]
defines: QV75XJBFCS
uses: [WPR0NVC9PC, PR11BZQQPG, 0WQXY32Q8D, 0A7KV2WB7A]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue%E2%80%93Stieltjes_integration
---

## Definition

Let $F \colon \R \to \R$ be a [[non-decreasing|0A7KV2WB7A]] function that is right-continuous at every point, that is, a [[Stieltjes function|WPR0NVC9PC]].
The *Lebesgue–Stieltjes measure* of $F$ is the unique [[measure|PR11BZQQPG]] $\mu_F$ on the [[Borel sigma-algebra|0WQXY32Q8D]] of $\R$ such that
$$\mu_F((a, b]) = F(b) - F(a) \quad \text{for all } a < b.$$

## Remarks

Existence comes from the Carathéodory extension theorem applied to the premeasure $(a, b] \mapsto F(b) - F(a)$ on half-open intervals; right-continuity is what makes it countably additive.
Uniqueness holds because $\R$ is a countable union of intervals $(-n, n]$ of finite measure.
Many authors also call the completion of $\mu_F$ the Lebesgue–Stieltjes measure.
Example: $F(x) = x$ gives Lebesgue measure on the Borel sets.
Example: for $F = \mathbf{1}_{[0, \infty)}$, which is right-continuous, $\mu_F$ is the Dirac measure at $0$, and $\mu_F(\set{a}) = F(a) - \lim_{x \to a^-} F(x)$ in general.
Non-example: $F(x) = -x$ is not non-decreasing, and the formula would give $(0, 1]$ the negative value $-1$.
Two functions $F$ and $G$ give the same measure if and only if $F - G$ is constant.
The notation $dF$ is common, as in $\int g \, dF$.
