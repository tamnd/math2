---
tag: RKAJ2ZPA1T
kind: example
name: Two existential quantifiers can be exchanged
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 0FYQMKFE77
    note: two existential quantifiers commute, so their order never changes the meaning, unlike a universal and an existential quantifier
uses: [0FYQMKFE77, 0MSRQHCNN9]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Example

Let $P(x, y)$ be the predicate "$x + y = 5$ and $x - y = 1$" on $\mathbb{Z}$.
We show that $\exists x \, \exists y \, P(x, y)$ and $\exists y \, \exists x \, P(x, y)$ are both true, and that the two orders are equivalent for every predicate.
So this is a case where the order of quantifiers does not change the meaning.

1. Adding the two equations gives $2x = 6$, so $x = 3$, and then $y = 5 - 3 = 2$.
2. $P(3, 2)$ is true, since $3 + 2 = 5$ and $3 - 2 = 1$.
3. So $\exists y \, P(3, y)$ holds with $y = 2$, and $\exists x \, \exists y \, P(x, y)$ holds with $x = 3$.
4. In the same way, $\exists x \, P(x, 2)$ holds with $x = 3$, and $\exists y \, \exists x \, P(x, y)$ holds with $y = 2$.
5. In general, both orders are true exactly when some pair $(a, b) \in D \times D$ satisfies $P(a, b)$.
   Each order asks for one $x$ and one $y$, and neither choice must work for more than one value of the other variable.
6. So $\exists x \, \exists y \, P(x, y) \equiv \exists y \, \exists x \, P(x, y)$ for every predicate $P$ on every domain $D$.

## Remarks

The [[existential quantifier|0MSRQHCNN9]] commutes with itself.
The universal quantifier also commutes with itself, because $\forall x \, \forall y \, P(x, y)$ and $\forall y \, \forall x \, P(x, y)$ both say that every pair satisfies $P$.
The order matters only between quantifiers of different kinds, as in the [[order of quantifiers|0FYQMKFE77]].
If we replace $\exists y$ by $\forall y$, the statement $\exists x \, \forall y \, P(x, y)$ is false, because for any $x$ the instance $y = 0$ fails $x + y = 5$ or $x - y = 1$.

## Explanations

### L1 human

"There is a boy and there is a girl who are friends" and "there is a girl and there is a boy who are friends" say the same thing.
Both claim that at least one friendly pair exists.
The order in which we name the two people does not matter.
With "every" and "some" mixed, the order does matter.

### L2 human

To decide whether two adjacent quantifiers can be exchanged, look at their kinds.
If both are $\exists$, the statement asks for one pair, so the order is free.
If both are $\forall$, the statement claims something for all pairs, so the order is free.
If one is $\forall$ and one is $\exists$, the order changes the dependence of the witness, and the statements can differ.
For instance, in $\forall x \, \exists y \, \exists z \, (y + z = x)$ over $\mathbb{Z}$, the quantifiers $\exists y$ and $\exists z$ can be exchanged, and the statement stays true with $y = x$ and $z = 0$.
Watch out: in $\forall x \, \exists y \, \exists z$, the variable $x$ cannot change places with $y$ or $z$.
