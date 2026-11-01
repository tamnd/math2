---
tag: NFXKNDJX9C
kind: statement
role: theorem
name: Functional equation of the Riemann zeta function
msc: [11M06]
uses: [1XWBY4N0VT, 0H5SYBSED9, 0ZZ7ZYDR8W]
about: [1XWBY4N0VT]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_zeta_function
---

## Statement

Let $\zeta$ be the [[Riemann zeta function|1XWBY4N0VT]] and $\Gamma$ the [[gamma function|0H5SYBSED9]].
Then, as an identity of [[meromorphic functions|0ZZ7ZYDR8W]] on $\C$,
$$\zeta(s) = 2^s \pi^{s-1} \sin\!\left(\frac{\pi s}{2}\right) \Gamma(1 - s) \, \zeta(1 - s).$$
Equivalently, the completed zeta function $\xi_0(s) = \pi^{-s/2} \, \Gamma(s/2) \, \zeta(s)$ satisfies $\xi_0(s) = \xi_0(1 - s)$ for all $s \in \C \setminus \set{0, 1}$.

## Remarks

One proof uses the theta function $\theta(t) = \sum_{n \in \Z} e^{-\pi n^2 t}$ for $t > 0$.
Poisson summation gives $\theta(1/t) = \sqrt{t} \, \theta(t)$.
A Mellin transform expresses $\xi_0(s)$ as an integral of $(\theta(t) - 1)/2$ against $t^{s/2 - 1}$.
Splitting the integral at $t = 1$ and using the symmetry of $\theta$ gives a formula that is visibly invariant under $s \mapsto 1 - s$.
The same formula gives the meromorphic continuation of $\zeta$ to $\C$.
Example: at $s = -1$ the right side is $\frac{1}{2} \cdot \frac{1}{\pi^2} \cdot (-1) \cdot \Gamma(2) \cdot \zeta(2) = -\frac{1}{12}$, using $\zeta(2) = \pi^2/6$, so $\zeta(-1) = -1/12$.
At $s = -2, -4, -6, \dots$ the sine factor vanishes while $\Gamma(1 - s) \zeta(1 - s)$ is finite and nonzero, so these are zeros of $\zeta$, the trivial zeros.

## Explanations

### L1 human

The zeta function is first defined only for $\operatorname{Re} s > 1$.
The functional equation links its value at $s$ to its value at $1 - s$, a reflection in the point $1/2$.
So knowing $\zeta$ on the right half of the plane determines it on the left half.

### L2 human

The equation shows that the zeros of $\zeta$ with $\operatorname{Re} s < 0$ are the trivial zeros $-2, -4, \dots$.
The other zeros lie in the critical strip $0 \le \operatorname{Re} s \le 1$, placed symmetrically about the line $\operatorname{Re} s = 1/2$.
The [[Riemann hypothesis|VCGF9YR36X]] says that they lie on this line.
[[Dirichlet L-functions|9D2Z543EJQ]] of primitive characters and many other L-functions satisfy functional equations of the same shape.
