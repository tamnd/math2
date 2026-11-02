---
tag: K24YAC8P7X
kind: definition
name: Spherical Bessel functions
msc: [33C10, 34B30]
defines: 4K2DZV0D0D
uses: [CZCMRDWDYW, GRSNDJG363]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Definition

Let $n \ge 0$ be an integer and let $x > 0$.
Let $J_\nu$ and $Y_\nu$ be the [[Bessel functions of the first kind|CZCMRDWDYW]] and of the [[second kind|GRSNDJG363]].
The *spherical Bessel functions* of order $n$ are
$$j_n(x) = \sqrt{\frac{\pi}{2x}}\, J_{n + 1/2}(x), \qquad y_n(x) = \sqrt{\frac{\pi}{2x}}\, Y_{n + 1/2}(x).$$

## Remarks

They solve $x^2 y'' + 2x y' + \left( x^2 - n(n+1) \right) y = 0$, which is the radial equation of $\Delta u + u = 0$ in spherical coordinates.
Example: $J_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sin x$, so $j_0(x) = \frac{\sin x}{x}$; one checks $x^2 j_0'' + 2x j_0' + x^2 j_0 = x (x j_0)'' + x^2 j_0 = x (\sin x)'' + x \sin x = 0$.
Likewise $y_0(x) = -\frac{\cos x}{x}$.
In general $j_n(x) = (-x)^n \left( \frac{1}{x} \frac{d}{dx} \right)^n \frac{\sin x}{x}$.
The spherical Hankel functions are $h^{(1)}_n = j_n + i y_n$ and $h^{(2)}_n = j_n - i y_n$; for instance $h^{(1)}_0(x) = -i \frac{e^{ix}}{x}$.
A non-example: $J_n(x)$ for an integer $n$ is a cylindrical, not a spherical, Bessel function; it is not elementary.
