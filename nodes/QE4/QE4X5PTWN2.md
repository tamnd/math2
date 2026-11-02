---
tag: QE4X5PTWN2
kind: definition
name: Least harmonic majorant
msc: [31B05, 31A05]
defines: G0H97JZRS9
uses: [ZDHPQWWCQW, 0DEB0JMN0W, Z1MHMGFNFW, 02BH3MCBQB, PCZBE7EX01]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]], and let $u \colon \Omega \to [-\infty, \infty)$ be a function.
A *least harmonic majorant* of $u$ is a [[harmonic majorant|ZDHPQWWCQW]] $h_0$ of $u$ such that $h_0 \le h$ on $\Omega$ for every harmonic majorant $h$ of $u$.

## Remarks

A least harmonic majorant is unique when it exists, since two of them are each at most the other.
If $\Omega$ is connected and $u$ is [[subharmonic|Z1MHMGFNFW]] with at least one harmonic majorant, then $u$ has a least harmonic majorant.
The *greatest harmonic minorant* of a function $v$ is defined in the same way; it is $-h_0$, where $h_0$ is the least harmonic majorant of $-v$.

Example: on the unit disc $\mathbb{D} \subseteq \C$, the least harmonic majorant of $u(z) = \abs{z}^2$ is the constant $1$.
It is a harmonic majorant.
Let $h$ be any harmonic majorant, and let $\abs{a} < r < 1$.
Since $h \ge r^2$ on the circle of radius $r$, the [[Poisson integral formula|PCZBE7EX01]] on that circle gives $h(a) \ge r^2$.
Letting $r \to 1$ gives $h(a) \ge 1$.

Non-example: the constant $2$ is a harmonic majorant of $\abs{z}^2$ on $\mathbb{D}$, but it is not least, because $1$ is also a harmonic majorant and $2 \le 1$ fails.
