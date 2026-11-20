---
tag: ~b408bbbf
kind: example
name: The positive integers are not an elementary substructure of the natural numbers
msc: ["03C07"]
topics: [2RE7GWWXM5]
audience: ug2
not_instance_of:
  - target: 8WZF9SBP39
    note: the formula "x is the least element" holds of 1 in the positive integers and fails in the natural numbers
uses: [8WZF9SBP39, 676H7EGTKJ, P3B1V182N4, NDTJ2E895C]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Elementary substructures and elementary extensions
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Example

Let $L = \set{<}$, and let $\N_{>0} = \set{1, 2, 3, \dots}$ be the set of positive integers.
We check that $(\N_{>0}, <)$ is a [[substructure|676H7EGTKJ]] of $(\N, <)$ and is [[elementarily equivalent|P3B1V182N4]] to it, but it is not an [[elementary substructure|8WZF9SBP39]].

1. $\N_{>0} \subseteq \N$, and the order of $\N_{>0}$ is the restriction of the order of $\N$. The signature has no constants and no functions, so $(\N_{>0}, <)$ is a substructure.
2. The map $n \mapsto n + 1$ is a bijection from $\N$ onto $\N_{>0}$, and $m < n$ if and only if $m + 1 < n + 1$. So it is an isomorphism of orders.
3. [[Isomorphic structures satisfy the same sentences|NDTJ2E895C]], so $(\N_{>0}, <) \equiv (\N, <)$.
4. Let $\varphi(x)$ be the formula $\forall y \, \neg(y < x)$, which says that $x$ is the least element.
5. In $\N_{>0}$, no element is less than $1$. So $(\N_{>0}, <) \models \varphi(1)$.
6. In $\N$, we have $0 < 1$. So $(\N, <) \models \neg\varphi(1)$.
7. So the parameter $1 \in \N_{>0}$ satisfies $\varphi$ in the substructure and not in the structure, and $(\N_{>0}, <) \not\preceq (\N, <)$.

## Remarks

The example shows that a substructure can be elementarily equivalent to the whole structure, and even isomorphic to it, without being elementary.
So the three relations "isomorphic", "elementarily equivalent" and "elementary substructure" must be kept apart.
The same proof works for every final segment $\set{k, k + 1, \dots}$ with $k \ge 1$, with the parameter $k$.
The set $(2\N, <)$ of even numbers fails for another reason: $\exists z \, (0 < z \land z < 2)$ holds in $\N$ and fails in $2\N$.
In fact $\N$ is the only elementary substructure of $(\N, <)$: an elementary substructure must contain the least element $0$, which is definable, and with each element $n$ its successor $n + 1$, which is definable from $n$.

## Explanations

### L1 human

The numbers $1, 2, 3, \dots$ and the numbers $0, 1, 2, \dots$ have the same shape: each starts with a smallest number and goes up one step at a time.
So any statement about the order alone, with no named numbers, is true for one list exactly when it is true for the other.
But put the first list inside the second.
Then the number $1$ is the smallest in the first list and not in the second, because $0$ comes before it.
A statement about the named number $1$ changes its truth value, so the first list is not an elementary part of the second.

### L2 human

We check the claim that $\N$ has no proper elementary substructure.

1. Let $M \preceq \N$. The sentence $\exists x \, \varphi(x)$ holds in $\N$, so some $m \in M$ satisfies $\varphi$ in $\N$, and the only such element is $0$. So $0 \in M$.
2. Let $\sigma(x, y)$ be the formula $x < y \land \neg\exists z \, (x < z \land z < y)$, "$y$ is the successor of $x$".
3. If $n \in M$, then $\N \models \exists y \, \sigma(n, y)$, so some $m \in M$ has $\N \models \sigma(n, m)$, and then $m = n + 1$.
4. By induction on $n$, every $n \in \N$ lies in $M$, so $M = \N$.

The typical use of this example is to test a claim about elementary substructures before trying to prove it.
A trap is to confuse "$\mathcal{M}$ is isomorphic to $\mathcal{N}$" with "$\mathcal{M}$ is an elementary substructure of $\mathcal{N}$".
