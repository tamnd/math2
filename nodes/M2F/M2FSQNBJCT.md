---
tag: M2FSQNBJCT
kind: definition
name: Heaviside cover-up method
msc: [26C15, 44A10]
defines: SRQ5P3077W
uses: [0WCZH4AFMT, 030VFEREKG, 00EHX6FWC0]
sources:
  - url: https://en.wikipedia.org/wiki/Heaviside_cover-up_method
---

## Definition

Let $P$ and $Q$ be complex polynomials with $\deg P < \deg Q$, and let $F = P/Q$ be the [[rational function|0WCZH4AFMT]].
Let $a$ be a [[root|00EHX6FWC0]] of $Q$ of multiplicity $m \ge 1$, and write $Q(s) = (s - a)^m R(s)$ with $R$ a polynomial and $R(a) \ne 0$.
In the [[partial fraction decomposition|030VFEREKG]] of $F$, let $c$ be the coefficient of $1/(s - a)^m$.
The *Heaviside cover-up method* computes this coefficient as
$$c = \frac{P(a)}{R(a)} = \Big[ (s - a)^m F(s) \Big]_{s = a}.$$
When $a$ is a simple root, this equals $P(a)/Q'(a)$.

## Remarks

The formula holds because $(s - a)^m F(s)$ equals $c$ plus terms that vanish at $s = a$.
Example: for $F(s) = \frac{1}{(s - 1)(s - 2)(s - 3)}$, cover-up gives the coefficients $\frac{1}{(1-2)(1-3)} = \tfrac12$, $\frac{1}{(2-1)(2-3)} = -1$ and $\frac{1}{(3-1)(3-2)} = \tfrac12$.
Its inverse Laplace transform is therefore $\tfrac12 e^{t} - e^{2t} + \tfrac12 e^{3t}$.
Non-example: for a repeated root the method gives only the top coefficient.
For $\frac{1}{s (s - 1)^2} = \frac{A}{s} + \frac{B}{s - 1} + \frac{C}{(s - 1)^2}$, cover-up gives $A = 1$ and $C = 1$.
The true value $B = -1$ does not come from covering up; one finds it by comparing coefficients or by differentiating $(s - 1)^2 F(s)$ at $s = 1$.
