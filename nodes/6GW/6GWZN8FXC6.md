---
tag: 6GWZN8FXC6
kind: definition
name: Harmonic majorant
msc: [31B05, 31A05]
defines: ZDHPQWWCQW
uses: [02BH3MCBQB, 0DEB0JMN0W, Z1MHMGFNFW, QK1KWYZNRD, PNNNFJVF6W]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]], and let $u \colon \Omega \to [-\infty, \infty)$ be a function, usually [[subharmonic|Z1MHMGFNFW]].
A *harmonic majorant* of $u$ is a [[harmonic function|0DEB0JMN0W]] $h$ on $\Omega$ such that $u(x) \le h(x)$ for every $x \in \Omega$.

## Remarks

Symmetrically, a harmonic minorant of $v$ is a harmonic $h$ with $h \le v$, so $h$ is a harmonic minorant of $v$ exactly when $-h$ is a harmonic majorant of $-v$.
For a holomorphic $f$ on the unit disc and $0 < p < \infty$, $f$ lies in the [[Hardy space|PNNNFJVF6W]] $H^p$ if and only if the subharmonic function $\abs{f}^p$ has a harmonic majorant.

Example: on the unit disc $\mathbb{D} \subseteq \C$, let $u(z) = \abs{z}^2$.
The constant $h = 1$ is harmonic and $\abs{z}^2 < 1$ on $\mathbb{D}$, so $h$ is a harmonic majorant of $u$.

Non-example: on all of $\C$, $u(z) = \abs{z}^2$ has no harmonic majorant.
A harmonic $h$ with $h \ge \abs{z}^2 \ge 0$ would be a harmonic function bounded below on $\C$, hence constant by [[Liouville's theorem for harmonic functions|QK1KWYZNRD]].
No constant is at least $\abs{z}^2$ for all $z$.
