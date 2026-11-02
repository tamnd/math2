---
tag: 91PCJMS5VC
kind: definition
name: F-distribution
msc: ["62E15", "60E05"]
defines: PBT8VRJADK
uses: [0RFMMBHFTV, 0E9502NT92, 04YG690N5V, 0NQ5798SB1]
sources:
  - url: https://en.wikipedia.org/wiki/F-distribution
---

## Definition

Let $d_1$ and $d_2$ be positive integers.
Let $U_1$ and $U_2$ be [[independent|0E9502NT92]] random variables with [[chi-squared distributions|0RFMMBHFTV]] with $d_1$ and $d_2$ degrees of freedom.
The distribution of
$$X = \frac{U_1 / d_1}{U_2 / d_2}$$
is the *F-distribution* with $d_1$ and $d_2$ degrees of freedom, written $F(d_1, d_2)$.

## Remarks

It has the [[probability density function|04YG690N5V]]
$$f(x) = \frac{1}{B(d_1/2, d_2/2)} \left(\frac{d_1}{d_2}\right)^{d_1/2} x^{d_1/2 - 1} \left(1 + \frac{d_1}{d_2} x\right)^{-(d_1 + d_2)/2}, \quad x > 0,$$
where $B$ is the beta function.
The same formula with real $d_1, d_2 > 0$ defines $F(d_1, d_2)$ for non-integer parameters.
Its mean is $d_2/(d_2 - 2)$ when $d_2 > 2$.
If $X \sim F(d_1, d_2)$, then $1/X \sim F(d_2, d_1)$.

Example: let $T$ have the [[Student t-distribution|0NQ5798SB1]] with $\nu$ degrees of freedom, so $T = Z/\sqrt{V/\nu}$ with $Z$ standard normal and $V$ chi-squared with $\nu$ degrees of freedom, independent.
Then $T^2 = (Z^2/1)/(V/\nu)$, and $Z^2$ is chi-squared with $1$ degree of freedom, so $T^2 \sim F(1, \nu)$.

Non-example: the independence clause matters.
If $d_1 = d_2$ and $U_2 = U_1$, then $X = 1$ always, which is not an F-distribution.
