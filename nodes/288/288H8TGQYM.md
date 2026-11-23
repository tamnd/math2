---
tag: 288H8TGQYM
kind: example
name: The successor map cannot start a Veblen hierarchy
msc: ["03E10"]
topics: [XTTKZTYDSD]
audience: grad
not_instance_of:
  - target: JQFAE9S2F4
    note: the map α ↦ α + 1 is strictly increasing but not continuous at limits, and it has no fixed points, so the fixed-point step of the Veblen construction has nothing to enumerate
uses: [6QFEVWKE25, PXTF18X433, ERTAM0SFVB]
sources:
  - url: https://en.wikipedia.org/wiki/Veblen_function
    locator: Veblen hierarchy
---

## Example

Let $s(\alpha) = \alpha + 1$ on the ordinals.
The [[Veblen function|6QFEVWKE25]] starts from a [[normal function|PXTF18X433]] and enumerates its fixed points, so we check whether $s$ can play that role.

1. The map $s$ is strictly increasing: $\alpha < \beta$ gives $\alpha + 1 \le \beta < \beta + 1$.
2. The map $s$ is not continuous at $\omega$.
   The value is $s(\omega) = \omega + 1$, but the limit of the earlier values is
   $$\sup_{n < \omega} s(n) = \sup_n (n + 1) = \omega.$$
3. The map $s$ has no fixed points, since $\alpha < \alpha + 1$ for every $\alpha$.
4. So the class of fixed points is empty, and there is no function $\varphi_1$ that enumerates it.

## Remarks

The example shows that continuity is not a technical detail: a strictly increasing map that is not continuous may have no fixed points at all.

Now change the side on which we add.
The map $\alpha \mapsto 1 + \alpha$ is normal, and its fixed points are exactly the infinite ordinals, since $1 + \alpha = \alpha$ holds exactly for $\alpha \ge \omega$.
The construction then works, with $\varphi_1(\alpha) = \omega + \alpha$.
It gives a much slower hierarchy than the one that starts from $\alpha \mapsto \omega^\alpha$.

## Explanations

### L1 human

The rule "add one" moves every ordinal up by one step.
So no ordinal stays where it is, and there is nothing to list.
The Veblen construction lists the ordinals that a rule leaves unchanged, so it cannot start from "add one".

### L2 human

We compare $\alpha + 1$ and $1 + \alpha$ at $\omega$.
First, $\omega + 1$ is the successor of $\omega$, so $\omega + 1 \ne \omega$.
Second, adding $1$ on the left is a limit of finite sums.
$$1 + \omega = \sup_n (1 + n) = \omega$$
So $\omega$ is a fixed point of $\alpha \mapsto 1 + \alpha$.
For finite $n$, $1 + n = n + 1 \ne n$, so the fixed points start exactly at $\omega$.

The typical use of the example is to explain why the definition requires normal functions.
Watch out: ordinal addition is not commutative, so $\alpha + 1$ and $1 + \alpha$ behave in opposite ways.
