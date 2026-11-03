---
tag: AG9ZVFQ1WW
kind: definition
name: Wang–Landau algorithm
msc: [82M31, 65C05]
defines: M70E3VNB19
uses: [DR0E829VX6, GYNMZ9201M, R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Wang_and_Landau_algorithm
---

## Definition

Let $S$ be a finite set of configurations, and let $H \colon S \to \mathcal{E}$ be an energy function onto a finite set $\mathcal{E}$.
The density of states is $g(E) = \abs{\set{\sigma \in S : H(\sigma) = E}}$.
Fix a symmetric proposal rule on $S$, a flatness threshold $\theta \in (0, 1)$ and a final tolerance $\epsilon > 0$.
The *Wang–Landau algorithm* keeps an estimate $\ln \tilde g(E)$ and a histogram $h(E)$ for $E \in \mathcal{E}$, and a modification factor $\ln f$.

1. Start with $\ln \tilde g(E) = 0$ and $h(E) = 0$ for all $E$, $\ln f = 1$, and any configuration $\sigma$.
2. Propose $\sigma'$ from $\sigma$ and accept it with probability $\min\big(1, \tilde g(H(\sigma)) / \tilde g(H(\sigma'))\big)$.
3. After each proposal, let $E$ be the energy of the current configuration, and increase $\ln \tilde g(E)$ by $\ln f$ and $h(E)$ by $1$.
4. When $h$ is flat, that is, $h(E) \ge \theta \cdot \frac{1}{\abs{\mathcal{E}}} \sum_{E'} h(E')$ for all $E$, reset $h$ to $0$ and replace $\ln f$ by $\frac12 \ln f$.
5. Stop when $\ln f < \epsilon$; the output is $\tilde g$, an estimate of $g$ up to a constant factor.

## Remarks

With a fixed $\tilde g$, the walk of clause 2 is at energy $E$ with long-run probability proportional to $g(E) / \tilde g(E)$.
So if $\tilde g = g$, it visits each energy level equally often.
The updates of clause 3 push $\tilde g$ towards $g$, and the shrinking factor $f$ makes the corrections finer.
The constant is fixed by a known value, such as $\sum_E g(E) = \abs{S}$ or the number of ground states.
Example: run the method for the [[Ising model|R0KGM32QN6]] on a finite graph.
Then the partition function at every inverse temperature $\beta$ is estimated by $\sum_E \tilde g(E) e^{-\beta E}$, and this gives the [[Boltzmann distribution|GYNMZ9201M]] of the energy.
Non-example: with $\ln f$ kept fixed, the estimate never converges, because each visit changes $\tilde g$ by a fixed amount and the statistical error stays of order $\ln f$.
The method is not a Markov chain with a fixed stationary distribution, since the weights change during the run.
With the halving schedule the error can saturate.
A schedule in which $\ln f$ decreases like $1/t$ in the late stage is used to avoid this.

## Explanations

### L1 human

The walk avoids energies it has already seen often, so it ends up visiting every energy.
The record of how much it had to penalize each energy is the estimate of how many states that energy has.
