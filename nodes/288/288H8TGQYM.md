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
The [[Veblen function|6QFEVWKE25]] starts from a [[normal function|PXTF18X433]] and enumerates its fixed points.
We check that $s$ fails both requirements.

1. $s$ is strictly increasing: $\alpha < \beta$ gives $\alpha + 1 \le \beta < \beta + 1$.
2. $s$ is not continuous at $\omega$: $s(\omega) = \omega + 1$, but $\sup_{n < \omega} s(n) = \sup_n (n + 1) = \omega$.
3. $s$ has no fixed points, since $\alpha < \alpha + 1$ for every $\alpha$.
4. So the class of fixed points is empty, and a function $\varphi_1$ that enumerates it cannot be defined.

## Remarks

The example shows that continuity is not a technical detail: a strictly increasing function that is not continuous may have no fixed points at all.
Change the map to $\alpha \mapsto 1 + \alpha$, which is normal: its fixed points are the ordinals $\alpha \ge \omega$, since $1 + \alpha = \alpha$ exactly for infinite $\alpha$.
Then the construction works, with $\varphi_1(\alpha) = \omega + \alpha$, but it gives a slower hierarchy than the one from $\alpha \mapsto \omega^\alpha$.

## Explanations

### L1 human

The rule "add one" moves every ordinal up by one step.
So no ordinal stays where it is, and there is nothing to list.
The Veblen construction lists the ordinals that a rule leaves unchanged, so it cannot start from "add one".

### L2 human

We compare $\alpha + 1$ and $1 + \alpha$ at $\omega$.

1. $\omega + 1$ is the successor of $\omega$, so $\omega + 1 \ne \omega$.
2. $1 + \omega = \sup_n (1 + n) = \omega$, so $\omega$ is a fixed point of $\alpha \mapsto 1 + \alpha$.
3. In general $1 + \alpha = \alpha$ for every infinite $\alpha$, and $1 + n = n + 1 \ne n$ for finite $n$.

The typical use is to explain why the definition requires normal functions.
The trap: ordinal addition is not commutative, so the two maps behave in opposite ways.
