---
tag: HTS2CSMGDA
kind: definition
name: Fixed-point combinator
msc: [03B40, 68N18]
defines: JWQQEZ1W00
uses: [BD756KR8FM, Y9B9CVY6SJ, R6QVS6P21N]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed-point_combinator
---

## Definition

Work in the untyped [[lambda calculus|BD756KR8FM]] with [[beta conversion|Y9B9CVY6SJ]] $=_\beta$.
A *fixed-point combinator* is a closed term $Y$ such that for every term $F$,
$$Y\, F =_\beta F\, (Y\, F).$$
So $Y\, F$ is a [[fixed point|R6QVS6P21N]] of $F$ up to $\beta$-conversion.

## Remarks

Example: Curry's combinator $\mathbf{Y} = \lambda f.\, (\lambda x.\, f\, (x\, x))\, (\lambda x.\, f\, (x\, x))$.
Let $W = \lambda x.\, F\, (x\, x)$.
Then $\mathbf{Y}\, F \to_\beta W\, W \to_\beta F\, (W\, W)$.
Also $F\, (\mathbf{Y}\, F) \to_\beta F\, (W\, W)$, so $\mathbf{Y}\, F =_\beta F\, (\mathbf{Y}\, F)$.

Turing's combinator $\Theta = A\, A$ with $A = \lambda x.\, \lambda y.\, y\, (x\, x\, y)$ has the stronger property $\Theta\, F \twoheadrightarrow_\beta F\, (\Theta\, F)$.

Non-example: the identity $\mathbf{I} = \lambda x.\, x$ is closed, but $\mathbf{I}\, F =_\beta F$, which in general is not $\beta$-convertible to $F\, (\mathbf{I}\, F) =_\beta F\, F$.
For instance with $F = \lambda z.\, \lambda w.\, z$, the terms $F$ and $F\, F$ have the distinct normal forms $\lambda z.\, \lambda w.\, z$ and $\lambda w.\, \lambda z.\, \lambda w'.\, z$.

The existence of $\mathbf{Y}$ gives the fixed-point theorem of the lambda calculus: every term has a fixed point.
