---
tag: JJ1S2E9D2S
kind: example
name: Infinite subsets of a pure set are elementary substructures
msc: ["03C07"]
topics: [2RE7GWWXM5]
audience: ug2
instance_of: [8WZF9SBP39]
illustrates: [60SA99BER7]
uses: [8WZF9SBP39, 60SA99BER7, NDTJ2E895C, XY6CJMDY5M]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Tarski–Vaught test
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Example

Let $L = \emptyset$ be the empty signature, so that an $L$-structure is a nonempty set and the only atomic formulas are equations $x = y$.
Let $N$ be an infinite set and let $M \subseteq N$ be an infinite subset.
We check that $M \preceq N$, that is, $M$ is an [[elementary substructure|8WZF9SBP39]] of $N$.

1. $L$ has no constants and no function symbols, so every nonempty subset of $N$ is the domain of a substructure. In particular $M$ is a substructure of $N$.
2. By the [[Tarski-Vaught test|60SA99BER7]], it is enough to show: if $\varphi(x_1, \dots, x_n, y)$ is a formula, $a_1, \dots, a_n \in M$, $b \in N$ and $N \models \varphi(\bar a, b)$, then $N \models \varphi(\bar a, c)$ for some $c \in M$.
3. If $b \in M$, take $c = b$.
4. Otherwise $b \notin M$, so $b$ differs from each $a_i$. The set $M$ is infinite, so there is $c \in M$ with $c \ne a_1, \dots, a_n$.
5. Let $\sigma \colon N \to N$ exchange $b$ and $c$ and fix every other element. It is a bijection, and in the empty signature every bijection is an [[automorphism|XY6CJMDY5M]].
6. Neither $b$ nor $c$ is one of the $a_i$, so $\sigma(a_i) = a_i$ for each $i$, and $\sigma(b) = c$.
7. [[Automorphisms preserve formulas|NDTJ2E895C]], so $N \models \varphi(\bar a, c)$.
8. So the condition of step 2 holds, and $M \preceq N$.

## Remarks

The example shows that in a structure with many automorphisms, elementary substructures are easy to find.
The hypothesis that $M$ is infinite is needed.
If $M$ has exactly $k$ elements, then the sentence "there are at least $k + 1$ distinct elements" holds in $N$ and fails in $M$.
In step 4 this is the point where $c$ cannot be found: all elements of $M$ may already be among the parameters.
A consequence: any two infinite sets $A$ and $B$ are [[elementarily equivalent|P3B1V182N4]].
Indeed, choose countably infinite subsets $A_0 \subseteq A$ and $B_0 \subseteq B$; then $A \equiv A_0 \cong B_0 \equiv B$.
So the theory of infinite sets is [[complete|655K8Y7VS8]].

## Explanations

### L1 human

Imagine a set with no structure at all: no order, no operations, only the question "are these two elements equal".
Then any infinite part of the set looks exactly like the whole set.
Whatever we can say about a few named elements of the part, such as "there is an element different from these three", is true in the part exactly when it is true in the whole.
A finite part fails: if the part has $5$ elements, then "there are $6$ different elements" is false in the part and true in the whole.

### L2 human

We check one formula by hand, with $N = \N$ and $M$ the set of even numbers.

1. Let $\varphi(x_1, x_2, y) = (y \ne x_1 \land y \ne x_2)$, with the parameters $a_1 = 0$ and $a_2 = 2$.
2. In $N$ the witness $b = 1$ works, since $1 \ne 0$ and $1 \ne 2$.
3. The proof chooses $c \in M$ different from $0$ and $2$, for example $c = 4$.
4. The exchange of $1$ and $4$ fixes $0$ and $2$, and $4 \ne 0$, $4 \ne 2$. So $N \models \varphi(0, 2, 4)$.

The typical use of this example is as the simplest case of the automorphism method for the Tarski-Vaught test.
A trap is to forget that the parameters must stay fixed: exchanging $1$ with $0$ would give a wrong witness.
