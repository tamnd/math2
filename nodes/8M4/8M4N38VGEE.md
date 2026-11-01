---
tag: 8M4N38VGEE
kind: definition
name: Quasi-analytic function
msc: ["26E10"]
defines: YF1KAWB5MB
uses: [0BE3QDH73A, 084NGSTWM7, 0JD5ZNW0F4, KV0GW9K7JS, 09RTYYHXKA]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-analytic_function
    locator: Definitions
---

## Definition

Let $a < b$ and let $M = (M_k)_{k \ge 0}$ be a sequence of positive real numbers.
The class $C^M([a, b])$ is the set of [[smooth functions|0BE3QDH73A]] $f \colon [a, b] \to \R$ for which there are constants $A, B > 0$ with
$$\abs{f^{(k)}(x)} \le A B^k M_k \quad \text{for all } k \ge 0 \text{ and all } x \in [a, b].$$
The class $C^M([a, b])$ is *quasi-analytic* if the following holds.
If $f \in C^M([a, b])$ and $f^{(k)}(x_0) = 0$ for some $x_0 \in [a, b]$ and all $k \ge 0$, then $f = 0$ on $[a, b]$.
A *quasi-analytic function* is a function in a quasi-analytic class.

## Remarks

Equivalently, two functions in a quasi-analytic class that have the same derivatives of all orders at one point are equal.
At the endpoints, the [[derivatives|084NGSTWM7]] are one-sided.

Example: $M_k = k!$.
A function with $\abs{f^{(k)}} \le A B^k k!$ on $[a, b]$ is [[analytic|0JD5ZNW0F4]], with Taylor series of radius at least $1/B$ around each point.
If all its derivatives vanish at $x_0$, then it vanishes near $x_0$, and by moving along $[a, b]$ in steps it vanishes everywhere.
So $C^M([a, b])$ is quasi-analytic.

Non-example: $M_k = (k!)^2$.
Here $\sum_{k \ge 1} M_{k-1}/M_k = \sum_{k \ge 1} 1/k^2$ converges, so by the [[Denjoy–Carleman theorem|KV0GW9K7JS]] the class is not quasi-analytic.
It contains a nonzero function that vanishes on a subinterval, and all its derivatives vanish at the points of that subinterval.
