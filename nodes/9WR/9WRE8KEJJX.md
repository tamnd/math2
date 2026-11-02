---
tag: 9WRE8KEJJX
kind: definition
name: Bromwich integral
msc: [44A10, "30E20"]
defines: 5KNAXNHRY6
uses: [0DG0Z72CQD, 00FWNP9TXY, 05XT5AVJBK]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_Laplace_transform
---

## Definition

Let $a$ be a real number, and let $F$ be a [[holomorphic function|0DG0Z72CQD]] on the half-plane $\{s \in \C : \operatorname{Re} s > a\}$.
Let $\gamma > a$ be real and let $t$ be real.
The *Bromwich integral* of $F$ along the line $\operatorname{Re} s = \gamma$, at time $t$, is
$$\frac{1}{2 \pi i} \int_{\gamma - i \infty}^{\gamma + i \infty} e^{s t} F(s) \, ds = \frac{1}{2 \pi i} \lim_{T \to \infty} \int_{\gamma - i T}^{\gamma + i T} e^{s t} F(s) \, ds.$$
Each integral on the right is the [[contour integral|00FWNP9TXY]] along the vertical segment from $\gamma - i T$ to $\gamma + i T$.
The Bromwich integral exists at $t$ when this limit exists.

## Remarks

Example: let $F(s) = 1/s$ on $\operatorname{Re} s > 0$, and $\gamma > 0$.
For $t > 0$ one closes the segment by a large arc to the left, whose contribution tends to $0$.
The residue of $e^{s t}/s$ at $0$ is $1$, so the integral is $1$.
For $t < 0$ one closes to the right, where there are no poles, and gets $0$; for $t = 0$ the symmetric limit is $\frac{1}{2 \pi i} \lim_{T \to \infty} \left( \log(\gamma + i T) - \log(\gamma - i T) \right) = \tfrac{1}{2}$.
Non-example: for $F(s) = 1$ and $t \ne 0$, the integral over the segment equals $e^{\gamma t} \sin(T t) / (\pi t)$, which has no limit as $T \to \infty$; so the Bromwich integral does not exist.
The limit is a symmetric one; it can exist even when $e^{s t} F(s)$ is not absolutely integrable on the line.
The integral is also called the Fourier–Mellin integral.
When $F$ is the [[Laplace transform|05XT5AVJBK]] of a suitable function $f$, the integral equals $f(t)$ at each $t > 0$ where $f$ is continuous; this is Mellin's inverse formula.
