---
tag: 5MP7DM0V5V
kind: counterexample
name: Failure of Kalman's conjecture
msc: [93D05, 34D23, 34C25]
uses: [037ZNY7NAG, 0NB689782W, 0N8NGKDZDZ, 0AA97XA70K]
sources:
  - url: https://en.wikipedia.org/wiki/Kalman%27s_conjecture
    locator: Mathematical statement of Kalman's conjecture (Kalman problem)
---

## Counterexample

Kalman's conjecture concerns systems of the form
$$\dot x = P x + q\, f(e), \qquad e = r^{T} x.$$
Here $x \in \R^n$, $P$ is a constant real $n \times n$ matrix, and $q, r \in \R^n$ are constant vectors.
The function $f \colon \R \to \R$ is differentiable with $f(0) = 0$.
Assume that $k_1 < f'(e) < k_2$ for all $e$, and that for every $k \in (k_1, k_2)$ the [[linear system|037ZNY7NAG]] $\dot x = (P + k\, q r^{T}) x$ is [[asymptotically stable|0NB689782W]].
The conjecture claims that then the [[equilibrium|0N8NGKDZDZ]] $x = 0$ attracts every solution.

The claim is false in general.
For $n \le 3$ it is true.
But for some $n > 3$ there are $P$, $q$, $r$ and $f$ that satisfy all the hypotheses, while the system has a non-constant [[periodic orbit|0AA97XA70K]].
A solution on that orbit does not tend to $0$, so $0$ is not a global attractor.

## Remarks

Kalman stated the problem in 1957.
In the counterexamples constructed by Leonov, Kuznetsov and coauthors, the periodic orbit is stable and coexists with the stable equilibrium at $0$.
Its basin of attraction does not touch a small neighbourhood of the equilibrium, so it is a hidden oscillation: simulation from initial points near $0$ does not reveal it.
Once a counterexample exists in dimension $n$, adding decoupled coordinates with $\dot w = -w$ gives one in every larger dimension.
For the discrete-time analogue the conjecture holds only for $n = 1$.

## Explanations

### L1 human

Replace a nonlinear part of a feedback loop by straight lines whose slopes lie in the range of the slopes of the nonlinearity.
If every such linear system is stable, it is tempting to think that the nonlinear system is stable as well.
Kalman's conjecture says so, and it is true in low dimension.
In higher dimensions it can fail: the nonlinear system can keep oscillating forever, although every linear comparison system is stable.
