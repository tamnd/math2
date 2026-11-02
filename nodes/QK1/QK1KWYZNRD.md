---
tag: QK1KWYZNRD
kind: statement
role: theorem
name: Liouville's theorem for harmonic functions
msc: [31B05]
uses: [0DEB0JMN0W, N76R7JWMNJ, YNH832D50W]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_function
---

## Statement

Let $n \ge 1$ and let $u \colon \R^n \to \R$ be [[harmonic|0DEB0JMN0W]] on all of $\R^n$.
If $u$ is bounded above or bounded below on $\R^n$, then $u$ is constant.

## Remarks

Proof idea for a bounded function, $\abs{u} \le M$: by the [[gradient estimate|N76R7JWMNJ]] on the ball $B(x, r)$, $\abs{\nabla u(x)} \le n M / r$ for every $r > 0$.
Letting $r \to \infty$ gives $\nabla u = 0$ everywhere, so $u$ is constant.
If $u$ is only bounded below, say $u \ge m$, apply [[Harnack's inequality|YNH832D50W]] to the nonnegative harmonic function $u - m$ on larger and larger balls.
It shows that $u - m$ is bounded, and the first case applies.
The theorem fails on proper subsets: on the half-space $\set{x_n > 0}$, $u = x_n$ is bounded below and not constant.
Some one-sided condition is needed: $u(x, y) = x$ is harmonic on $\R^2$ and not constant.
A harmonic function on $\R^n$ with $\abs{u(x)} \le C(1 + \abs{x})^k$ is a harmonic polynomial of degree at most $k$.

## Explanations

### L1 human

A harmonic function defined on the whole space cannot stay below a ceiling, or above a floor, unless it is flat.
Every nonconstant harmonic function on the whole space takes arbitrarily large and arbitrarily small values.

### L2 human

For $n = 2$ this is the real counterpart of Liouville's theorem for entire functions, and the two imply each other through harmonic conjugates.
The theorem gives uniqueness of solutions of Poisson's equation on $\R^n$ that tend to $0$ at infinity.
It is the prototype of Liouville theorems for elliptic equations and for harmonic maps.
On $\R^n$ minus a point, or on other spaces, the analogous question leads to the distinction between parabolic and hyperbolic spaces.
