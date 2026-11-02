---
tag: S9FVESJ0CS
kind: statement
role: lemma
name: Lambek's lemma
msc: [18C10]
uses: [28NQ0KRHD3, EK85VSSRMR, 0MWKJ44V5A, 00E0YZCERH]
about: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Initial_algebra
---

## Statement

Let $F \colon \mathcal{C} \to \mathcal{C}$ be a [[functor|28NQ0KRHD3]].
An $F$-algebra is a pair $(A, a)$ of an object $A$ and a morphism $a \colon F(A) \to A$.
A morphism of $F$-algebras $h \colon (A, a) \to (B, b)$ is a morphism $h \colon A \to B$ with $h \circ a = b \circ F(h)$.
If $(I, i)$ is an [[initial object|EK85VSSRMR]] of the category of $F$-algebras, then $i \colon F(I) \to I$ is an isomorphism.

## Remarks

The pair $(F(I), F(i))$ is an $F$-algebra, so by initiality there is a unique algebra morphism $j \colon (I, i) \to (F(I), F(i))$.
Then $i \circ j$ is an algebra morphism from $(I, i)$ to itself, so it equals $\id_I$ by uniqueness.
Also $j \circ i = F(i) \circ F(j) = F(i \circ j) = \id_{F(I)}$, using that $j$ is an algebra morphism.
So $j$ is the inverse of $i$.

Example: on the category of sets let $F(X) = 1 + X$, where $1 = \set{*}$.
The initial $F$-algebra is the set of [[natural numbers|0MWKJ44V5A]] with the map sending $*$ to $0$ and $n$ to $n + 1$.
The lemma says that this map $1 + \N \to \N$ is a bijection: every natural number is either $0$ or a successor, in exactly one way.

Example of a consequence: the [[power set|00E0YZCERH]] functor on sets has no initial algebra.
An initial algebra would give a bijection between a set and its power set, which Cantor's theorem rules out.

The dual statement holds as well: the structure map of a terminal $F$-coalgebra is an isomorphism.

## Explanations

### L1 human

An initial algebra is the smallest structure built by a recipe $F$, like the natural numbers built from zero and successor.
The lemma says that such a structure is a fixed point of the recipe: applying the recipe once more gives nothing new.
For lists, it says that every list is either empty or an element followed by a list, in a unique way.

### L2 human

The lemma is the starting point of the theory of inductive and coinductive data types.
It shows that an initial algebra, when it exists, is a fixed point $F(I) \cong I$ of the functor.
It also gives quick non-existence results, as with the power set functor.
Its dual, for terminal coalgebras, says that infinite streams over $A$ satisfy $A \times S \cong S$.
