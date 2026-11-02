---
tag: A915CSRFEF
kind: definition
name: Numerical integration
msc: [65D30, 65D32, 41A55]
defines: 7HYF6YG0RS
uses: [021WEM680W, RSAK8YHMXF]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_integration
---

## Definition

Let $a < b$ be real numbers and let $F$ be a class of [[integrable functions|RSAK8YHMXF]] $f \colon [a, b] \to \R$, with the [[definite integral|021WEM680W]] $I(f) = \int_a^b f(x)\, dx$.
A *numerical integration method* on $F$ is a rule that assigns to each $f \in F$ a number $Q(f)$.
The number $Q(f)$ is computed from finitely many values $f(x_1), \dots, f(x_n)$ at points $x_i \in [a, b]$, and possibly from finitely many values of derivatives of $f$.
Its *error* at $f$ is $E(f) = I(f) - Q(f)$.
*Numerical integration* is the design and analysis of such methods, so that $\abs{E(f)}$ is small for the functions of interest.

## Remarks

The same definition applies to integrals over regions of $\R^d$ or with a weight function; in several dimensions one often speaks of cubature.
Example: the midpoint method $Q(f) = (b - a) f\big(\tfrac{a + b}{2}\big)$ on continuous functions uses one value; for $f(x) = x^2$ on $[0, 1]$ it gives $1/4$, with error $1/3 - 1/4 = 1/12$.
Non-example: $Q(f) = F(b) - F(a)$ with an antiderivative $F$ is exact, but it is not a numerical integration method in this sense, because it needs an antiderivative, not finitely many values of $f$.
The points $x_i$ may also be chosen adaptively, depending on earlier values, as in adaptive quadrature, or at random, as in Monte Carlo integration.
