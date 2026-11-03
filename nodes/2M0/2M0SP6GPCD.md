---
tag: 2M0SP6GPCD
kind: statement
role: theorem
name: Sundman's convergent series for the three-body problem
msc: [70F07, 70F16]
uses: [JE1Z920QKT, 0MZB06ST2B, 7147M98XNR]
about: [JE1Z920QKT]
sources:
  - url: https://en.wikipedia.org/wiki/Three-body_problem
---

## Statement

Consider the [[three-body problem|JE1Z920QKT]] with masses $m_1, m_2, m_3 > 0$ and gravitational constant $G > 0$.
Take initial positions that are pairwise distinct and initial velocities such that the total [[angular momentum|7147M98XNR]] $c = \sum_i m_i\, x_i \times x_i'$ is not zero.
Then there is a new independent variable $\sigma$, related to the time $t$ by an increasing bijection from $\R$ onto $(-1, 1)$, with this property.
The time $t$ and the coordinates of the three bodies are given by [[power series|0MZB06ST2B]] in $\sigma$ that converge for $\abs{\sigma} < 1$.
So these series describe the motion for all real times $t$, through any binary collisions.

## Remarks

The proof has two parts.
First, Sundman showed that a triple collision forces the total angular momentum to vanish.
So for $c \ne 0$ only binary collisions can occur, and the system stays away from a total collapse.
Second, binary collisions can be regularised by a time change $dt = \Gamma\, d\tau$, for a suitable function $\Gamma$ of the distances.
In the variable $\tau$ the solution extends analytically through collisions and is analytic in a strip $\abs{\operatorname{Im} \tau} < \delta$.
A conformal map sends that strip onto the unit disc, and the new variable on the disc is $\sigma$.
The hypothesis $c \ne 0$ is needed: with zero angular momentum the bodies can meet in a triple collision, which cannot be regularised in this way.
Sundman published the result in 1912.
Wang Qiudong extended it in 1991 to the $n$-body problem for solutions without singularities.
The series converge so slowly that they are of no practical use for computing orbits.

## Explanations

### L1 human

The three-body problem has no simple formula for its solution.
Still, Sundman proved that there is an infinite series that gives the exact motion for all time.
The catch is that one needs an absurd number of terms to get any useful accuracy.
So the theorem settles a question of principle, not of practice.

### L2 human

The result shows that "no closed-form solution" and "no convergent series solution" are different things.
The key step is the exclusion of triple collisions when the angular momentum is not zero, together with the regularisation of binary collisions.
Poincaré's non-integrability results remain true: the series give no first integrals and say little about the qualitative long-term behaviour.
