---
tag: TAHM74ZNWB
kind: statement
role: theorem
name: Abian–Brown theorem
msc: [06A06, 47H10]
uses: [0QV2JS9RJ3, 0S8FE7ZMFM, 0R3H5PANRQ, 0A7KV2WB7A, DBD64TH52D]
about: [DBD64TH52D]
sources:
  - url: https://en.wikipedia.org/wiki/Knaster%E2%80%93Tarski_theorem
---

## Statement

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]] in which every nonempty [[chain|0S8FE7ZMFM]] has a [[supremum|0R3H5PANRQ]].
Let $f \colon P \to P$ be a [[monotone|0A7KV2WB7A]] map, and let $a \in P$ satisfy $a \le f(a)$.
Then $f$ has a fixed point $p$ with $a \le p$.
Moreover, $p$ can be chosen as the least element of the set $\set{x \in P : f(x) = x \text{ and } a \le x}$.

## Remarks

Proof idea: define $x_0 = a$, $x_{\alpha + 1} = f(x_\alpha)$, and $x_\lambda = \sup_{\alpha < \lambda} x_\alpha$ at limit ordinals $\lambda$.
By transfinite induction, $(x_\alpha)$ is increasing and each $x_\alpha$ satisfies $x_\alpha \le f(x_\alpha)$, so the suprema exist.
The sequence cannot be strictly increasing for all ordinals, since $P$ is a set, so $x_{\alpha + 1} = x_\alpha$ for some $\alpha$, and $p = x_\alpha$ is a fixed point.
If $q$ is a fixed point with $a \le q$, induction gives $x_\alpha \le q$ for all $\alpha$, so $p$ is the least such fixed point.
The theorem contains the existence part of the [[Knaster–Tarski theorem|RHXP3HA64M]]: in a complete lattice, take $a$ to be the least element.
The hypothesis $a \le f(a)$ is needed.
On the two-element antichain $\set{a, b}$, every nonempty chain is a single point, and the swap of $a$ and $b$ is monotone and has no fixed point.

## Explanations

### L1 human

If a monotone rule moves some point $a$ upward, keep applying it.
The points climb, and whenever the climb runs through infinitely many steps, jump to the top of what has been reached.
Because every chain has a top, the climb never gets stuck, and since there are only so many points it must stop at a point that the rule fixes.
This fixed point is the lowest one above $a$.

### L2 human

The theorem weakens the completeness hypothesis of the Knaster–Tarski theorem to chain-completeness, at the price of needing a starting point $a$ with $a \le f(a)$.
In a chain-complete poset with a least element, every monotone map has a least fixed point.
Compared with the [[Bourbaki–Witt theorem|9EABA9ZDZS]], it asks for monotonicity instead of $x \le f(x)$ for all $x$, and in return it gives a least fixed point above $a$.
