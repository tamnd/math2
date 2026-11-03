---
tag: ZPYE0W7YYV
kind: definition
name: Switched system
msc: [93C30, 34A38]
defines: 7RFWKNDQ67
uses: [1EW58ZYR8Y, 0NT64JV96A, 0299VCW1TH, 0AW1E6YTJY]
sources:
  - url: https://en.wikipedia.org/wiki/Hybrid_system
---

## Definition

Let $N \ge 1$ and let $f_1, \ldots, f_N \colon \R^n \to \R^n$ be locally [[Lipschitz|0AW1E6YTJY]] [[vector fields|0299VCW1TH]], the *subsystems*.
A *switching signal* is a piecewise constant function $\sigma \colon [0, \infty) \to \set{1, \ldots, N}$ that is continuous from the right.
It must have finitely many discontinuities in every bounded interval, and these are the *switching times*.
The *switched system* defined by $f_1, \ldots, f_N$ is the family of [[ordinary differential equations|0NT64JV96A]]
$$x'(t) = f_{\sigma(t)}(x(t)),$$
one for each switching signal $\sigma$ in a given class.
A *solution* for $\sigma$ is a continuous function $x$ that satisfies the equation on every interval between consecutive switching times.

## Remarks

The class of switching signals may be all of them (arbitrary switching), or those with a minimum time between switches (dwell time).
It may also consist of signals given by a rule $\sigma(t) = \phi(x(t))$ that depends on the state.
A *switched linear system* has $f_i(x) = A_i x$ for matrices $A_i \in \R^{n \times n}$.
A switched system is a special [[hybrid system|1EW58ZYR8Y]] with no resets: the state is continuous at the switching times.
If all subsystems share a common Lyapunov function, the switched system is stable under arbitrary switching.

Example: $n = 1$, $f_1(x) = -x$ and $f_2(x) = -2x$.
For any switching signal, the solution is $x(t) = x(0) \exp\big(-\int_0^t a_{\sigma(s)}\, ds\big)$ with $a_1 = 1$, $a_2 = 2$, so $\abs{x(t)} \le \abs{x(0)} e^{-t} \to 0$.

Non-example: the bouncing ball, whose velocity jumps from $v$ to $-cv$ at each impact, is a hybrid system.
It is not a switched system in this sense, because its state is not continuous at the switching times.

Even when every $A_i$ has all eigenvalues in the open left half-plane, a switched linear system can have unbounded solutions for suitable switching signals.
