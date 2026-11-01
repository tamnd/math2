---
tag: WMBJSNG57F
kind: statement
role: theorem
name: Baker's theorem
msc: [11J86]
uses: [0MNF0BYFQC, 02QGGD5G87, 0CRMGPAH83, 0VTQXTCR2G]
about: [0MNF0BYFQC, 02QGGD5G87]
sources:
  - url: https://en.wikipedia.org/wiki/Baker%27s_theorem
same_as:
  wikidata: Q3527009
  wikipedia: Baker's theorem
---

## Statement

Let $\overline{\Q}$ be the field of complex [[algebraic numbers|0MNF0BYFQC]].
Let $\alpha_1, \dots, \alpha_n$ be nonzero algebraic numbers, and let $\lambda_i$ be a value of the [[complex logarithm|02QGGD5G87]] of $\alpha_i$ for each $i$.
Suppose that $\lambda_1, \dots, \lambda_n$ are [[linearly independent|0CRMGPAH83]] over $\Q$.
Then $1, \lambda_1, \dots, \lambda_n$ are linearly independent over $\overline{\Q}$.

## Remarks

The proof extends the method of Gelfond.
It builds an auxiliary function in several variables that vanishes to high order at many points, then uses an extrapolation step and an estimate to reach a contradiction.
The method also gives an effective lower bound.
Let $\Lambda = \beta_0 + \beta_1 \lambda_1 + \dots + \beta_n \lambda_n$ with algebraic $\beta_i$, and suppose $\Lambda \ne 0$.
Then $\abs{\Lambda}$ is bounded below by an explicit function of the degrees and heights of the $\alpha_i$ and $\beta_i$.
The [[Gelfond–Schneider theorem|RN58Z2NWAC]] is a special case.
Another consequence: $e^{\beta_0} \alpha_1^{\beta_1} \cdots \alpha_n^{\beta_n}$ is [[transcendental|0VTQXTCR2G]] for nonzero algebraic $\alpha_i$ and $\beta_i$.
For example, $\pi + \log 2$ is transcendental: indeed $\pi = -i \log(-1)$, and $\log(-1) = i\pi$ and $\log 2$ are linearly independent over $\Q$.
The hypothesis of independence over $\Q$ is necessary: $\log 4 - 2 \log 2 = 0$ is a relation with algebraic coefficients.

## Explanations

### L1 human

Logarithms of algebraic numbers behave as independently as they possibly can.
If no relation with rational coefficients links them, then no relation with algebraic coefficients does either.
The quantitative form says that such a combination, when it is not zero, cannot be extremely close to zero.

### L2 human

The effective lower bounds for linear forms in logarithms are the key input for many effective results in Diophantine equations.
They give explicit bounds for the solutions of [[Thue equations|3Q6CFPQZDF]] and of $S$-unit equations.
They were also used in the solution of the [[class number problem|KTGAS9DGRX]] for imaginary quadratic fields of class number one.
The theorem is a step toward [[Schanuel's conjecture|65PV4VFP9Y]], which would give algebraic independence instead of linear independence.
