---
tag: RGNF33GVHX
kind: concept
name: Proving a relation is an equivalence relation
aliases: [proving-equivalence-relations]
msc: ["00A35", "03E20"]
topics: [MEKKHHQTKB, G9JFJGY4TQ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [05AVARPXA2, 0G8VEZ3WTK, 0X8NMST0J2, 061J5VGSPT, 0GJZW9JFZQ, 08QMKTWF9T, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalence_relation
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Equivalence_class
    locator: lead section
  - book: isbn:9781108439534
    locator: Chapter 4
---

## Summary

A relation that is meant to work like "is the same as" must pass three tests: everything is related to itself, the relation can be read backward, and it can be chained.
Each test is a short proof from the definition of the relation, for arbitrary elements.

The standard goal is congruence modulo $n$ on $\mathbb{Z}$, where $a \equiv b \pmod n$ means that $n$ divides $a - b$.
Reflexive: $a - a = 0 = n \cdot 0$.
Symmetric: if $a - b = nk$, then $b - a = n(-k)$.
Transitive: if $a - b = nk$ and $b - c = n\ell$, then adding gives
$$a - c = (a - b) + (b - c) = n(k + \ell).$$
The [[full example|76XBZHHG5S]] writes out each step.

In general, a [[relation|05AVARPXA2]] $\sim$ on a set $X$ is an [[equivalence relation|0G8VEZ3WTK]] when it is [[reflexive|0X8NMST0J2]], $x \sim x$ for every $x \in X$; [[symmetric|061J5VGSPT]], $x \sim y$ implies $y \sim x$; and [[transitive|0GJZW9JFZQ]], $x \sim y$ and $y \sim z$ imply $x \sim z$.
A second route skips the three checks: if $x \sim y$ means $f(x) = f(y)$ for some function $f$, then $\sim$ is an equivalence relation at once.

## Motivation

Mathematics often treats different objects as the same for one purpose.
The fractions $\tfrac12$ and $\tfrac24$ name the same number, and $3$ and $10$ leave the same remainder on division by $7$.
To build new objects out of such groups, the relation "the same for this purpose" must behave like equality.
The three properties are exactly the properties of equality that the construction of [[equivalence classes|0W95W33CMP]] needs.

Each property has a job.
Without reflexivity some element lies in no class, without symmetry the class of $x$ depends on which side $x$ stands, and without transitivity two classes overlap without being equal.
So every [[definition by abstraction|B60DBNF77S]], such as the integers modulo $n$, the rational numbers as classes of pairs, or a quotient group, starts with this proof.
The element-by-element reasoning is the same [[direct proof|0NTF6DMVAP]] as in [[double inclusion|MKHVRNW68H]].

## Notation

Equivalence relations are written $\sim$, $\equiv$, $\cong$ or $\approx$; the symbol $\cong$ often means "isomorphic", and $\equiv$ often means a congruence.
The class of $x$ is $[x]$, $[x]_\sim$ or $\bar{x}$, and the set of classes is the [[quotient set|0011MTQMR6]] $X/{\sim}$.
Some books treat a relation as a set of pairs $R \subseteq X \times X$ and write $x \mathrel{R} y$ for $(x, y) \in R$.
In Lean's Mathlib, `Equivalence r` bundles the three fields `refl`, `symm` and `trans`, and a `Setoid` is a type with a chosen equivalence relation.

## Remarks

### More goals of the same shape

On pairs $(a, b)$ of integers with $b \ne 0$, put $(a, b) \sim (c, d)$ when $ad = bc$; this is how the [[rational numbers arise by abstraction|KF8H084HDE]].
Reflexivity and symmetry are immediate from $ab = ba$.
For transitivity, $ad = bc$ and $cf = de$ give
$$adf = bcf = bde,$$
so $d(af - be) = 0$, and $d \ne 0$ lets us cancel to get $af = be$.
The hypothesis $d \ne 0$ is used exactly here.

On $n \times n$ matrices, [[similarity|0E89HQATM8]], $B = P^{-1} A P$ for an invertible $P$, is an equivalence relation.
Reflexivity uses $P = I$, symmetry uses $P^{-1}$, and transitivity uses the product of the two matrices.

### The function route and partitions

If $x \sim y$ means $f(x) = f(y)$, the three properties of $\sim$ are the three properties of equality, so there is nothing more to check.
This is the [[equivalence relation induced by a function|0KT8TGXD8K]], and its classes are the non-empty level sets of $f$.
For [[points at the same distance from the origin|VA8BKK7M32]], $f(x, y) = x^2 + y^2$, and the classes are the origin and the circles about it.
Every equivalence relation has this form, with $f(x) = [x]$.

A third route goes through a [[partition|08QMKTWF9T]]: if $X$ is split into disjoint non-empty blocks, "in the same block" is an equivalence relation.
In the other direction, [[the classes of an equivalence relation form a partition|01HT2CH8BH]], and the [[correspondence of relations and partitions|074482Q7CD]] makes the two views the same.

### Relations that fail one test

The three properties are independent, and each failure has a standard example.
On $\mathbb{R}$, [[closeness within 1|75AGATX8HN]], $\lvert x - y \rvert \le 1$, is reflexive and symmetric, but $0$ is close to $1$, $1$ is close to $2$, and $0$ is not close to $2$.
The order $\le$ is reflexive and transitive, but $1 \le 2$ and $2 \not\le 1$.
The relation $xy > 0$ on $\mathbb{R}$ is symmetric and transitive, but not reflexive, since $0 \cdot 0 = 0$.
On $\mathbb{R} \setminus \{0\}$ the same rule is an equivalence relation with two classes, the positive and the negative numbers.

### Watch out

A tempting argument "proves" reflexivity from the other two properties: take $y$ with $x \sim y$, then $y \sim x$ by symmetry, so $x \sim x$ by transitivity.
The argument needs some $y$ related to $x$, and there may be none.
For $xy > 0$ and $x = 0$, no $y$ satisfies $0 \cdot y > 0$, and reflexivity fails there.
So you must check reflexivity on its own.

Two other slips are common.
Checking $1 \sim 1$ and $2 \sim 2$ tests examples and proves nothing about arbitrary elements.
Writing "$x \sim y$ and $y \sim x$ give $x \sim x$" proves one special case of transitivity, with $z = x$, not transitivity itself.

### History

Equivalence relations grew from special cases, such as congruence of integers in Gauss's *Disquisitiones Arithmeticae* of 1801.
Frege defined the direction of a line from the relation of parallelism in his *Foundations of Arithmetic* of 1884, an early definition by abstraction.

### Try it

Is $x \sim y \iff x - y \in \mathbb{Z}$ an equivalence relation on $\mathbb{R}$?
Yes: $x - x = 0$ is an integer, $y - x = -(x - y)$ is an integer, and $x - z = (x - y) + (y - z)$ is a sum of integers.

Is "$a$ divides $b$" an equivalence relation on the positive integers?
No: it is reflexive and transitive, but $1$ divides $2$ and $2$ does not divide $1$.

## Explanations

### L1 human

Some relations work like "is the same as" for one purpose, such as "has the same birthday as".
Such a relation must pass three tests.
Each person has the same birthday as themselves.
If Ann has the same birthday as Ben, then Ben has the same birthday as Ann.
If Ann matches Ben and Ben matches Cara, then Ann matches Cara.
"Lives less than 1 kilometer from" passes the first two tests and fails the third, since Ann can be near Ben and Ben near Cara while Ann is far from Cara.

### L2 human

We prove that $x \sim y \iff x^2 - y^2 = 3(x - y)$ is an equivalence relation on $\mathbb{R}$, first by the three tests and then by a function.

1. Reflexive: $x^2 - x^2 = 0 = 3(x - x)$.
2. Symmetric: multiply $x^2 - y^2 = 3(x - y)$ by $-1$ to get $y^2 - x^2 = 3(y - x)$.
3. Transitive: add $x^2 - y^2 = 3(x - y)$ and $y^2 - z^2 = 3(y - z)$ to get $x^2 - z^2 = 3(x - z)$.
4. The function route: the defining equation rearranges to $x^2 - 3x = y^2 - 3y$, so $x \sim y$ exactly when $f(x) = f(y)$ for $f(x) = x^2 - 3x$.
5. The class of $x$ is the set of $t$ with $t^2 - 3t = x^2 - 3x$, that is,
   $$(t - x)(t + x - 3) = 0, \quad \text{so } [x] = \{x, 3 - x\}.$$
   Check: $[1] = \{1, 2\}$, and $1 - 3 = -2 = 4 - 6$.

The function route fits any relation that rearranges to "a quantity of $x$ equals the same quantity of $y$".
Watch out: do not stop after reflexivity and symmetry, since transitivity is the test that fails most often.

### L3 human

An equivalence relation on $X$ is the same thing as a partition of $X$, and the same thing as a surjection from $X$ onto some set, up to a bijection of the target.
The three proof routes match these three views of a quotient.
In a category, the function route becomes the kernel pair of a morphism, and an equivalence relation that is a kernel pair is called effective.
In algebra, the equivalence relations that respect the operations are congruences, and for groups and rings they correspond to normal subgroups and ideals, so the three tests become the subgroup or ideal test.
Once the relation is fixed, every operation on classes needs a proof that it is [[well-defined|HNGZEBKVY2]].
