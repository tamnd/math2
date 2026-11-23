---
tag: 1DQ1M6ZWS4
kind: definition
name: Definable relations
aliases: [definable-relation, definability-in-a-structure]
msc: ["03B10", "03C07"]
topics: [NJDME6F845]
audience: ug2
defines: CY1TXHF6KQ
uses: [983GZBQYT4, HYJ10AF6RT, 1WTCZB4DVB, NDTJ2E895C, DSQ17TNW1C]
formal:
  - system: lean4
    library: mathlib
    decl: Set.Definable
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Definable_set
    locator: lead section
  - book: isbn:9780122384523
    locator: Chapter 2
---

## Definition

A relation on a structure is definable when one formula of the language picks out exactly its tuples; for example, in $(\mathbb{R}, +, \cdot)$ the formula $\exists y \, (x = y \cdot y)$ picks out the nonnegative reals.

Let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]] with domain $M$, and let $A \subseteq M$.
A relation $R \subseteq M^n$ is definable in $\mathcal{M}$ with parameters from $A$ when there are an $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \ldots, x_n, y_1, \ldots, y_m)$ and elements $b_1, \ldots, b_m \in A$ with
$$R = \{ (a_1, \ldots, a_n) \in M^n : \mathcal{M} \models \varphi[a_1, \ldots, a_n, b_1, \ldots, b_m] \}.$$
Here $\mathcal{M} \models \varphi[\vec{a}, \vec{b}]$ is [[satisfaction|1WTCZB4DVB]] under an assignment that sends $x_i$ to $a_i$ and $y_j$ to $b_j$.
The relation $R$ is definable when it is definable with parameters from $M$.
It is $\emptyset$-definable, or definable without parameters, when it is definable with parameters from $\emptyset$, that is, by a formula whose free variables are among $x_1, \ldots, x_n$.
A function $f \colon M^n \to M$ is definable when its graph is a definable relation in $M^{n+1}$, and an element $b$ is definable when $\{b\}$ is.

## Notation

The relation defined by $\varphi$ is written $\varphi(\mathcal{M})$ or $\varphi(M^n)$, and $\varphi(\mathcal{M}, \vec{b})$ when parameters are used.
For $n = 1$ we speak of a definable set.
In Mathlib, `Set.Definable A L s` says that the set $s$ of tuples is definable in the language $L$ with parameters from $A$.
The [[coincidence lemma|FM580NZ9W6]] is what makes the set $\varphi(\mathcal{M})$ well defined: the answer depends only on the values of the free variables.

## Remarks

### The squares and the order of the reals

Work in the field $(\mathbb{R}, +, \cdot, 0, 1)$, whose signature has no symbol for the order.
Let $\varphi(x) = \exists y \, (x = y \cdot y)$.
For $x = 9$ the witness $y = 3$ gives $9 = 3 \cdot 3$, so $9$ is in the set.
For $x = -1$ no real $y$ works, because $y \cdot y \ge 0$ for every real $y$.
In general $a$ is in the set exactly when $a \ge 0$, because every nonnegative real has a square root.
So $\varphi$ defines the nonnegative reals, without parameters.

Now the order itself comes for free.
Since $b - a \ge 0$ exactly when $b - a$ is a square, we have
$$a \le b \iff \mathcal{M} \models \exists z \, (y = x + z \cdot z)\,[a, b].$$
Check: for $(a, b) = (1, 5)$ take $z = 2$, and $1 + 2 \cdot 2 = 5$.
The strict order $<$ is worked out in [[the order in the field of reals|TCJZNK8PT2]].

### More examples

In $(\mathbb{N}, +)$, the [[even numbers|JY67Q6H6H9]] are $\emptyset$-definable by $\exists y \, (y + y = x)$.
In $(\mathbb{Z}, <)$, the [[successor relation|P50P8AZNEE]] is $\emptyset$-definable by "$x < y$ and nothing lies between", although the signature has no function symbols.
In every structure, the diagonal $\{ (a, a) : a \in M \}$ is $\emptyset$-definable by $x_1 = x_2$.
Every finite subset $\{b_1, \ldots, b_k\}$ of $M$ is definable with parameters, by $x = y_1 \vee \cdots \vee x = y_k$.

### The rules you can use

The relations definable with parameters from $A$ are closed under finite unions, finite intersections and complements, because $\vee$, $\wedge$ and $\neg$ act on the defining formulas.
They are closed under Cartesian products, by putting the two formulas side by side with disjoint variables.
They are closed under projection: if $R \subseteq M^{n+1}$ is defined by $\varphi(\vec{x}, x_{n+1})$, then $\exists x_{n+1} \, \varphi$ defines $\{ \vec{a} : (\vec{a}, c) \in R \text{ for some } c \}$.
In the reals, the order $\le$ is such a projection: it is the ternary relation $y = x + z \cdot z$ with the coordinate $z$ removed.

### Proving that a set is not definable

Every [[automorphism|DSQ17TNW1C]] of $\mathcal{M}$ that fixes each element of $A$ maps each relation definable with parameters from $A$ onto itself.
This follows from [[isomorphism invariance of truth|NDTJ2E895C]], and it is the standard method to prove non-definability.
In $(\mathbb{Z}, +)$, the map $n \mapsto -n$ is an automorphism that moves $1$ to $-1$, so the [[positive integers are not definable|9ZGWM7XXJ5]] without parameters.
In $(\mathbb{R}, <)$, the shift $x \mapsto x + 1$ is an automorphism, so $\{0\}$ is not $\emptyset$-definable, while with the parameter $0$ it is defined by $x = y_1$.

The converse of the method fails: a set can be fixed by all automorphisms without being definable.
The structure $(\mathbb{N}, <)$ has only the identity as an automorphism, so all of its uncountably many subsets are invariant.
But a countable signature and a countable domain give only countably many formulas with parameters, so most of these subsets are not definable.

### Watch out

Parameters change the answer.
In $(\mathbb{R}, <)$, the set $\{0\}$ is definable with parameters but not without, so always say which kind of definability you mean.

A definable relation is defined by one formula.
The set $\mathbb{N}$ is the union of the definable sets $\{0\}, \{1\}, \{2\}, \ldots$ in the field $(\mathbb{R}, +, \cdot, 0, 1)$, but $\mathbb{N}$ itself is not definable there.

Use only the symbols of the signature.
In $(\mathbb{N}, +)$ the term $2 \cdot x$ is not allowed, and you must write $x + x$.

### History

Tarski studied definable sets of real numbers in a paper of 1931.
The automorphism method is related to Padoa's method of 1900 for showing that a primitive notion cannot be defined from the others.

### Try it

Define the number $0$ in $(\mathbb{N}, +)$ without parameters.
Use $x + x = x$: if $a + a = a$ then $a = 0$, and $0 + 0 = 0$.

Is the set $\{2\}$ definable without parameters in $(\mathbb{Z}, +)$?
No: the automorphism $n \mapsto -n$ sends $2$ to $-2$, so every $\emptyset$-definable set that contains $2$ also contains $-2$, and $\{2\}$ does not.

## Explanations

### L1 human

A set is definable when you can describe it with the words of the language and nothing else.
With only plus and times on the real numbers, "is a square" describes exactly the numbers that are zero or positive.
So "zero or positive" is definable, and from that, "less than or equal" is definable too.
To show that something is not definable, find a symmetry of the structure that moves it.

### L2 human

Here is a typical task: is "less than" definable in $(\mathbb{N}, +)$?
Try $\varphi(x, y) = \exists z \, (x + z = y \wedge \neg (z + z = z))$, which says that $y$ is $x$ plus a nonzero number.
For $(2, 5)$, the witness $z = 3$ gives $2 + 3 = 5$ and $3 + 3 \ne 3$, so $\varphi$ holds.
For $(5, 2)$, a witness would need $5 + z = 2$, and no natural number does that, so $\varphi$ fails.
For $(4, 4)$, the only $z$ with $4 + z = 4$ is $z = 0$, and $0 + 0 = 0$, so $\varphi$ fails.
So $\varphi$ defines $<$ on $\mathbb{N}$, and from now on we may use $<$ inside other formulas about $(\mathbb{N}, +)$.

### L3 human

Definable relations are the subject of model theory, which studies the whole family of definable sets of a structure.
Tame classes of structures are defined through this family: in an o-minimal structure, every definable subset of $M$ is a finite union of points and intervals.
By Tarski's quantifier elimination for real closed fields, the definable sets of $(\mathbb{R}, +, \cdot, 0, 1)$ are exactly the semialgebraic sets, which is why $\mathbb{N}$ is not definable there.
The model theory page on the [[definable set|CY1TXHF6KQ]] treats these questions.
