---
tag: Q3Y1HBD8NN
kind: statement
role: theorem
name: Dunford–Pettis theorem
msc: ["46E30", 46B50, 28A20]
uses: [SASP14MA1Z, VRVVKMXDGV, P6KHVSTPZV, 63Z1Q4FS23]
about: [SASP14MA1Z, VRVVKMXDGV]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_integrability
---

## Statement

Let $(X, \Sigma, \mu)$ be a measure space with $\mu$ a [[finite measure|63Z1Q4FS23]], and let $K$ be a subset of [[$L^1(\mu)$|SASP14MA1Z]].
Then the following are equivalent.

1. $K$ is relatively compact in the [[weak topology|P6KHVSTPZV]] of $L^1(\mu)$.
2. $K$ is [[uniformly integrable|VRVVKMXDGV]]: $\lim_{M \to \infty} \sup_{f \in K} \int_{\set{\abs{f} > M}} \abs{f} \, d\mu = 0$.

## Remarks

When $\mu$ is finite, condition 2 implies that $K$ is bounded in $L^1$.
One proof of 2 $\Rightarrow$ 1 views $K$ inside the bidual $L^\infty(\mu)^*$ and takes a weak-$*$ cluster point.
Uniform integrability makes the set functions $E \mapsto \int_E f \, d\mu$, $f \in K$, uniformly absolutely continuous, so the cluster point is a countably additive measure absolutely continuous with respect to $\mu$.
The [[Radon–Nikodym theorem|1ZSZS5G1Q4]] then gives it as an element of $L^1(\mu)$.
The converse uses the Eberlein–Šmulian theorem to reduce to sequences.

Example: on $[0, 1]$ with Lebesgue measure, a set bounded in $L^2$ is uniformly integrable, because $\int_{\set{\abs{f} > M}} \abs{f} \le \norm{f}_2^2 / M$.
So bounded subsets of $L^2$ are weakly relatively compact in $L^1$.

Boundedness in $L^1$ alone is not enough.
The functions $f_n = n \mathbf{1}_{[0, 1/n]}$ on $[0, 1]$ all have norm $1$, but $\int_{\set{f_n > M}} f_n = 1$ for $n > M$.
No subsequence converges weakly in $L^1$: as measures, $f_n \, dx$ concentrate at the point $0$.

## Explanations

### L1 human

In $L^1$, bounded sequences need not have limits even in a weak sense, because the mass of the functions can pile up on smaller and smaller sets.
The theorem says that this concentration is the only obstruction.
If the functions cannot put a fixed amount of mass where they are very large, then every sequence has a weakly convergent subsequence.

### L2 human

The theorem is the $L^1$ substitute for the weak compactness of bounded sets in reflexive spaces such as $L^p$, $1 < p < \infty$.
In probability it is the analytic side of the fact that uniformly integrable families of random variables behave well under limits, as in the [[Vitali convergence theorem|C3CKZAZ57Z]].
In the calculus of variations it gives weak limits for sequences with superlinear integral bounds, by the de la Vallée-Poussin criterion.
