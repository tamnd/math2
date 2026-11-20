---
tag: ~65feae4d
kind: example
name: The inclusion of the even integers in the integer order is not elementary
msc: ["03C07"]
topics: [2RE7GWWXM5]
audience: ug2
not_instance_of:
  - target: CGH8C8EA9N
    note: the formula "some element lies between x and y" holds of 0 and 2 in the integers and fails in the even integers
uses: [CGH8C8EA9N, SCRB74SWQN, P3B1V182N4, NDTJ2E895C]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Elementary substructures and elementary extensions
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Example

Let $L = \set{<}$, let $2\Z$ be the set of even integers, and let $h \colon 2\Z \to \Z$ be the inclusion map.
We check that $h$ is an [[embedding|SCRB74SWQN]] between [[elementarily equivalent|P3B1V182N4]] structures, but not an [[elementary embedding|CGH8C8EA9N]].

1. $h$ is injective, and $m < n$ in $2\Z$ exactly when $m < n$ in $\Z$. So $h$ is an embedding of orders.
2. The map $g \colon \Z \to 2\Z$, $g(n) = 2n$, is a bijection, and $m < n$ if and only if $2m < 2n$. So $g$ is an isomorphism of $(\Z, <)$ onto $(2\Z, <)$.
3. [[Isomorphic structures satisfy the same sentences|NDTJ2E895C]], so $(2\Z, <) \equiv (\Z, <)$.
4. Let $\varphi(x, y)$ be the formula $\exists z \, (x < z \land z < y)$.
5. In $\Z$, the element $z = 1$ satisfies $0 < 1 < 2$. So $(\Z, <) \models \varphi(0, 2)$.
6. In $2\Z$, an element $z$ with $0 < z < 2$ would be an even integer strictly between $0$ and $2$, and there is none. So $(2\Z, <) \models \neg\varphi(0, 2)$.
7. So $h(0) = 0$ and $h(2) = 2$ satisfy $\varphi$ in $\Z$, while $0$ and $2$ fail it in $2\Z$, and $h$ is not elementary.

## Remarks

The example shows that an embedding between elementarily equivalent structures, even isomorphic ones, need not be elementary.
Elementarity is about formulas with parameters, and the parameters $0$ and $2$ see the gap that the inclusion opens.
The same happens for $n \mathbb{Z} \subseteq \Z$ for every $n \ge 2$, with the parameters $0$ and $n$.
For $n = 1$ the inclusion is the identity map, which is elementary.
In contrast, $(\Q, <) \preceq (\R, <)$, because in a dense order no such gap can appear; see [[this example|~89a66bd3]].
The map $g$ of step 2 is an elementary embedding of $(\Z, <)$ onto $(2\Z, <)$, since it is an isomorphism; it is the inclusion $h$ that fails.

## Explanations

### L1 human

The even numbers $\dots, -2, 0, 2, 4, \dots$ with their order look exactly like all the integers with their order: just halve every number.
But when we place the even numbers inside the integers, something changes.
Among the even numbers there is nothing between $0$ and $2$.
Among all integers the number $1$ lies between them.
So the statement "there is a number between $0$ and $2$" changes its truth value, and the inclusion is not elementary.

### L2 human

We find the smallest change that repairs the example, to see which feature breaks elementarity.

1. The failure comes from two parameters $a < b$ of $2\Z$ with an integer strictly between them.
2. Every pair of consecutive even integers $2k < 2k + 2$ has the integer $2k + 1$ between them.
3. So the formula $\varphi(x, y) = \exists z \, (x < z \land z < y)$ fails for every consecutive pair in $2\Z$ and holds for it in $\Z$.
4. A substructure $A \subseteq \Z$ avoids this failure only if consecutive elements of $A$ are consecutive in $\Z$, that is, only if $A$ is an interval of $\Z$.
5. An interval that is a proper subset of $\Z$ has a least or a greatest element, and $\Z$ has neither, so it is not even elementarily equivalent to $\Z$.

So $\Z$ itself is the only elementary substructure of $(\Z, <)$.
The typical use of such an example is to show that a property of a substructure cannot be transferred to the whole structure.
A trap is to conclude non-elementarity from the existence of an isomorphism; isomorphism of the two structures says nothing about the inclusion.
