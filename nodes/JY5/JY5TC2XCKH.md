---
tag: JY5TC2XCKH
kind: definition
name: Multiply transitive group action
msc: [20B20, 20B22]
defines: BDJ1AX4XBB
uses: [0WCY42EV9V, 02GK6HZYBT, 0AYMP41THN, 0515A6D2Y1, 0Z5905Q73D, 0ZXZ82FTX2, Y10S0751KG, T1KR4KPX8P]
sources:
  - url: https://en.wikipedia.org/wiki/Multiply_transitive_group_action
---

## Definition

Let a group $G$ [[act|0WCY42EV9V]] on a set $\Omega$, and let $k$ be a positive integer with $k \le \abs{\Omega}$.
The action is *$k$-transitive* if for all $k$-tuples $(x_1, \dots, x_k)$ and $(y_1, \dots, y_k)$ of pairwise distinct elements of $\Omega$ there is $g \in G$ with $g x_i = y_i$ for $i = 1, \dots, k$.
The action is *sharply $k$-transitive* if, moreover, this element $g$ is unique for all such pairs of $k$-tuples.

## Remarks

A $1$-transitive action is a [[transitive action|02GK6HZYBT]].
A $k$-transitive action is $j$-transitive for every $j \le k$.
For $\abs{\Omega} \ge 2$, an action is $2$-transitive if and only if it is transitive and the [[stabiliser|0AYMP41THN]] $G_\omega$ of one point $\omega$ is transitive on $\Omega \setminus \set{\omega}$.

Example: the [[symmetric group|0515A6D2Y1]] $S_n$ is $n$-transitive on $\set{1, \dots, n}$, since any bijection between two orderings of distinct points extends to a permutation.
For $n \ge 3$, the [[alternating group|0Z5905Q73D]] $A_n$ is $(n-2)$-transitive.
Indeed, let $\sigma \in S_n$ do the job, and let $\tau$ swap the two points not among $y_1, \dots, y_{n-2}$.
Then $\tau \sigma$ also does the job, and one of $\sigma$ and $\tau \sigma$ is even.
For a [[finite field|0ZXZ82FTX2]] $\F_q$, the maps $x \mapsto ax + b$ with $a \ne 0$ act sharply $2$-transitively on $\F_q$.

Non-example: the eight symmetries of a square, acting on its corners $1, 2, 3, 4$ in cyclic order.
The action is transitive, but no symmetry sends the pair $(1, 2)$ of neighbouring corners to the pair $(1, 3)$ of opposite corners, so it is not $2$-transitive.

Each $2$-transitive action is [[primitive|Y10S0751KG]].
Camille Jordan showed that for $k \ge 4$ the only finite sharply $k$-transitive groups are $S_k$, $S_{k+1}$, $A_{k+2}$, and the [[Mathieu groups|T1KR4KPX8P]] $M_{11}$ for $k = 4$ and $M_{12}$ for $k = 5$.
