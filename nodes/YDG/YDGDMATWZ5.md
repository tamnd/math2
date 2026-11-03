---
tag: YDGDMATWZ5
kind: definition
name: Gillespie algorithm
msc: [65C05, 60J28, "92E20"]
defines: VPJ35XK0A9
uses: [VTE4ZCT4WJ, 0E99F51GVB, 0AREFQ9Z65, TWQFE0FZZS]
sources:
  - url: https://en.wikipedia.org/wiki/Gillespie_algorithm
---

## Definition

Let a chemical system have $M$ reaction channels with state-change vectors $\nu_1, \dots, \nu_M$ and propensity functions $a_1, \dots, a_M$, as in the [[chemical master equation|VTE4ZCT4WJ]].
Let $x_0$ be an initial state and $T > 0$ a final time.
The *Gillespie algorithm* produces a path $t \mapsto x(t)$ on $[0, T]$ as follows.

1. Set $t = 0$ and $x = x_0$.
2. Compute $a_0(x) = \sum_{j=1}^M a_j(x)$. If $a_0(x) = 0$, stop: the state stays $x$ forever.
3. Draw independent random numbers $u_1, u_2$ with the [[uniform distribution|0AREFQ9Z65]] on $(0, 1)$.
4. Set $\tau = \frac{1}{a_0(x)} \ln \frac{1}{u_1}$, so that $\tau$ has the [[exponential distribution|0E99F51GVB]] with rate $a_0(x)$.
5. Let $j$ be the smallest index with $\sum_{k=1}^{j} a_k(x) > u_2\, a_0(x)$, so that $j$ is chosen with probability $a_j(x)/a_0(x)$.
6. If $t + \tau > T$, stop. Otherwise set $t \leftarrow t + \tau$ and $x \leftarrow x + \nu_j$, and return to step 2.

## Remarks

The path is constant between the jump times, and its law is exactly that of the [[continuous-time Markov chain|TWQFE0FZZS]] whose forward equation is the chemical master equation.
The reason is that, from state $x$, the channels fire after independent exponential times with rates $a_j(x)$.
The minimum of these times is exponential with rate $a_0(x)$, and channel $j$ is the first with probability $a_j(x)/a_0(x)$.
Example: for $A \to \emptyset$ with $a_1(n) = cn$, the algorithm waits an exponential time of rate $cn$ and then lowers $n$ by $1$, until $n = 0$.
Non-example: a scheme that advances time by a fixed step $h$ and fires each channel $j$ with probability $a_j(x) h$ is not the Gillespie algorithm.
It is only an approximation, with an error that vanishes as $h \to 0$.
The cost per step grows with the number of reactions per unit time, which motivates approximate methods such as tau-leaping.
