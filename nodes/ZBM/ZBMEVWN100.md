---
tag: ZBMEVWN100
kind: problem
name: Cauchy's functional equation
msc: [39B22, 39B52]
uses: [0X3WGX95FE, 0A7KV2WB7A, 0KCQ9Y3QKA, 0HTGB13FE2]
about: [0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation
history:
  posed_by: "Augustin-Louis Cauchy"
  first_stated: "1821"
---

## Problem

Find all [[functions|0EPAT51DXQ]] $f \colon \R \to \R$ such that
$$f(x + y) = f(x) + f(y) \quad \text{for all } x, y \in \R.$$

## Remarks

The problem is solved.
Every solution satisfies $f(0) = 0$, $f(-x) = -f(x)$ and $f(qx) = q f(x)$ for every rational $q$, by induction on sums and then division.
So $f(q) = cq$ for all rational $q$, where $c = f(1)$.
If $f$ is also [[continuous|0X3WGX95FE]], then by density of $\Q$ in $\R$ the solution is $f(x) = cx$ for all real $x$.
The same conclusion holds under each of these weaker conditions on a solution $f$:

1. $f$ is continuous at one point;
2. $f$ is [[monotone|0A7KV2WB7A]] on some interval;
3. $f$ is bounded above on some interval;
4. $f$ is measurable for Lebesgue measure.

Without such a condition there are other solutions.
Take a [[basis|0KCQ9Y3QKA]] of $\R$ as a vector space over $\Q$, which exists by the [[axiom of choice|0HTGB13FE2]].
Every $\Q$-linear map $\R \to \R$ solves the equation, and choosing its values on the basis freely gives solutions that are not of the form $cx$.
The graph of such a non-linear solution is dense in the plane $\R^2$.

## Explanations

### L1 human

The equation asks for functions that turn sums into sums.
The lines through the origin, $f(x) = cx$, are the obvious answers, and they are the only reasonable ones.
Strange solutions exist only when one allows wild functions, which need the axiom of choice to construct and cannot be drawn.
