---
tag: T12FSF2J2V
kind: statement
role: theorem
name: Liouville's theorem for planar harmonic functions
msc: [31A05]
uses: [0DEB0JMN0W, CVDGP7DKZ3, 050F2FMTKF, 0EHKVRF4J6, Z1MHMGFNFW, QK1KWYZNRD]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_function
---

## Statement

Let $u \colon \C \to \R$ be a [[harmonic function|0DEB0JMN0W]] on the whole plane.
Assume that $u$ is bounded above or bounded below.
Then $u$ is constant.

## Remarks

Proof idea: $\C$ is simply connected, so by [[the existence of harmonic conjugates|CVDGP7DKZ3]] there is an entire function $f$ with $\operatorname{Re} f = u$.
If $u \le M$ on $\C$, then $g = e^{f}$ is entire with $\abs{g} = e^{u} \le e^{M}$.
By [[Liouville's theorem|0EHKVRF4J6]], $g$ is constant, so $f' e^{f} = g' = 0$, hence $f' = 0$ and $u$ is constant.
If $u$ is bounded below, apply this to $-u$.
A one-sided bound is needed: $u(x + iy) = x$ is harmonic, nonconstant, and unbounded in both directions.
The theorem is the planar case of [[Liouville's theorem for harmonic functions|QK1KWYZNRD]] on $\R^n$.
In the plane even more is true: a [[subharmonic function|Z1MHMGFNFW]] on $\C$ that is bounded above is constant.
This stronger form fails in $\R^n$ for $n \ge 3$, where $-\min(1, \abs{x}^{2-n})$ is subharmonic, bounded above, and not constant.

## Explanations

### L1 human

A harmonic function on the whole plane cannot stay below a ceiling unless it is flat.
Think of a membrane stretched over the entire plane: if it never rises above some height, it must be level everywhere.

### L2 human

The proof shows a typical planar technique: pass to a holomorphic function with real part $u$ and use complex analysis.
The theorem gives quick uniqueness results, for example for harmonic functions on $\C$ with a given one-sided bound.
Its subharmonic form says that $\C$ is a parabolic surface in potential theory: it carries no nonconstant negative subharmonic function.
