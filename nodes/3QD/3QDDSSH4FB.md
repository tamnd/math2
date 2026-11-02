---
tag: 3QDDSSH4FB
kind: statement
role: theorem
name: Convergence of the Neumann series for Volterra kernels
msc: [45D05]
uses: [ATPSAHYG7C, 9QNBFERMHD, ARTJV1XCRX, H1HWSWME6B, 07EJHQYR9A]
about: [ATPSAHYG7C, ARTJV1XCRX]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%E2%80%93Neumann_series
---

## Statement

Let $a < b$, let $\Delta = \set{(t, s) : a \le s \le t \le b}$, and let $K \colon \Delta \to \C$ be continuous with $M = \max_\Delta \abs{K}$.
Define the [[iterated kernels|9QNBFERMHD]] on $\Delta$ by $K_1 = K$ and
$$K_{n+1}(t, s) = \int_s^t K(t, u) \, K_n(u, s) \, du, \quad n \ge 1.$$
Then the following hold.

1. Each $K_n$ is continuous on $\Delta$ and $\abs{K_n(t, s)} \le M^n \dfrac{(t - s)^{n - 1}}{(n - 1)!}$ for all $(t, s) \in \Delta$.
2. For every $\lambda \in \C$, the series $R(t, s; \lambda) = \sum_{n \ge 1} \lambda^{n - 1} K_n(t, s)$ converges absolutely and uniformly on $\Delta$, and uniformly for $\lambda$ in bounded sets.
3. The sum $R$ is continuous on $\Delta$, entire in $\lambda$, and $\abs{R(t, s; \lambda)} \le M e^{\abs{\lambda} M (t - s)}$.
4. For every continuous $f \colon [a, b] \to \C$, the [[Liouville–Neumann series|H1HWSWME6B]] $x = f + \sum_{n \ge 1} \lambda^n \int_a^t K_n(t, s) f(s) \, ds$ converges uniformly on $[a, b]$, and its sum
$$x(t) = f(t) + \lambda \int_a^t R(t, s; \lambda) \, f(s) \, ds$$
solves the [[Volterra equation of the second kind|ATPSAHYG7C]] $x(t) = f(t) + \lambda \int_a^t K(t, s) \, x(s) \, ds$.

## Remarks

The bound in item 1 is proved by induction: $\abs{K_{n+1}(t, s)} \le \int_s^t M \cdot M^n \frac{(u - s)^{n - 1}}{(n - 1)!} \, du = M^{n+1} \frac{(t - s)^n}{n!}$.
The factorial makes the series of item 2 converge like the exponential series, by the Weierstrass M-test, whatever the size of $\lambda$.
The function $R$ is the [[resolvent kernel|ARTJV1XCRX]] of $K$.
Example: for $K = 1$ on $[0, b]$, $K_n(t, s) = (t - s)^{n-1}/(n-1)!$ and $R(t, s; \lambda) = e^{\lambda (t - s)}$.
Then $x = 1 + \lambda \int_0^t x$ has the solution $x(t) = 1 + \lambda \int_0^t e^{\lambda(t - s)} \, ds = e^{\lambda t}$.
For a Fredholm kernel on $[a, b] \times [a, b]$ the same series converges only for $\abs{\lambda}$ small; the Volterra structure, with integration over $[s, t]$ only, is what produces the factorial.

## Explanations

### L1 human

The Neumann series solves an equation by substituting it into itself again and again.
In general, this only works if the kernel is small.
For a Volterra kernel, each substitution integrates over a shrinking triangle of past times, and the size of the $n$-th term drops like $1/(n - 1)!$.
So the iteration always converges, as the exponential series does.

### L2 human

The theorem shows that the Volterra integral operator has spectral radius $0$: it is quasinilpotent.
Consequently $I - \lambda V$ is invertible for every $\lambda$, which gives the [[unique solvability of Volterra equations of the second kind|WG4GVC9HR8]].
The same estimate, applied to a nonlinearity that is Lipschitz in $x$ uniformly on $[a, b]$, gives a global solution of the Picard–Lindelöf type on all of $[a, b]$.
The bound in item 3 is of [[Grönwall|07EJHQYR9A]] type, and it controls how solutions depend on $f$.
