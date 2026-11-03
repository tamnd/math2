---
kind: concept
msc:
- 65D25
- 26A24
name: Central difference approximation of the derivative
sources:
- url: https://github.com/active-calculus/active-calculus-single-mbx/blob/e597daa657ba5ec0953157aa8c44834dceb63eb2/source/sec-1-5-units.xml#L222
  locator: source/sec-1-5-units.xml:222
tag: 98CATX7FHJ
uses:
- 0V1EJCT8G6
- 97DDM0ZBYG
- 8HSQHDNFEF
---

## Summary

Fix a point $a$ and a step $h > 0$. The central difference approximation estimates the [[derivative|0V1EJCT8G6]] $f'(a)$ by the slope of the line through the points of the graph at $a-h$ and $a+h$.

The estimate is the number $\frac{f(a+h) - f(a-h)}{2h}$. It is a [[difference quotient|97DDM0ZBYG]] that is centred at $a$. Its numerator is the [[central difference|8HSQHDNFEF]] of step $2h$, taken at $a$, and it is divided by the width $2h$.
