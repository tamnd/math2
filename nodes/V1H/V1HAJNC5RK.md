---
tag: V1HAJNC5RK
kind: statement
role: theorem
name: Kolmogorov continuity theorem
msc: [60G17, 60G07]
uses: [0QH5ENKZM1, 0WQNRCNY3M, 012PBA0FMD, 22735FGJV6]
about: [0QH5ENKZM1, 012PBA0FMD]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_continuity_theorem
same_as:
  wikidata: Q5638321
  wikipedia: Kolmogorov continuity theorem
---

## Statement

Let $(X_t)_{t \in [0, \infty)}$ be a [[stochastic process|0QH5ENKZM1]] with values in $\R^n$.
Assume that there are constants $\alpha > 0$, $\beta > 0$ and $C > 0$ such that
$$E\left[\abs{X_t - X_s}^\alpha\right] \le C \abs{t - s}^{1 + \beta} \quad \text{for all } s, t \ge 0.$$
Then $X$ has a continuous modification: there is a process $(\tilde X_t)_{t \ge 0}$ such that $P(\tilde X_t = X_t) = 1$ for every $t \ge 0$ and every path $t \mapsto \tilde X_t(\omega)$ is continuous.
Moreover, for every $\gamma \in (0, \beta / \alpha)$, the paths of $\tilde X$ are locally [[Hölder continuous|012PBA0FMD]] of order $\gamma$.

## Remarks

Idea of the proof.
On the dyadic times $k 2^{-m}$, Markov's inequality and the hypothesis give $P(\abs{X_{(k+1)2^{-m}} - X_{k 2^{-m}}} > 2^{-\gamma m}) \le C 2^{-m(1 + \beta - \alpha \gamma)}$.
Summing over the $2^m$ times in $[0, 1]$ and over $m$ gives a convergent series when $\gamma < \beta / \alpha$.
By the [[Borel–Cantelli lemma|0T6WS7TT77]], the increments on dyadic times are eventually small, so $X$ is uniformly Hölder continuous on the dyadic times, and one defines $\tilde X$ as its continuous extension.

Example: for a [[Wiener process|22735FGJV6]] $W$ and an integer $m \ge 2$, $W_t - W_s$ is normal with variance $\abs{t - s}$, so $E[\abs{W_t - W_s}^{2m}] = c_m \abs{t - s}^m$ for a constant $c_m$.
The theorem applies with $\alpha = 2m$ and $\beta = m - 1$, and gives Hölder continuity of every order $\gamma < (m - 1)/(2m)$.
Letting $m \to \infty$, Brownian paths are locally Hölder continuous of every order $\gamma < 1/2$.

The exponent $1 + \beta$ must exceed $1$.
For a Poisson process $N$, $E[\abs{N_t - N_s}] = \abs{t - s}$, so the bound holds with $\alpha = 1$ and exponent $1$, but the paths of $N$ have jumps and $N$ has no continuous modification.

For processes indexed by $t \in [0, 1]^d$, the same conclusion holds with $\abs{t - s}^{d + \beta}$ in place of $\abs{t - s}^{1 + \beta}$.

## Explanations

### L1 human

A random process might be defined only through its values at each fixed time, with no guarantee that its paths are continuous.
The theorem gives a simple test.
If the average size of the jump between two times shrinks fast enough as the times get close, then one can choose a version with continuous paths.
This is how one shows that Brownian motion can be taken to have continuous paths.

### L2 human

The theorem bridges the [[finite-dimensional distributions|Y0CN7V3B7E]] of a process, which say nothing about path properties, and the regularity of its paths.
It is used to construct Brownian motion and the Brownian sheet, to prove continuity of solutions of stochastic differential equations in their initial data, and to obtain Hölder exponents.
Its proof is a chaining argument, a technique that also yields the Kolmogorov–Chentsov tightness criteria in spaces of continuous functions.
