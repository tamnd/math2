---
tag: TDZVCWYJ9F
kind: concept
name: Functional completeness
aliases: [adequate-set-of-connectives, expressive-adequacy]
msc: ["03B05", "06E30", "08A40", "03B50"]
topics: [JDK63589SA]
audience: ug1
uses: [TT7WT5HPN9, H31CS3HK5P, QS0XVAN9BG, 0X05GS525E, 0GVDFAY4KW]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_completeness
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Functional_completeness
    locator: Characterization of functional completeness
  - url: https://en.wikipedia.org/wiki/Functional_completeness
    locator: Minimal functionally complete operator sets
  - book: isbn:9781482237726
    locator: Chapter 1
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Summary

A set of connectives is functionally complete when it can express every truth table.
Then nothing is lost if a language, a proof system or a chip uses only those connectives.

A truth function of $n$ variables is a map $f : \{ 0, 1 \}^n \to \{ 0, 1 \}$, also called a [[Boolean function|0X05GS525E]].
A set $C$ of [[logical connectives|QS0XVAN9BG]] is functionally complete, or adequate, when every truth function with $n \geq 1$ is the truth function of a [[formula|TT7WT5HPN9]] built from the variables $p_1, \ldots, p_n$ with connectives from $C$ only.
The sets $\{ \neg, \land, \lor \}$, $\{ \neg, \land \}$, $\{ \neg, \lor \}$, $\{ \neg, \to \}$, $\{ \uparrow \}$ and $\{ \downarrow \}$ are functionally complete, and $\{ \land, \lor \}$ and $\{ \to \}$ are not.
[[Post's functional completeness theorem|WGBR7JHBV4]] decides the question for every set of connectives with five tests.

## Motivation

The usual language of propositional logic has five connectives: $\neg$, $\land$, $\lor$, $\to$ and $\leftrightarrow$.
There are $2^{2^n}$ truth functions of $n$ variables, for example $16$ of two variables, so it is a real question whether five connectives can express them all.
Functional completeness says that they can, and that fewer connectives are enough.

This matters in two places.
In logic, a language with few connectives has short definitions and short proofs by induction, and the [[Hilbert system|1MGMQX43B8]] L uses only $\neg$ and $\to$ for this reason.
In circuit design, a gate that is complete by itself, such as the NAND gate, can build every circuit, so a chip needs only one kind of gate.

## Notation

Let $\varphi$ be a formula whose variables are among $p_1, \ldots, p_n$.
Its truth function $f_\varphi$ sends $a = (a_1, \ldots, a_n)$ to the [[truth value|H31CS3HK5P]] of $\varphi$ under the assignment $p_i \mapsto a_i$, and we say that $\varphi$ expresses $f_\varphi$.
A $k$-ary connective is identified with a truth function of $k$ variables, and a formula over $C$ uses connectives from $C$ only.
The Sheffer stroke, or NAND, is $p \uparrow q = \neg(p \land q)$, and the Peirce arrow, or NOR, is $p \downarrow q = \neg(p \lor q)$.
Mendelson says "adequate set of connectives", and some books say "expressively complete".
The [[formal definition|FSZ6PCKN0F]] states the notion for operations on any finite set.

## Remarks

### NAND alone is enough

Here is the whole idea in one computation.
NAND is false only when both inputs are true.
Feed the same variable into both inputs:
$$p \uparrow p = \neg(p \land p) \equiv \neg p.$$
So NAND gives negation.
Now negate a NAND with this trick, and you get conjunction back:
$$(p \uparrow q) \uparrow (p \uparrow q) = \neg (p \uparrow q) = \neg\neg(p \land q) \equiv p \land q.$$
Check at $p = 1$, $q = 0$: here $p \uparrow q = 1$, and $1 \uparrow 1 = 0$, which is the value of $p \land q$.

Negation and conjunction together express everything, as the next two subsections show.
So $\{ \uparrow \}$ is functionally complete, and [[the Sheffer stroke example|PT7VB7691W]] checks every line with truth tables.
The same argument works for NOR, with $\neg p \equiv p \downarrow p$ and $p \lor q \equiv (p \downarrow q) \downarrow (p \downarrow q)$.

### Negation, conjunction and disjunction

Why can $\neg$, $\land$ and $\lor$ express every truth function?
The answer is the [[disjunctive normal form|0GVDFAY4KW]].
Let $f : \{ 0, 1 \}^n \to \{ 0, 1 \}$ with $n \geq 1$.
For a row $a$, the minterm $m_a$ is the conjunction of $p_i$ for $a_i = 1$ and $\neg p_i$ for $a_i = 0$, and it is true at $a$ and false at every other row.
If $f$ takes the value $1$ somewhere, the formula
$$\varphi = \bigvee_{f(a) = 1} m_a$$
is true at a row $b$ exactly when $f(b) = 1$, so it expresses $f$.
If $f$ is constantly $0$, the formula $p_1 \land \neg p_1$ expresses it.
In both cases $\varphi$ uses only $\neg$, $\land$, $\lor$ and the variables $p_1, \ldots, p_n$.

### Moving completeness from one set to another

Suppose $C$ is functionally complete, and each connective of $C$ can be expressed over another set $D$.
Then $D$ is functionally complete too.
For each $k$-ary $c \in C$, fix a formula $\delta_c(p_1, \ldots, p_k)$ over $D$ that expresses $c$.
Translate a formula $\varphi$ over $C$ into a formula $\varphi^*$ over $D$ by recursion: $p^* = p$, and $c(\varphi_1, \ldots, \varphi_k)^*$ is $\delta_c$ with $\varphi_i^*$ put in place of $p_i$.
By [[structural induction|12MQ2NJ29A]], $\varphi^*$ has the same truth function as $\varphi$, because at each row $\delta_c$ computes $c$ of the values of its parts.

With this transfer, one equivalence per connective is enough.
$\{ \neg, \land \}$ is complete because $p \lor q \equiv \neg(\neg p \land \neg q)$.
$\{ \neg, \lor \}$ is complete because $p \land q \equiv \neg(\neg p \lor \neg q)$.
$\{ \neg, \to \}$ is complete because $p \lor q \equiv \neg p \to q$; [[this example|FPJFV3R8QP]] gives the details.
$\{ \uparrow \}$ is complete by the computation above, which expresses $\neg$ and $\land$.

### How to prove that a set is not complete

To show that $C$ is not complete, you cannot just fail to find a formula.
You need an invariant: a property that every connective of $C$ has, that survives composition, and that some function lacks.
Call $f$ 1-preserving when $f(1, \ldots, 1) = 1$.
A variable is 1-preserving.
If $c$ is 1-preserving and $\varphi_1, \ldots, \varphi_k$ are true at the all-ones row, then $c(\varphi_1, \ldots, \varphi_k)$ takes the value $c(1, \ldots, 1) = 1$ there.
So, by structural induction, every formula over a set of 1-preserving connectives is 1-preserving.

The connectives $\land$, $\lor$, $\to$ and $\leftrightarrow$ are all 1-preserving, and $\neg$ is not.
So $\{ \land, \lor, \to, \leftrightarrow \}$ cannot express $\neg p$, and neither can any subset of it, such as $\{ \land, \lor \}$ or $\{ \to \}$.
[[This non-example|H4B12PWDE6]] writes out the proof for $\{ \land, \lor \}$.
Other invariants catch other sets: $\{ \neg, \leftrightarrow \}$ expresses only affine functions, and $\land$ is not affine.

### Only NAND and NOR work alone

Let $\circ$ be a binary connective with $\{ \circ \}$ complete.
If $0 \circ 0 = 0$, every formula over $\{ \circ \}$ is false at the all-zeros row, and $\neg p$ is lost, so $0 \circ 0 = 1$.
In the same way $1 \circ 1 = 0$.
If $0 \circ 1 = 1 \circ 0$, the table of $\circ$ is the table of $\uparrow$ (both values $1$) or of $\downarrow$ (both values $0$).

Suppose instead $0 \circ 1 = 1$ and $1 \circ 0 = 0$.
Then $x \circ y = \neg x$ for all $x, y$, so every formula over $\{ \circ \}$ is equivalent to a literal.
But $p \land q$ is not equivalent to a literal: it differs from $p$ at $(1, 0)$, from $q$ at $(0, 1)$, and from $\neg p$ and $\neg q$ at $(0, 0)$.
The case $0 \circ 1 = 0$, $1 \circ 0 = 1$ gives $x \circ y = \neg y$ and fails in the same way.
So of the $16$ binary connectives, exactly two are complete alone.

### The general setting

For a finite set $A$ with at least two elements, a set $F$ of operations on $A$ is functionally complete when the [[clone|PTKR703G6A]] it generates contains every operation on $A$.
The clone of $F$ is the smallest set of operations that contains $F$ and the projections and is closed under composition.
For $A = \{ 0, 1 \}$ this is the notion above, since variables are projections and connectives applied to formulas are compositions.

A set $F$ is complete exactly when it lies in no maximal clone.
For $A = \{ 0, 1 \}$ there are five maximal clones, and they give [[Post's theorem|WGBR7JHBV4]].
For larger $A$ they are listed by [[Rosenberg's classification|GF1RK91VED]].
For every finite $A$ there are single operations that are complete alone, the [[Sheffer functions|1K829SJG3K]].

### Watch out

A formula may use only the given connectives and variables, and the constants $\top$ and $\bot$ are not free.
For example $\{ \to \}$ is not complete, but $\{ \to, \bot \}$ is, since $\neg p \equiv p \to \bot$.

A completeness proof must express every connective of a set already known to be complete.
Showing $p \lor q \equiv \neg p \to q$ alone proves nothing until you also have $\neg$, which here is in the set.

A non-completeness proof needs an invariant that holds for all formulas over the set.
Saying "I could not find a formula for $\neg p$" is not a proof.

### History

Charles Sanders Peirce found around 1880 that NAND alone, and NOR alone, can express all truth functions, but he did not publish this.
Henry Sheffer published the completeness of a single connective in 1913, and NAND is now called the [[Sheffer stroke|1NNYWRN6B8]].
Emil Post gave the full criterion for sets of Boolean functions in his 1941 monograph *The Two-Valued Iterative Systems of Mathematical Logic*, with the description of all clones on $\{ 0, 1 \}$ now called [[Post's lattice|MA20X7JCET]].

### Try it

Express $p \to q$ with NAND only.
Since $p \to q \equiv \neg(p \land \neg q)$, the answer is $p \uparrow (q \uparrow q)$.
Check at $p = 1$, $q = 0$: $q \uparrow q = 1$ and $1 \uparrow 1 = 0$, which is the value of $p \to q$.

Is $\{ \lor, \leftrightarrow \}$ complete?
No: both connectives are 1-preserving, so $\neg p$ cannot be expressed.

## Explanations

### L1 human

A set of connectives is complete when it can say everything that a truth table can say.
With "not", "and" and "or" we can describe each truth table: we list the rows where the answer is "true".
In fact "not" and "and" are enough, because "$p$ or $q$" means the same as "not (not $p$ and not $q$)".
Even one connective, NAND ("not both"), is enough, and this is why computer chips can be built from NAND gates only.
"And" and "or" alone are not enough: when all inputs are true, every formula made from them is true, so they cannot say "not $p$".

### L2 human

We show that $\{ \neg, \to \}$ is complete and that $\{ \land, \leftrightarrow \}$ is not.
For the first set, express the connectives of the complete set $\{ \neg, \land, \lor \}$:
$$p \lor q \equiv \neg p \to q, \qquad p \land q \equiv \neg(p \to \neg q).$$
Check the second at $p = 1$, $q = 1$: $\neg q = 0$, so $p \to \neg q = 0$, and its negation is $1$, as $p \land q$ is.
Transfer then gives completeness.
For the second set, both connectives give $1$ when both inputs are $1$, so every formula over the set is true at the all-ones row, and $\neg p$ cannot be expressed.
The typical use is in proofs by induction on formulas: if the language has only $\neg$ and $\to$, the induction has only two cases, and completeness says that nothing is lost.

### L3 human

Functional completeness says that a set of operations generates the full clone on $\{ 0, 1 \}$.
The clones on $\{ 0, 1 \}$ form a countable lattice, [[Post's lattice|MA20X7JCET]], and the complete sets are those not contained in any of its five coatoms.
For a finite set with $k \geq 3$ elements the lattice of clones is uncountable, but it still has finitely many coatoms, the maximal clones, and Rosenberg's classification sorts them into six families.
In many-valued logic the same question asks which connectives of a $k$-valued logic express all $k$-valued truth functions.
