---
tag: ~ad7bce8a
kind: statement
role: theorem
name: Buss's witnessing theorem
aliases: [buss-main-theorem, witnessing-theorem-s12]
msc: ["03F30", "68Q15"]
topics: [RA380RWEC0]
audience: research
uses: [~55a002f3, GVT2NKN37K, TDQ7AXGM6P, Z742YPHPNS, ~5b376b4b, AYRZ98Y0NW]
about: [~55a002f3, ~3d1b2721, Z742YPHPNS]
proofs: [~926bd098]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Buss's witnessing theorem
  - url: https://en.wikipedia.org/wiki/Polynomial_hierarchy
    locator: Definitions
history:
  first_stated: "1985"
  notes: "S. R. Buss, Bounded Arithmetic, PhD thesis, Princeton University, 1985; revised version published by Bibliopolis, Naples, 1986."
---

## Statement

We use Buss's theories $S^i_2$ in the language $0, S, +, \cdot, \floor{x/2}, \abs{x}, \#, \le$ of [[bounded arithmetic|~55a002f3]].
The class $\Sigma^b_i$ counts alternations of bounded quantifiers and ignores sharply bounded quantifiers $(Qx \le \abs{t})$.
For $i \ge 1$, $\square^p_i = \mathrm{FP}^{\Sigma^p_{i-1}}$ is the class of functions computable in [[polynomial time|GVT2NKN37K]] with an oracle for a $\Sigma^p_{i-1}$ set.
So $\square^p_1 = \mathrm{FP}$, the polynomial-time functions, and $\Sigma^p_k$ is the $k$-th level of the [[polynomial hierarchy|TDQ7AXGM6P]].

A function $f : \N^k \to \N$ is $\Sigma^b_i$-definable in a theory $R$ if some $\Sigma^b_i$ formula $A(\bar x, y)$ satisfies three conditions:

1. $A(\bar n, f(\bar n))$ is true in $\N$ for all $\bar n$;
2. $R \vdash \forall \bar x \, \exists y \, A(\bar x, y)$;
3. $R \vdash \forall \bar x \, \forall y \, \forall z \, (A(\bar x, y) \land A(\bar x, z) \to y = z)$.

**Theorem.** Let $i \ge 1$.

1. (Witnessing.) Let $A(\bar x, y)$ be a $\Sigma^b_i$ formula with $S^i_2 \vdash \forall \bar x \, \exists y \, A(\bar x, y)$. Then there is $f \in \square^p_i$ such that $f$ is $\Sigma^b_i$-definable in $S^i_2$ and $A(\bar n, f(\bar n))$ holds for all $\bar n \in \N^k$. Also, $S^i_2$ proves $\forall \bar x \, A(\bar x, f(\bar x))$, with $f$ added to the language by its definition.
2. (Definability.) Every function in $\square^p_i$ is $\Sigma^b_i$-definable in $S^i_2$.
3. (Predicates.) Let $A$ be $\Sigma^b_i$ and $B$ be $\Pi^b_i$ with $S^i_2 \vdash \forall \bar x \, (A(\bar x) \leftrightarrow B(\bar x))$. Then the set defined by $A$ is in $\Delta^p_i = \mathrm{P}^{\Sigma^p_{i-1}}$. Conversely, each $\Delta^p_i$ set is defined in this way.

So the $\Sigma^b_i$-definable functions of $S^i_2$ are exactly the $\square^p_i$ functions.
For $i = 1$: the $\Sigma^b_1$-definable functions of $S^1_2$ are exactly the polynomial-time functions, and the $\Delta^b_1$-definable predicates are exactly the sets in $\mathrm{P}$.

## Remarks

### Why each hypothesis is needed

- The formula $A$ must be $\Sigma^b_i$. For $i = 1$, let $C(x)$ be a $\Pi^b_1$ formula that says "$x$ codes a propositional tautology". Let $A(x, y)$ be $(y = 1 \land C(x)) \lor (y = 0 \land \neg C(x))$. Then $S^1_2 \vdash \forall x \, \exists y \, A(x, y)$ by the law of excluded middle. A witnessing function decides the tautologies, so it is not in $\mathrm{FP}$ unless $\mathrm{P} = \mathrm{NP}$. The formula $A$ is not $\Sigma^b_1$.
- The level must match. With $C$ a $\Sigma^b_1$ formula for satisfiability, the same $A$ is provable and its witness decides an $\mathrm{NP}$-complete set. The witness lies in $\square^p_2$, and it is in $\mathrm{FP}$ only if $\mathrm{P} = \mathrm{NP}$.
- The theory matters. $T^1_2$ proves $S^1_2$ and has induction $\Sigma^b_1$-$\mathrm{IND}$ on the value of $x$. Its $\Sigma^b_1$-definable functions are given by polynomial local search, and $\mathrm{PLS}$ is not known to be in $\mathrm{FP}$.

### Consequences

- $S^1_2$ is a [[feasibly constructive|~3d1b2721]] theory: from a proof of $\forall x \, \exists y \, A$ with $A \in \Sigma^b_1$ one extracts a polynomial-time algorithm for $y$.
- $S^1_2$ is conservative over $\mathsf{PV}_1$ for $\forall \Sigma^b_1$ sentences, when both are formulated with the $\mathsf{PV}$ symbols.
- If $S^1_2$ proves that a $\Sigma^b_1$ property and a $\Pi^b_1$ property are equivalent, the property is in $\mathrm{P}$. So a proof in $S^1_2$ that a set is in $\mathrm{NP} \cap \mathrm{coNP}$ already gives a polynomial-time algorithm.
- An unprovability criterion: let $A \in \Sigma^b_1$, and assume that no polynomial-time function $f$ satisfies $A(n, f(n))$ for all $n$. Then $S^1_2$ does not prove $\forall x \, \exists y \, A(x, y)$.

### Converse

Part 2 is the converse of part 1.
Its proof for $i = 1$ is Buss's bootstrapping, an induction on Cobham's description of $\mathrm{FP}$.

### Generalizations

- For $T^i_2$, the $\Sigma^b_{i+1}$-definable functions are exactly the $\square^p_{i+1}$ functions. This follows from part 1 and the $\Sigma^b_{i+1}$-conservativity of $S^{i+1}_2$ over $T^i_2$ (Buss).
- For $T^1_2$, the $\Sigma^b_1$-definable functions are the functions computed by polynomial local search, the class $\mathrm{PLS}$, followed by a polynomial-time function (Buss and Krajíček).
- The $\forall \Sigma^b_{i+1}$ consequences of $T^i_2$, for $\forall \exists \forall$ formulas, are described by the [[Krajíček-Pudlák-Takeuti theorem|~2d7d49f7]].
- The two-sorted theories of Cook and Nguyen give the same kind of theorem for classes below $\mathrm{P}$. For example, the provably total functions of $V^0$ are the $\mathrm{AC}^0$ functions.

## History

Buss proved the theorem in his 1985 Princeton thesis, published as the book *Bounded Arithmetic* in 1986.
He introduced the theories $S^i_2$ and $T^i_2$ and the smash function $x \# y = 2^{\abs{x} \cdot \abs{y}}$ there.
The proof of part 1 uses free-cut elimination and a witness predicate.
Cook's equational theory $\mathsf{PV}$ of 1975 had given a quantifier-free theory for polynomial time; Buss gave the first-order analogue with quantifiers and induction.

## Explanations

### L1 human

Some proofs that an object exists also show how to find it fast.
Buss found a system of axioms for numbers in which this is always true for a large class of statements.
If the system proves "for every $x$ there is a $y$ with a simple property", then a fast computer program finds such a $y$ from $x$.
Fast means: the number of steps is at most a fixed power of the number of digits of $x$.
Conversely, every fast program can be described and proved total inside the system.

### L2 human

We extract an algorithm from a simple proof in $S^1_2$.

1. $S^1_2$ proves $\forall x \, \exists y \le x \, (y \cdot y \le x \land x < (y + 1) \cdot (y + 1))$, the existence of an [[integer square root|~a28a9bef]].
2. The formula after $\forall x \, \exists y$ is open, so it is $\Sigma^b_1$.
3. The theorem gives a polynomial-time $f$ with $f(x) = \floor{\sqrt x}$.
4. The proof uses polynomial induction, and its step passes from $\floor{x/4}$ to $x$. So $f(x)$ is $2 f(\floor{x/4})$ or $2 f(\floor{x/4}) + 1$, whichever is correct.
5. This recursion has about $\abs{x}/2$ steps, each a multiplication and a comparison.

The typical use is a test: if a statement implies a fast algorithm for a hard problem, it is not provable in $S^1_2$ unless that problem is easy.
A trap is to apply the theorem to a formula $A$ outside $\Sigma^b_1$; the conclusion then fails, as the hypotheses section shows.

### L3 human

The theorem is the bounded-arithmetic analogue of the classical fact that the provably total functions of $\mathsf{I}\Sigma_1$ are the primitive recursive functions.
In both cases a cut-elimination argument turns a proof into a program.
Here the program is built by limited recursion on notation, which matches polynomial induction $\Sigma^b_1$-$\mathrm{PIND}$.

The hierarchy $S^1_2 \subseteq T^1_2 \subseteq S^2_2 \subseteq \cdots$ thus matches the hierarchy $\square^p_1 \subseteq \mathrm{PLS} \subseteq \square^p_2 \subseteq \cdots$ of search problems.
Whether the theories are distinct is the [[separation problem|~4ddef1ef]], and it is tied to the question whether the polynomial hierarchy collapses.
