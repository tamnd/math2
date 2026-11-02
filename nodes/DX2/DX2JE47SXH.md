---
tag: DX2JE47SXH
kind: definition
name: Surface of general type
msc: [14J29]
defines: SV4CK2XP8M
uses: [KFTECAATKG, ZW00Q0SAGR, W05VYY4HBR]
sources:
  - url: https://en.wikipedia.org/wiki/Surface_of_general_type
---

## Definition

Let $X$ be a smooth projective [[algebraic surface|KFTECAATKG]] over an algebraically closed field.
$X$ is a *surface of general type* if its [[Kodaira dimension|ZW00Q0SAGR]] is $2$.

## Remarks

Equivalently, with $K_X$ the [[canonical divisor|W05VYY4HBR]], there is a constant $c > 0$ with $h^0(X, nK_X) \ge c n^2$ for all large divisible $n$; that is, $K_X$ is big.
Being of general type is a birational property.
A minimal surface of general type satisfies $K_X^2 \ge 1$ and $\chi(\mathcal{O}_X) \ge 1$.
Example: a smooth surface $X \subset \mathbb{P}^3$ of degree $d \ge 5$ has $K_X = (d - 4) H$ by adjunction, with $H$ a plane section.
Since $d - 4 \ge 1$, $K_X$ is ample and $h^0(nK_X)$ grows like $n^2$, so $X$ is of general type.
Non-example: a smooth quartic surface in $\mathbb{P}^3$ has $K_X = 0$, so $h^0(nK_X) = 1$ for all $n \ge 1$ and its Kodaira dimension is $0$.
Example: the product $C_1 \times C_2$ of two curves of genus at least $2$ is of general type.
