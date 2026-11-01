---
tag: 5CVYTHWY96
kind: definition
name: Algebraic independence
msc: [12F20]
defines: KV4PT6KW10
uses: [0WQ1A8SHTZ, 0Q9EZS90GY, 00SW8B91E7, 0EVHJFTG9Z, 079EGSD32Y]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_independence
---

## Definition

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]] and let $S \subseteq L$.
The set $S$ is *algebraically independent over $K$* if, for every $n \ge 1$, all distinct $s_1, \dots, s_n \in S$ and every nonzero polynomial $f \in K[x_1, \dots, x_n]$, one has $f(s_1, \dots, s_n) \ne 0$.
Otherwise $S$ is *algebraically dependent over $K$*.

## Remarks

Equivalently, the evaluation map from the [[polynomial ring|0Q9EZS90GY]] $K[x_s : s \in S]$ to $L$ that sends $x_s$ to $s$ is injective.
A one-element set $\set{s}$ is algebraically independent if and only if $s$ is [[transcendental|00SW8B91E7]] over $K$.
Example: in $K(x, y)$, the set $\set{x, y}$ is independent, since a polynomial $f(x, y)$ that is zero as an element of $K(x, y)$ is the zero polynomial.
Example: $\set{\pi}$ is independent over $\Q$, because $\pi$ is a [[transcendental number|079EGSD32Y]].
Non-example: $\set{\pi, \pi^2}$ is dependent over $\Q$, since $f(x_1, x_2) = x_2 - x_1^2$ is nonzero and vanishes at $(\pi, \pi^2)$.
Algebraic independence implies [[linear independence|0EVHJFTG9Z]] over $K$, by taking $f$ linear; the converse fails, as $\set{1, \pi}$ shows.
