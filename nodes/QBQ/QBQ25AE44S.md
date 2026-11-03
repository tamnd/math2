---
tag: QBQ25AE44S
kind: definition
name: Featherstone's algorithm
msc: ["70E55", "70E60"]
defines: VPM6Q15C6J
uses: [87RX5SJ7DJ, 062D9KXJB1, WVGTEH6P10]
sources:
  - url: https://en.wikipedia.org/wiki/Featherstone%27s_algorithm
---

## Definition

Let a [[multibody system|87RX5SJ7DJ]] have bodies $1, \ldots, n$ and a fixed base $0$, whose joint graph is a rooted [[tree|062D9KXJB1]].
Let body $i$ be joined to its parent $\lambda(i)$ by joint $i$, with joint coordinates $q_i$, velocities $\dot q_i$ and applied joint forces $\tau_i$.
*Featherstone's algorithm* computes the joint accelerations $\ddot q_1, \ldots, \ddot q_n$ in three passes over the tree.

1. Outward pass: compute the velocity of each body from that of its parent and $\dot q_i$, and its velocity-dependent acceleration terms.
2. Inward pass: compute each body's *articulated-body inertia* and *bias force* from its own inertia and the values of its children.
3. Outward pass: compute $\ddot q_i$ from the parent's acceleration, $\tau_i$ and the articulated quantities of body $i$, then the acceleration of body $i$.

The outward passes go from the base to the leaves, and the inward pass from the leaves to the base.
The articulated-body inertia and bias force describe how body $i$ with all its descendants responds to a force on body $i$.

## Remarks

Each pass does a bounded amount of work per body, so the total cost is $O(n)$.
The quantities are usually written in spatial vector notation, with $6$-dimensional velocities and forces combining the linear and angular parts.

Example: take a single body on one revolute joint to the base.
The inward pass gives just the inertia of the body itself, built from its [[inertia tensor|WVGTEH6P10]].
The last pass reduces to $I\ddot q = \tau + \tau_g$, with $I$ the moment of inertia about the joint axis and $\tau_g$ the torque of gravity about it.

Non-example: a four-bar linkage has a joint graph with a cycle, so there is no tree order of its bodies.
The algorithm does not apply directly; the loop must be cut and then closed by constraint forces.

## Explanations

### L1 human

Featherstone's algorithm solves the forward dynamics of a branching chain of rigid bodies with three sweeps along the chain.
Its cost grows only linearly with the number of bodies.
