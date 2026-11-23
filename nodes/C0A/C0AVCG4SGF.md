---
tag: C0AVCG4SGF
kind: example
name: Every element has a larger element, as a sentence
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [DKFGQTRYZE]
uses: [Q85MMH5DEY, Y3FZTH5158, K7XDVK5854]
sources:
  - url: https://en.wikipedia.org/wiki/Sentence_(mathematical_logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Free and bound variables
---

## Example

Let $\sigma = \{ < \}$ with one binary relation symbol, and let $\varphi = \forall x \, \exists y \, (x < y)$.
We check that $\varphi$ is a [[sentence|DKFGQTRYZE]] and find its truth value in two structures.

1. $\operatorname{FV}(x < y) = \{ x, y \}$, because $x < y$ is atomic.
2. $\operatorname{FV}(\exists y \, (x < y)) = \{ x, y \} \setminus \{ y \} = \{ x \}$.
3. $\operatorname{FV}(\varphi) = \{ x \} \setminus \{ x \} = \emptyset$, so $\varphi$ is a sentence by the [[definition|Q85MMH5DEY]].
4. In $(\mathbb{N}, <)$ the sentence is [[true|K7XDVK5854]]: for each $n \in \mathbb{N}$, the element $n + 1$ satisfies $n < n + 1$.
5. In the finite order $(\{ 0, 1, 2 \}, <)$ the sentence is false: for $x = 2$ no element $y$ satisfies $2 < y$.

## Remarks

The sentence says that the order has no largest element.
Every nonempty finite linear order has a largest element, so $\varphi$ is false in all of them, and it is true in $(\mathbb{Z}, <)$, $(\mathbb{Q}, <)$ and $(\mathbb{R}, <)$.
Its truth value depends only on the structure, since $\varphi$ has no free variables to assign.

Watch out for the order of the quantifiers.
Swapping them gives $\exists y \, \forall x \, (x < y)$, which asks for one element above all elements, itself included.
This sentence is false in every structure where $<$ is irreflexive, because the choice $x = y$ would need $y < y$.

## Explanations

### L1 human

"Every number has a larger number" is a complete claim.
For the natural numbers it is true: $7$ has the larger number $8$, and the same works for each number.
For the three numbers $0, 1, 2$ it is false, because nothing is larger than $2$.
The claim is about the whole collection of numbers, not about one chosen number.

### L2 human

We evaluate $\varphi$ in $(\mathbb{N}, <)$ from the inside out.
The formula $x < y$ defines the set of pairs $(a, b)$ with $a < b$.
The formula $\exists y \, (x < y)$ defines the set of $a$ that have some $b > a$, and this set is all of $\mathbb{N}$, since $b = a + 1$ works.
The sentence $\forall x \, \exists y \, (x < y)$ is true exactly when this set is the whole domain, so it is true.
The typical use of such sentences is to describe a class of structures, here the orders with no largest element.
