---
tag: MNAWWP9J1X
kind: statement
role: proposition
name: Density of the graph of a discontinuous additive function
msc: [39B22]
uses: [KF719SZD5T, 0JBJYT69ZV, 0BSJSX7ME2]
about: [KF719SZD5T]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation
---

## Statement

Let $f \colon \R \to \R$ be an [[additive function|KF719SZD5T]], that is, $f(x + y) = f(x) + f(y)$ for all $x, y \in \R$.
Assume that there is no constant $c$ with $f(x) = cx$ for all $x \in \R$.
Then the [[graph|0JBJYT69ZV]] $\set{(x, f(x)) : x \in \R}$ is a [[dense subset|0BSJSX7ME2]] of the plane $\R^2$.

## Remarks

Additivity gives $f(qx) = q f(x)$ for all rational $q$ and real $x$.
Since $f$ is not linear, there are nonzero $x_1, x_2$ with $f(x_1)/x_1 \ne f(x_2)/x_2$.
Then the vectors $v_1 = (x_1, f(x_1))$ and $v_2 = (x_2, f(x_2))$ are linearly independent in $\R^2$.
The graph contains every point $q_1 v_1 + q_2 v_2$ with $q_1, q_2 \in \Q$, because $f(q_1 x_1 + q_2 x_2) = q_1 f(x_1) + q_2 f(x_2)$.
These points are dense in $\R^2$, since $v_1, v_2$ form a basis of $\R^2$ and $\Q$ is dense in $\R$.
A typical instance is the [[coordinate function of a Hamel basis|FFTNS66XG6]].

## Explanations

### L1 human

A line through the origin is a thin set in the plane.
A non-linear additive function is the opposite: its graph comes arbitrarily close to every point of the plane.
So such a function is as far from a drawable curve as possible.

### L2 human

This proposition explains why any mild regularity makes an additive function linear.
A dense graph meets every small rectangle, so the function is unbounded above and below on every interval.
Hence boundedness on one interval, as in [[Darboux's theorem|2F30ZHN1RT]], already rules out the non-linear case.
The proof only uses that $f$ is $\Q$-linear, which every additive function on $\R$ is.
