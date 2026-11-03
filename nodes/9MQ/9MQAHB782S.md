---
tag: 9MQAHB782S
kind: definition
name: Fractional programming
msc: [90C32]
defines: NQ52QHDMMV
uses: [02AS45T3H9, 07GR3TNW4H]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_programming
---

## Definition

Let $S \subseteq \R^n$ be a nonempty set and let $f, g \colon S \to \R$ be functions with $g(x) > 0$ for all $x \in S$.
The *fractional program* with these data is: maximise $f(x)/g(x)$ over $x \in S$.
It is a *concave fractional program* if:

1. $S$ is a [[convex set|02AS45T3H9]];
2. $f$ is concave and $f(x) \ge 0$ for all $x \in S$;
3. $g$ is [[convex|07GR3TNW4H]] on $S$.

*Fractional programming* is the study and solution of such problems.

## Remarks

Example: $S = [0, 2]$, $f(x) = x$ and $g(x) = 1 + x^2$.
Here $g > 0$ on $S$, $S$ is convex, $f$ is linear and nonnegative on $S$, and $g$ is convex, so this is a concave fractional program.
Since $(1 + x^2) - 2x = (1 - x)^2 \ge 0$, the ratio is at most $1/2$, with equality at $x = 1$.

Non-example: $S = [0, 2]$, $f(x) = x$ and $g(x) = x - 1$ do not define a fractional program, because $g(1) = 0$ violates $g > 0$ on $S$.

Dinkelbach's criterion: suppose that $\max_{x \in S} \big(f(x) - q\, g(x)\big)$ is attained for every $q \in \R$, and let $F(q)$ be this maximum.
Then $x^* \in S$ maximises $f/g$ if and only if $F(q^*) = 0$ for $q^* = f(x^*)/g(x^*)$.
For a concave fractional program, each $F(q)$ with $q \ge 0$ is the value of a convex problem.
