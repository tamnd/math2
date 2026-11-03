---
tag: ME8KF8J8AZ
kind: definition
name: Lemke's algorithm
msc: [90C33, 90C49]
defines: GFPSSH1C2M
uses: [8G30AFBZNQ]
sources:
  - url: https://en.wikipedia.org/wiki/Lemke%27s_algorithm
---

## Definition

Let $M$ be a real $n \times n$ matrix and $q \in \R^n$, and consider the [[linear complementarity problem|8G30AFBZNQ]] $w = M z + q$, $w, z \ge 0$, $z^T w = 0$.
Fix a covering vector $d \in \R^n$ with all $d_i > 0$, usually $d = (1, \dots, 1)^T$.
*Lemke's algorithm* works with the augmented system
$$w = M z + q + d z_0, \qquad w \ge 0, \ z \ge 0, \ z_0 \ge 0,$$
in an extra variable $z_0$, and keeps a basis of $n$ variables, the others being $0$.

1. If $q \ge 0$, return $z = 0$, $w = q$.
2. Otherwise let $r$ be an index with $-q_r/d_r = \max_i (-q_i/d_i)$, set $z_0 = -q_r/d_r$ and $z = 0$, and pivot $z_0$ into the basis in place of $w_r$.
3. Let the entering variable be the complement of the variable that just left the basis ($z_i$ if $w_i$ left, $w_i$ if $z_i$ left).
4. Increase the entering variable while the basic variables stay nonnegative. If it can increase without bound, stop with a secondary ray.
5. Otherwise the minimum ratio test gives a basic variable that reaches $0$ first; pivot it out. If it is $z_0$, return the current $(w, z)$, which solves the problem. Else go to step 3.

## Remarks

At every step $z_i w_i = 0$ for all $i$ except at most one, so the output in step 5 satisfies $z^T w = 0$ with $z_0 = 0$.
Under a nondegeneracy assumption no basis repeats, so the algorithm ends after finitely many pivots.
If $M$ is copositive-plus (for example positive semidefinite) and the algorithm ends in a secondary ray, then the problem has no solution.

Example: $n = 1$, $M = 1$, $q = -2$, $d = 1$.
Step 2 sets $z_0 = 2$ with $w = 0$; then $z$ enters, and as $z$ grows $z_0 = 2 - z$ decreases ($w$ stays $0$), reaching $0$ at $z = 2$.
So $z_0$ leaves and the output is $z = 2$, $w = 0$, which solves $w = z - 2$.

Non-example: the simplex method with the usual most-negative-reduced-cost rule is not Lemke's algorithm, since its entering variable is not chosen as the complement of the leaving one.
