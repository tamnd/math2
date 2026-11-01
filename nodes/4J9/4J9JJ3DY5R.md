---
tag: 4J9JJ3DY5R
kind: definition
name: Hilbert symbol
msc: [11S31, "11E08"]
defines: WFG4YMBYVQ
uses: [J85FZEQG38, 0JTC045NNZ, 0DKCECSYCF, BT6T702C28]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_symbol
---

## Definition

Let $K$ be a [[local field|J85FZEQG38]] whose characteristic is not $2$.
For $a, b \in K^\times$, the *Hilbert symbol* $(a, b)_K$ is
$$(a, b)_K = \begin{cases} 1 & \text{if } z^2 = a x^2 + b y^2 \text{ has a solution } (x, y, z) \in K^3 \setminus \set{(0, 0, 0)}, \\ -1 & \text{otherwise.} \end{cases}$$

## Remarks

The value only depends on the classes of $a$ and $b$ modulo squares.
Equivalently, $(a, b)_K = 1$ exactly when $a$ is a norm from the field $K(\sqrt{b})$.
The symbol is symmetric and bimultiplicative, and $(a, 1 - a)_K = 1$ for $a \neq 1$.
Example: $(-1, -1)_\R = -1$, because $z^2 = -x^2 - y^2$ forces $x = y = z = 0$ over $\R$.
Example: $(2, 7)_\R = 1$, because $(x, y, z) = (1, 1, 3)$ solves $z^2 = 2x^2 + 7y^2$.
Non-example: the solution $(0, 0, 0)$ must be excluded; it solves every such equation, so allowing it would make every symbol equal to $1$.
For $K = \Q_p$ with $p$ odd, write $a = p^\alpha u$ and $b = p^\beta v$ with units $u, v \in \Z_p^\times$.
Then $(a, b)_p = (-1)^{\alpha \beta (p - 1)/2} \left(\frac{u}{p}\right)^\beta \left(\frac{v}{p}\right)^\alpha$, with [[Legendre symbols|0JTC045NNZ]] of the residues of $u$ and $v$.
