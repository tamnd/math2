---
tag: W6GG3FJMNQ
kind: example
name: d'Alembert's equation
msc: [34A09, 34A05]
instance_of: [08WWTN738R]
uses: [0T6D4PE51C, 0CZA0NCFWP, 0SKYFQAFYD]
sources:
  - url: https://en.wikipedia.org/wiki/D%27Alembert%27s_equation
same_as:
  wikidata: Q1272852
  wikipedia: D'Alembert's equation
---

## Example

Let $f$ and $g$ be continuously differentiable functions on an open interval $J$.
*d'Alembert's equation*, also called Lagrange's equation, is the implicit first-order equation
$$y = x\, f(y') + g(y'),$$
for an unknown $y$ of $x$ with $y' \in J$.
When $f(p) = p$ for all $p$, it is [[Clairaut's equation|0T6D4PE51C]].
Method: write $p = y'$ and differentiate, which gives $p = f(p) + \left(x f'(p) + g'(p)\right) \frac{dp}{dx}$.
Where $p \ne f(p)$, view $x$ as a function of $p$; then $(p - f(p))\, \frac{dx}{dp} = f'(p)\, x + g'(p)$ is a linear equation for $x(p)$.
Each root $p_0$ of $p = f(p)$ gives the line $y = p_0 x + g(p_0)$, which may be a [[singular solution|0CZA0NCFWP]].

Instance: $y = x\, (y')^2$, so $f(p) = p^2$ and $g = 0$.
For $p \ne 0, 1$, the linear equation is $(p - p^2)\, dx/dp = 2 p x$, so $dx/dp = 2x/(1 - p)$ and $x = C/(1 - p)^2$.
This leads to the solutions $y = (\sqrt{x} - k)^2$ for $x > 0$ and a constant $k$.
Check: $y' = 1 - k/\sqrt{x}$, so $x (y')^2 = (\sqrt{x} - k)^2 = y$.
The roots $p = 0$ and $p = 1$ of $p = p^2$ give the lines $y = 0$ and $y = x$, which also solve the equation: $x \cdot 0^2 = 0$ and $x \cdot 1^2 = x$.

## Explanations

### L1 human

d'Alembert's equation gives $y$ as a combination of $x$ and the slope $y'$, rather than giving the slope directly.
The trick is to treat the slope as the new variable: then $x$ satisfies a linear equation, which can be solved.
Besides the [[general solution|0SKYFQAFYD]] there can be special straight-line solutions, as in Clairaut's equation.
