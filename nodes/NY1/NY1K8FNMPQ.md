---
tag: NY1K8FNMPQ
kind: definition
name: Dolbeault operator
msc: [32W05, 58J10, 32Q99]
defines: M2F4N31JQ2
uses: [JSGWAN2RJV, 0E3G0GRPZ6, 0ZHSTAG8ZY, WMXDVF36ZT, 0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_differential_form
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] of complex dimension $n$.
For integers $p, q \ge 0$, let $\Omega^{p,q}(X)$ be the space of smooth complex [[differential forms|0E3G0GRPZ6]] of type $(p, q)$.
In each holomorphic chart $(z_1, \ldots, z_n)$ they are the sums $\sum_{\abs{I} = p, \abs{J} = q} f_{IJ} \, dz_I \wedge d\bar z_J$ with smooth functions $f_{IJ}$.
The [[exterior derivative|0ZHSTAG8ZY]] maps $\Omega^{p,q}(X)$ into $\Omega^{p+1,q}(X) \oplus \Omega^{p,q+1}(X)$.
The *Dolbeault operator* $\bar\partial \colon \Omega^{p,q}(X) \to \Omega^{p,q+1}(X)$ is $d$ followed by the projection onto $\Omega^{p,q+1}(X)$.

## Remarks

In a chart, with the [[Wirtinger derivatives|WMXDVF36ZT]] $\partial / \partial \bar z_k = \frac{1}{2}(\partial / \partial x_k + i \, \partial / \partial y_k)$ for $z_k = x_k + i y_k$,
$$\bar\partial \Bigl(\sum_{I, J} f_{IJ} \, dz_I \wedge d\bar z_J\Bigr) = \sum_{I, J} \sum_{k=1}^n \frac{\partial f_{IJ}}{\partial \bar z_k} \, d\bar z_k \wedge dz_I \wedge d\bar z_J.$$
The other component of $d$ is written $\partial$, so $d = \partial + \bar\partial$, and $d^2 = 0$ gives $\bar\partial^2 = 0$, $\partial^2 = 0$ and $\partial \bar\partial + \bar\partial \partial = 0$.
The splitting of $d$ into two components uses that the complex structure comes from holomorphic charts.
The cohomology of $\bar\partial$ on $\Omega^{p, \bullet}(X)$ is the Dolbeault cohomology $H^{p,q}_{\bar\partial}(X)$, and the same construction works for forms with values in a holomorphic vector bundle.

Example: on $X = \C$ with coordinate $z$, let $f(z) = z^2$.
Then $\partial f / \partial \bar z = 0$, so $\bar\partial f = 0$, as for every [[holomorphic function|0NAHXR1FRH]].

Non-example: the function $g(z) = \bar z$ on $\C$ is not holomorphic, and indeed $\bar\partial g = \frac{\partial \bar z}{\partial \bar z} \, d\bar z = d\bar z \ne 0$.

## Explanations

### L1 human

The Dolbeault operator takes the derivative of a form in the antiholomorphic directions only, and holomorphic functions are exactly the functions it kills.
