---
tag: 5Y9D4SWRCF
kind: example
name: A bootstrap without continuity fails
msc: ["00A35", "26A15"]
topics: [MEKKHHQTKB]
audience: ug3
not_instance_of:
  - target: YKA0ADKYFR
    note: the function is not continuous, so the set where the bootstrap bound holds is not closed and the argument does not close
uses: [YKA0ADKYFR, 7094T3DFW2, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: lead section
---

## Example

Let $A = 1$ and $\varepsilon = \tfrac18$, so $4 \varepsilon A = \tfrac12 < 1$.
Define $u \colon [0, 2] \to [0, \infty)$ by
$$u(t) = 0 \text{ for } 0 \le t < 1, \qquad u(t) = 7 \text{ for } 1 \le t \le 2.$$
We check that $u$ satisfies every hypothesis of [[the continuity argument|7094T3DFW2]] except continuity, and that its conclusion fails.

1. $u(0) = 0 \le 1 = A$.
2. Multiplying by $8$, the inequality $u \le 1 + \tfrac18 u^2$ becomes $u^2 - 8u + 8 \ge 0$.
3. The roots of $r^2 - 8r + 8$ are $4 \pm 2\sqrt2$, so the inequality holds exactly when $u \le 4 - 2\sqrt2 \approx 1.172$ or $u \ge 4 + 2\sqrt2 \approx 6.828$.
4. For $t < 1$, $u(t) = 0$ and $0 - 0 + 8 = 8 \ge 0$.
5. For $t \ge 1$, $u(t) = 7$ and $49 - 56 + 8 = 1 \ge 0$.
6. The conclusion would be $u(t) \le 2A = 2$, and it fails on $[1, 2]$, where $u = 7$.
7. The closed step breaks: $S = \{ t : u(t) \le 2 \} = [0, 1)$ is non-empty and open in $[0, 2]$, but the limit $1$ of the points $1 - \tfrac1n \in S$ is not in $S$.
8. The cause is that $u$ is not [[continuous|0X3WGX95FE]] at $1$: $u(1 - \tfrac1n) = 0$ for each $n$, while $u(1) = 7$.

## Remarks

The inequality $u \le A + \varepsilon u^2$ alone does not bound $u$.
It allows a lower range $[0, 4 - 2\sqrt2]$ and an upper range $[4 + 2\sqrt2, \infty)$.
[[Bootstrapping|YKA0ADKYFR]] works because a continuous $u$ cannot pass from the lower range to the upper range without a value in the forbidden zone between them.
A jump avoids that zone, and any value $c \ge 4 + 2\sqrt2$ in place of $7$ gives the same failure.

In applications, continuity in time comes from the local existence theorem.
A proof by bootstrapping must cite it, because it is the only reason the argument closes.

## Explanations

### L1 human

A rule says that a quantity is either small, at most about $1.17$, or large, at least about $6.83$.
A quantity that changes smoothly and starts small stays small, because it cannot cross the gap between the two ranges.
But a quantity that may jump can leap from $0$ to $7$ in one moment, and the rule is still true at each time.
So the rule alone does not keep the quantity small.

### L2 human

We compare the jump with a continuous function that tries to reach $7$.

1. Let $v(t) = 7t$ on $[0, 1]$, continuous with $v(0) = 0$ and $v(1) = 7$.
2. At $t = \tfrac14$, $v = 1.75$ and $1.75^2 - 8 \cdot 1.75 + 8 = 3.0625 - 14 + 8 = -2.9375 < 0$.
3. So $v$ violates the hypothesis $v \le 1 + \tfrac18 v^2$ at $t = \tfrac14$.
4. By the [[intermediate value theorem|00KAFBR32E]], every continuous function from $0$ to $7$ takes the value $2$, where the hypothesis fails, since $4 - 16 + 8 = -4 < 0$.

This non-example locates the role of continuity in a bootstrap proof.
Watch out: the inequality has the form "$u$ is at most something", yet it does not bound $u$ by itself.
