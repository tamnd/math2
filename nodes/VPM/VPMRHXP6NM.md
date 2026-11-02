---
tag: VPMRHXP6NM
kind: statement
role: theorem
name: Control variates
msc: [65C05]
uses: [A01GEGWKVB, 0477R9PYAE, 0KBFAWYRTE, 0DNN9B6Q2F, 0WQNRCNY3M]
about: [A01GEGWKVB]
sources:
  - url: https://en.wikipedia.org/wiki/Control_variates
same_as:
  wikidata: Q3554721
  wikipedia: Control variates
---

## Statement

Let $Y$ and $C$ be random variables with finite variance, where $\mu = \mathbb E C$ is known and $\operatorname{Var} C > 0$.
For a real number $\beta$ let $Z_\beta = Y - \beta (C - \mu)$.
Then:

1. $\mathbb E Z_\beta = \mathbb E Y$ for every $\beta$;
2. $\operatorname{Var} Z_\beta = \operatorname{Var} Y - 2\beta \operatorname{Cov}(Y, C) + \beta^2 \operatorname{Var} C$;
3. this variance is smallest for $\beta^* = \operatorname{Cov}(Y, C) / \operatorname{Var} C$, and $\operatorname{Var} Z_{\beta^*} = (1 - \rho^2) \operatorname{Var} Y$, where $\rho$ is the [[correlation coefficient|0DNN9B6Q2F]] of $Y$ and $C$.

## Remarks

Clause 1 holds because $\mathbb E(C - \mu) = 0$, and clause 2 is the expansion of the [[variance|0477R9PYAE]] of a difference.
Clause 3 minimises the quadratic in $\beta$; substituting $\beta^*$ gives $\operatorname{Var} Y - \operatorname{Cov}(Y, C)^2 / \operatorname{Var} C = (1 - \rho^2)\operatorname{Var} Y$.
Example: to estimate $\mathbb E e^U = e - 1$ for $U$ uniform on $(0, 1)$, use $C = U$ with $\mu = \frac12$.
Here $\operatorname{Cov}(e^U, U) = 1 - \frac{e - 1}{2} \approx 0.1409$ and $\operatorname{Var} U = \frac{1}{12}$, so $\beta^* \approx 1.690$ and $\operatorname{Var} Z_{\beta^*} \approx 0.0039$, against $\operatorname{Var} e^U \approx 0.2420$.
In practice $\beta^*$ is estimated from the same samples, by least squares regression of $Y$ on $C$; this introduces a bias of order $1/n$, which is usually negligible.
If $C$ is uncorrelated with $Y$, then $\rho = 0$ and no gain is possible.

## Explanations

### L1 human

Suppose a quantity $Y$ is hard to average, but a related quantity $C$ has an exactly known average.
On each sample, see how far $C$ is from its known average, and correct $Y$ by a multiple of that error.
If $Y$ and $C$ move together, the correction removes much of the noise in $Y$.
The better $C$ tracks $Y$, the larger the gain: a correlation of $0.99$ cuts the variance by a factor of about $50$.

### L2 human

Control variates is a [[variance reduction|A01GEGWKVB]] technique that turns side knowledge, the exact mean of $C$, into accuracy.
In option pricing, the price of a similar option with a closed-form value is a classic control.
With several controls $C_1, \ldots, C_k$ the optimal coefficients solve a linear least squares problem, and the variance becomes $(1 - R^2)\operatorname{Var} Y$, with $R^2$ the squared multiple correlation.
The multilevel Monte Carlo method can be seen as a recursive use of control variates, with coarse approximations as controls for fine ones.
