---
tag: SD649DT8VX
kind: definition
name: Maximum and minimum
msc: [26A06, 49K05]
defines: 5X1YMSR204
uses: [0XHDTE5YMZ, 0Z7HDDXX3X, 0BTMQ04556, 04CPG9K1C4, 0WS1A8E2P9]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_and_minimum
    locator: Definition
---

## Definition

Let $D$ be a nonempty set, let $f \colon D \to \R$ be a [[function|0XHDTE5YMZ]], and let $a \in D$.

1. The function $f$ attains its *maximum* at $a$ if $f(x) \le f(a)$ for all $x \in D$. Then $f(a)$ is the *maximum value* of $f$, written $\max_{x \in D} f(x)$.
2. The function $f$ attains its *minimum* at $a$ if $f(x) \ge f(a)$ for all $x \in D$. Then $f(a)$ is the *minimum value* of $f$, written $\min_{x \in D} f(x)$.
3. A point $a$ as in 1 or 2 is a *global extremum*, or *absolute extremum*, of $f$.

## Remarks

The maximum value of $f$ is the [[greatest element|0Z7HDDXX3X]] of the image $f(D)$, when it exists.
Then it equals the [[supremum|0BTMQ04556]] of $f(D)$, and the supremum is attained.
The maximum value is unique, but it can be attained at several points.
For $D \subseteq \R^n$, every global extremum is a [[local extremum|04CPG9K1C4]].

Example: $f(x) = x^2$ on $D = [-1, 2]$ attains its maximum at $a = 2$.
Indeed, for $x \in [-1, 2]$ one has $\abs{x} \le 2$, so $x^2 \le 4 = f(2)$.

Non-example: $f(x) = x$ on $D = (0, 1)$ has no maximum.
For each $a \in (0, 1)$, the point $x = (a + 1)/2$ lies in $D$ and $f(x) > f(a)$.
The supremum of $f(D)$ is $1$, but it is not a value of $f$.
The [[extreme value theorem|0WS1A8E2P9]] gives a maximum and a minimum for every continuous function on a closed bounded interval.
