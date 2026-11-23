---
tag: PPTAB8J099
kind: example
name: A general structure that fails comprehension
msc: ["03B16", "03C85"]
topics: [MDHDYV8QZW]
audience: grad
not_instance_of:
  - target: KWEJFK5943
    note: the comprehension instance for the formula x = y with parameter 0 has no witness in the family of sets
uses: [KWEJFK5943, 5GS6DRJ5SY]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Semantics
---

## Example

A general structure may choose any families of relations, but a Henkin model must contain each relation that a formula defines.
The smallest example of the difference has two points.
Let $L$ be the empty signature and $M = \set{0, 1}$.
Let $\mathfrak{G} = (M, (D_n)_{n \ge 1})$ with $D_1 = \set{\emptyset, M}$ and $D_n = \mathcal{P}(M^n)$ for $n \ge 2$.
We show that $\mathfrak{G}$ is a general structure but not a [[Henkin model|KWEJFK5943]].

1. $D_1$ is a set of subsets of $M$, and each $D_n$ with $n \ge 2$ is a set of $n$-ary relations on $M$.
   So $\mathfrak{G}$ is a general structure.
2. Take the formula $\varphi(x, y) := x = y$, in which $X$ is not free.
   The [[comprehension schema|5GS6DRJ5SY]] gives the instance $\forall y \, \exists X \, \forall x \, (X(x) \leftrightarrow x = y)$.
3. Take $y = 0$.
   A witness $X$ must satisfy $X(x) \leftrightarrow x = 0$ for $x = 0$ and for $x = 1$, so $X = \set{0}$.
4. The set $\set{0}$ is not in $D_1$.
   So no $X \in D_1$ is a witness, and the instance is false in $\mathfrak{G}$.
5. So $\mathfrak{G}$ fails the comprehension condition, and it is not a Henkin model.

## Remarks

### What the missing set changes

Only the comprehension condition fails, and the other conditions of a general structure hold.
In $\mathfrak{G}$ the sentence $\forall X \, \forall x \, \forall y \, (X(x) \to X(y))$ is true, because each set in $D_1$ is empty or all of $M$.
In the full structure on $M$ the same sentence is false: take $X = \set{0}$, $x = 0$ and $y = 1$.
So in $\mathfrak{G}$ the second-order definition of equality, $\forall X \, (X(x) \to X(y))$, does not define equality.
The L2 explanation shows this in detail.

### How to repair it

If we add $\set{0}$ and $\set{1}$ to $D_1$, we get the full structure, which is a Henkin model.

### Why the schema needs parameters

The map that swaps $0$ and $1$ keeps $D_1$ and every $D_n$ fixed, so it is an automorphism of $\mathfrak{G}$.
So a formula without parameters defines a set of pairs, triples and so on that the swap keeps fixed.
For $n = 1$, such a set is $\emptyset$ or $M$, and both are in $D_1$.
For $n \ge 2$, every relation is in $D_n$.
So $\mathfrak{G}$ satisfies every comprehension instance without parameters.
This is why the parameters $\bar{y}$ and $\bar{Y}$ are a part of the schema.

## Explanations

### L1 human

A Henkin model must allow every set that the language can describe.
On the two points $0$ and $1$, the language can describe the set "the points equal to $0$", which is $\set{0}$.
Our structure allows only the empty set and the whole set.
So it misses a set that the language describes, and it fails the test.

### L2 human

We see the effect on one sentence.

1. Let $\theta := \forall x \, \forall y \, \big( \forall X \, (X(x) \to X(y)) \to x = y \big)$.
2. In the full structure on $M$, the choice $X = \set{x}$ shows that $\forall X \, (X(x) \to X(y))$ implies $y = x$.
   So $\theta$ is true there.
3. In $\mathfrak{G}$, take $x = 0$ and $y = 1$.
   The set $\emptyset$ does not contain $0$, and the set $M$ contains $1$, so $\forall X \, (X(0) \to X(1))$ is true.
4. But $0 \neq 1$, so $\theta$ is false in $\mathfrak{G}$.

Check: the two sets of $D_1$ give the two implications $\bot \to \bot$ and $\top \to \top$, and both are true.

The typical use of this example is to show why the definition of a Henkin model asks for comprehension.
The trap is to think that any choice of families $D_n$ gives a reasonable semantics.
Without comprehension, even the second-order definition of equality fails.
