---
tag: TNMQDK0RR0
kind: statement
role: theorem
name: Hadamard three-circle theorem for subharmonic functions
msc: [31A05, 30C80]
uses: [Z1MHMGFNFW, 9XJ5FBQD7M, 07Q7CNM5WF, 0CW52NV5TC, 7TXCCCA17A, V00Q05ZW1G]
about: [Z1MHMGFNFW]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_three-circle_theorem
---

## Statement

Let $0 < r_1 < r_2$ and let $u$ be [[subharmonic|Z1MHMGFNFW]] on an open subset of $\C$ that contains the closed [[annulus|0CW52NV5TC]] $A = \set{z : r_1 \le \abs{z} \le r_2}$.
For $r_1 \le r \le r_2$ let $M(r) = \max_{\abs{z} = r} u(z)$, and assume that $M(r_1)$ and $M(r_2)$ are finite.
Then for every $r$ with $r_1 \le r \le r_2$,
$$M(r) \le \frac{\log(r_2/r)}{\log(r_2/r_1)}\, M(r_1) + \frac{\log(r/r_1)}{\log(r_2/r_1)}\, M(r_2).$$
Equivalently, $M(r)$ is a [[convex function|07Q7CNM5WF]] of $\log r$ on $[r_1, r_2]$.

## Remarks

The maximum $M(r)$ exists because an upper semicontinuous function attains its maximum on a compact circle.
Proof idea: choose real $a, b$ such that $h(z) = a + b \log\abs{z}$ equals $M(r_1)$ on $\abs{z} = r_1$ and $M(r_2)$ on $\abs{z} = r_2$.
The function $h$ is harmonic on $\C \setminus \set{0}$, so $u - h$ is subharmonic on the open annulus, and its upper limits at the two boundary circles are at most $0$.
The [[maximum principle for subharmonic functions|9XJ5FBQD7M]] gives $u \le h$ on $A$, so $M(r) \le a + b \log r$, which is the stated inequality.
Applying the same bound to every sub-annulus gives convexity in $\log r$.

Example: for $u(z) = \log\abs{z}$, $M(r) = \log r$ is linear in $\log r$ and equality holds.
For a holomorphic $f$, the function $\log\abs{f}$ is [[subharmonic|7TXCCCA17A]], and the theorem becomes the classical [[Hadamard three-circle theorem|V00Q05ZW1G]] for $\log \max_{\abs{z}=r} \abs{f(z)}$.

## Explanations

### L1 human

Take the largest value of a subharmonic function on each circle around the origin.
Plotted against the logarithm of the radius, these largest values form a convex curve.
So the maximum on a middle circle is controlled by the maxima on an inner and an outer circle.

### L2 human

The proof is a direct comparison with the harmonic functions $a + b\log\abs{z}$, which are the radial harmonic functions in the plane.
The same argument in $\R^n$ with $n \ge 3$ shows that the maximum over spheres is convex as a function of $r^{2-n}$.
The result is a standard tool for growth estimates of holomorphic and subharmonic functions, together with the Phragmén–Lindelöf principle.
