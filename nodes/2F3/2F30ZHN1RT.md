---
tag: 2F30ZHN1RT
kind: statement
role: theorem
name: Darboux's theorem on additive functions bounded on an interval
msc: [39B22]
uses: [KF719SZD5T, 0Q1D85B8G6]
about: [KF719SZD5T]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation
---

## Statement

Let $f \colon \R \to \R$ be an [[additive function|KF719SZD5T]], that is, $f(x + y) = f(x) + f(y)$ for all $x, y \in \R$.
Assume that there are real numbers $a < b$ and $M$ such that $f(x) \le M$ for all $x$ in the [[interval|0Q1D85B8G6]] $(a, b)$.
Then $f(x) = f(1)\, x$ for all $x \in \R$.

## Remarks

Set $c = f(1)$ and $g(x) = f(x) - cx$.
Then $g$ is additive and $g(q) = 0$ for every rational $q$, so $g(x + q) = g(x)$ for all real $x$ and rational $q$.
Every real $x$ has a rational $q$ with $x + q \in (a, b)$, and $g$ is bounded above on $(a, b)$, so $g$ is bounded above on all of $\R$.
If $g(x_0) \ne 0$ for some $x_0$, then $g(n x_0) = n g(x_0)$ or $g(-n x_0) = -n g(x_0)$ grows without bound as $n \to \infty$, a contradiction.
So $g = 0$ and $f(x) = cx$.
The same holds if $f$ is bounded below on an interval, since then $-f$ is bounded above.
Without any bound the conclusion fails: [[additive functions built from a Hamel basis|FFTNS66XG6]] are not linear.

## Explanations

### L1 human

An additive function is either a straight line through the origin or a wild function.
This theorem says that a wild additive function cannot stay below a fixed level even on a tiny interval.
So a single bound on a small piece of the line already forces the function to be linear.

### L2 human

This is the basic regularity criterion for [[Cauchy's functional equation|ZBMEVWN100]].
Continuity at a point, monotonicity on an interval and measurability all imply boundedness on some interval, so they all reduce to this result.
For measurable functions this reduction goes through the Steinhaus theorem; see [[measurable solutions of Cauchy's equation|TWANGP59RB]].
The same idea shows that the graph of a non-linear additive function is [[dense in the plane|MNAWWP9J1X]].
