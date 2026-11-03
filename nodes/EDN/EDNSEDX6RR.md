---
tag: EDNSEDX6RR
kind: definition
name: Action
msc: [70H25, 70H30, 49S05]
defines: T0WAGV4KP4
uses: [47JMCBM3VJ, 1EQM0DJ4NC]
sources:
  - url: https://en.wikipedia.org/wiki/Action_(physics)
---

## Definition

Let $(Q, L)$ be a [[Lagrangian system|47JMCBM3VJ]] with configuration space $Q$ and Lagrangian $L(t, q, \dot q)$.
Fix times $t_0 < t_1$.
The *action* of a $C^1$ path $q \colon [t_0, t_1] \to Q$ is
$$S[q] = \int_{t_0}^{t_1} L\big(t, q(t), \dot q(t)\big)\, dt.$$
So $S$ is a [[functional|1EQM0DJ4NC]] on the set of paths in $Q$ over $[t_0, t_1]$.

## Remarks

Another standard quantity is the *abbreviated action* $S_0[q] = \int \sum_i p_i \, dq_i$, with $p_i = \partial L / \partial \dot q_i$, used in Maupertuis's principle.
In physics the action is measured in joule-seconds, the unit of Planck's constant.

Example: a free particle of mass $m$ on the line, $L = \tfrac12 m\dot q^2$, moving from $q(0) = 0$ to $q(1) = a$.
The path $q(t) = at$ has action $\int_0^1 \tfrac12 m a^2\, dt = \tfrac12 m a^2$.
The path $q(t) = at^2$ has action $\int_0^1 \tfrac12 m (2at)^2\, dt = \tfrac23 m a^2$, which is larger.

Non-example: the Lagrangian $L$ itself is not the action; it is a function of one instant, while the action depends on a whole path.

## Explanations

### L1 human

The action of a path is the time integral of the Lagrangian along it.
It is one number for the whole path, and comparing it over all paths singles out the true motion.
