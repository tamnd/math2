---
tag: 45XV8FNBVH
kind: statement
role: theorem
name: Worpitzky's theorem
sources:
  - wikipedia: en:8658125@r1315598397
    locator: Convergence problem, section Elementary results > Worpitzky's theorem
    note: adopted
    mention: wikipedia://en/8658125#K3X8
    sections: [Statement]
inventory: [7MF0RM9CNJ]
---

## Statement

By applying the fundamental inequalities to the continued fraction

$$x = \cfrac{1}{1 + \cfrac{a_2}{1 + \cfrac{a_3}{1 + \cfrac{a_4}{1 + \ddots}}}}\,$$

it can be shown that the following statements hold if |*a*<sub>*i*</sub>| ≤ $\tfrac{1}{4}$ for the partial numerators *a*<sub>*i*</sub>, *i* = 2, 3, 4, ...

- The continued fraction *x* converges to a finite value, and converges uniformly if the partial numerators *a*<sub>*i*</sub> are complex variables.
- The value of *x* and of each of its convergents *x*<sub>*i*</sub> lies in the circular domain of radius 2/3 centered on the point *z* = 4/3; that is, in the region defined by

$\Omega = \lbrace z: |z - 4/3| \leq 2/3 \rbrace.\,$

- The radius $\tfrac{1}{4}$ is the largest radius over which *x* can be shown to converge without exception, and the region Ω is the smallest image space that contains all possible values of the continued fraction *x*.

Because the proof of Worpitzky's theorem employs Euler's continued fraction formula to construct an infinite series that is equivalent to the continued fraction *x*, and the series so constructed is [[absolutely convergent|0YBDSJARWN]], the [[Weierstrass M-test|0NX5NWAFC9]] can be applied to a modified version of *x*. If

$$f(z) = \cfrac{1}{1 + \cfrac{c_2z}{1 + \cfrac{c_3z}{1 + \cfrac{c_4z}{1 + \ddots}}}}\,$$

and a positive real number *M* exists such that |*c*<sub>*i*</sub>| ≤ *M* (*i* = 2, 3, 4, ...), then the sequence of convergents {*f*<sub>*i*</sub>(*z*)} converges uniformly when

$$|z| < \frac{1}{4M}\,$$

and *f*(*z*) is analytic on that open disk.
