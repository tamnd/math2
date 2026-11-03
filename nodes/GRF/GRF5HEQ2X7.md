---
tag: GRF5HEQ2X7
kind: definition
name: Arbitrage pricing theory
msc: [91G30, 91G10]
defines: 8ACQ87FEJF
uses: [Q626SC54P7, 0PNRKMRC55, 0WQNRCNY3M, 0KBFAWYRTE]
sources:
  - url: https://en.wikipedia.org/wiki/Arbitrage_pricing_theory
---

## Definition

Consider risky assets $i = 1, 2, \dots$ with returns $R_i$ over one period.
A *linear factor model* with $k$ factors is a representation
$$R_i = a_i + \sum_{j=1}^k b_{ij} F_j + \varepsilon_i,$$
where:

1. the factors $F_1, \dots, F_k$ are [[random variables|0PNRKMRC55]] with mean $0$;
2. the noise terms $\varepsilon_i$ have mean $0$ and are uncorrelated with the factors and with each other;
3. the variances of the $\varepsilon_i$ are bounded by a common constant.

The numbers $b_{ij}$ are the *factor loadings*.
*Arbitrage pricing theory* asserts that there are constants $\lambda_0, \lambda_1, \dots, \lambda_k$ with
$$\mathbb{E}[R_i] = \lambda_0 + \sum_{j=1}^k b_{ij} \lambda_j$$
for all $i$, either exactly or approximately in the sense of no asymptotic [[arbitrage|Q626SC54P7]].
The constant $\lambda_j$ is the *risk premium* of factor $j$, and $\lambda_0$ is the riskless return when a riskless asset exists.

## Remarks

Example: one factor and no noise.
Let $R_1 = a_1 + b F$ and $R_2 = a_2 + b F$ with the same loading $b$.
Buying asset $1$ and selling asset $2$, one unit each, costs nothing and returns $a_1 - a_2$ for sure.
Without arbitrage this must be $0$, so $a_1 = a_2$ and both assets have the same expected return, as the pricing relation requires.

Non-example: if the noise terms are strongly correlated with each other, clause 2 fails.
Then the noise does not diversify away in large portfolios, and the pricing relation need not hold even approximately.

With noise, the relation holds in a large market only approximately: the sum of the squared pricing errors over all assets is finite.
