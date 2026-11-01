---
tag: DN98H15VZF
kind: statement
role: theorem
name: Nehari's theorem on univalence
msc: [30C55, 30C45]
uses: [6ZPKWE0VAZ, R91E83SDBD, 8G5ABXRK85, 0DG0Z72CQD]
about: [6ZPKWE0VAZ, R91E83SDBD]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarzian_derivative
---

## Statement

Let $\mathbb{D}$ be the [[unit disc|8G5ABXRK85]], and let $f \colon \mathbb{D} \to \C$ be [[holomorphic|0DG0Z72CQD]] with $f'(z) \ne 0$ for all $z \in \mathbb{D}$.
Let $S(f)$ be its [[Schwarzian derivative|6ZPKWE0VAZ]].
If
$$\abs{S(f)(z)} \le \frac{2}{(1 - \abs{z}^2)^2} \qquad \text{for all } z \in \mathbb{D},$$
then $f$ is [[univalent|R91E83SDBD]] on $\mathbb{D}$.

## Remarks

Locally, $f = u_1/u_2$ for two independent solutions of the linear equation $u'' + \frac{1}{2} S(f)\, u = 0$.
If $f(a) = f(b)$ with $a \ne b$, then some solution of this equation vanishes at both $a$ and $b$.
A disc automorphism moves $a$ and $b$ onto a diameter.
The bound on $S(f)$ then allows a comparison of Sturm type with the equation $u'' + (1 - x^2)^{-2} u = 0$ on $(-1, 1)$.
That equation has the solution $\sqrt{1 - x^2}$ without zeros, which leads to a contradiction.
The constant $2$ cannot be replaced by any larger constant.
In the other direction, the Kraus–Nehari theorem says that every univalent $f$ on $\mathbb{D}$ satisfies $\abs{S(f)(z)} \le 6/(1 - \abs{z}^2)^2$, with equality at $z = 0$ for the [[Koebe function|EZQFWKF03Q]].
Example: $f(z) = e^{cz}$ has $S(f) = -c^2/2$, so for $\abs{c} \le 2$ the bound holds, since $(1 - \abs{z}^2)^{-2} \ge 1$; such $f$ is univalent on $\mathbb{D}$, as two points of $\mathbb{D}$ cannot differ by $2\pi i k / c$ with $k \ne 0$.

## Explanations

### L1 human

The Schwarzian derivative measures how far a map is from being a Möbius map, and Möbius maps are injective.
Nehari's theorem says that if the Schwarzian derivative is small enough, measured against the size of the disc near the boundary, then the map is injective.
It turns a global property, injectivity, into a pointwise bound that can be checked.

### L2 human

The weight $(1 - \abs{z}^2)^{-2}$ is the square of the density of the hyperbolic metric, so the condition is invariant under automorphisms of the disc.
Together with the necessary bound $6$, it shows that the Schwarzian derivatives of univalent functions all have bounded hyperbolic size, and that all small enough ones come from univalent functions.
This point of view leads to the Bers embedding of the universal Teichmüller space.
It also leads to the theorem of Ahlfors and Weill that a slightly stronger bound gives a quasiconformal extension of $f$ to the plane.
