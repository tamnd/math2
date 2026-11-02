---
tag: C6QQ3HM5S4
kind: definition
name: Tropical variety
msc: [14T10, 14T20]
defines: FT2GJEHWY5
uses: [B85T5VKR3M, 02SJG1HC32, 096Z9MP2ME, 66FQFAJNS4, SENTYNSKSF]
sources:
  - url: https://en.wikipedia.org/wiki/Tropical_geometry
---

## Definition

Let $K$ be a field with a [[valuation|B85T5VKR3M]] $\operatorname{val} \colon K^\times \to \R$, and let $K[x_1^{\pm 1}, \dots, x_n^{\pm 1}]$ be the ring of Laurent polynomials.
For $f = \sum_{u \in \Z^n} c_u x^u$ with finitely many nonzero $c_u$, the *tropicalization* of $f$ is the function $\operatorname{trop}(f) \colon \R^n \to \R$,
$$\operatorname{trop}(f)(w) = \min_{u : c_u \neq 0} \big( \operatorname{val}(c_u) + u \cdot w \big).$$
The *tropical hypersurface* of $f \neq 0$ is the set $\operatorname{Trop}(f)$ of all $w \in \R^n$ at which this minimum is attained for at least two exponents $u$.
For an [[ideal|096Z9MP2ME]] $I$ of $K[x_1^{\pm 1}, \dots, x_n^{\pm 1}]$, the *tropical variety* of $I$ is
$$\operatorname{Trop}(I) = \bigcap_{f \in I,\ f \neq 0} \operatorname{Trop}(f).$$

## Remarks

Fundamental theorem: let $K$ be [[algebraically closed|02SJG1HC32]] with $\operatorname{val}$ nontrivial.
Then $\operatorname{Trop}(I)$ is the closure in $\R^n$ of the points $(\operatorname{val}(z_1), \dots, \operatorname{val}(z_n))$, for $z$ a zero of $I$ in the [[torus|66FQFAJNS4]] $(K^\times)^n$.
A typical such field is the field of [[Puiseux series|SENTYNSKSF]] over $\C$, with the valuation given by the lowest exponent.
If moreover $I$ is prime and its zero set has dimension $d$, then $\operatorname{Trop}(I)$ is the support of a pure $d$-dimensional polyhedral complex.

Example: let $f = x + y + 1$ with all coefficients of valuation $0$.
Then $\operatorname{trop}(f)(w_1, w_2) = \min(w_1, w_2, 0)$.
The minimum is attained twice exactly on the three rays $\set{w_1 = w_2 \le 0}$, $\set{w_1 = 0 \le w_2}$ and $\set{w_2 = 0 \le w_1}$, which form the tropical line.
Non-example: the point $(1, 1)$ is not on it, since there $\min(1, 1, 0) = 0$ is attained only by the constant term.

The intersection must run over all of $I$: the intersection of $\operatorname{Trop}(f)$ over a set of generators of $I$ can be strictly larger than $\operatorname{Trop}(I)$.
A finite generating set for which equality holds is a tropical basis.
