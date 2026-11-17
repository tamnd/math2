---
tag: 7TDHDN8P96
kind: concept
name: Many-sorted logic
aliases: [many-sorted-first-order-logic, multi-sorted-logic]
msc: ["03B10", "03C07"]
topics: [PSRDJXRW53]
audience: grad
uses: [086QKPF0A6, WDVVEYD6AT, 6D3WA7N2W4, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Many-sorted_logic
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: "Chapter: Beyond First-order Logic"
---

## Summary

Many-sorted first-order logic has several domains of objects, one for each sort, instead of one domain.
Each variable has a sort, and each function and relation symbol of the [[signature|WDVVEYD6AT]] says which sorts its arguments and its value have.
Only well-sorted [[terms|6D3WA7N2W4]] and formulas are allowed, and a quantifier $\forall x{:}s$ ranges over the domain of the sort $s$.
Many-sorted logic has the same metatheory as one-sorted [[first-order logic|086QKPF0A6]], to which it reduces by unary predicates for the sorts.

## Motivation

Many structures in mathematics have two or more kinds of objects.
A vector space has scalars and vectors, a graph can be given by vertices and edges, and a geometry has points and lines.
In one-sorted logic, all these objects live in one domain, and each axiom must say which kind of object it speaks about.
Sorts make this bookkeeping part of the syntax, so that ill-sorted expressions such as "scalar plus vector" are not even terms.

## Notation

1. A many-sorted signature has a set $S$ of sorts. A function symbol has a type $f \colon s_1 \times \dots \times s_n \to s$, and a relation symbol has a type $R \subseteq s_1 \times \dots \times s_n$.
2. Each sort $s$ has its own countable set of variables, written $x{:}s$ or $x^s$.
3. A structure $\mathcal{M}$ has a nonempty domain $M_s$ for each sort $s$, and $f^{\mathcal{M}} \colon M_{s_1} \times \dots \times M_{s_n} \to M_s$.
4. Equality is usually one symbol $=_s$ for each sort $s$, between terms of the same sort.
5. In universal algebra, the term part of this syntax is the theory of [[many-sorted algebras|WAQJJ5GX68]].

## Remarks

### Examples

1. [[Vector spaces as two-sorted structures|Z8Z0HGXK6D]], with a sort for scalars and a sort for vectors, describe all vector spaces over all fields in one theory.
2. [[The relativization of a two-sorted sentence|HHZMPDMADJ]] translates many-sorted sentences into one-sorted ones with a unary predicate for each sort.
3. Incidence geometry uses sorts for points and lines and one relation symbol $I$ of type $\mathrm{point} \times \mathrm{line}$.
4. Henkin semantics for second-order logic is a many-sorted first-order logic, with one sort for elements and one sort for each arity of relations.

### Non-examples

1. [[The expression "scalar plus vector"|E65AYA3Q14]] is not a term of the two-sorted language of vector spaces, because $+$ on vectors needs two arguments of the vector sort.
2. Full second-order logic is not a many-sorted first-order logic, because its relation sort must range over all subsets of the domain, not over any nonempty set.
3. A two-sorted structure with an empty domain for one sort is not allowed in the usual semantics, which asks every $M_s$ to be nonempty.

### Basic properties

1. Relativization: add a unary predicate $P_s$ for each sort, and replace $\forall x{:}s \, \varphi$ by $\forall x \, (P_s(x) \to \varphi^*)$ and $\exists x{:}s \, \varphi$ by $\exists x \, (P_s(x) \land \varphi^*)$.
2. With axioms saying that each $P_s$ is nonempty and that each $f$ maps the right sorts to the right sort, $\Sigma \models \varphi$ in many-sorted logic exactly when $\Sigma^* \cup \mathrm{Ax} \models \varphi^*$ in one-sorted logic.
3. So the completeness theorem, the compactness theorem and the Löwenheim-Skolem theorem hold for many-sorted logic.
4. Unique readability and the definitions of free variables and substitution carry over, with sorts checked at each clause.
5. Substitution $\varphi[t/x]$ is defined only when $t$ has the sort of $x$.

### History

Logicians used sorted variables informally for a long time, for example for points and lines in geometry.
Hao Wang's paper of 1952 on the logic of many-sorted theories studied the many-sorted calculus as a formal system.
Henkin's completeness theorem of 1950 for the theory of types treated higher-order logic with general models as many-sorted first-order logic.

### Common errors

1. A student thinks that sorts add expressive power beyond first-order logic. By relativization, they do not.
2. A student forgets that each sort needs a nonempty domain. The relativization then needs the axioms $\exists x \, P_s(x)$.
3. A student applies a function symbol to an argument of the wrong sort, for example writes $v \cdot a$ when the scalar multiplication has type $F \times V \to V$.

## Explanations

### L1 human

Some structures have two kinds of things, like numbers and vectors.
Many-sorted logic gives each kind its own variables.
For example, $a$ and $b$ stand for numbers, and $u$ and $v$ stand for vectors.
Then "$a \cdot v$" makes sense, but "$a + v$" does not, because one cannot add a number to a vector.

### L2 human

We write the axiom $a \cdot (u + v) = a \cdot u + a \cdot v$ of vector spaces in two-sorted and in one-sorted form.

1. Two-sorted: $\forall a{:}F \, \forall u{:}V \, \forall v{:}V \, (a \cdot (u + v) = a \cdot u + a \cdot v)$.
2. One-sorted, with predicates $F$ and $V$: $\forall a \, \forall u \, \forall v \, ((F(a) \land V(u) \land V(v)) \to a \cdot (u + v) = a \cdot u + a \cdot v)$.
3. The one-sorted form also needs axioms such as $\forall a \, \forall v \, ((F(a) \land V(v)) \to V(a \cdot v))$.
4. In the one-sorted form, $a \cdot v$ also has some value when $a$ is a vector, and the axioms say nothing about it.

The typical use of sorts is to write the axioms of structures with several kinds of objects without these side conditions.
A trap: the one-sorted translation must interpret each function symbol on all arguments, including ill-sorted ones.

### L3 human

Many-sorted logic is the base of model theory with imaginaries, where $T^{\mathrm{eq}}$ adds a sort for each definable equivalence relation.
Valued fields are often studied in a three-sorted language, with sorts for the field, the value group and the residue field.
Algebraic specification in computer science uses many-sorted equational logic, and order-sorted logic adds a partial order on the sorts.
Type theory goes further: types can depend on terms, and function types are sorts of their own.
Henkin semantics shows that higher-order logic with general models is a many-sorted first-order logic, so it is complete and compact.
Full second-order logic differs only in its semantics, which fixes the relation sorts to be full power sets.
