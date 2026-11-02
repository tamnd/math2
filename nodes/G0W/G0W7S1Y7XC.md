---
tag: G0W7S1Y7XC
kind: definition
name: Nevanlinna theory in several variables
msc: [32H30, 32A22]
defines: DERJPQ04BQ
uses: [1EHH63VNAD, 0G4F0XB9X2, ZT9A6JK8QF, YT6Z0GWS0W, 0CRMGPAH83]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna_theory
---

## Definition

Let $n \ge 1$, let $\mathbb{P}^n$ be complex [[projective space|ZT9A6JK8QF]], and let $f \colon \C \to \mathbb{P}^n$ be a holomorphic curve.
A *reduced representation* of $f$ is a map $F = (f_0, \ldots, f_n) \colon \C \to \C^{n+1} \setminus \set{0}$ with [[entire|0G4F0XB9X2]] components and $f = [f_0 : \cdots : f_n]$.
It exists, and it is unique up to multiplication by a nowhere-zero entire function.
Let $\norm{\cdot}$ be the Euclidean norm on $\C^{n+1}$ and let $r > 0$.
Nevanlinna theory in several variables studies $f$ through the following functions of $r$.

1. The *characteristic function* $T_f(r) = \dfrac{1}{2\pi} \displaystyle\int_0^{2\pi} \log \norm{F(re^{i\theta})} \, d\theta - \log \norm{F(0)}$.
2. For a hyperplane $H = \set{a_0 x_0 + \cdots + a_n x_n = 0}$ with $a = (a_0, \ldots, a_n) \ne 0$ and $f(\C) \not\subset H$, write $\ip{F}{a} = a_0 f_0 + \cdots + a_n f_n$. The *counting function* $N_f(r, H) = \displaystyle\int_0^r \frac{n(t) - n(0)}{t} \, dt + n(0) \log r$, where $n(t)$ is the number of zeros of $\ip{F}{a}$ in $\set{\abs{z} \le t}$, counted with multiplicity.
3. The *proximity function* $m_f(r, H) = \dfrac{1}{2\pi} \displaystyle\int_0^{2\pi} \log \frac{\norm{F(re^{i\theta})} \, \norm{a}}{\abs{\ip{F(re^{i\theta})}{a}}} \, d\theta$.

The same notions exist for holomorphic maps from $\C^m$ to $\mathbb{P}^n$ or to projective varieties.
They use averages over spheres in $\C^m$, and divisors in place of hyperplanes.

## Remarks

The function $T_f$ does not depend on the reduced representation.
If $F$ is replaced by $gF$ with $g$ entire and nowhere zero, then $\log\abs{g}$ is harmonic, so its mean over the circle of radius $r$ is $\log\abs{g(0)}$.
Jensen's formula applied to $\ip{F}{a}$ gives the *first main theorem* $T_f(r) = m_f(r, H) + N_f(r, H) + O(1)$ as $r \to \infty$.

Example: let $g$ be a nonconstant entire function and $f = [1 : g] \colon \C \to \mathbb{P}^1$, with $F = (1, g)$.
Then $T_f(r) = \frac{1}{2\pi}\int_0^{2\pi} \log\sqrt{1 + \abs{g(re^{i\theta})}^2}\, d\theta + O(1)$.
Since $\log^+ \abs{w} \le \log\sqrt{1 + \abs{w}^2} \le \log^+\abs{w} + \frac12 \log 2$, this differs from the one-variable [[Nevanlinna characteristic|YT6Z0GWS0W]] $T(r, g)$ by a bounded amount.

Non-example: if $f(\C) \subset H$, then $\ip{F}{a} \equiv 0$ and the counting and proximity functions of $H$ are not defined.

Hyperplanes $H_1, \ldots, H_q$ are in *general position* if any $n + 1$ of their coefficient vectors are [[linearly independent|0CRMGPAH83]].
Cartan's second main theorem concerns a linearly nondegenerate $f$, that is, $f(\C)$ lies in no hyperplane, and hyperplanes $H_1, \ldots, H_q$ in general position.
It states that $(q - n - 1)\, T_f(r) \le \sum_{j=1}^q N_f(r, H_j) + O(\log T_f(r) + \log r)$.
The inequality holds for all $r$ outside a set of finite Lebesgue measure.
