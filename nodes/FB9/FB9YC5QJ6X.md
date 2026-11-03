---
tag: FB9YC5QJ6X
kind: definition
name: Signaling game
msc: [91A28, 91A27, 91A18]
defines: DNVNS5HNYR
uses: [4Y8AF9H9HA, 2XQ7VWT8KJ, 00NBBSXRQS, 0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Signaling_game
---

## Definition

A finite *signaling game* consists of:

1. two players, the sender $S$ and the receiver $R$;
2. a finite set $T$ of types of the sender and a [[prior|00NBBSXRQS]] [[probability distribution|0DVDCMA2DK]] $p$ on $T$ with $p(t) > 0$ for every $t \in T$;
3. a finite set $M$ of messages and a finite set $A$ of actions of the receiver;
4. payoff functions $u_S, u_R \colon T \times M \times A \to \R$.

The game is played as follows.
A type $t \in T$ is drawn according to $p$, and only the sender observes it.
The sender chooses a message $m \in M$.
The receiver observes $m$, but not $t$, and chooses an action $a \in A$.
The payoffs are $u_S(t, m, a)$ and $u_R(t, m, a)$.
A strategy of the sender is a map from $T$ to $M$, or to distributions on $M$.
A strategy of the receiver is a map from $M$ to $A$, or to distributions on $A$.

## Remarks

A signaling game is an [[extensive-form game|4Y8AF9H9HA]] with a first move of chance, and also a dynamic [[Bayesian game|2XQ7VWT8KJ]] in which only the sender has several types.
Its usual solution concept is perfect Bayesian equilibrium: the receiver's belief after a message is the Bayesian posterior whenever that message is sent with positive probability.

Example: let $T = \set{\text{high}, \text{low}}$ be the ability of a worker, $M = \set{\text{educate}, \text{not}}$ and $A = \set{\text{high wage}, \text{low wage}}$.
Education costs the low type more than the high type, and the employer's payoff is highest when the wage matches the true ability.
All four clauses hold, so this is a signaling game; it is a finite version of Spence's job market model.

Non-example: if the receiver also observes the type $t$ before acting, then the message carries no information that she lacks.
The game is then one of complete information, and it fails the requirement that only the sender observes $t$.
