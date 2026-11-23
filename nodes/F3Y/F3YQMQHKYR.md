---
tag: F3YQMQHKYR
kind: example
name: The identity operator is not a Magari operator
msc: ["03G25", "03F45"]
topics: [3E7M66WW6Q]
audience: research
not_instance_of:
  - target: YTA4C8QCB0
    fails: [3]
    note: with the identity map as the box, the Löb law fails at x = 0, since the box of (box 0 implies 0) is 1 but box 0 is 0
uses: [PHWAN904PT, 0XADJKM699, BDEX7HET71]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_algebra
    locator: lead section
---

## Example

Let $B = \{0, 1\}$ be the two-element [[Boolean algebra|0XADJKM699]], and define $\square x = x$ for both $x \in B$.
This reads "provable" as "true".
We check the three properties of the [[definition of a Magari algebra|PHWAN904PT]].

1. Property 1 holds, since $\square 1 = 1$ by the definition of $\square$.
2. Property 2 holds, since $\square(x \wedge y) = x \wedge y = \square x \wedge \square y$.
3. Property 3 fails at $x = 0$.
   First, $\square 0 \to 0 = 0 \to 0 = \neg 0 \vee 0 = 1$.
4. So the left side of property 3 is $\square(\square 0 \to 0) = \square 1 = 1$.
5. The right side is $\square 0 = 0$, and $1 \ne 0$.

So $(B, \square)$ is not a [[Magari algebra|YTA4C8QCB0]], and the only property that fails is the Löb law.

## Remarks

### A reflexive point

The same structure is the subset algebra of a frame with one point $w$ and the arrow $w R w$.
There $w \in \square X$ exactly when $w \in X$, so $\square X = X$ for both subsets $X$ of $\{w\}$.
The failure of the Löb law matches the fact that Löb's axiom is not valid on a reflexive point.

### An interior algebra that is not a Magari algebra

The identity map is the simplest interior operator, so $(B, \square)$ is an [[interior algebra|BDEX7HET71]].
Under $p \mapsto 0$, Löb's axiom $\square(\square p \to p) \to \square p$ takes the value $1 \to 0 = 0$.
Interior algebras are the algebras of the modal logic $\mathsf{S4}$, so Löb's axiom is not a theorem of $\mathsf{S4}$.
This fits the general fact that the one-element algebra is the only algebra that is both an interior algebra and a Magari algebra.

### The repair

If we change $\square$ to the constant map $\square x = 1$, all three properties hold; see [[the two-element Magari algebra|BB0SVFTESA]].
In frame terms, we delete the arrow $w R w$, and the point then has no successors.

## Explanations

### L1 human

Here "it is provable" is read as "it is true".
Then "if it is provable, then it is true" is always true, so it is also "provable".
Löb's rule would then say that every statement is provable, also the false one.
So this reading breaks Löb's rule.

### L2 human

We evaluate Löb's axiom at $p \mapsto 0$ step by step.

1. $\square p = 0$.
2. $\square p \to p = \neg 0 \vee 0 = 1$.
3. $\square(\square p \to p) = 1$.
4. The whole formula is $1 \to 0 = \neg 1 \vee 0 = 0$.

So the formula takes the value $0$, and the algebra is not a model of $\mathsf{GL}$.
The typical use of this check is to see that "provable" in $\mathsf{GL}$ cannot mean "true", because the reflection law $\square p \to p$ and Löb's axiom together give every formula.
The trap is to stop after properties 1 and 2, which hold here, and conclude that the operator is a Magari operator.
