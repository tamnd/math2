---
tag: 8HA39P7ZFN
kind: definition
name: Richardson extrapolation
msc: [65B05, 40A25]
defines: WMTZG71K2Y
uses: [0RYTGBJAGN, 0F1WR9C83K]
sources:
  - url: https://en.wikipedia.org/wiki/Richardson_extrapolation
---

## Definition

Let $A^*$ be a number and let $A(h)$ be approximations of $A^*$, defined for small $h > 0$.
Assume that there are a constant $c$ and exponents $0 < k < k'$ such that
$$A(h) = A^* + c\, h^k + O(h^{k'}) \quad (h \to 0),$$
in [[big O notation|0RYTGBJAGN]].
For a fixed ratio $t > 1$, the *Richardson extrapolation* of $A$ is
$$R(h) = \frac{t^k A(h/t) - A(h)}{t^k - 1}.$$
Then $R(h) = A^* + O(h^{k'})$.

## Remarks

The last claim is a direct computation: in $t^k A(h/t) - A(h)$ the terms $t^k c (h/t)^k$ and $c h^k$ cancel, and $t^k A^* - A^* = (t^k - 1)A^*$.
Example: for a function $f$ with five continuous derivatives, the central difference $A(h) = \frac{f(x+h) - f(x-h)}{2h}$ satisfies $A(h) = f'(x) + \frac{f'''(x)}{6} h^2 + O(h^4)$.
With $k = 2$ and $t = 2$, the extrapolation $\frac{4A(h/2) - A(h)}{3}$ approximates the [[derivative|0F1WR9C83K]] $f'(x)$ with error $O(h^4)$.
Non-example: if the true error is $A(h) = A^* + h$ but one uses $k = 2$, then $R(h) = A^* + \frac{h}{3}$, which is still of first order; the exponent $k$ must be the true leading exponent.
The procedure can be repeated with the next exponent of the error expansion, which gives a triangular table of extrapolated values.

## Explanations

### L1 human

Compute with two step sizes, and use the known shape of the error to remove its main part.
