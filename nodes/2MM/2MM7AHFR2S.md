---
tag: 2MM7AHFR2S
kind: definition
name: Backward difference operator
msc: [39A70, 39A12]
defines: MK5JGVDPS9
uses: [CYW8E2HTWN, 0XHDTE5YMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Definition

Let $G$ and $H$ be additive abelian groups, and let $h \in G$.
The *backward difference operator* with step $h$ sends a function $f \colon G \to H$ to the function $\nabla_h f \colon G \to H$ given by
$$\nabla_h f(x) = f(x) - f(x - h) \qquad (x \in G).$$
When $h = 1$, one writes $\nabla$ for $\nabla_1$.
For a sequence $u \colon \Z \to H$, this gives $(\nabla u)_n = u_n - u_{n-1}$.

## Remarks

It is a [[finite difference|7JSQZ126BP]] in the backward direction.
Example: for $f(x) = x^2$ on $\R$, $\nabla_h f(x) = x^2 - (x - h)^2 = 2hx - h^2$.
Non-example: $f(x + h) - f(x)$ is in general not $\nabla_h f(x)$; for $f(x) = x^2$ it equals $2hx + h^2$.
The two operators are related by $\nabla_h f(x) = \Delta_h f(x - h)$, where $\Delta_h$ is the [[forward difference operator|8E0EBA8X07]].
In operator form, $\nabla_h = I - E_{-h}$, with $E_{-h} f(x) = f(x - h)$ a [[shift operator|MBK6AE6734]].
