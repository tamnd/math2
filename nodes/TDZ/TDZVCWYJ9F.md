---
tag: TDZVCWYJ9F
kind: concept
name: Functional completeness
aliases: [adequate-set-of-connectives, expressive-adequacy]
msc: ["03B05", "06E30", "08A40", "03B50"]
topics: [JDK63589SA]
audience: ug1
uses: [~7139c138, ~41f42e3d, QS0XVAN9BG, 0X05GS525E, 0GVDFAY4KW]
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

A truth function of $n$ variables is a map $f : \set{0,1}^n \to \set{0,1}$, also called a [[Boolean function|0X05GS525E]].
A set $C$ of [[logical connectives|QS0XVAN9BG]] is functionally complete, or adequate, when every truth function with $n \geq 1$ is the truth function of a [[formula|~7139c138]] built from variables with connectives from $C$ only.
The sets $\set{\neg, \land, \lor}$, $\set{\neg, \land}$, $\set{\neg, \lor}$, $\set{\neg, \to}$, $\set{\uparrow}$ and $\set{\downarrow}$ are functionally complete.
The sets $\set{\land, \lor}$ and $\set{\to}$ are not.
[[Post's functional completeness theorem|WGBR7JHBV4]] decides the question for every set of connectives with five simple tests.

## Motivation

The usual language of propositional logic has five connectives, $\neg$, $\land$, $\lor$, $\to$ and $\leftrightarrow$.
There are $2^{2^n}$ truth functions of $n$ variables, for example $16$ binary ones, and a natural question is whether the five connectives can express all of them.
Functional completeness says yes, and it also says that fewer connectives are enough.
This matters in two places.
In logic, a proof system with few connectives has few axioms and short proofs by induction; the [[Hilbert system|1MGMQX43B8]] L uses only $\neg$ and $\to$ for this reason.
In circuit design, a gate type that is complete alone, such as the NAND gate, can build every circuit.

## Notation

Let $\varphi$ be a formula whose variables are among $p_1, \ldots, p_n$.
Its truth function $f_\varphi : \set{0,1}^n \to \set{0,1}$ sends $a = (a_1, \ldots, a_n)$ to the [[truth value|~41f42e3d]] of $\varphi$ under the assignment $p_i \mapsto a_i$.
A $k$-ary connective is identified with a truth function of $k$ variables.
A formula over $C$ is a formula built from variables with connectives from $C$ only.
The set $C$ is functionally complete when for each $n \geq 1$ and each $f : \set{0,1}^n \to \set{0,1}$ there is a formula $\varphi$ over $C$, with variables among $p_1, \ldots, p_n$, such that $f_\varphi = f$.
We say that $\varphi$ expresses $f$, and that a connective $c$ is expressible over $D$ when some formula over $D$ expresses $c$.
The Sheffer stroke (NAND) is $p \uparrow q = \neg(p \land q)$, and the Peirce arrow (NOR) is $p \downarrow q = \neg(p \lor q)$.
Other names: an adequate set of connectives (Mendelson, Enderton), an expressively complete set.

## Remarks

### Examples

- $\set{\neg, \land, \lor}$ is functionally complete, by the [[disjunctive normal form|0GVDFAY4KW]]; see the basic properties below.
- $\set{\neg, \land}$ and $\set{\neg, \lor}$ are functionally complete, by [[De Morgan's laws|09PKJKA6J0]].
- $\set{\uparrow}$ is functionally complete; [[this example|~bb0e9183]] checks the three needed definitions with truth tables.
- $\set{\neg, \to}$ is functionally complete; [[this example|~6c159f70]] gives the details.
- $\set{\downarrow}$ is functionally complete, with $\neg p \equiv p \downarrow p$ and $p \lor q \equiv (p \downarrow q) \downarrow (p \downarrow q)$.

### Non-examples

- $\set{\land, \lor}$ is not functionally complete: every formula over it is true when all its variables are true, so $\neg p$ cannot be expressed. [[This non-example|~7e2817d5]] gives the full proof.
- $\set{\to}$ is not functionally complete: every formula over it is true when all its variables are true. The same holds for $\set{\land, \lor, \to, \leftrightarrow}$ and for $\set{\to, \lor}$.
- $\set{\neg, \leftrightarrow}$ is not functionally complete: every formula over it expresses an affine function, and $\land$ is not affine; see [[Post's theorem|WGBR7JHBV4]].

### Basic properties

**The set $\set{\neg, \land, \lor}$ is functionally complete.**
Let $f : \set{0,1}^n \to \set{0,1}$ with $n \geq 1$.

1. For $a \in \set{0,1}^n$, the minterm $m_a$ is the conjunction of the literals $p_i$ for $a_i = 1$ and $\neg p_i$ for $a_i = 0$. It is true at $a$ and false at every other assignment.
2. If $f$ takes the value $1$ somewhere, let $\varphi = \bigvee_{f(a) = 1} m_a$. It is true at $b$ exactly when some $m_a$ with $f(a) = 1$ is true at $b$, that is, when $f(b) = 1$. So $f_\varphi = f$.
3. If $f$ is the constant $0$, then $\varphi = p_1 \land \neg p_1$ expresses $f$.
4. In both cases $\varphi$ is a formula over $\set{\neg, \land, \lor}$ with variables among $p_1, \ldots, p_n$.

**Transfer.**
Let $C$ be functionally complete, and let each connective of $C$ be expressible over $D$.
Then $D$ is functionally complete.

1. For each $k$-ary $c \in C$, fix a formula $\delta_c(p_1, \ldots, p_k)$ over $D$ that expresses $c$.
2. To each formula $\varphi$ over $C$ we assign a formula $\varphi^*$ over $D$ by recursion: $p^* = p$ for a variable $p$, and $c(\varphi_1, \ldots, \varphi_k)^* = \delta_c(\varphi_1^*, \ldots, \varphi_k^*)$, the result of substituting $\varphi_i^*$ for $p_i$ in $\delta_c$.
3. By [[structural induction|12MQ2NJ29A]], $\varphi^*$ has the same truth function as $\varphi$, and its variables are among those of $\varphi$. In the induction step, the value of $\delta_c(\varphi_1^*, \ldots, \varphi_k^*)$ at $a$ is $c$ applied to the values of the $\varphi_i^*$, which by the induction hypothesis are the values of the $\varphi_i$.
4. Given $f$, take a formula $\varphi$ over $C$ that expresses $f$. Then $\varphi^*$ is a formula over $D$ that expresses $f$.

**Consequences of transfer.**
Each line expresses the connectives of a set already known to be complete, so each set is complete.

1. $\set{\neg, \land}$: $p \lor q \equiv \neg(\neg p \land \neg q)$, by De Morgan's laws and double negation.
2. $\set{\neg, \lor}$: $p \land q \equiv \neg(\neg p \lor \neg q)$.
3. $\set{\neg, \to}$: $p \lor q \equiv \neg p \to q$, then use item 2.
4. $\set{\uparrow}$: $\neg p \equiv p \uparrow p$ and $p \land q \equiv (p \uparrow q) \uparrow (p \uparrow q)$, then use item 1.
5. $\set{\downarrow}$: $\neg p \equiv p \downarrow p$ and $p \lor q \equiv (p \downarrow q) \downarrow (p \downarrow q)$, then use item 2.

**Preservation arguments for non-completeness.**
To show that $C$ is not complete, find a property of truth functions that every connective of $C$ has, that is kept by composition, and that some function lacks.
For example, call $f$ 1-preserving when $f(1, \ldots, 1) = 1$.

1. A variable $p_i$ expresses a 1-preserving function.
2. Let $c \in C$ be $k$-ary and 1-preserving, and let $\varphi_1, \ldots, \varphi_k$ express 1-preserving functions. At the all-ones assignment each $\varphi_i$ is true, so $c(\varphi_1, \ldots, \varphi_k)$ takes the value $c(1, \ldots, 1) = 1$.
3. By structural induction, every formula over $C$ expresses a 1-preserving function. But $\neg$ is not 1-preserving.
4. Since $\land$, $\lor$, $\to$ and $\leftrightarrow$ are 1-preserving, $\set{\land, \lor, \to, \leftrightarrow}$ is not complete.

**Only two binary connectives are complete alone.**
Let $\circ$ be a binary connective such that $\set{\circ}$ is functionally complete.
Then $\circ$ is $\uparrow$ or $\downarrow$.

1. If $0 \circ 0 = 0$, then every formula over $\set{\circ}$ is false at the all-zeros assignment, by the argument above with $0$ in place of $1$. Then $\neg p$ is not expressible. So $0 \circ 0 = 1$.
2. In the same way, $1 \circ 1 = 0$.
3. If $0 \circ 1 = 1 \circ 0 = 1$, the table of $\circ$ is that of $\uparrow$. If $0 \circ 1 = 1 \circ 0 = 0$, it is that of $\downarrow$.
4. Suppose $0 \circ 1 = 1$ and $1 \circ 0 = 0$. With steps 1 and 2, $x \circ y = \neg x$ for all $x, y$.
5. Then by structural induction each formula over $\set{\circ}$ is equivalent to a literal: $\varphi \circ \psi \equiv \neg\varphi$, and the negation of a formula equivalent to a literal is equivalent to a literal.
6. But $p \land q$ is not equivalent to a literal in $p, q$: at $(1,0)$ it differs from $p$, at $(0,1)$ from $q$, and at $(0,0)$ from $\neg p$ and from $\neg q$. So this case is impossible.
7. The case $0 \circ 1 = 0$ and $1 \circ 0 = 1$ gives $x \circ y = \neg y$ and is impossible in the same way.

**The general setting.**
For a finite set $A$ with at least two elements, a set $F$ of operations $A^n \to A$ is functionally complete when the [[clone|PTKR703G6A]] generated by $F$ contains every operation on $A$.
This clone is the smallest set of operations that contains $F$ and the projections and is closed under composition.
The [[definition node|FSZ6PCKN0F]] states this general form.
For $A = \set{0,1}$ this is the notion above, applied to the truth functions of formulas.
The set $F$ is complete exactly when it lies in no maximal clone; for $A = \set{0,1}$ there are five maximal clones, which give [[Post's theorem|WGBR7JHBV4]], and for larger $A$ they are listed by [[Rosenberg's classification|GF1RK91VED]].
For every finite $A$ there are single operations that are complete alone, the [[Sheffer functions|1K829SJG3K]].

### History

Charles Sanders Peirce found around 1880 that NAND alone, and NOR alone, can express all truth functions, but he did not publish this.
Henry Sheffer published the completeness of a single connective in 1913, and the NAND connective is now called the [[Sheffer stroke|1NNYWRN6B8]].
Emil Post gave the full criterion for sets of Boolean functions in his 1941 monograph "The Two-Valued Iterative Systems of Mathematical Logic", together with the description of all clones on $\set{0,1}$, now called [[Post's lattice|MA20X7JCET]].

### Common errors

- To forget that a formula must use only the given connectives and variables. The constants $\top$ and $\bot$ are not free: $\set{\to, \bot}$ is complete, since $\neg p \equiv p \to \bot$, but $\set{\to}$ is not.
- To show one expressible connective and stop. A proof of completeness must express all the connectives of a set that is already known to be complete.
- To show non-completeness by failing to find a formula. A proof needs an invariant, such as "true when all variables are true", that holds for all formulas over the set.

## Explanations

### L1 human

A set of connectives is complete when it can say everything that a truth table can say.
With "not", "and" and "or" we can describe each truth table: we list the rows where the answer is "true".
In fact "not" and "and" are enough, because "$p$ or $q$" means the same as "not (not $p$ and not $q$)".
Even one connective, NAND ("not both"), is enough, and this is why computer chips can be built from NAND gates only.
"And" and "or" alone are not enough: if all inputs are true, every formula made from them is true, so they cannot say "not $p$".

### L2 human

We show that $\set{\neg, \to}$ is complete and that $\set{\land, \leftrightarrow}$ is not.

1. Over $\set{\neg, \to}$: $p \lor q \equiv \neg p \to q$, and $p \land q \equiv \neg(p \to \neg q)$. So $\neg$, $\land$, $\lor$ are expressible, and transfer from $\set{\neg, \land, \lor}$ gives completeness.
2. Over $\set{\land, \leftrightarrow}$: both connectives give $1$ when both inputs are $1$. By induction every formula over this set is true at the all-ones assignment.
3. The function $\neg p$ is false at $p = 1$, so it is not expressible over $\set{\land, \leftrightarrow}$.

The typical use is in proofs by induction on formulas: if the language has only $\neg$ and $\to$, the induction has only two cases, and completeness guarantees that nothing is lost.
A trap: the formulas $\top$ and $\bot$ count as connectives of arity $0$, and a set that contains $\bot$ can become complete when it was not before.

### L3 human

Functional completeness is the statement that a set of operations generates the full clone on $\set{0,1}$.
Clones on $\set{0,1}$ form a countable lattice, [[Post's lattice|MA20X7JCET]], and the complete sets are those not contained in any of its five coatoms.
For a finite set with $k \geq 3$ elements the lattice of clones is uncountable, but it still has finitely many coatoms, the maximal clones; Rosenberg's classification lists them in six families.
In many-valued logic, the same questions ask which sets of connectives of a $k$-valued logic express all $k$-valued truth functions.
