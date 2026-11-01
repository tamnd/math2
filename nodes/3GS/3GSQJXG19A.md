---
tag: 3GSQJXG19A
kind: definition
name: Schwarzian derivative
msc: [30C55, 30C35]
defines: 6ZPKWE0VAZ
uses: [0DG0Z72CQD, 097KNJFJ7V, 0B346DDAM5]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarzian_derivative
---

## Definition

Let $U \subseteq \C$ be a [[domain|097KNJFJ7V]], and let $f \colon U \to \C$ be [[holomorphic|0DG0Z72CQD]] with $f'(z) \ne 0$ for all $z \in U$.
The *Schwarzian derivative* of $f$ is the holomorphic function $S(f) \colon U \to \C$ given by
$$S(f) = \left(\frac{f''}{f'}\right)' - \frac{1}{2}\left(\frac{f''}{f'}\right)^2 = \frac{f'''}{f'} - \frac{3}{2}\left(\frac{f''}{f'}\right)^2.$$

## Remarks

Other notations are $\set{f, z}$ and $S_f$.
The two expressions agree, since $(f''/f')' = f'''/f' - (f''/f')^2$.
Example: for $f(z) = e^z$ on $\C$, $f'' / f' = 1$, so $S(f) = 0 - \frac{1}{2} = -\frac{1}{2}$.
For a [[Möbius transformation|0B346DDAM5]] $T(z) = (az + b)/(cz + d)$ with $ad - bc \ne 0$, one gets $S(T) = 0$; conversely $S(f) = 0$ on a domain only for restrictions of Möbius maps.
Non-example: $f(z) = z^2$ on $\C$ has $f'(0) = 0$, so it is excluded; indeed $S(f)(z) = -\frac{3}{2z^2}$ on $\C \setminus \set{0}$ has a pole at $0$.
The chain rule is $S(f \circ g) = (S(f) \circ g)\,(g')^2 + S(g)$, so $S(T \circ f) = S(f)$ for every Möbius $T$.
The definition extends to locally injective meromorphic functions, with $S(f)$ holomorphic, since $S(1/f) = S(f)$.
