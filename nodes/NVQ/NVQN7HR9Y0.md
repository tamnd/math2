---
tag: NVQN7HR9Y0
kind: definition
name: Korteweg–De Vries equation
msc: [35Q53, 35Q51]
defines: KTT75QC72Z
uses: [GC5BDZ6QBC, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Korteweg–De_Vries_equation
---

## Definition

The *Korteweg–De Vries equation* is the [[partial differential equation|GC5BDZ6QBC]]
$$u_t + u_{xxx} + 6 u u_x = 0$$
for an unknown real function $u(x, t)$ of $x \in \R$ and $t \in \R$.
Here subscripts denote [[partial derivatives|09EGC6F8PT]], for example $u_{xxx} = \partial_x^3 u$.

## Remarks

Example: for $c > 0$, the function $u(x,t) = f(x - ct)$ with $f(\xi) = \tfrac{c}{2} \mathrm{sech}^2\!\big(\tfrac{\sqrt{c}}{2}\xi\big)$ is a solution.
Substituting $u = f(x - ct)$ gives $-c f' + f''' + 6 f f' = 0$, and after one integration $f'' = c f - 3 f^2$.
With $b = \sqrt{c}/2$ and $s = \mathrm{sech}(b\xi)$, one computes $f'' = \tfrac{c}{2} b^2 (4 s^2 - 6 s^4) = \tfrac{c^2}{2} s^2 - \tfrac{3c^2}{4} s^4$, which equals $c f - 3 f^2$.

Non-example: $u(x,t) = x$ is not a solution, because $u_t + u_{xxx} + 6 u u_x = 6x \ne 0$.

Other normalisations are common, such as $u_t + u_{xxx} - 6 u u_x = 0$, obtained by replacing $u$ with $-u$.
Any equation $u_t + \alpha u_{xxx} + \beta u u_x = 0$ with $\alpha, \beta \ne 0$ reduces to this form by scaling $x$, $t$ and $u$.
