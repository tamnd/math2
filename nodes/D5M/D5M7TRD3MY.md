---
tag: D5M7TRD3MY
kind: statement
role: theorem
name: Lax equivalence theorem
msc: [65M12, 65M06, 65J10]
uses: [X7HYEBA5SA, W09B9NZ9B5, 06GZ956657, 06EKW1AKXF, 075VBY4K4X, FQVVNYV6N8]
about: [X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Lax_equivalence_theorem
same_as:
  wikidata: Q256303
  wikipedia: Lax equivalence theorem
---

## Statement

Let $X$ be a [[Banach space|06GZ956657]] and $T > 0$.
Let $A$ be a linear operator in $X$ such that the [[initial value problem|075VBY4K4X]] $u'(t) = A u(t)$, $u(0) = u_0$, is [[well-posed|W09B9NZ9B5]].
This means there are bounded linear solution operators $E(t)$, $t \ge 0$, with $\sup_{0 \le t \le T} \norm{E(t)} < \infty$.
Moreover $u(t) = E(t) u_0$ is a genuine solution for $u_0$ in a dense subspace $D \subseteq X$.
Let $C(k)$, $0 < k \le k_0$, be bounded linear operators on $X$ defining the one-step [[finite difference scheme|X7HYEBA5SA]] $u^{n+1} = C(k) u^n$ with time step $k$.
Assume the scheme is consistent: for every $u_0 \in D$,
$$\lim_{k \to 0} \sup_{0 \le t \le T} \frac{\norm{C(k) u(t) - u(t + k)}}{k} = 0, \qquad u(t) = E(t) u_0.$$
Then the following are equivalent:

1. The scheme is stable: there are constants $K$ and $k_1 > 0$ with $\norm{C(k)^n} \le K$ whenever $0 < k \le k_1$ and $0 \le nk \le T$, where $\norm{\cdot}$ is the [[operator norm|06EKW1AKXF]].
2. The scheme is convergent: for every $u_0 \in X$, every $t \in [0, T]$, and all sequences $k_j \to 0$ and integers $n_j$ with $n_j k_j \to t$, one has $C(k_j)^{n_j} u_0 \to E(t) u_0$ in $X$.

## Remarks

Stability implies convergence by a telescoping sum: $C(k)^n u_0 - E(nk) u_0 = \sum_{m=0}^{n-1} C(k)^{n-1-m} \left( C(k) E(mk) - E((m+1)k) \right) u_0$.
Each factor $C(k)^{n-1-m}$ is bounded by $K$, and the $n$ consistency errors are each $o(k)$.
Density of $D$ and the uniform bounds then cover all $u_0$.
Convergence implies stability by the uniform boundedness principle, since the orbits $C(k)^n u_0$ stay bounded for each $u_0$.
Example: for $u_t = u_{xx}$ on $\R$ in the maximum norm, the explicit scheme $u_j^{n+1} = u_j^n + r(u_{j+1}^n - 2u_j^n + u_{j-1}^n)$ with fixed $r = k/h^2 \le \tfrac12$ satisfies $\norm{C(k)} \le 1$, so it converges.
With $r > \tfrac12$ the mode $u_j^0 = (-1)^j$ is multiplied by $1 - 4r < -1$ at each step, so the scheme is unstable and does not converge.
The theorem is for linear problems; for nonlinear schemes stability and consistency do not in general characterize convergence.

## Explanations

### L1 human

A numerical method for a time-dependent equation is consistent if each single step makes only a small error.
It is stable if errors do not blow up when many steps are taken.
The theorem says that, for linear problems that are well-posed, a consistent method gives the right answer as the steps shrink exactly when it is stable.
So the hard question "does the method converge?" reduces to the easier question "is it stable?".

### L2 human

In practice consistency is checked by Taylor expansion, and stability by a norm bound on the step operator $C(k)$, often through von Neumann's Fourier analysis in $L^2$.
For explicit schemes for hyperbolic equations, stability leads to the [[Courant–Friedrichs–Lewy condition|FQVVNYV6N8]] on $k/h$.
The result is due to Lax and Richtmyer, in their 1956 paper on the stability of linear finite difference equations.
The same structure, "consistency plus stability gives convergence", reappears for boundary value problems and for finite element methods, where Céa's lemma plays the role of stability.
