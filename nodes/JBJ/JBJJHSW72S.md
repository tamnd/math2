---
tag: JBJJHSW72S
kind: definition
name: Hybrid system
msc: [34A38, 93C30]
defines: 1EW58ZYR8Y
uses: [0299VCW1TH, 0NT64JV96A, 03CPD1HGF3]
sources:
  - url: https://en.wikipedia.org/wiki/Hybrid_system
---

## Definition

Several formal models of hybrid systems are in use; a common one is the hybrid automaton.
A *hybrid automaton* with continuous state space $\R^n$ consists of the following data.

1. A finite set $Q$ of discrete states, called modes.
2. For each mode $q \in Q$, a [[vector field|0299VCW1TH]] $f_q \colon \R^n \to \R^n$ and a set $D_q \subseteq \R^n$, the domain of $q$.
3. A set $E \subseteq Q \times Q$ of edges, that is, allowed mode switches.
4. For each edge $e \in E$, a guard $G_e \subseteq \R^n$ and a reset map $R_e$ that gives a nonempty set $R_e(x) \subseteq \R^n$ for each $x \in G_e$.
5. A set $\mathrm{Init} \subseteq Q \times \R^n$ of initial states.

An *execution* is a finite or infinite sequence of intervals $[\tau_0, \tau_0'], [\tau_1, \tau_1'], \ldots$ with $\tau_i' = \tau_{i+1}$.
On the interval $[\tau_i, \tau_i']$ it has a mode $q_i$ and a curve $x_i$ that solves $x' = f_{q_i}(x)$ and stays in $D_{q_i}$.
The start satisfies $(q_0, x_0(\tau_0)) \in \mathrm{Init}$.
At each switch, $e = (q_i, q_{i+1}) \in E$, $x_i(\tau_i') \in G_e$ and $x_{i+1}(\tau_{i+1}) \in R_e(x_i(\tau_i'))$.
A *hybrid system* is a system modelled by such data, or by an equivalent formalism with flows and jumps.

## Remarks

The discrete part alone is a finite-state machine, and the continuous part in one mode is an [[ordinary differential equation|0NT64JV96A]].
Example: the bouncing ball has one mode and the state $x = (h, v)$ of height and velocity.
Its vector field is $f(h, v) = (v, -g)$ with $g > 0$, and its domain is $h \ge 0$.
It has one edge from the mode to itself, with guard $\set{h = 0, v \le 0}$ and reset $R(0, v) = \set{(0, -c v)}$, where $0 \le c < 1$.
Between impacts the ball follows a parabola, and each impact multiplies its speed by $c$.
For $0 < c < 1$ the impacts accumulate at a finite time; this Zeno behaviour has no analogue for ordinary differential equations.
Non-example: data with infinitely many modes, one for each integer, fail clause 1, which asks for a finite set of modes; such models need a more general framework.
