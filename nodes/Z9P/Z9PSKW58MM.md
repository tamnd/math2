---
tag: Z9PSKW58MM
kind: definition
name: Zinbiel algebra
msc: [17A30, 18M60]
defines: QQKRCAKD5V
uses: [60W3THKGA7, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Zinbiel_algebra
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]].
A *Zinbiel algebra* over $K$ is a [[nonassociative algebra|60W3THKGA7]] over $K$, that is, a vector space $A$ with a bilinear product $(a, b) \mapsto a \circ b$, such that
$$(a \circ b) \circ c = a \circ (b \circ c) + a \circ (c \circ b) \quad \text{for all } a, b, c \in A.$$

## Remarks

Example: let $A = x\Q[x]$ be the polynomials without constant term, with $f \circ g = \int_0^x f'(t)\, g(t)\, dt$.
For $f, g \in A$, integration by parts gives $f \circ g + g \circ f = fg$.
Then $(a \circ b) \circ c = \int_0^x (a \circ b)' c \, dt = \int_0^x a' b c \, dt$, and $a \circ (b \circ c) + a \circ (c \circ b) = \int_0^x a' (b \circ c + c \circ b)\, dt = \int_0^x a' b c \, dt$.
On monomials the product is $x^m \circ x^n = \frac{m}{m + n} x^{m + n}$.

Non-example: $A = \Q$ with the usual product.
For $a = b = c = 1$ the left side is $1$ and the right side is $2$.

In any Zinbiel algebra, $a * b = a \circ b + b \circ a$ is commutative and associative.
Some authors write the identity with the opposite product, as $a \circ (b \circ c) = (a \circ b) \circ c + (b \circ a) \circ c$.
