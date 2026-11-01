---
tag: ZWT5HGRFXX
kind: statement
role: theorem
name: Newton–Puiseux theorem
msc: [13F25, 14H20, 12J25]
uses: [SENTYNSKSF, YZWYF7DXTW, 02SJG1HC32, 0MCXX29HWY, 1ZB13N78XW]
about: [SENTYNSKSF]
sources:
  - url: https://en.wikipedia.org/wiki/Puiseux_series
---

## Statement

Let $k$ be an [[algebraically closed field|02SJG1HC32]] of [[characteristic|1ZB13N78XW]] $0$.
Let $P$ be the field of [[Puiseux series|SENTYNSKSF]] in $X$ over $k$.
Then $P$ is algebraically closed, and it is an [[algebraic closure|0MCXX29HWY]] of the [[field of formal Laurent series|YZWYF7DXTW]] $k((X))$.

In particular, every polynomial in $Y$ of degree $n \ge 1$ with coefficients in $k((X))$ has $n$ roots in $P$, counted with multiplicity.

## Remarks

Proof idea (Newton's method): let $F(Y)$ be a polynomial with coefficients in $P$.
A slope of the [[Newton polygon|H7QNCE2QZJ]] of $F$ for the $X$-adic valuation gives a possible leading exponent $\gamma$ of a root.
A root $c \ne 0$ in $k$ of an associated polynomial gives the leading term $c X^\gamma$.
One then substitutes $Y = X^\gamma(c + Y_1)$ and repeats.
In characteristic $0$ one shows that the denominators of the exponents stop growing, so the process produces a Puiseux series.
A second proof shows that every finite extension of $k((X))$ of degree $n$ is $k((X^{1/n}))$.
Example: the roots of $Y^2 - X^3$ are $\pm X^{3/2}$, and the roots of $Y^2 - X^2(1 + X)$ are $\pm X(1 + X)^{1/2}$, with $(1 + X)^{1/2}$ given by the binomial series.
The characteristic $0$ hypothesis is necessary: over an algebraic closure of $\F_p$, the polynomial $Y^p - Y - X^{-1}$ has no root in the field of Puiseux series.

## Explanations

### L1 human

Solving a polynomial equation in $Y$ whose coefficients are power series in $X$ usually needs fractional powers of $X$.
The theorem says that fractional powers with a common denominator are always enough, when the coefficients come from an algebraically closed field such as $\C$.
For example $Y^2 = X^3$ is solved by $Y = X^{3/2}$.

### L2 human

Geometrically, the theorem parametrizes each branch of a plane algebraic curve $F(X, Y) = 0$ through a point by $X = t^m$, $Y = $ a power series in $t$.
The exponents of the Puiseux expansion are the start of the classification of plane curve singularities.
Over $\C$ the Puiseux series that arise from polynomials converge near $0$, and they describe the branches analytically.
The Newton polygon is the computational tool, and [[Henselian fields|3ACEE4N6NE]] give the general frame for lifting approximate roots.
