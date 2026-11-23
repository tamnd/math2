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

A vector space has two kinds of objects, scalars and vectors, and the law $a \ast (u + v) = a \ast u + a \ast v$ only makes sense when $a$ is a scalar and $u$, $v$ are vectors.
Many-sorted logic builds this into the grammar: each variable has a sort, and a quantifier ranges over the objects of one sort only.
It has the same theorems as ordinary [[first-order logic|086QKPF0A6]], but its formulas look like the mathematics they describe.

Exactly, a many-sorted [[signature|WDVVEYD6AT]] has a set $S$ of sorts.
Each function symbol has a type $f \colon s_1 \times \dots \times s_n \to s$, and each relation symbol a type $R \subseteq s_1 \times \dots \times s_n$, with all $s_i$ and $s$ in $S$.
Each sort has its own variables, and $f(t_1, \dots, t_n)$ is a [[term|6D3WA7N2W4]] of sort $s$ only when each $t_i$ is a term of sort $s_i$.
A [[structure|983GZBQYT4]] gives a nonempty domain $M_s$ for each sort $s$ and maps $f^{\mathcal{M}} \colon M_{s_1} \times \dots \times M_{s_n} \to M_s$.
A quantifier $\forall x{:}s$ ranges over $M_s$.

## Motivation

Many structures have several kinds of objects.
A vector space has scalars and vectors, a graph can be given by vertices and edges, and a plane geometry has points and lines.
In one-sorted logic all of these live in one domain, and each axiom must say which kind of object it speaks about.
Sorts make this bookkeeping part of the syntax, so that an expression such as "scalar plus vector" is not even a term.

Sorts also matter outside mathematics.
Typed programming languages and proof assistants check sorts as types, and algebraic specification of software uses many-sorted equational logic.
Later sub-areas use sorts for second-order logic with general models and for the imaginaries of model theory.

## Notation

Books write a variable of sort $s$ as $x{:}s$, $x^s$ or $x_s$, and a function type as $f \colon s_1 \times \dots \times s_n \to s$ or $f \colon s_1 \cdots s_n \to s$.
Equality is usually one symbol $=_s$ for each sort, used only between terms of the same sort, and the subscript is often dropped.
The term part of this syntax is the theory of [[many-sorted algebras|WAQJJ5GX68]] in universal algebra.

## Remarks

### A two-sorted theory

The standard example is [[vector spaces as two-sorted structures|Z8Z0HGXK6D]].
The sorts are $F$ for scalars and $V$ for vectors, and scalar multiplication has the type $\ast \colon F \times V \to V$.
One theory then has all vector spaces over all fields as its models.
It can also quantify over scalars, so "$\dim \ge 2$" becomes the single sentence
$$\exists u{:}V \, \exists v{:}V \, \forall a{:}F \, \forall b{:}F \, \big( a \ast u + b \ast v = 0_V \to (a = 0_F \land b = 0_F) \big).$$
Incidence geometry is another example, with sorts for points and lines and one relation symbol $I$ of type $\mathrm{point} \times \mathrm{line}$.

### What the sorts rule out

Sorts reject ill-formed expressions before any question of truth comes up.
In the language of vector spaces, [[adding a scalar to a vector is not a well-sorted term|E65AYA3Q14]], because $+_V$ needs two arguments of sort $V$ and $+_F$ needs two of sort $F$.
In the same way $v \ast a$ is not a term, since $\ast$ wants its scalar first.
A structure with an empty domain for one sort is also ruled out in the usual semantics, which asks each $M_s$ to be nonempty.

### Back to one sort

Sorts add convenience but no power.
Add a unary relation symbol $P_s$ for each sort $s$, and translate each formula $\varphi$ to $\varphi^*$ by
$$(\forall x{:}s \, \psi)^* = \forall x \, (P_s(x) \to \psi^*), \qquad (\exists x{:}s \, \psi)^* = \exists x \, (P_s(x) \land \psi^*).$$
Add axioms $\mathrm{Ax}$ that say each $P_s$ is nonempty and each function symbol maps arguments of the right sorts to a value of the right sort.
Then for sentences, $\Sigma \models \varphi$ holds in many-sorted logic exactly when $\Sigma^* \cup \mathrm{Ax} \models \varphi^*$ holds in one-sorted logic.
[[The relativization of a two-sorted sentence|HHZMPDMADJ]] carries this out in full.
So completeness, compactness and the Löwenheim-Skolem theorem hold for many-sorted logic too.
Unique readability, free variables and substitution carry over, with one extra rule: $\varphi[t/x]$ is defined only when $t$ has the sort of $x$.

### Watch out

The first trap is to think that sorts make the logic stronger than first-order logic; the translation above shows they do not.
The second trap is to forget the nonempty axioms $\exists x \, P_s(x)$.
Without them, a one-sorted structure may have no element of sort $s$, and then $\forall x \, (P_s(x) \to x \neq x)$, the translation of $\forall x{:}s \, (x \neq x)$, is true there although no many-sorted structure makes it true.
The third trap is the order of arguments: with $\ast \colon F \times V \to V$, the expression $v \ast a$ is not a term, although books write both $av$ and $va$.

### History

Logicians used sorted variables informally for a long time, for example for points and lines in geometry.
Henkin's completeness theorem of 1950 for the theory of types treated higher-order logic with general models as a many-sorted first-order logic.
Hao Wang studied the many-sorted calculus as a formal system in a paper of 1952 on the logic of many-sorted theories.

### Try it

In the two-sorted language of vector spaces, is $(a \cdot_F b) \ast (u +_V v)$ a term, and of which sort?
Yes: $a \cdot_F b$ has sort $F$ and $u +_V v$ has sort $V$, so $\ast$ gives a term of sort $V$.

Relativize $\exists v{:}V \, \forall a{:}F \, (a \ast v = v)$.
The answer is $\exists v \, \big( P_V(v) \land \forall a \, (P_F(a) \to a \ast v = v) \big)$, which is true in every vector space with $v = 0_V$.

## Explanations

### L1 human

Some structures have two kinds of things, like numbers and arrows in the plane.
Many-sorted logic gives each kind its own letters: $a$ and $b$ for numbers, $u$ and $v$ for arrows.
Then "$2$ times the arrow $(1, 3)$" makes sense and gives $(2, 6)$.
But "$2$ plus the arrow $(1, 3)$" is not allowed, because the rules of the language forbid it before anyone asks what it means.

### L2 human

We write the law $a \ast (u + v) = a \ast u + a \ast v$ in two-sorted and in one-sorted form.
The two-sorted form is
$$\forall a{:}F \, \forall u{:}V \, \forall v{:}V \, \big( a \ast (u +_V v) = a \ast u +_V a \ast v \big).$$
The one-sorted form, with unary predicates $F$ and $V$ for the sorts, is
$$\forall a \, \forall u \, \forall v \, \big( (F(a) \land V(u) \land V(v)) \to a \ast (u + v) = a \ast u + a \ast v \big).$$
The one-sorted theory also needs closure axioms such as $\forall a \, \forall v \, \big( (F(a) \land V(v)) \to V(a \ast v) \big)$.
And in a one-sorted structure, $a \ast v$ has some value even when $a$ is a vector, about which the axioms say nothing.
This is the typical gain of sorts: the axioms are written without side conditions and without meaningless terms.
Watch out that the one-sorted translation must still give each function symbol a value on ill-sorted arguments.

### L3 human

Many-sorted logic underlies model theory with imaginaries, where $T^{\mathrm{eq}}$ adds a sort for each definable equivalence relation.
Valued fields are often studied in a three-sorted language, with sorts for the field, the value group and the residue field.
Algebraic specification uses many-sorted equational logic, and order-sorted logic adds a partial order on the sorts.
Type theory goes further: types can depend on terms, and function types are sorts of their own.
Henkin semantics shows that higher-order logic with general models is a many-sorted first-order logic, so it is complete and compact.
Full second-order logic differs only in its semantics, which forces the relation sorts to be full power sets.
