---
tag: 6GWRCGBGWC
kind: definition
name: Dolbeault cohomology
msc: [32L10, 32C35, 58A10]
defines: Y3900T2EY5
uses: [JSGWAN2RJV, DC81TCR98Y, M1VKCW3RFW]
sources:
  - url: https://en.wikipedia.org/wiki/Dolbeault_cohomology
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] and let $p, q \ge 0$ be integers.
Let $\mathcal{A}^{p,q}(X)$ be the complex vector space of smooth [[(p,q)-forms|DC81TCR98Y]] on $X$, with $\mathcal{A}^{p,-1}(X) = 0$.
Let $\bar\partial \colon \mathcal{A}^{p,q}(X) \to \mathcal{A}^{p,q+1}(X)$ be the [[dbar operator|M1VKCW3RFW]], which satisfies $\bar\partial \circ \bar\partial = 0$.
The *Dolbeault cohomology group* of bidegree $(p,q)$ is the quotient vector space
$$H^{p,q}_{\bar\partial}(X) = \frac{\ker\big(\bar\partial \colon \mathcal{A}^{p,q}(X) \to \mathcal{A}^{p,q+1}(X)\big)}{\im\big(\bar\partial \colon \mathcal{A}^{p,q-1}(X) \to \mathcal{A}^{p,q}(X)\big)}.$$

## Remarks

The class of a $\bar\partial$-closed form $\alpha$ is written $[\alpha]$; two closed forms define the same class when they differ by $\bar\partial \beta$.
Example: on $X = \C$, every smooth $(0,1)$-form $g\, d\bar z$ with compact support is $\bar\partial$ of the function $u(z) = \frac{1}{2\pi i} \int_\C \frac{g(w)}{w - z}\, dw \wedge d\bar w$, so it gives the zero class in $H^{0,1}_{\bar\partial}(\C)$; in fact $H^{0,1}_{\bar\partial}(\C) = 0$.
Example: $H^{p,0}_{\bar\partial}(X)$ is the space of holomorphic $p$-forms on $X$, since there are no $(p,-1)$-forms to divide by.
A nonzero class: let $X = \C/\Lambda$ with $\Lambda = \Z + i\Z$.
The form $d\bar z$ is $\bar\partial$-closed on $X$, but it is not $\bar\partial u$ for a smooth function $u$ on $X$.
Indeed, if it were, the lift $\tilde u$ of $u$ to $\C$ would satisfy $\partial \tilde u / \partial \bar z = 1$, so $h = \tilde u - \bar z$ would be entire.
Then $h(z + 1) = h(z) - 1$ and $h(z + i) = h(z) + i$, so $h'$ is a doubly periodic entire function; it is bounded, hence a constant $a$ by Liouville's theorem.
The two relations give $a = -1$ and $a = 1$, a contradiction.
So $[d\bar z] \ne 0$ in $H^{0,1}_{\bar\partial}(X)$.
The groups are also written $H^{p,q}(X)$ when no confusion with other cohomologies arises.
