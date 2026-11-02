---
tag: A2QG6D75KR
kind: counterexample
name: Failure of Aizerman's conjecture
msc: [93D05, 34D23, 34C25]
uses: [037ZNY7NAG, 0NB689782W, 0N8NGKDZDZ, 0BARQY52N5, 5MP7DM0V5V]
sources:
  - url: https://en.wikipedia.org/wiki/Aizerman%27s_conjecture
    locator: Mathematical statement of Aizerman's conjecture (Aizerman problem)
---

## Counterexample

Aizerman's conjecture concerns systems of the form
$$\dot x = P x + q\, f(e), \qquad e = r^{T} x,$$
where $x \in \R^n$, $P$ is a constant real $n \times n$ matrix, $q, r \in \R^n$ are constant vectors, and $f \colon \R \to \R$ satisfies $f(0) = 0$.
Assume that $k_1 < f(e)/e < k_2$ for all $e \ne 0$, and that for every $k \in (k_1, k_2)$ the [[linear system|037ZNY7NAG]] $\dot x = (P + k\, q r^{T}) x$ is [[asymptotically stable|0NB689782W]].
The conjecture claims that then the [[equilibrium|0N8NGKDZDZ]] $x = 0$ is globally asymptotically stable.

The claim is false in general.
Let $P$, $q$, $r$, $f$ be a [[counterexample to Kalman's conjecture|5MP7DM0V5V]].
So $f$ is differentiable, $f(0) = 0$, $k_1 < f' < k_2$, and all the linear systems above are asymptotically stable.
Yet the system has a non-constant periodic solution.
For $e \ne 0$ the [[mean value theorem|0BARQY52N5]] gives $\xi$ between $0$ and $e$ with $f(e)/e = f'(\xi)$, so $k_1 < f(e)/e < k_2$.
Hence the same system satisfies the hypotheses of Aizerman's conjecture.
Its periodic solution does not tend to $0$, so the conclusion fails.

## Remarks

Aizerman posed the problem in 1949.
The hypothesis of Aizerman's conjecture bounds the secant slopes $f(e)/e$, while Kalman's conjecture bounds the slopes $f'$; the second hypothesis is stronger, so Kalman's conjecture is the weaker claim.
This is why a counterexample to Kalman's conjecture is also one to Aizerman's.
In the counterexamples constructed by Leonov, Kuznetsov and coauthors, a stable periodic orbit coexists with the stable equilibrium, a so-called hidden oscillation.

## Explanations

### L1 human

Suppose a feedback loop is stable whenever its nonlinearity is replaced by a straight line through the origin with a slope in a given range.
The conjecture says that the loop is then also stable with the nonlinearity itself.
This sounds plausible, since the nonlinearity always lies between such lines.
It is false: some of these systems oscillate forever, although every linear comparison system settles down.
