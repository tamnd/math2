---
tag: PF83EHMFEG
kind: definition
name: Dbar operator
msc: [32W05]
defines: M1VKCW3RFW
uses: [DC81TCR98Y, WMXDVF36ZT, 0ZHSTAG8ZY]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_differential_form
---

## Definition

Let $U \subseteq \C^n$ be an open set, with coordinates $z_1, \dots, z_n$.
For a smooth function $f \colon U \to \C$, put
$$\bar\partial f = \sum_{k=1}^n \frac{\partial f}{\partial \bar z_k} \, d\bar z_k,$$
where $\partial / \partial \bar z_k$ is the [[Wirtinger derivative|WMXDVF36ZT]] in the variable $z_k$.
For a [[$(p, q)$-form|DC81TCR98Y]] $\omega = \sum_{I, J} \omega_{IJ} \, dz_I \wedge d\bar z_J$ on $U$, the *$\bar\partial$ operator* gives the $(p, q+1)$-form
$$\bar\partial \omega = \sum_{I, J} \bar\partial \omega_{IJ} \wedge dz_I \wedge d\bar z_J = \sum_{I, J} \sum_{k=1}^n \frac{\partial \omega_{IJ}}{\partial \bar z_k} \, d\bar z_k \wedge dz_I \wedge d\bar z_J.$$
It is extended to all complex forms by additivity over the types.

## Remarks

The operator $\partial$ is defined in the same way with $\partial / \partial z_k$ and $dz_k$; it sends $(p, q)$-forms to $(p+1, q)$-forms.
On forms on $U$, the [[exterior derivative|0ZHSTAG8ZY]] is $d = \partial + \bar\partial$, and $\bar\partial \circ \bar\partial = 0$.
It obeys the Leibniz rule $\bar\partial(\alpha \wedge \beta) = \bar\partial \alpha \wedge \beta + (-1)^{k} \alpha \wedge \bar\partial \beta$ for $\alpha$ of degree $k$.
Example: for $f(z_1, z_2) = \abs{z_1}^2 + z_2$, $\partial f / \partial \bar z_1 = z_1$ and $\partial f / \partial \bar z_2 = 0$, so $\bar\partial f = z_1 \, d\bar z_1$.
Non-example: $\bar\partial$ is not the exterior derivative, since $\bar\partial z_1 = 0$ while $d z_1 = dz_1 \ne 0$; the $(1, 0)$ part of $d$ is dropped.
A $C^1$ function $f$ satisfies $\bar\partial f = 0$ on $U$ if and only if it is holomorphic on $U$.
Because holomorphic changes of coordinates preserve types, $\bar\partial$ is well defined on complex manifolds.
