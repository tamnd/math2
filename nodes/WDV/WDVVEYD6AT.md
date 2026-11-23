---
tag: WDVVEYD6AT
kind: concept
name: Signature
aliases: [vocabulary, similarity-type, first-order-language]
msc: ["03C07", "03B10"]
topics: [PSRDJXRW53]
audience: ug2
uses: [MSXX2P86CY, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Signature_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
  - url: https://builds.openlogicproject.org/
    locator: "Chapter: Syntax and Semantics"
same_as:
  wikidata: Q741810
  wikipedia: Signature (logic)
---

## Summary

A signature is the list of special symbols that a first-order language may use, each with the number of inputs it takes.
For ordered fields the list is
$$\{ +, \cdot, -, 0, 1, < \},$$
where $+$ and $\cdot$ take two inputs, $-$ takes one, $0$ and $1$ take none, and $<$ is a relation of two inputs.
With these symbols you can write $x \cdot (y + 1)$ and $0 < x$, but not $\sqrt{x}$ or $x \le y$, since those symbols are not on the list.

Exactly, a [[signature|PWHJZYBNEY]] $\sigma$ consists of a set of function symbols and a disjoint set of relation symbols, together with an [[arity|MSXX2P86CY]] in $\{ 0, 1, 2, \dots \}$ for each symbol.
A function symbol of arity $0$ is a constant symbol.
The signature holds only the non-logical symbols: the variables, connectives, quantifiers, parentheses and the equality symbol are logical, and every language has them.
Terms, formulas and [[structures|983GZBQYT4]] are always taken over a fixed signature.

## Motivation

The same set $\mathbb{Z}$ can be studied as an ordered set, as a group or as a ring.
Each view uses different symbols, so different statements make sense.
In the signature $\{ < \}$ the sentence $\forall x \, \exists y \, (x < y)$ makes sense, but $\forall x \, (x \cdot 1 = x)$ does not, because $\cdot$ and $1$ are missing.
The signature makes this choice explicit before any axioms are written.

Fixing the symbols first also lets us state results for all languages at once.
The [[compactness theorem|1NR3HAWG9D]] and the [[Löwenheim-Skolem theorem|484M0TZ1S7]] hold for every signature, with the size of the signature as a parameter.
Many proofs work by changing the signature, for example by adding new constants, so the notion returns throughout logic.

## Notation

Books write $\sigma$, $\tau$, $L$ or $\mathcal{L}$, and we write $\sigma$, with "$\sigma$-term" and "$\sigma$-formula" for the terms and formulas over $\sigma$.
Other names are vocabulary, similarity type and language.
The arity of a symbol $s$ is $\operatorname{ar}(s)$, and arities are often listed in order, as in "$\{ +, \cdot, 0 \}$ with arities $2, 2, 0$".
In Mathlib a signature is `FirstOrder.Language`, with families `Functions n` and `Relations n` of symbols indexed by the arity $n$.

## Remarks

### Reading a signature

Take the ring signature $\{ +, \cdot, -, 0, 1 \}$ with arities $2, 2, 1, 0, 0$.
It has five function symbols, two of them constants, and no relation symbols.
So every atomic formula over it is an equation, such as $x \cdot (y + z) = x \cdot y + x \cdot z$.
The order signature $\{ < \}$ is the opposite case: one binary relation symbol and no function symbols, so the only terms are the variables.
The signatures of set theory, $\{ \in \}$, and of graphs, $\{ E \}$, also have a single binary relation symbol.
The empty signature has no symbols at all, and its formulas are built from equations $x = y$ alone, so they can talk only about how many elements there are.
More languages are collected in [[standard first-order languages|CG8FE46WJC]].

### One structure, two signatures

Groups can be described in $\{ \cdot, e, {}^{-1} \}$ or in $\{ \cdot \}$ alone, as in [[groups in two signatures|CBKC2DMXEQ]].
Both give the same groups, but not the same substructures.
In $\{ \cdot \}$ the set $\mathbb{N}$ is a substructure of $(\mathbb{Z}, +)$, since it is closed under $+$, yet it is not a subgroup.
In the larger signature a substructure must also contain the value of $e$ and be closed under ${}^{-1}$, so it is a subgroup.

A signature can also be very large.
[[A constant for each real number|Z5YZ05NYDR]] gives an uncountable signature, which lets $\mathbb{R}$ name all of its own elements.

### What a signature is not

[[One symbol for unary and binary minus|YG6J9BDB67]] is not a signature, because each symbol has exactly one arity.
"A binary operation $\cdot$ that is associative" is not a signature either: associativity is an axiom, and a set of axioms over $\sigma$ is a [[first-order theory|92SWXST1ZM]].
The bare set $\{ +, \cdot \}$ is not a signature until the arities are given, since the letter $+$ could be binary in one language and ternary in another.
And $=$ is not in the signature in most books, because it is a logical symbol with a fixed meaning.

### The first facts

When $\sigma$ is countable, there are countably many $\sigma$-terms and $\sigma$-formulas; in general there are $\max(|\sigma|, \aleph_0)$ of each.
When $\sigma \subseteq \sigma'$, every $\sigma$-formula is a $\sigma'$-formula.
A $\sigma'$-structure becomes a $\sigma$-structure, its reduct, when we forget the extra symbols, and $\sigma$-formulas are true in the same places in both.
Every signature can be made relational: a function symbol $f$ of arity $n$ becomes a relation symbol $R_f$ of arity $n + 1$ for the graph of $f$.

### Watch out

A symbol and its meaning are two different things.
The symbol $+$ is a mark in $\sigma$, and addition on $\mathbb{Z}$ is one meaning for it among many.
In the structure $(\{ 0, 1 \}, +)$ with $+$ read as addition modulo $2$, the term $1 + 1$ has the value $0$.
So a question such as "is $1 + 1 = 2$ true?" has no answer until a structure is chosen.

### History

Birkhoff's paper of 1935 on abstract algebras described an algebra by its operations and their arities, which universal algebra calls the type of the algebra.
Model theory later added relation symbols to this data, and the name "similarity type" comes from that tradition.

### Try it

Which of these are terms over the ring signature: $x + 1$, $-(x \cdot y)$, $x < 1$?
The first two are terms; $x < 1$ uses a relation symbol that the ring signature lacks.

How many relation symbols does the signature of ordered fields have?
Exactly one, the symbol $<$; the other five symbols are function symbols, and two of them are constants.

## Explanations

### L1 human

Before writing rules for a game, you list the pieces you may use.
A signature is that list for a mathematical language.
For groups, one may take a symbol $\cdot$ that joins two things, a symbol ${}^{-1}$ that acts on one thing, and a constant $e$.
The rules of groups, such as associativity, come later and are not part of the list.
For example, $x \cdot e$ uses only listed symbols, but $x + e$ does not, because $+$ is not on the list.

### L2 human

We replace the function symbol $\cdot$ of groups by a relation symbol, as in the last of the first facts.
Let $M$ be a ternary relation symbol, and read $M(x, y, z)$ as "$x \cdot y = z$".
One axiom says that $M$ is the graph of a function:
$$\forall x \, \forall y \, \exists z \, \big(M(x, y, z) \land \forall w \, (M(x, y, w) \to w = z)\big).$$
The new signature has no function symbols, so the term $x \cdot (y \cdot z)$ has no direct translation.
Instead, the equation $x \cdot (y \cdot z) = w$ becomes
$$\exists u \, \big(M(y, z, u) \land M(x, u, w)\big),$$
with a new variable $u$ for the inner value $y \cdot z$.
Check in $(\mathbb{Z}, +)$ with $x = 1$, $y = 2$, $z = 3$: then $u = 5$ and $w = 6$, and indeed $1 + (2 + 3) = 6$.
Every formula over $\{ \cdot \}$ translates in this way, with the same truth in every group.
Relational signatures are common in finite model theory and in proofs where terms get in the way.
Watch out: without the graph axiom, a structure for $\{ M \}$ need not come from any binary operation.

### L3 human

A signature is the data of a first-order language, and the logic itself is the same for every signature.
Many proofs change the signature on purpose: Henkin's proof of completeness adds new constants, Skolemization adds function symbols, and Morleyization adds one relation symbol for each formula.
The elementary diagram of a structure $\mathcal{M}$ uses $\sigma$ with one new constant for each element of $M$; in Mathlib this expansion is `FirstOrder.Language.withConstants`, written `L[[A]]`.
[[Many-sorted logic|7TDHDN8P96]] uses signatures that also list sorts, so that each symbol has a sort for each argument and for its value.
In categorical logic a purely functional signature with equational axioms gives a Lawvere theory, and its models are product-preserving functors into sets.
