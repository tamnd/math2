---
tag: 8HEYE9EZMW
kind: statement
role: proposition
name: General associativity
aliases: [generalized-associative-law]
msc: [08A02, 20A05]
topics: [BAZT8JJ70S]
audience: ug1
about: [0K8F7PVDMX, 0M418FE7BB]
uses: [0K8F7PVDMX, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Associative_property
    locator: Generalized associative law
  - book: isbn:9780471433347
    locator: Section 1.1
---

## Statement

Let $S$ be a set with an [[associative|0K8F7PVDMX]] [[binary operation|0M418FE7BB]] $\ast$.
For $n \geq 1$ and $a_1, \ldots, a_n \in S$, define the left product $[a_1 \cdots a_n]$ by recursion: $[a_1] = a_1$, and $[a_1 \cdots a_n] = [a_1 \cdots a_{n-1}] \ast a_n$ for $n \geq 2$.
A bracketing of the sequence $a_1, \ldots, a_n$ is an element of $S$ that is built by these rules:

1. For $n = 1$, the only bracketing is $a_1$.
2. For $n \geq 2$, a bracketing is $x \ast y$, where $1 \leq k \leq n - 1$, $x$ is a bracketing of $a_1, \ldots, a_k$, and $y$ is a bracketing of $a_{k+1}, \ldots, a_n$.

Then each bracketing of $a_1, \ldots, a_n$ is equal to $[a_1 \cdots a_n]$.
Thus all the ways to put parentheses in $a_1 \ast a_2 \ast \cdots \ast a_n$ give the same element, and we write it $a_1 a_2 \cdots a_n$.

## Remarks

### Why each hypothesis is needed

The only hypothesis is that $\ast$ is associative.
Without it, the statement fails already for $n = 3$.
For subtraction on $\mathbb{Z}$, the two bracketings $(5 - 3) - 2 = 0$ and $5 - (3 - 2) = 4$ of $5, 3, 2$ are different.
The order of the elements is fixed in the statement; the proposition does not allow us to permute them.
To permute the factors we also need [[commutativity|099E72KTF8]].

### Consequences

In a [[semigroup|0XMEM406JM]], a [[monoid|0N6R902FG1]] or a [[group|G5S1M9]], the product $g_1 g_2 \cdots g_n$ has one meaning.
In particular, the power $g^n = g g \cdots g$ with $n$ factors is well defined, and this is the start of the [[laws of exponents|00DRK90Z6K]].
The proposition also gives $(a_1 \cdots a_k)(a_{k+1} \cdots a_n) = a_1 \cdots a_n$ for each $k$, which is the form that most proofs use.
For example, the inverse of a product in a group can be checked as $(ab)(b^{-1}a^{-1}) = a(bb^{-1})a^{-1}$.

### Converse

The converse is true: if all bracketings of all sequences of length $3$ agree, then $(a \ast b) \ast c = a \ast (b \ast c)$ for all $a, b, c$, which is associativity.
So the proposition for $n = 3$ is the definition of associativity, and the content of the proposition is the step from $n = 3$ to all $n$.

### Generalizations

The number of bracketings of a sequence of $n$ elements is the [[Catalan number|0YWZJEABB2]] $C_{n-1}$; for $n = 4$ there are $5$ bracketings.
For a [[monoidal category|M3MSQ3NKAE]], where associativity holds only up to a natural isomorphism, the analogous result is the [[coherence theorem|2W2X7EBG2S]] of Mac Lane.

## History

Textbooks of abstract algebra state the result in their first chapter.
For example, Dummit and Foote state it in Section 1.1 as the generalized associative law.

## Explanations

### L1 human

Suppose that brackets never matter for three numbers in a row.
The proposition says that then brackets never matter for four, five or any number of numbers in a row.
For example, with addition, $((1 + 2) + 3) + 4$, $(1 + 2) + (3 + 4)$ and $1 + (2 + (3 + 4))$ are all $10$.
The order of the numbers must stay the same; only the brackets move.

### L2 human

We show by hand that the $5$ bracketings of four elements $a, b, c, d$ agree, using only the law $(xy)z = x(yz)$.

1. $(a(bc))d = ((ab)c)d$, by the law for $x = a$, $y = b$, $z = c$ inside the outer product.
2. $(ab)(cd) = ((ab)c)d$, by the law for $x = ab$, $y = c$, $z = d$.
3. $a((bc)d) = a(b(cd))$, by the law for $x = b$, $y = c$, $z = d$ inside the outer product.
4. $a(b(cd)) = (ab)(cd)$, by the law for $x = a$, $y = b$, $z = cd$.
5. By steps 2 and 4, $a(b(cd)) = ((ab)c)d$, and by step 3, $a((bc)d)$ is the same element.

So all five bracketings equal the left product $((ab)c)d$.
The typical use is silent: a proof writes $g_1 g_2 g_3 g_4$ and then regroups the factors as it needs.
A trap is to regroup and also reorder: $(ab)(cd) = (ac)(bd)$ is false in general, because it moves $b$ past $c$.

### L3 human

The proposition says that the free semigroup on a set, the set of nonempty words with concatenation, is the correct model of all products in an associative structure: a product depends only on the word $a_1 a_2 \cdots a_n$.
The same induction works in any [[magma|9689SFPVE9]] that satisfies the associative law.
In the language of universal algebra, the proposition says that the identity between two bracketings follows from the associative law by equational reasoning.
For structures where associativity holds only up to isomorphism, the Mac Lane coherence theorem plays the same role, and the bracketings form the vertices of the [[associahedra|KPNY26EKNP]] of Stasheff.
In group theory, the proposition is used on every page, mostly without a name, for products, powers and conjugates.
