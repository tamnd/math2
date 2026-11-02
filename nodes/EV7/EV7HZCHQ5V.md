---
tag: EV7HZCHQ5V
kind: definition
name: Mixed model
msc: [62J05]
defines: JNTTAHTPDD
uses: [A06SGFCSCE, 0XN3K7RSZY, 0V7G6WMFK0, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Mixed_model
---

## Definition

A *linear mixed model* is a statistical model for a random vector $y \in \R^n$ of the form
$$y = X\beta + Z u + \varepsilon,$$
where:

1. $X$ is a known real $n \times p$ matrix and $\beta \in \R^p$ is an unknown vector of *fixed effects*;
2. $Z$ is a known real $n \times q$ matrix and $u$ is a random vector of *random effects* with $u \sim N_q(0, G)$;
3. $\varepsilon \sim N_n(0, R)$ is a random error vector, independent of $u$;
4. the [[covariance matrices|0V7G6WMFK0]] $G$ and $R$ are [[positive definite|0KX66CZMBB]] and depend on unknown variance parameters.

Here $N_k(m, S)$ is the [[multivariate normal distribution|0XN3K7RSZY]].

## Remarks

The model implies $y \sim N_n(X\beta, \, Z G Z^T + R)$.
Without the term $Z u$ it is a [[general linear model|A06SGFCSCE]] with one response.

Example: the random intercept model.
For groups $i = 1, \dots, a$ and members $j = 1, \dots, m$, let $y_{ij} = \beta_0 + b_i + \varepsilon_{ij}$ with independent $b_i \sim N(0, \tau^2)$ and $\varepsilon_{ij} \sim N(0, \sigma^2)$.
This fits the definition with $p = 1$, $X$ the column of ones, $q = a$, $Z$ the matrix of group indicators, $G = \tau^2 I_a$ and $R = \sigma^2 I_{am}$.
Two members of the same group have covariance $\tau^2$ and correlation $\tau^2 / (\tau^2 + \sigma^2)$, the intraclass correlation.

Non-example: if the group shifts $b_i$ are treated as unknown constants rather than random variables, clause 2 fails.
The model is then a fixed effects model, a general linear model with the group indicators among the columns of $X$.

Given the variance parameters, $\beta$ is estimated by generalized least squares and $u$ is predicted by its best linear unbiased predictor.
The variance parameters are usually estimated by restricted maximum likelihood.
