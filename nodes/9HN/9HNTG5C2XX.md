---
tag: 9HNTG5C2XX
kind: definition
name: Perturbation theory of linear operators
msc: [47A55, 47A10]
defines: JTZK8DZ257
uses: [06GZ956657, KRJX5RA0PW]
sources:
  - url: https://en.wikipedia.org/wiki/Perturbation_theory
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]] and let $T$ be a linear [[operator|KRJX5RA0PW]] in $X$ with domain $D(T)$.
A linear operator $V$ in $X$ is *relatively bounded with respect to $T$*, or *$T$-bounded*, if:

1. $D(T) \subseteq D(V)$, and
2. there are constants $a, b \ge 0$ with $\norm{Vx} \le a \norm{x} + b \norm{Tx}$ for all $x \in D(T)$.

The infimum of the numbers $b$ for which some $a$ makes clause 2 hold is the *$T$-bound* of $V$.
The operator $T + V$ with domain $D(T)$ is a *perturbation* of $T$.
Perturbation theory of linear operators studies which properties of $T$ pass to $T + V$, or to $T + \kappa V$ for small $\kappa$.

## Remarks

Example: every bounded operator $V$ on $X$ is $T$-bounded with $T$-bound $0$, since $\norm{Vx} \le \norm{V}\norm{x}$.
Non-example: on $L^2(\R)$, let $T = -i \, d/dx$ with domain the Sobolev space $H^1(\R)$, and let $V = -d^2/dx^2$ with domain $H^2(\R)$.
Clause 1 fails, since $H^1(\R)$ is not contained in $H^2(\R)$.

A basic result is the Kato–Rellich theorem.
If $T$ is [[self-adjoint|0NEGN5CRSC]] on a Hilbert space and $V$ is symmetric and $T$-bounded with $T$-bound less than $1$, then $T + V$ is self-adjoint on $D(T)$.
Another is [[Weyl's theorem|X9XRGMDCQZ]]: a compact perturbation does not change the [[essential spectrum|FRZG0E15SK]] of a self-adjoint operator.
