---
tag: HQYYC50SFQ
kind: definition
name: Glauber dynamics
msc: [82C20, 60J10, 82C22]
defines: AKP85F38KP
uses: [R0KGM32QN6, DG9F3W6MZM, 0G48PYM96Q, CTGN6CK1ZS]
sources:
  - url: https://en.wikipedia.org/wiki/Glauber_dynamics
---

## Definition

Let $G = (V, E)$ be a finite graph, let $J \in \R$, $h \in \R$ and $\beta \ge 0$, and let $\Omega = \set{-1, +1}^V$.
Let $\pi$ be the [[Ising model|R0KGM32QN6]] [[Gibbs measure|DG9F3W6MZM]] on $\Omega$, given by $\pi(\sigma) \propto e^{-\beta H(\sigma)}$ with
$$H(\sigma) = -J \sum_{\set{u, v} \in E} \sigma_u \sigma_v - h \sum_{v \in V} \sigma_v.$$
The *Glauber dynamics* (heat-bath version) for $\pi$ is the [[Markov chain|0G48PYM96Q]] on $\Omega$ whose step from a configuration $\sigma$ is:

1. choose a vertex $v \in V$ uniformly at random;
2. keep $\sigma_u$ for all $u \ne v$;
3. set the new spin at $v$ to $+1$ with probability
$$p_v(\sigma) = \frac{1}{1 + e^{-2\beta (J S_v + h)}}, \qquad S_v = \sum_{u : \set{u, v} \in E} \sigma_u,$$
and to $-1$ with probability $1 - p_v(\sigma)$.

## Remarks

The number $p_v(\sigma)$ is the conditional probability under $\pi$ that the spin at $v$ is $+1$ given the other spins: the two candidates have weights $e^{\pm\beta(JS_v + h)}$.
The chain satisfies [[detailed balance|CTGN6CK1ZS]] with respect to $\pi$, so $\pi$ is stationary, and since it is irreducible and aperiodic it converges to $\pi$.
Example: take a single edge $\set{a, b}$ with $h = 0$, and start from $\sigma = (+1, +1)$.
The chain picks $a$ with probability $1/2$ and flips it with probability $1 - p_a = 1/(1 + e^{2\beta J})$.
So the move to $(-1, +1)$ has probability $\tfrac12 (1 + e^{2\beta J})^{-1}$, and the reverse move has probability $\tfrac12 (1 + e^{-2\beta J})^{-1}$.
Detailed balance holds because $\pi(+,+)/\pi(-,+) = e^{2\beta J}$, which is the reverse move probability divided by the forward one.
Non-example: the chain that picks a uniform vertex and always flips its spin fails clause 3.
Its stationary law is uniform on $\Omega$, which differs from $\pi$ when $\beta J \ne 0$ and $E$ is non-empty.
The same scheme works for any Gibbs measure on a product space; the continuous-time version updates each vertex at the times of an independent rate-one Poisson clock.
Glauber's 1963 paper treated the one-dimensional Ising chain with single spin-flip rates of this kind; the Metropolis rule is another common choice with the same stationary law.
