---
tag: J3D1T7F0CB
kind: definition
name: Markov chain mixing time
msc: [60J10, 60J22]
defines: 8TV1YW8EXC
uses: [033TJBZDG0, 0F462493EA, 0KRH5157WP, B1E1ES1BYD]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_chain_mixing_time
---

## Definition

Let $S$ be a finite set and let $P$ be the [[transition matrix|0F462493EA]] of an irreducible and aperiodic [[Markov chain|033TJBZDG0]] on $S$.
Let $\pi$ be its [[stationary distribution|0KRH5157WP]].
The *total variation distance* between probability distributions $\mu$ and $\nu$ on $S$ is
$$\norm{\mu - \nu}_{TV} = \max_{A \subseteq S} \abs{\mu(A) - \nu(A)} = \frac12 \sum_{x \in S} \abs{\mu(x) - \nu(x)}.$$
For an integer $t \ge 0$ let $d(t) = \max_{x \in S} \norm{P^t(x, \cdot) - \pi}_{TV}$, where $P^t(x, \cdot)$ is row $x$ of $P^t$.
For $\varepsilon \in (0, 1)$, the *mixing time* is
$$t_{\mathrm{mix}}(\varepsilon) = \min\set{t \ge 0 : d(t) \le \varepsilon},$$
and $t_{\mathrm{mix}} = t_{\mathrm{mix}}(1/4)$.

## Remarks

The minimum exists because $d(t) \to 0$ by the [[convergence theorem|B1E1ES1BYD]] for ergodic chains.
Example: on $S = \set{1, 2}$ let every entry of $P$ be $1/2$.
Then $\pi = (1/2, 1/2)$, $d(0) = 1/2$ and $P^t(x, \cdot) = \pi$ for $t \ge 1$, so $t_{\mathrm{mix}} = 1$.
Non-example: for $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ the chain is periodic, $d(t) = 1/2$ for all $t$, and $t_{\mathrm{mix}}(\varepsilon)$ does not exist for $\varepsilon < 1/2$.
The function $d$ is nonincreasing, and $t_{\mathrm{mix}}(\varepsilon) \le \ceil{\log_2 (1/\varepsilon)} \, t_{\mathrm{mix}}$.
