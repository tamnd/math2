---
tag: EZQFWKF03Q
kind: example
name: Koebe function
msc: [30C45, 30C55]
instance_of: [R91E83SDBD]
sources:
  - url: https://en.wikipedia.org/wiki/Koebe_quarter_theorem
---

## Example

The *Koebe function* is
$$k(z) = \frac{z}{(1 - z)^2} = \sum_{n=1}^{\infty} n z^n, \qquad \abs{z} < 1.$$
It is a [[univalent function|R91E83SDBD]] on the unit disc $\mathbb{D}$ in the class $S$, and $k(\mathbb{D}) = \C \setminus (-\infty, -1/4]$.

Check: one has
$$k(z) = \frac{1}{4}\left( \left(\frac{1 + z}{1 - z}\right)^2 - 1 \right).$$
The Möbius map $z \mapsto (1+z)/(1-z)$ maps $\mathbb{D}$ bijectively onto the right half-plane $\set{\operatorname{Re} w > 0}$.
Squaring maps the right half-plane bijectively onto $\C \setminus (-\infty, 0]$.
Finally $w \mapsto (w - 1)/4$ maps $\C \setminus (-\infty, 0]$ onto $\C \setminus (-\infty, -1/4]$.
A composition of injective holomorphic maps is injective and holomorphic, and $k(0) = 0$, $k'(0) = 1$.

## Remarks

The point $-1/4$ is not in the image, so the radius $1/4$ in the [[Koebe quarter theorem|WX0HMW4GT7]] cannot be improved.
The coefficients are $a_n = n$, so the bound $\abs{a_n} \le n$ of the [[Bieberbach conjecture|ZMRFSYVWQT]] is attained for every $n$.
The rotations $e^{-i\theta} k(e^{i\theta} z)$ with $\theta \in \R$ are also in $S$ and are the extremal functions of many problems on $S$.

## Explanations

### L1 human

The Koebe function maps the unit disc onto the whole plane with one slit cut out along the negative real axis, from $-1/4$ to $-\infty$.
It is the extreme case of the class of normalised univalent functions: it stretches the disc as much as possible.
Its boundary slit comes as close as $1/4$ to the origin, and its power series coefficients $1, 2, 3, \ldots$ are as large as allowed.
