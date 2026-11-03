---
tag: 5QKF6AMKDX
kind: definition
name: Cheap talk
msc: [91A28, 91A27]
defines: RYQPF59M3X
uses: [DNVNS5HNYR, 0DVDCMA2DK, RG94E9CBQJ]
sources:
  - url: https://en.wikipedia.org/wiki/Cheap_talk
---

## Definition

Let $T$, $M$, $A$, $p$, $u_S$ and $u_R$ be the types, messages, actions, prior and payoffs of a [[signaling game|DNVNS5HNYR]].
It is a *cheap talk game* if the payoffs do not depend on the message.
That is, there are functions $v_S, v_R \colon T \times A \to \R$ with $u_S(t, m, a) = v_S(t, a)$ and $u_R(t, m, a) = v_R(t, a)$ for all $t \in T$, $m \in M$ and $a \in A$.
The sets $T$ and $A$ may be infinite, for example intervals of $\R$, with $p$ a [[probability distribution|0DVDCMA2DK]] on $T$.

## Remarks

Suppose the receiver has a best response to the prior.
Then the game has a *babbling* equilibrium: the sender's message does not depend on her type, and the receiver ignores it and plays a best response to the prior.
This is a [[perfect Bayesian equilibrium|RG94E9CBQJ]] with beliefs equal to the prior after every message.

Example: in the model of Crawford and Sobel, $T = A = [0, 1]$, the type is uniform on $[0, 1]$, $v_R(t, a) = -(a - t)^2$ and $v_S(t, a) = -(a - t - b)^2$ with a bias $b > 0$.
The payoffs do not depend on the message, so this is a cheap talk game.
In every equilibrium, $[0, 1]$ is split into finitely many intervals and the sender in effect reveals only which interval contains her type.
The largest possible number of intervals tends to infinity as $b \to 0$.

Non-example: in Spence's job market model, education is a costly message that lowers the worker's payoff.
So $u_S$ depends on the message, and the model is a signaling game but not a cheap talk game.
