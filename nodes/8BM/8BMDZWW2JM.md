---
tag: 8BMDZWW2JM
kind: definition
name: Similarity solution for the heat equation
msc: [35C06, 35K05, "80A19"]
defines: PWSV93XK14
uses: [3DJMFT0SQM, VNB1BFDEYK, 1EG3DWPNZN, YGMTZJY1MR]
sources:
  - url: https://en.wikipedia.org/wiki/Self-similar_solution
---

## Definition

Let $\alpha > 0$, and let $I$ be either $\R$ or $(0, \infty)$.
Consider the [[heat equation|VNB1BFDEYK]] $u_t = \alpha u_{xx}$ for $u \colon I \times (0, \infty) \to \R$.
A *similarity solution* of it is a solution of the form
$$u(x, t) = t^{-a} f(\eta), \qquad \eta = \frac{x}{2 \sqrt{\alpha t}},$$
for a real number $a$ and a twice differentiable function $f$ on $I$.
These are the [[similarity solutions|3DJMFT0SQM]] with exponents $(a, 1/2)$ in the general sense.

## Remarks

Substituting the form gives $u_t = t^{-a-1}\big(-a f - \tfrac{\eta}{2} f'\big)$ and $\alpha u_{xx} = t^{-a-1} \tfrac14 f''$.
So $u$ solves the heat equation exactly when $f'' + 2 \eta f' + 4 a f = 0$.
Example with $a = 0$: the equation $f'' + 2 \eta f' = 0$ gives $f' = C e^{-\eta^2}$, hence $f = A + B \operatorname{erf}(\eta)$ with the [[error function|1EG3DWPNZN]].
The choice $A = 1$, $B = -1$ gives $u = \operatorname{erfc}\big(x / (2\sqrt{\alpha t})\big)$, the temperature of the half-space $x > 0$ initially at $0$ with surface held at $1$.
Example with $a = 1/2$: the equation is $(f' + 2 \eta f)' = 0$, solved by $f = C e^{-\eta^2}$, which gives $u = C t^{-1/2} e^{-x^2/(4 \alpha t)}$.
With $C = (4 \pi \alpha)^{-1/2}$ this is the [[heat kernel|YGMTZJY1MR]] for diffusivity $\alpha$.
Non-example: $u(x, t) = e^{-\alpha t} \sin x$ solves the heat equation on $\R$ but is not a similarity solution.
At each time its zeros are the points of $\pi \Z$, while a similarity solution has zero set $2\sqrt{\alpha t}\, Z$ for a fixed set $Z$, which changes with $t$ unless $Z \subseteq \set{0}$.
Similarity solutions arise for problems whose initial and boundary data are compatible with the scaling $x \mapsto \lambda x$, $t \mapsto \lambda^2 t$, such as constant data on a half-line or a point source.
