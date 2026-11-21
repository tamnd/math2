---
tag: FQXCHW7DDG
kind: example
name: A set that is a type in one order and not in another
msc: ["03C07"]
topics: [Z772KEC9BY]
audience: grad
not_instance_of:
  - target: 9V71Q3SD1G
    note: "the set {0 < x, x < 1} is not consistent with the theory of the integer order with names for 0 and 1"
uses: [9V71Q3SD1G, 2W4S2H4VYA]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Definitions
---

## Example

Let $A = \set{0, 1}$ and let $p(x) = \set{0 < x, \; x < 1}$, a set of formulas with the parameters $0$ and $1$.
We show that $p$ is not a [[type|9V71Q3SD1G]] over $A$ in $(\Z, <)$, and that it is a type over $A$ in $(\Q, <)$.

1. In $(\Z, <)$ no integer lies strictly between $0$ and $1$.
2. So the sentence $\neg \exists x \, (0 < x \wedge x < 1)$ is in $\operatorname{Th}_A(\Z, <)$.
3. A model of $\operatorname{Th}_A(\Z, <) \cup p$ would have an element $b$ with $0 < b < 1$, against this sentence.
4. So $\operatorname{Th}_A(\Z, <) \cup p$ is not satisfiable, and $p$ is not a type over $A$ in $(\Z, <)$.
5. In $(\Q, <)$ the rational number $1/2$ satisfies both formulas of $p$.
6. So $p$ is a type over $A$ in $(\Q, <)$, and $(\Q, <)$ realizes it.

## Remarks

The two structures disagree only in the parameters: $(\Z, <)$ is discrete and $(\Q, <)$ is a [[dense linear order|2W4S2H4VYA]].
In the theory of $(\Z, <)$ with two new constants $c_0 < c_1$ that are not named, the set $\set{c_0 < x, \; x < c_1}$ is consistent, because $c_0$ and $c_1$ can be $0$ and $2$.
So the example shows that a type over $A$ must be consistent with everything that the structure says about $A$.
No elementary extension of $(\Z, <)$ has an element between $0$ and $1$, since the sentence of step 2 stays true there.

## Explanations

### L1 human

The wish "a number above $0$ and below $1$" makes sense among fractions, and $1/2$ meets it.
Among whole numbers the same wish is impossible, and no larger model of the same facts can meet it.
So whether a wish list is a type depends on the structure and on the named elements.

### L2 human

The test for a type over $A$ is the satisfiability of $\operatorname{Th}_A(\mathcal{M}) \cup p$.

1. By compactness this is the same as: every finite part of $p$ is realized in $\mathcal{M}$.
2. Here the finite part $p$ itself is not realized in $(\Z, <)$, so the test fails.

The trap is to test $p$ only against the theory of the structure without the names of $0$ and $1$.
