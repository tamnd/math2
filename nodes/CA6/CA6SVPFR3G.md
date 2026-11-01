---
tag: CA6SVPFR3G
kind: definition
name: Coupling from the past
msc: [65C05, 60J10, 60J22]
defines: NZXD2SBY7F
uses: [033TJBZDG0, 0F462493EA, 0KRH5157WP, 0AREFQ9Z65, HTR7J0W66V]
sources:
  - url: https://en.wikipedia.org/wiki/Coupling_from_the_past
---

## Definition

Let $S$ be a finite set and let $P$ be the [[transition matrix|0F462493EA]] of an irreducible and aperiodic [[Markov chain|033TJBZDG0]] on $S$.
Let $\pi$ be its [[stationary distribution|0KRH5157WP]].
Let $\phi \colon S \times [0, 1] \to S$ be an *update function*: if $U$ is [[uniform|0AREFQ9Z65]] on $[0, 1]$, then $P(\phi(x, U) = y) = P(x, y)$ for all $x, y \in S$.
Let $U_{-1}, U_{-2}, \ldots$ be independent and uniform on $[0, 1]$.
For $t \ge 1$ define the map $F_{-t} \colon S \to S$ by
$$F_{-t} = \phi_{-1} \circ \phi_{-2} \circ \cdots \circ \phi_{-t}, \quad \phi_{-k}(x) = \phi(x, U_{-k}).$$
*Coupling from the past* is the algorithm that computes $F_{-t}$ for $t = 1, 2, 4, 8, \ldots$, always with the same $U_{-k}$.
It stops at the first such $t$ for which $F_{-t}$ is constant, and it outputs the common value $F_{-t}(x)$.

## Remarks

If $\tau = \min\set{t : F_{-t} \text{ is constant}}$ is finite almost surely, the output has law exactly $\pi$.
Indeed, $F_{-t} = F_{-\tau} \circ (\phi_{-\tau-1} \circ \cdots \circ \phi_{-t})$ has the same constant value for all $t \ge \tau$, while $F_{-t}(x)$ has law $P^t(x, \cdot)$, which tends to $\pi$.
Example: take a chain that jumps to a fresh sample of $\pi$ at each step, with an update $\phi(x, u)$ that does not depend on $x$.
Then $F_{-1}$ is constant, and the output $\phi(x, U_{-1})$ has law $\pi$.
Non-example: running the [[coupled|HTR7J0W66V]] copies forward from time $0$ and outputting their value at the first meeting time is biased.
Take $S = \set{0, 1}$, $\phi(0, u) = 0$ for $u < 1/2$, $\phi(0, u) = 1$ otherwise, and $\phi(1, u) = 0$.
Then the forward copies always meet at $0$, while $\pi = (2/3, 1/3)$.
If $S$ has a partial order with a top and a bottom element and $\phi(\cdot, u)$ is monotone, it suffices to follow the top and the bottom states.
