---
tag: 8NXV1W4Y5Q
kind: definition
name: Moran process
msc: [92D15, 60J10]
defines: A9M7VKRRV9
uses: [033TJBZDG0]
sources:
  - url: https://en.wikipedia.org/wiki/Moran_process
---

## Definition

Let $N \ge 2$ be the population size, and consider two types $A$ and $B$ with fitnesses $r > 0$ and $1$.
The *Moran process* is the [[Markov chain|033TJBZDG0]] $(X_t)_{t \ge 0}$ on $\set{0, 1, \dots, N}$, where $X_t$ is the number of individuals of type $A$, with the following step.

1. One individual is chosen to reproduce, with probability proportional to its fitness.
2. Independently, one individual is chosen uniformly at random to die.
3. The offspring, of the same type as its parent, takes the place of the individual that died.

So, for $0 < i < N$, the transition probabilities are
$$P(i \to i + 1) = \frac{r i}{r i + N - i} \cdot \frac{N - i}{N}, \qquad P(i \to i - 1) = \frac{N - i}{r i + N - i} \cdot \frac{i}{N},$$
and $P(i \to i) = 1 - P(i \to i + 1) - P(i \to i - 1)$.
The process is *neutral* when $r = 1$.

## Remarks

The states $0$ and $N$ are absorbing.
The ratio $P(i \to i - 1) / P(i \to i + 1)$ equals $1/r$ for every $0 < i < N$.
This gives the fixation probability of $A$ from state $i$:
$$\frac{1 - r^{-i}}{1 - r^{-N}} \quad (r \ne 1), \qquad \frac{i}{N} \quad (r = 1).$$

Example: for $N = 2$, $r = 2$ and $X_t = 1$, one gets $P(1 \to 2) = (2/3)(1/2) = 1/3$ and $P(1 \to 0) = (1/3)(1/2) = 1/6$.
The fixation probability from state $1$ is $(1 - 1/2)/(1 - 1/4) = 2/3$, which equals $(1/3)/(1/3 + 1/6)$.

Non-example: a process that replaces the whole population at once, as in the [[Wright–Fisher model|SR4F169EKF]], is not a Moran process, since $X_t$ can jump by more than $1$.

In the continuous-time version, each individual reproduces at a rate equal to its fitness, and the jump chain is the same.
