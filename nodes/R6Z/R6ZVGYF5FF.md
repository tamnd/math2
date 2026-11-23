---
tag: R6ZVGYF5FF
kind: example
name: Every family of sets has a union in third-order logic
msc: ["03B16"]
topics: [MDHDYV8QZW]
audience: grad
instance_of: [K40YJX8K1G]
uses: [K40YJX8K1G, KWEJFK5943, 5GS6DRJ5SY]
sources:
  - url: https://en.wikipedia.org/wiki/Higher-order_logic
    locator: lead section
---

## Example

A typical third-order sentence quantifies over families of sets, and this one says that every family has a union.
Let $L$ be any signature, let $\mathcal{X}$ be a variable of type $((\iota))$, and let $Y, Z$ be variables of type $(\iota)$.
Consider the sentence of third-order [[higher-order logic|K40YJX8K1G]]
$$\upsilon := \forall \mathcal{X} \, \exists Y \, \forall x \, \big( Y(x) \leftrightarrow \exists Z \, (\mathcal{X}(Z) \land Z(x)) \big).$$
We show that $\upsilon$ is true in every structure, in the standard semantics.

1. The type $((\iota))$ has order $3$, so $\upsilon$ is a sentence of third-order logic.
   It is not second-order.
2. Let $\mathcal{M}$ be an $L$-structure with domain $M$.
   In the standard semantics, $\mathcal{X}$ ranges over $\mathcal{P}(\mathcal{P}(M))$, and $Y$ and $Z$ range over $\mathcal{P}(M)$.
3. Fix a family $\mathcal{F} \in \mathcal{P}(\mathcal{P}(M))$ as the value of $\mathcal{X}$.
4. Let $U = \bigcup \mathcal{F} = \set{a \in M : a \in S \text{ for some } S \in \mathcal{F}}$.
   Then $U \subseteq M$, so $U$ is an allowed value of $Y$.
5. Take $Y = U$ and an element $a \in M$.
   If $a \in U$, then $a \in S$ for some $S \in \mathcal{F}$, so $Z = S$ makes $\mathcal{X}(Z) \land Z(a)$ true.
6. If some $Z = S$ makes $\mathcal{X}(Z) \land Z(a)$ true, then $S \in \mathcal{F}$ and $a \in S$, so $a \in U$.
7. So $Y(a) \leftrightarrow \exists Z \, (\mathcal{X}(Z) \land Z(a))$ holds for every $a$.
   Since $\mathcal{F}$ was arbitrary, $\mathcal{M} \models \upsilon$.

## Remarks

In the [[Henkin semantics|KWEJFK5943]], step 4 needs the union $U$ to belong to the domain of type $(\iota)$.
The [[comprehension schema|5GS6DRJ5SY]] instance for the formula $\exists Z \, (\mathcal{X}(Z) \land Z(x))$, with $\mathcal{X}$ as a parameter, gives this.
So $\upsilon$ is true in every Henkin model as well.

We can replace the union by the intersection, with the formula $\forall Z \, (\mathcal{X}(Z) \to Z(x))$.
The same steps work, and the intersection of the empty family is $M$.

## Explanations

### L1 human

Take some collections of numbers, for example $\set{1, 2}$ and $\set{2, 5}$.
Pour them all together, and we get one collection $\set{1, 2, 5}$, their union.
The sentence says that this is always possible, for any choice of collections.
It speaks about collections of collections, so it lives two levels above the numbers.
That is why it is a third-order sentence.

### L2 human

We check the sentence on $M = \set{1, 2, 3}$ for one family.

1. Take $\mathcal{F} = \set{\set{1}, \set{1, 3}}$, a set of subsets of $M$.
2. The union is $U = \set{1} \cup \set{1, 3} = \set{1, 3}$.
3. For $a = 1$, we have $1 \in U$, and $Z = \set{1}$ is in $\mathcal{F}$ and contains $1$.
4. For $a = 2$, we have $2 \notin U$, and no member of $\mathcal{F}$ contains $2$.
5. For $a = 3$, we have $3 \in U$, and $Z = \set{1, 3}$ is in $\mathcal{F}$ and contains $3$.
6. So $Y = U$ is a witness for this family.

Check: both sides of the biconditional are true for $a = 1$ and $a = 3$, and both are false for $a = 2$.

Sentences like $\upsilon$ state closure properties of the power set inside logic, as set theory does with its axioms.
The trap is to read $\mathcal{X}(Z)$ as "$Z$ is a subset of something".
It says that the set $Z$ is a member of the family $\mathcal{X}$.
