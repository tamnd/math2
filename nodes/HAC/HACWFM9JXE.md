---
tag: HACWFM9JXE
kind: definition
name: Elliptic integral
msc: ["33E05"]
defines: NXMCYGCB59
uses: [0XDK9CGYKJ, 0W29TBTY12, 0F7FQS6XY6]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_integral
---

## Definition

Let $R(x, y)$ be a [[rational function|0XDK9CGYKJ]] of two variables, and let $P$ be a polynomial of degree $3$ or $4$ with no repeated roots.
An *elliptic integral* is an integral of the form
$$f(x) = \int_c^x R\big(t, \sqrt{P(t)}\big) \, dt,$$
where $c$ is a constant and $\sqrt{\cdot}$ is a [[square root|0F7FQS6XY6]].

Let $0 \le k < 1$, let $\varphi$ be real, and let $n$ be a real parameter with $n \sin^2\theta \ne 1$ for $\theta$ between $0$ and $\varphi$.
The *incomplete elliptic integrals in Legendre form* of the first, second and third kind are
$$F(\varphi, k) = \int_0^\varphi \frac{d\theta}{\sqrt{1 - k^2 \sin^2\theta}}, \qquad E(\varphi, k) = \int_0^\varphi \sqrt{1 - k^2 \sin^2\theta} \, d\theta,$$
$$\Pi(n; \varphi, k) = \int_0^\varphi \frac{d\theta}{(1 - n \sin^2\theta)\sqrt{1 - k^2 \sin^2\theta}}.$$
The number $k$ is the *modulus*.

## Remarks

The substitution $t = \sin\theta$ turns $F(\varphi, k)$ into $\int_0^{\sin\varphi} dt / \sqrt{(1 - t^2)(1 - k^2 t^2)}$, an elliptic integral with $P(t) = (1 - t^2)(1 - k^2 t^2)$, which has the four distinct roots $\pm 1$ and $\pm 1/k$ when $0 < k < 1$.
Example: the ellipse $x = a\sin\theta$, $y = b\cos\theta$ with $0 < b < a$ has arc length element $\sqrt{a^2\cos^2\theta + b^2\sin^2\theta}\,d\theta = a\sqrt{1 - e^2\sin^2\theta}\,d\theta$, where $e^2 = 1 - b^2/a^2$; so its arc length from $\theta = 0$ to $\theta = \varphi$ is $a E(\varphi, e)$.
Non-example: $\int_0^x dt / \sqrt{1 - t^2} = \arcsin x$ is not an elliptic integral, since $P(t) = 1 - t^2$ has degree $2$.
Every elliptic integral is a sum of elementary functions and constant multiples of integrals of the three Legendre kinds.
The values at $\varphi = \pi/2$ are the complete integrals $K(k) = F(\pi/2, k)$, [[of the first kind|RM54CPPE12]], and $E(k) = E(\pi/2, k)$, [[of the second kind|VS2PSX14C8]].
