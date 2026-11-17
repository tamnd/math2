---
tag: 0K8F7PVDMX
kind: concept
name: Associativity
aliases: [associative-property]
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
uses: [0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Associative_property
    locator: Definition
  - book: isbn:9780471433347
    locator: Section 1.1
same_as:
  wikidata: Q177251
  wikipedia: Associative property
---

## Summary

Let $S$ be a set with a [[binary operation|0M418FE7BB]] $\ast$.
The operation $\ast$ is associative when $(a \ast b) \ast c = a \ast (b \ast c)$ for all $a, b, c \in S$.
The law says that the grouping of three elements does not change the result, while the order of the elements stays the same.
Associativity lets us omit the parentheses in a product of several elements, and it is the first of the axioms of a [[group|G5S1M9]].

## Motivation

A binary operation combines two elements.
To combine three elements $a$, $b$, $c$ in this order, we must first combine two of them.
There are two ways to do this: $(a \ast b) \ast c$ and $a \ast (b \ast c)$.
For addition of numbers the two ways give the same result, so the expression $2 + 3 + 4$ has one meaning.
For subtraction they do not: $(5 - 3) - 2 = 0$, but $5 - (3 - 2) = 4$.
Associativity is the condition under which an expression such as $a \ast b \ast c$ has one meaning.
[[General associativity|8HEYE9EZMW]] extends this to products of any length.

## Notation

For an associative operation, we write $a \ast b \ast c$ or $abc$ without parentheses.
For an operation that is not associative, a convention must fix the grouping.
For subtraction, the convention is $a - b - c = (a - b) - c$.
For exponentiation, the convention is $a^{b^c} = a^{(b^c)}$.

## Remarks

### Examples

1. Addition and multiplication of [[integers|0C4JS9RF5M]], [[rational numbers|0NCJ5WXN6Z]], [[real numbers|08J2M1JYAG]] and [[complex numbers|09FTAET5Z4]] are associative.
2. [[Composition of functions is associative|50BK1KV2Z0]], because both groupings of $f \circ g \circ h$ send $x$ to $f(g(h(x)))$.
3. [[Matrix multiplication|JW8JBGJKE3]] on $n \times n$ matrices is associative, because it corresponds to the composition of linear maps.
4. [[The operation a + b + ab on the integers is associative|Z522RSJ213]], because both groupings give $a + b + c + ab + ac + bc + abc$.
5. The operation $\max$ on $\mathbb{R}$ is associative, because both $\max(\max(a, b), c)$ and $\max(a, \max(b, c))$ are the largest of the three numbers.
6. Union of subsets of a set is associative, because each grouping of $A \cup B \cup C$ is the set of the elements that are in at least one of the three sets. Intersection is associative for the same kind of reason.

### Non-examples

1. [[Subtraction is not associative|HSWMSJVY2S]]: $(5 - 3) - 2 = 0$, but $5 - (3 - 2) = 4$.
2. [[Exponentiation is not associative|PBDAR83RK6]]: $(2^3)^2 = 64$, but $2^{(3^2)} = 512$.
3. [[The cross product is not associative|VRA3B0V8CD]]: for the standard basis vectors, $(\mathbf{i} \times \mathbf{i}) \times \mathbf{j} = \mathbf{0}$, but $\mathbf{i} \times (\mathbf{i} \times \mathbf{j}) = -\mathbf{j}$.
4. The average $a \ast b = (a + b)/2$ on $\mathbb{R}$ is not associative: $(0 \ast 0) \ast 4 = 2$, but $0 \ast (0 \ast 4) = 1$.

### Basic properties

1. [[General associativity|8HEYE9EZMW]]: when $\ast$ is associative, all the ways to put parentheses in $a_1 \ast a_2 \ast \cdots \ast a_n$ give the same element.
2. Associativity and [[commutativity|099E72KTF8]] are independent. Composition of functions is associative and not commutative. The average $(a + b)/2$ is commutative and not associative.
3. When $\ast$ is associative on $S$ and a subset $T$ is closed under $\ast$, the restriction of $\ast$ to $T$ is associative, because the law holds for all elements of $S$.
4. When $\ast$ is associative, the powers $a^n = a \ast a \ast \cdots \ast a$ ($n$ factors) are well defined for $n \geq 1$, and $a^m \ast a^n = a^{m + n}$. The [[laws of exponents|00DRK90Z6K]] give these rules in a group.
5. To check associativity on a set with $n$ elements, we must check $n^3$ triples, unless a structure such as composition of functions gives a proof for all triples at once.

### History

The law was used in arithmetic long before it had a name.
In his paper of 1854 on groups, Arthur Cayley noted that the symbols of a group are associative but in general not commutative.
The octonions, found by John Graves in 1843 and independently by Cayley in 1845, have a multiplication that is not associative.

### Common errors

1. Associativity is confused with commutativity. Associativity changes the grouping and keeps the order: $(ab)c = a(bc)$. It does not say that $ab = ba$.
2. Only some triples are checked. One triple with $(a \ast b) \ast c \neq a \ast (b \ast c)$ shows that $\ast$ is not associative, but a few good triples do not prove associativity.
3. An expression such as $2^{3^2}$ is read with the wrong grouping. For an operation that is not associative, the reader must know the convention.

## Explanations

### L1 human

Associativity says that in a chain of the same operation, the place of the brackets does not matter.
For example, $(2 + 3) + 4 = 5 + 4 = 9$ and $2 + (3 + 4) = 2 + 7 = 9$.
So we can write $2 + 3 + 4$ with no brackets.
The order of the numbers stays the same; only the grouping changes.
Subtraction is different: $(5 - 3) - 2 = 0$, but $5 - (3 - 2) = 4$.
So for subtraction the brackets matter.

### L2 human

We check that the operation $a \ast b = a + b + ab$ on $\mathbb{Z}$ is associative.
Let $a, b, c$ be integers.

1. By the definition, $a \ast b = a + b + ab$.
2. Thus $(a \ast b) \ast c = (a + b + ab) + c + (a + b + ab)c$.
3. We expand: $(a \ast b) \ast c = a + b + c + ab + ac + bc + abc$.
4. In the same way, $b \ast c = b + c + bc$, and $a \ast (b \ast c) = a + (b + c + bc) + a(b + c + bc)$.
5. We expand: $a \ast (b \ast c) = a + b + c + ab + ac + bc + abc$.
6. The results of steps 3 and 5 are equal, so $\ast$ is associative.

The typical use of associativity is in the test of the group axioms: it is the axiom that needs the most algebra, because it involves three arbitrary elements.
Often a shortcut helps: here $a \ast b + 1 = (a + 1)(b + 1)$, so $\ast$ is ordinary multiplication after the shift $x \mapsto x + 1$, and multiplication is associative.
A trap is a commutative operation that is not associative, such as the average $(a + b)/2$.
The commutativity can make the operation look friendly, but $(0 \ast 0) \ast 4 = 2$ and $0 \ast (0 \ast 4) = 1$.

### L3 human

A set with an associative binary operation is a [[semigroup|0XMEM406JM]], and a semigroup with an identity element is a [[monoid|0N6R902FG1]].
The number of ways to put parentheses in a product of $n$ factors is the [[Catalan number|0YWZJEABB2]] $C_{n-1}$, so associativity identifies $C_{n-1}$ expressions: $5$ expressions for $n = 4$.
Important operations are not associative: the bracket of a [[Lie algebra|5JJYBJ6A8K]] satisfies the [[Jacobi identity|ZKFN197MBR]] in place of associativity, and the [[octonions|1HRMT3DSX2]] satisfy only the weaker alternative laws.
In a category, composition of morphisms is associative by an axiom, and a group is the same as a category with one object in which every morphism is invertible.
When associativity holds only up to an isomorphism, as for the tensor product of vector spaces, the [[coherence theorem|2W2X7EBG2S]] of Mac Lane shows that one condition on four factors, the pentagon identity, makes all the bracketings agree.
In group theory, associativity is the axiom that makes products such as $g_1 g_2 \cdots g_n$, powers $g^n$ and the [[order of an element|0WE2NHZJ7B]] meaningful, and the structures with fewer laws are the subject of the topic on [[magmas, quasigroups and loops|BYW6P3R65W]].
