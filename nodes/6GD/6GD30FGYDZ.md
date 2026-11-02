---
tag: 6GD30FGYDZ
kind: statement
role: theorem
name: Cantor normal form
msc: ["03E10", "03F15"]
uses: [0RDJK7EQYY, KAEDCQ8RM6]
about: [KAEDCQ8RM6]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_arithmetic
    locator: Cantor normal form
---

## Statement

Let $\alpha > 0$ be an [[ordinal number|0RDJK7EQYY]], with [[ordinal arithmetic|KAEDCQ8RM6]].
Then there are an integer $k \ge 1$, ordinals $\beta_1 > \beta_2 > \cdots > \beta_k$ and positive integers $c_1, \ldots, c_k$ such that
$$\alpha = \omega^{\beta_1} \cdot c_1 + \omega^{\beta_2} \cdot c_2 + \cdots + \omega^{\beta_k} \cdot c_k.$$
The integer $k$, the ordinals $\beta_i$ and the integers $c_i$ are unique.

## Remarks

The proof is by induction on $\alpha$.
Let $\beta_1$ be the largest ordinal with $\omega^{\beta_1} \le \alpha$.
Division with remainder gives $\alpha = \omega^{\beta_1} \cdot c_1 + \rho$ with $0 < c_1 < \omega$ and $\rho < \omega^{\beta_1}$, and the induction hypothesis applies to $\rho$.
Example: $\omega^2 + \omega \cdot 3 + 5$ is already in normal form, with exponents $2 > 1 > 0$.
The normal form has $\beta_1 \le \alpha$, and equality can occur: for $\varepsilon_0$, the least ordinal with $\omega^{\varepsilon_0} = \varepsilon_0$, the normal form is $\omega^{\varepsilon_0}$.
For ordinals below [[epsilon nought|KT50SMH3EC]], the exponents are smaller than the ordinal, and repeating the normal form on them gives a finite notation.
The same holds with any base $b \ge 2$ in place of $\omega$, with coefficients $0 < c_i < b$.

## Explanations

### L1 human

Every ordinal can be written as a polynomial in $\omega$, with decreasing exponents and positive whole coefficients.
This is like writing a whole number in base ten, but with base $\omega$.
For instance, $\omega^2 \cdot 2 + 7$ means two copies of $\omega^2$ followed by seven more points.
The expression is unique, so it can be used to name and compare ordinals.

### L2 human

The Cantor normal form makes ordinal arithmetic computable on notations.
Two ordinals in normal form are compared by their leading terms, as polynomials are compared by degree.
Iterating the form on exponents gives the standard notation system for ordinals below $\varepsilon_0$, which appears in Gentzen's consistency proof for Peano arithmetic and in [[Goodstein's theorem|XQMNJF241J]].
Beyond $\varepsilon_0$ one needs stronger notations, such as those of the [[Veblen function|JQFAE9S2F4]].
