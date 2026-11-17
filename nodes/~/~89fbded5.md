---
tag: ~89fbded5
kind: example
name: Equality of sets is definable in third-order logic
msc: ["03B16"]
topics: [MDHDYV8QZW]
audience: grad
instance_of: [K40YJX8K1G]
uses: [K40YJX8K1G, G6X7SZSNC5]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Definition of equality
---

## Example

Let $X$ and $Y$ be variables of type $(\iota)$, and let $\mathcal{Z}$ be a variable of type $((\iota))$.
Consider the formula of third-order [[higher-order logic|K40YJX8K1G]]

$$\epsilon(X, Y) := \forall \mathcal{Z} \, (\mathcal{Z}(X) \to \mathcal{Z}(Y)).$$

We show that in the standard semantics, $\epsilon(X, Y)$ is true exactly when $X$ and $Y$ have the same value.

1. The type $((\iota))$ has order $3$, so $\epsilon$ is a third-order formula.
2. Let the values of $X$ and $Y$ be the sets $A, B \subseteq M$. In the standard semantics, $\mathcal{Z}$ ranges over all families of subsets of $M$.
3. Suppose $A = B$. For every family $\mathcal{F}$, if $A \in \mathcal{F}$, then $B \in \mathcal{F}$. So $\epsilon$ is true.
4. Suppose $\epsilon$ is true. Take $\mathcal{Z} = \set{A}$, a family of subsets of $M$. Then $\mathcal{Z}(X)$ is true, since $A \in \set{A}$.
5. By $\epsilon$, $\mathcal{Z}(Y)$ is true, so $B \in \set{A}$, and $B = A$.

## Remarks

The example lifts the second-order definition of equality, $\forall X \, (X(x) \to X(y))$, from individuals to sets.
Each level of the type hierarchy can define equality on the level below it in the same way.
Equality of sets is also definable one order lower, by extensionality: $\forall x \, (X(x) \leftrightarrow Y(x))$ is a second-order formula with the same meaning.
In a Henkin model, step 4 needs $\set{A}$ in the domain of type $((\iota))$; the comprehension instance for the formula $\forall x \, (W(x) \leftrightarrow X(x))$, with the variable $W$ of type $(\iota)$, gives it.

## Explanations

### L1 human

Two collections are the same exactly when every club that admits the first collection also admits the second.
To see why, take the club whose only member is the first collection.
If the second collection is also admitted, it must be the first one.
The clubs are collections of collections, so this definition lives at the third level.

### L2 human

We check step 4 on $M = \set{1, 2}$ with $A = \set{1}$ and $B = \set{2}$.

1. The family $\mathcal{Z} = \set{\set{1}}$ contains $A$.
2. It does not contain $B = \set{2}$.
3. So $\mathcal{Z}(X) \to \mathcal{Z}(Y)$ is false for this $\mathcal{Z}$, and $\epsilon(X, Y)$ is false, as it should be, since $A \neq B$.

The typical use is to define equality at each type, so that higher-order logic needs no primitive equality symbol above the individuals.
The trap is to use a family that contains both sets, such as $\mathcal{P}(M)$: it says nothing, because it admits every set.
