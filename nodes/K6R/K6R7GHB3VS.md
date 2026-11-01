---
tag: K6R7GHB3VS
kind: statement
role: theorem
name: Reflection principle
msc: [60J65]
uses: [552AWX3QXN, WND87FBAKC, 05AQE0QR0D]
about: [22735FGJV6]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_principle_(Wiener_process)
same_as:
  wikidata: Q7307248
  wikipedia: Reflection principle (Wiener process)
---

## Statement

Let $(W_t)_{t \ge 0}$ be a [[Wiener process|552AWX3QXN]], let $a > 0$, and let $\tau_a = \inf\set{t \ge 0 : W_t = a}$ be the first hitting time of $a$, a [[stopping time|WND87FBAKC]].

1. The process $\widetilde{W}$ defined by $\widetilde{W}_t = W_t$ for $t \le \tau_a$ and $\widetilde{W}_t = 2a - W_t$ for $t > \tau_a$ is again a Wiener process.
2. For every $t > 0$,
$$P\Bigl(\sup_{0 \le s \le t} W_s \ge a\Bigr) = 2\, P(W_t \ge a).$$

## Remarks

Part 1 follows from the strong Markov property: after $\tau_a$, the process $W_{\tau_a + s} - a$ is a Wiener process independent of the past, and so is its negative.
For part 2, the event $\{\sup_{s \le t} W_s \ge a\}$ equals $\{\tau_a \le t\}$, and it splits into $\{W_t \ge a\}$ and $\{\tau_a \le t, W_t < a\}$.
By part 1 the second event has the same probability as $\{\widetilde{W}_t > a\} = \{W_t > a\}$, and $P(W_t = a) = 0$.
As a consequence, $\sup_{s \le t} W_s$ has the same law as $\abs{W_t}$, and $P(\tau_a \le t) = 2\bigl(1 - \Phi(a/\sqrt{t})\bigr)$, where $\Phi$ is the standard normal distribution function.
Differentiating gives the density $\frac{a}{\sqrt{2\pi t^3}} e^{-a^2/(2t)}$ of $\tau_a$, which shows $\tau_a < \infty$ almost surely but $E[\tau_a] = \infty$.

## Explanations

### L1 human

Once a Brownian path touches the level $a$, it is equally likely to end above or below $a$.
Reflecting the rest of the path in the line $y = a$ turns one kind of path into the other.
So the chance that the path ever reaches $a$ by time $t$ is twice the chance that it ends above $a$ at time $t$.

### L2 human

The principle gives the joint law of $W_t$ and its running maximum, and the law of first passage times.
These are used to price barrier options and to study boundary crossing in sequential statistics.
The same reflection idea for simple random walks gives the ballot theorem and counts of lattice paths.
