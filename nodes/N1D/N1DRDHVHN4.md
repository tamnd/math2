---
tag: N1DRDHVHN4
kind: statement
role: theorem
name: Pollaczek–Khinchine formula
msc: [60K25, 90B22]
uses: [2P6TYP0RBZ, KHRTBP37VD, JN2YME6F4A, 0477R9PYAE]
about: [P64V0HTE78]
sources:
  - url: https://en.wikipedia.org/wiki/Pollaczek%E2%80%93Khinchine_formula
same_as:
  wikidata: Q3726543
  wikipedia: Pollaczek–Khinchine formula
---

## Statement

Consider the M/G/1 queue with first-come first-served service, where arrivals form a Poisson process of rate $\lambda > 0$.
The service times are independent copies of a random variable $S \ge 0$ with $\mathbb{E}[S^2] < \infty$, independent of the arrivals.
Assume $\rho = \lambda \mathbb{E}[S] < 1$.
Let $W_q$ be the stationary waiting time in the queue, before service starts, and let $L$ be the stationary number of customers in the system.
Then:

1. $\displaystyle \mathbb{E}[W_q] = \frac{\lambda \mathbb{E}[S^2]}{2(1 - \rho)}$ and $\displaystyle \mathbb{E}[L] = \rho + \frac{\lambda^2 \mathbb{E}[S^2]}{2(1 - \rho)}$.
2. The [[Laplace–Stieltjes transform|KHRTBP37VD]] of $W_q$ is, for $s > 0$,
$$\mathbb{E}\big[e^{-s W_q}\big] = \frac{(1 - \rho)\, s}{s - \lambda \big(1 - \tilde{G}(s)\big)}, \qquad \tilde{G}(s) = \mathbb{E}\big[e^{-s S}\big].$$

## Remarks

A mean-value proof: an arriving customer waits for the residual service of the customer in service plus the services of those already waiting.
Poisson arrivals see time averages, so the first part has mean $\rho \cdot \mathbb{E}[S^2] / (2\mathbb{E}[S]) = \lambda \mathbb{E}[S^2]/2$.
The second part has mean $\mathbb{E}[L_q] \mathbb{E}[S] = \lambda \mathbb{E}[W_q] \mathbb{E}[S]$ by [[Little's law|JN2YME6F4A]].
Solving gives the mean wait, and $\mathbb{E}[L] = \lambda(\mathbb{E}[W_q] + \mathbb{E}[S])$ by Little's law again.
The transform follows from the embedded Markov chain at departure times.
Writing $\mathbb{E}[S^2] = \mathbb{E}[S]^2 (1 + c_S^2)$, with $c_S^2$ the squared coefficient of variation, gives $\mathbb{E}[W_q] = \frac{\rho}{1 - \rho} \frac{1 + c_S^2}{2} \mathbb{E}[S]$, which grows with the [[variance|0477R9PYAE]] of $S$.
Example: for exponential service of rate $\mu$, $c_S^2 = 1$ and $\mathbb{E}[W_q] = \rho/(\mu(1 - \rho))$, the M/M/1 value; for constant service, $c_S^2 = 0$ and the wait is half as long.
If $\mathbb{E}[S^2] = \infty$ while $\rho < 1$, the queue is still stable but the mean waiting time is infinite.

## Explanations

### L1 human

At a single counter with random arrivals, the average wait depends on how busy the counter is and on how variable the service times are.
The formula makes this exact: the wait blows up as the load $\rho$ approaches $1$, and it is proportional to the mean square of the service time.
Two counters with the same average service time can have very different waits if one of them has more irregular services.

### L2 human

The formula is the basic result on the [[M/G/1 queue|Q3VCF5R06B]], and it is named after Felix Pollaczek and Aleksandr Khinchin.
The factor $(1 + c_S^2)/2$ reappears in [[Kingman's formula|8WT39NFCTP]], which approximates the mean wait of the G/G/1 queue in heavy traffic.
Part 2 determines the whole law of the waiting time and can be inverted numerically or expanded to get higher moments.
