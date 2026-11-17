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

Let $\sim$ be a [[relation|05AVARPXA2]] on a set $X$.
To prove that $\sim$ is an [[equivalence relation|0G8VEZ3WTK]], we prove three statements from the definition of $\sim$, each for arbitrary elements.
Reflexivity: $x \sim x$ for every $x \in X$.
Symmetry: for all $x, y \in X$, $x \sim y$ implies $y \sim x$.
Transitivity: for all $x, y, z \in X$, $x \sim y$ and $y \sim z$ imply $x \sim z$.
A second route avoids the three checks: if $x \sim y$ means $f(x) = f(y)$ for some function $f$, then $\sim$ is an equivalence relation at once, and its classes form a [[partition|08QMKTWF9T]] of $X$.
The method matters because each definition by abstraction, such as the integers modulo $n$, the rational numbers or a quotient group, starts with this proof.

## Motivation

Mathematics often treats different objects as "the same for the present purpose".
The fractions $\tfrac12$ and $\tfrac24$ name the same number, and the integers $3$ and $10$ leave the same remainder on division by $7$.
To build new objects from such classes, the relation "the same for the present purpose" must behave like equality.
The three properties of an equivalence relation are exactly the properties of equality that the construction of [[equivalence classes|0W95W33CMP]] needs.
Without reflexivity some element lies in no class, without symmetry the classes depend on the order of the elements, and without transitivity two classes overlap without being equal.
So each [[definition by abstraction|B60DBNF77S]] needs this proof before the classes can be used.

## Notation

1. Equivalence relations are written $\sim$, $\equiv$, $\cong$ or $\approx$. The symbol $\cong$ often means "isomorphic", and $\equiv$ often means a congruence.
2. The class of $x$ is written $[x]$, $[x]_\sim$ or $\bar{x}$, and the set of classes is the [[quotient set|0011MTQMR6]] $X/{\sim}$.
3. Some books write a relation as a set of pairs $R \subseteq X \times X$ and write $(x, y) \in R$ or $x \mathrel{R} y$ for $x \sim y$.
4. In Mathlib an equivalence relation is `Equivalence r`, with the fields `refl`, `symm` and `trans`, and a type with a chosen equivalence relation is a `Setoid`.

## Remarks

### Examples

1. [[Congruence modulo n is an equivalence relation|76XBZHHG5S]]: the three checks from the definition by divisibility, the standard model of the method.
2. [[Points at the same distance from the origin|VA8BKK7M32]]: the relation on the plane is proved to be an equivalence relation in two ways, directly and as the relation induced by a function.
3. On the set of pairs $(a, b)$ of integers with $b \neq 0$, the relation $(a, b) \sim (c, d) \iff ad = bc$ is an equivalence relation. Transitivity needs $b, d \neq 0$ and the cancellation of a non-zero factor, as in [[rational numbers defined by abstraction|KF8H084HDE]].
4. On the set of $n \times n$ matrices, [[similarity|0E89HQATM8]] $A \sim B \iff B = P^{-1} A P$ for an invertible $P$ is an equivalence relation. Reflexivity uses $P = I$, symmetry uses $P^{-1}$, and transitivity uses the product of the two matrices.
5. On $\mathbb{R}$, the relation $x \sim y \iff x - y \in \mathbb{Z}$ is an equivalence relation: $0$, $-(x - y)$ and $(x - y) + (y - z)$ are integers when $x - y$ and $y - z$ are integers.

### Non-examples

1. [[Closeness within 1 is not an equivalence relation|75AGATX8HN]]: the relation $\lvert x - y \rvert \le 1$ on $\mathbb{R}$ is reflexive and symmetric, but transitivity fails.
2. The relation $\le$ on $\mathbb{R}$ is reflexive and transitive, but it is not symmetric: $1 \le 2$ and $2 \not\le 1$.
3. The relation $x \sim y \iff xy > 0$ on $\mathbb{R}$ is symmetric and transitive, but it is not reflexive, because $0 \cdot 0 = 0$. On $\mathbb{R} \setminus \{0\}$ the same rule is an equivalence relation with the two classes of positive and negative numbers.

### Basic properties

1. The three properties are independent: for each property there is a relation with the other two properties and without this one. The non-examples above give one relation for each case.
2. A relation $x \sim y \iff f(x) = f(y)$ is always an equivalence relation, because equality is reflexive, symmetric and transitive. This is the [[equivalence relation induced by a function|0KT8TGXD8K]].
3. Each equivalence relation has this form: take $f(x) = [x]$, the map to the quotient set.
4. The classes of an equivalence relation form a partition of $X$, by the statement [[equivalence classes form a partition|01HT2CH8BH]]. Conversely each partition defines an equivalence relation: $x \sim y$ when $x$ and $y$ lie in the same block. This is the [[correspondence between equivalence relations and partitions|074482Q7CD]].
5. So there are three equivalent ways to prove that $\sim$ is an equivalence relation: the three checks, a function $f$ with $x \sim y \iff f(x) = f(y)$, or a partition whose blocks are the sets of related elements.

### History

The notion of an equivalence relation grew from many special cases, such as congruence of integers in Gauss's *Disquisitiones Arithmeticae* of 1801 and congruence of figures in geometry.
Frege used definitions by abstraction from an equivalence relation in 1884, with the direction of a line defined from parallelism.
Velleman treats equivalence relations and their proofs in the chapter on relations.

### Common errors

1. A student "proves" reflexivity from symmetry and transitivity: "$x \sim y$ gives $y \sim x$, and then $x \sim x$ by transitivity". The argument needs an element $y$ with $x \sim y$, and such a $y$ need not exist, as non-example 3 shows at $x = 0$.
2. A student checks the three properties on examples, such as $1 \sim 1$ and $2 \sim 2$, instead of for arbitrary elements.
3. A student proves transitivity with the same letter in two places, for example "$x \sim y$ and $y \sim x$ give $x \sim x$". This is a special case of transitivity, not transitivity.

## Explanations

### L1 human

Some relations work like "is the same as" for a purpose, such as "has the same birthday as".
Such a relation must pass three tests.
Each person has the same birthday as himself or herself.
If Ann has the same birthday as Ben, then Ben has the same birthday as Ann.
If Ann has the same birthday as Ben, and Ben as Cara, then Ann has the same birthday as Cara.
A relation like "lives less than 1 kilometre from" passes the first two tests but fails the third, since Ann can be close to Ben and Ben close to Cara while Ann is far from Cara.

### L2 human

We prove that the relation $x \sim y \iff x^2 - y^2 = 3(x - y)$ on $\mathbb{R}$ is an equivalence relation, first by the three checks and then by a function.

1. Reflexivity. For each $x$, $x^2 - x^2 = 0 = 3(x - x)$, so $x \sim x$.
2. Symmetry. If $x^2 - y^2 = 3(x - y)$, multiply by $-1$: $y^2 - x^2 = 3(y - x)$. So $y \sim x$.
3. Transitivity. If $x^2 - y^2 = 3(x - y)$ and $y^2 - z^2 = 3(y - z)$, add the two equations: $x^2 - z^2 = 3(x - z)$. So $x \sim z$.
4. The function route. The condition $x^2 - y^2 = 3(x - y)$ is equivalent to $x^2 - 3x = y^2 - 3y$. So $x \sim y \iff f(x) = f(y)$ with $f(x) = x^2 - 3x$.
5. So the relation is induced by $f$, and it is an equivalence relation by Basic property 2.
6. The class of $x$ is the set of solutions $t$ of $t^2 - 3t = x^2 - 3x$, that is, $(t - x)(t + x - 3) = 0$. So $[x] = \{x, 3 - x\}$.

The typical use of the function route is a relation defined by an equation that can be rearranged into the form "a quantity of $x$ equals the same quantity of $y$".
A trap is to stop after reflexivity and symmetry, because transitivity is the property that fails most often.

### L3 human

An equivalence relation on $X$ is the same as a partition of $X$, and the same as a surjection from $X$ onto some set, up to a bijection of the target.
So the three ways to prove the property correspond to the three descriptions of a quotient: a relation, a partition, and a map to the quotient.
In a category, the role of the function route is played by the kernel pair of a morphism.
An equivalence relation that is a kernel pair is called effective, and in an exact category each equivalence relation is effective.
In algebra, the relations that respect the operations are congruences, and for groups and rings they correspond to normal subgroups and ideals, so the three checks become the subgroup test or the ideal test.
For a relation that fails transitivity, such as closeness, one can take the smallest equivalence relation that contains it, or keep the closeness as a metric and work with topology instead.
Once an equivalence relation is fixed, each operation on the classes needs a proof that it is [[well-defined|HNGZEBKVY2]].
