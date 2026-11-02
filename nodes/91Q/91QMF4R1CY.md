---
tag: 91QMF4R1CY
kind: definition
name: Shift operator
msc: [39A70, 47B39]
defines: MBK6AE6734
uses: [0XHDTE5YMZ, 0QE8STGJH2]
sources:
  - url: https://en.wikipedia.org/wiki/Shift_operator
---

## Definition

Let $G$ be an additive abelian group, let $Y$ be a set, and let $h \in G$.
The *shift operator* $E_h$ with step $h$ sends a [[function|0XHDTE5YMZ]] $f \colon G \to Y$ to the function
$$E_h f \colon G \to Y, \qquad E_h f(x) = f(x + h).$$
For a [[sequence|0QE8STGJH2]] $u = (u_n)_{n \ge 0}$ in $Y$, the (left) shift $E$ is defined by $(E u)_n = u_{n+1}$ for $n \ge 0$.

## Remarks

Example: for $f(x) = \sin x$ and $h = \pi/2$, $E_h f(x) = \sin(x + \pi/2) = \cos x$.
Non-example: $f \mapsto f(2x)$ is not a shift operator; it rescales the argument instead of translating it.
The shifts compose by $E_h E_k = E_{h+k}$, and $E_0$ is the identity.
When $Y$ is an abelian group, $E_h$ is additive, and the [[forward difference operator|8E0EBA8X07]] is $\Delta_h = E_h - I$.
Other notations are $T_h$ and $\tau_h$; on sequences the left shift is also called the backward shift.
