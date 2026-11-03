---
tag: ZCV12ZPBG1
kind: definition
name: Boolean network
msc: [92C42, 94C11, 37N25]
defines: FH17G8B4SJ
uses: [0X05GS525E, 7FWX24X5MW, 0KFYGSHHF5]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_network
---

## Definition

Let $n \ge 1$.
A *Boolean network* with $n$ nodes is a map $F = (f_1, \dots, f_n) \colon \set{0, 1}^n \to \set{0, 1}^n$.
Each component $f_i \colon \set{0, 1}^n \to \set{0, 1}$ is a [[Boolean function|0X05GS525E]].
Its *synchronous dynamics* is a sequence of states $x(t) \in \set{0, 1}^n$.
The sequence obeys
$$x(t + 1) = F(x(t)), \qquad t = 0, 1, 2, \dots$$
Its *wiring diagram* is the [[directed graph|0KFYGSHHF5]] with an arc $j \to i$ whenever $f_i$ depends on $x_j$.

## Remarks

Since $\set{0, 1}^n$ has $2^n$ elements, every trajectory is eventually periodic; the periodic orbits are the [[attractors|7FWX24X5MW]] of the network, and fixed points are attractors of period $1$.
Example: $n = 2$, $f_1(x) = x_2$, $f_2(x) = 1 - x_1$ is a Boolean network; from $00$ one gets $01$, $11$, $10$, $00$, so the whole state space is one cycle of length $4$.
Non-example: the update $x_1(t + 1) = \tfrac{1}{2}(x_1(t) + x_2(t))$ is not Boolean, since it can take the value $\tfrac{1}{2}$.
In the *asynchronous* dynamics only one node, chosen by a rule or at random, is updated at each step.
A *random Boolean network* in Kauffman's sense chooses for each node $K$ inputs and a random Boolean function of them.
