---
tag: BB0SVFTESA
kind: example
name: The two-element Magari algebra
msc: ["03G25", "03F45"]
topics: [3E7M66WW6Q]
audience: research
instance_of: [YTA4C8QCB0]
uses: [PHWAN904PT, 0XADJKM699]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_algebra
    locator: lead section
---

## Example

Let $B = \{0, 1\}$ be the two-element [[Boolean algebra|0XADJKM699]], with $0 < 1$, $\neg 0 = 1$ and $\neg 1 = 0$.
Define $\square x = 1$ for both elements $x \in B$.
We check the three properties of the [[definition of a Magari algebra|PHWAN904PT]].

1. Property 1, $\square 1 = 1$, is the definition of $\square$ at $x = 1$.
2. Property 2, $\square(x \wedge y) = \square x \wedge \square y$, holds because the left side is $1$ by the definition of $\square$ and the right side is $1 \wedge 1 = 1$.
3. Property 3, $\square(\square x \to x) = \square x$, holds because the left side is $\square$ of some element, so it is $1$, and the right side is $\square x = 1$.

All three properties hold for all $x, y \in B$, so $(B, \square)$ is a [[Magari algebra|YTA4C8QCB0]].

## Remarks

### Provable without being true

Here $\square 0 = 1$ while $1 \not\le 0$, so the operation of a Magari algebra need not satisfy $\square x \le x$.
Under $p \mapsto 0$ the formula $\square p \to p$ takes the value $\square 0 \to 0 = \neg 1 \vee 0 = 0$.
By soundness, $\mathsf{GL}$ does not prove $\square p \to p$.

### Where the algebra comes from

The algebra is the subset algebra of a frame with one point $w$ and no arrows.
There $\square X = \{w\}$ for every $X$, because $w$ has no successors that could leave $X$.

The algebra also appears in arithmetic.
Let $M$ be a model of $\mathsf{PA} + \square \bot$, where $\square \bot$ is the sentence $\neg \mathrm{Con}(\mathsf{PA})$.
Send the class of a sentence $\sigma$ in the Magari algebra of $\mathsf{PA}$ to its truth value in $M$.
This map preserves the Boolean operations, because $M$ satisfies $\mathsf{PA}$.
It sends every $\square[\sigma]$ to $1$, because $\mathsf{PA} \vdash \square \bot \to \square \sigma$ and $M$ satisfies $\square \bot$.

### One algebra is not enough

The algebra validates $\square \bot$, which is not a theorem of $\mathsf{GL}$.
So this one algebra cannot witness the completeness of $\mathsf{GL}$, and a larger algebra such as [[the Magari algebra of a finite strict partial order|RWYEYCB7TD]] is needed to refute $\square \bot$.

### Changing the box

If we change $\square$ to the identity map, $\square x = x$, property 3 fails at $x = 0$; see [[the identity operator is not a Magari operator|F3YQMQHKYR]].
If we change $\square$ to the constant map $\square x = 0$, property 1 fails, since $\square 1 = 0$.
The fourth map from $\{0, 1\}$ to itself is negation, and it fails property 1 as well.
So the constant map with value $1$ is the only Magari operator on $\{0, 1\}$.

## Explanations

### L1 human

The algebra has only two values, "false" and "true".
We decide that "it is provable" always gives "true", whatever we put in.
Then every rule of a Magari algebra has "true" on both sides, so every rule holds.
This is what happens in a theory that proves everything, including false statements.

### L2 human

We compute Löb's axiom $\square(\square p \to p) \to \square p$ at $p \mapsto 0$.

1. $\square p = \square 0 = 1$.
2. $\square p \to p = \neg 1 \vee 0 = 0$.
3. $\square(\square p \to p) = \square 0 = 1$.
4. The whole formula is $1 \to 1 = \neg 1 \vee 1 = 1$.

So Löb's axiom takes the value $1$, as it must in every Magari algebra.
The typical use of this small algebra is to show that a formula is not a theorem of $\mathsf{GL}$, as with $\square p \to p$ above.
The trap is the converse: a formula with value $1$ here need not be a theorem of $\mathsf{GL}$, and $\square \bot$ is an example.
