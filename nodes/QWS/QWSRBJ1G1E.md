---
tag: QWSRBJ1G1E
kind: statement
role: theorem
name: Addition formulas for Jacobi elliptic functions
msc: ["33E05"]
uses: [P071B692JF]
about: [P071B692JF]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_elliptic_functions
---

## Statement

Let $0 < k < 1$, and let $\operatorname{sn}$, $\operatorname{cn}$, $\operatorname{dn}$ be the [[Jacobi elliptic functions|P071B692JF]] with modulus $k$.
For all complex $u, v$ such that both sides are defined, with
$$\Delta = 1 - k^2\operatorname{sn}^2 u \operatorname{sn}^2 v,$$
one has
$$\operatorname{sn}(u + v) = \frac{\operatorname{sn} u \operatorname{cn} v \operatorname{dn} v + \operatorname{sn} v \operatorname{cn} u \operatorname{dn} u}{\Delta},$$
$$\operatorname{cn}(u + v) = \frac{\operatorname{cn} u \operatorname{cn} v - \operatorname{sn} u \operatorname{sn} v \operatorname{dn} u \operatorname{dn} v}{\Delta},$$
$$\operatorname{dn}(u + v) = \frac{\operatorname{dn} u \operatorname{dn} v - k^2 \operatorname{sn} u \operatorname{sn} v \operatorname{cn} u \operatorname{cn} v}{\Delta}.$$

## Remarks

Proof idea: fix $c$ and set $v = c - u$; using the derivative rules $\operatorname{sn}' = \operatorname{cn}\operatorname{dn}$, $\operatorname{cn}' = -\operatorname{sn}\operatorname{dn}$, $\operatorname{dn}' = -k^2\operatorname{sn}\operatorname{cn}$ and the relations $\operatorname{sn}^2 + \operatorname{cn}^2 = 1$, $\operatorname{dn}^2 + k^2\operatorname{sn}^2 = 1$, one checks that each right side has derivative $0$ in $u$.
So each right side depends only on $u + v = c$, and putting $u = 0$ (where $\operatorname{sn} 0 = 0$, $\operatorname{cn} 0 = \operatorname{dn} 0 = 1$) shows it equals the left side.
By analytic continuation the identities hold wherever both sides are defined.
Example: for $k \to 0$ the formulas become $\sin(u + v) = \sin u\cos v + \sin v\cos u$ and the cosine addition formula, with $\operatorname{dn} = 1$ and $\Delta = 1$.
With $k = 1$, where $\operatorname{sn} = \tanh$ and $\operatorname{cn} = \operatorname{dn} = \operatorname{sech}$, the first formula becomes $\tanh(u + v) = (\tanh u + \tanh v)/(1 + \tanh u\tanh v)$, after factoring $1 - \tanh^2 u\tanh^2 v = (1 - \tanh u\tanh v)(1 + \tanh u\tanh v)$.
Example of use: with $v = K$, where $\operatorname{sn} K = 1$, $\operatorname{cn} K = 0$, $\operatorname{dn} K = k'$, one gets $\operatorname{sn}(u + K) = \operatorname{cn} u / \operatorname{dn} u$.

## Explanations

### L1 human

The sine and cosine of a sum can be written with the sines and cosines of the parts.
The Jacobi elliptic functions have the same property, but the formulas carry the denominator $1 - k^2\operatorname{sn}^2 u\operatorname{sn}^2 v$.
When the modulus $k$ is $0$, the denominator is $1$ and the familiar trigonometric formulas come back.

### L2 human

The addition formulas reflect the group law on the elliptic curve $y^2 = (1 - x^2)(1 - k^2x^2)$, parametrised by $x = \operatorname{sn} u$, $y = \operatorname{cn} u\operatorname{dn} u$.
They give the shifts by quarter and half periods, such as $\operatorname{sn}(u + 2K) = -\operatorname{sn} u$, from the special values at $K$ and $2K$.
They are also the algebraic addition theorem behind Euler's addition theorem for the integral $\int dt/\sqrt{(1 - t^2)(1 - k^2t^2)}$.
