---
tag: NRWXPBDJTE
kind: definition
name: Chemical master equation
msc: [60J28, "92E20", 80A30]
defines: VTE4ZCT4WJ
uses: [VHQA7XPMQ4, TWQFE0FZZS, TTH05RV6SW]
sources:
  - url: https://en.wikipedia.org/wiki/Master_equation
---

## Definition

Consider a well-mixed system of $N$ chemical species in a fixed volume, with state $x = (x_1, \dots, x_N) \in \Z_{\ge 0}^N$, where $x_i$ is the number of molecules of species $i$.
Let there be $M$ reaction channels.
Channel $j$ has a *state-change vector* $\nu_j \in \Z^N$ and a *propensity function* $a_j \colon \Z_{\ge 0}^N \to [0, \infty)$ with $a_j(x) = 0$ whenever $x + \nu_j \notin \Z_{\ge 0}^N$.
Here $a_j(x)\,dt$ is the probability that one reaction of channel $j$ occurs in the next small time interval of length $dt$, given the state $x$.
The *chemical master equation* is the system, for all $x \in \Z_{\ge 0}^N$ and $t \ge 0$,
$$\frac{\partial P(x, t)}{\partial t} = \sum_{j=1}^{M} \Big( a_j(x - \nu_j)\, P(x - \nu_j, t) - a_j(x)\, P(x, t) \Big).$$
Here $P(x, t)$ is the probability of the state $x$ at time $t$.
Terms with $x - \nu_j \notin \Z_{\ge 0}^N$ are read as $0$.

## Remarks

It is the forward equation of the [[continuous-time Markov chain|TWQFE0FZZS]] on $\Z_{\ge 0}^N$ that jumps from $x$ to $x + \nu_j$ at rate $a_j(x)$.
For mass-action kinetics, a channel whose reactants are $r_{1j}, \dots, r_{Nj}$ molecules of the species has $a_j(x) = c_j \prod_{i} \binom{x_i}{r_{ij}}$ for a constant $c_j > 0$.
Example: for $A \to \emptyset$ with $a(n) = cn$ and $\nu = -1$, the equation is $\partial_t P(n, t) = c(n+1) P(n+1, t) - cn P(n, t)$.
With $P(n, 0) = 1$ for $n = n_0$, the binomial law $P(n, t) = \binom{n_0}{n} e^{-cnt} (1 - e^{-ct})^{n_0 - n}$ solves it, as a direct differentiation shows.
Non-example: the [[rate equation|TTH05RV6SW]] $d[A]/dt = -k[A]$ describes a deterministic concentration, not a probability distribution over molecule numbers, so it is not a master equation.
When all propensities are affine in $x$, the mean of the solution obeys the corresponding rate equations exactly; for nonlinear propensities it does not in general.
