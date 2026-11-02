---
tag: V0SH1DY9FJ
kind: statement
role: theorem
name: Capacity equals transfinite diameter and Chebyshev constant
msc: [31A15, 30C85]
uses: [0R6EWFKRCF, DBQXRTC0VN, VSGTSQ7RY8, DMNN7E2BYA, F0RVAF11K9]
about: [DBQXRTC0VN, VSGTSQ7RY8, DMNN7E2BYA]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_radius
---

## Statement

Let $K$ be a [[compact set|0R6EWFKRCF]] in $\C$.
Let $\operatorname{cap}(K)$ be its [[logarithmic capacity|DBQXRTC0VN]], $\delta(K)$ its [[transfinite diameter|VSGTSQ7RY8]] and $\tau(K)$ its [[Chebyshev constant|DMNN7E2BYA]].
Then
$$\operatorname{cap}(K) = \delta(K) = \tau(K).$$

## Remarks

Proof idea for $\delta(K) \le \tau(K)$: in the Vandermonde determinant of $n$ points of $K$, replace the columns $1, z, \dots, z^{n-1}$ by monic polynomials of small norm on $K$.
The determinant does not change, and by Hadamard's inequality it is at most $n^{n/2}$ times the product of the column maxima.
For $\tau(K) \le \delta(K)$: if $z_1, \dots, z_{n+1}$ are [[Fekete points|F0RVAF11K9]] of $K$, the monic polynomial $\prod_{j \le n} (z - z_j)$ is bounded on $K$ by a ratio of Fekete products.
For $\operatorname{cap}(K) = \delta(K)$: the discrete energy of $n$ Fekete points is close to the least energy of a probability measure.
When $\operatorname{cap}(K) > 0$, the normalized counting measures of Fekete points converge weakly to the equilibrium measure.

Example: for $K = [-1, 1]$, the monic Chebyshev polynomials $2^{1-n} T_n$ have maximum $2^{1-n}$ on $K$ and are extremal.
So $\tau(K) = 1/2$, and the theorem gives $\operatorname{cap}(K) = \delta(K) = 1/2$.

The theorem holds for every compact $K$, including sets of capacity zero, where all three quantities vanish.
Fekete proved the equality of the transfinite diameter and the Chebyshev constant, and Szegő proved their equality with the capacity.

## Explanations

### L1 human

There are three natural ways to measure the size of a plane set $K$ through potential theory.
One uses the least energy of a unit charge on $K$.
One uses how far apart many points of $K$ can be spread.
One uses how small a monic polynomial can stay on $K$.
The theorem says that the three give the same number.

### L2 human

The theorem lets one compute capacity by whichever method is easiest for the set at hand.
Polynomials and Fekete points give upper and lower bounds that can be computed numerically.
It also explains the role of capacity in polynomial approximation: the $n$-th root of the norm of the best monic polynomial on $K$ tends to $\operatorname{cap}(K)$.
