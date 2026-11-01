---
tag: W96WPDEA6A
kind: definition
name: Stopping time
msc: [60G40, 60G05]
defines: WND87FBAKC
uses: [HNK1Y62G7V, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Stopping_time
---

## Definition

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \in T}, P)$ be a probability space with a [[filtration|HNK1Y62G7V]], where $T \subseteq [0, \infty)$, for example $T = \N$ or $T = [0, \infty)$.
A *stopping time* with respect to $(\mathcal{F}_t)$ is a map $\tau \colon \Omega \to T \cup \set{\infty}$ such that
$$\set{\omega \in \Omega : \tau(\omega) \le t} \in \mathcal{F}_t \quad \text{for every } t \in T.$$

## Remarks

In discrete time, $T = \N$, the condition is equivalent to $\set{\tau = n} \in \mathcal{F}_n$ for every $n \in \N$, since $\set{\tau = n} = \set{\tau \le n} \setminus \set{\tau \le n - 1}$ and $\set{\tau \le n} = \bigcup_{k \le n} \set{\tau = k}$.
The value $\infty$ means that the event never happens.

Example: let $(S_n)_{n \in \N}$ be a [[random walk|04VZE3FZXF]] with natural filtration $\mathcal{F}_n = \sigma(S_0, \dots, S_n)$, let $a \in \R$, and let $\tau = \min\set{n : S_n \ge a}$, with $\min \emptyset = \infty$.
Then $\set{\tau \le n} = \bigcup_{k \le n} \set{S_k \ge a} \in \mathcal{F}_n$, so $\tau$ is a stopping time.

Non-example: with the same walk started at $S_0 = 0$ and with steps $\pm 1$, let $N \ge 2$ and $\sigma = \max\set{n \le N : S_n = 0}$, the last visit to $0$ before time $N$.
The event $\set{\sigma \le 0}$ is the event that $S_n \ne 0$ for $1 \le n \le N$, which depends on steps after time $0$ and is not in $\mathcal{F}_0 = \set{\emptyset, \Omega}$.
So $\sigma$ is not a stopping time.

Constant times are stopping times, and the minimum and the maximum of two stopping times are stopping times.
The *$\sigma$-algebra of the past* at $\tau$ is $\mathcal{F}_\tau = \set{A \in \mathcal{F} : A \cap \set{\tau \le t} \in \mathcal{F}_t \text{ for all } t \in T}$.
