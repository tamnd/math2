---
tag: RH4R7GTTAX
kind: statement
role: theorem
name: Buss's witnessing theorem
aliases: [buss-main-theorem, witnessing-theorem-s12]
msc: ["03F30", "68Q15"]
topics: [RA380RWEC0]
audience: research
uses: [A2CFPP8JMN, GVT2NKN37K, TDQ7AXGM6P, Z742YPHPNS, YPQPC1WJMV, AYRZ98Y0NW]
about: [A2CFPP8JMN, H1B2VD0KVP, Z742YPHPNS]
proofs: [MBYJP2GY8Z]
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

Buss's witnessing theorem says that a proof of $\forall x \, \exists y \, A(x, y)$ in $S^1_2$, with $A$ a $\Sigma^b_1$ formula, gives a polynomial-time algorithm that finds $y$ from $x$.
Conversely, every polynomial-time function has such a proof.

We use Buss's theories $S^i_2$ of [[bounded arithmetic|A2CFPP8JMN]], whose class $\Sigma^b_i$ ignores sharply bounded quantifiers.
For $i \ge 1$, $\square^p_i = \mathrm{FP}^{\Sigma^p_{i-1}}$ is the class of functions computable in [[polynomial time|GVT2NKN37K]] with an oracle for a set in $\Sigma^p_{i-1}$, a level of the [[polynomial hierarchy|TDQ7AXGM6P]].
So $\square^p_1 = \mathrm{FP}$.
A function $f$ is $\Sigma^b_i$-definable in a theory $R$ if some $\Sigma^b_i$ formula $A(\bar x, y)$ is true of $\bar n$ and $f(\bar n)$ for all $\bar n$, and $R$ proves that $A$ has exactly one $y$ for each $\bar x$.

**Theorem.** Let $i \ge 1$.

1. (Witnessing.) Let $A(\bar x, y)$ be a $\Sigma^b_i$ formula with $S^i_2 \vdash \forall \bar x \, \exists y \, A(\bar x, y)$.
   Then some $f \in \square^p_i$ is $\Sigma^b_i$-definable in $S^i_2$, and $S^i_2$ proves $\forall \bar x \, A(\bar x, f(\bar x))$, with $f$ added by its definition.
   In particular $A(\bar n, f(\bar n))$ is true for all $\bar n$.
2. (Definability.) Every function in $\square^p_i$ is $\Sigma^b_i$-definable in $S^i_2$.
3. (Predicates.) Let $A$ be $\Sigma^b_i$ and $B$ be $\Pi^b_i$ with $S^i_2 \vdash \forall \bar x \, (A(\bar x) \leftrightarrow B(\bar x))$.
   Then $A$ defines a set in $\Delta^p_i = \mathrm{P}^{\Sigma^p_{i-1}}$, and each $\Delta^p_i$ set is defined in this way.

For $i = 1$, the $\Sigma^b_1$-definable functions of $S^1_2$ are exactly the polynomial-time functions, and the $\Delta^b_1$-definable predicates are exactly the sets in $\mathrm{P}$.

## Remarks

### A first use: square roots

The theory $S^1_2$ proves that every number has an [[integer square root|2HXW17RBWP]], in the form below.
$$S^1_2 \vdash \forall x \, \exists y \le x \, (y \cdot y \le x \land x < (y + 1) \cdot (y + 1)).$$
The formula after $\forall x \, \exists y$ has one bounded existential quantifier over an open formula, so it is $\Sigma^b_1$, and the theorem applies.
It gives a polynomial-time $f$ with $f(x) = \lfloor \sqrt x \rfloor$.
The proof by polynomial induction even shows which algorithm: take the root of $\lfloor x/4 \rfloor$, double it, and test whether adding $1$ still gives a square at most $x$.

### Why each hypothesis is needed

The formula $A$ must be $\Sigma^b_1$ when the theory is $S^1_2$.
Let $C(x)$ be a $\Pi^b_1$ formula that says "$x$ codes a propositional tautology", and let $A(x, y)$ be $(y = 1 \land C(x)) \lor (y = 0 \land \neg C(x))$.
Then $S^1_2 \vdash \forall x \, \exists y \, A(x, y)$ by excluded middle.
A witnessing function decides the tautologies, so it is not in $\mathrm{FP}$ unless $\mathrm{P} = \mathrm{NP}$.
The theorem does not apply, because $A$ is a Boolean combination of $\Pi^b_1$ formulas and lies only in $\Sigma^b_2$.
Part 1 for $i = 2$ does apply, and it puts the witness in $\square^p_2 = \mathrm{FP}^{\mathrm{NP}}$, which is correct.

The theory matters too.
$T^1_2$ contains $S^1_2$ and has induction on the value of $x$ for $\Sigma^b_1$ formulas.
Its $\Sigma^b_1$-definable functions are given by polynomial local search, the class $\mathrm{PLS}$, and $\mathrm{PLS}$ is not known to be in $\mathrm{FP}$.

### What it gives you

The theorem makes $S^1_2$ a [[feasibly constructive|H1B2VD0KVP]] theory, and it gives a test for unprovability.
Let $A$ be $\Sigma^b_1$, and assume that no polynomial-time $f$ satisfies $A(n, f(n))$ for all $n$.
Then $S^1_2$ does not prove $\forall x \, \exists y \, A(x, y)$.
So a lower bound in complexity theory becomes an unprovability result in logic.

Part 3 says that if $S^1_2$ proves that a $\Sigma^b_1$ property and a $\Pi^b_1$ property are equivalent, the property is in $\mathrm{P}$.
So a proof in $S^1_2$ that a set is in $\mathrm{NP} \cap \mathrm{coNP}$ already gives a polynomial-time algorithm for it.
With the symbols of [[Cook's PV|FMM44KFZQT]] added, $S^1_2$ proves the same $\forall \Sigma^b_1$ sentences as $\mathsf{PV}_1$.

### The converse

Part 2 is the converse of part 1.
Its proof for $i = 1$ is Buss's bootstrapping, an induction on Cobham's description of $\mathrm{FP}$ by composition and limited recursion on notation.
Each step of such a recursion is matched by one step of polynomial induction.

### Generalizations

For $T^i_2$, the $\Sigma^b_{i+1}$-definable functions are exactly the $\square^p_{i+1}$ functions.
This follows from part 1 and Buss's theorem that $S^{i+1}_2$ is $\forall \exists \Sigma^b_{i+1}$-conservative over $T^i_2$.
For $T^1_2$, Buss and Krajíček showed that the $\Sigma^b_1$-definable functions come from $\mathrm{PLS}$ problems followed by a polynomial-time function.
The [[Krajicek-Pudlak-Takeuti theorem|YP7KE8E6DC]] goes one quantifier further and describes the $\forall \exists \forall$ consequences by a game.
The two-sorted theories of Cook and Nguyen give the same kind of theorem below $\mathrm{P}$; for example, the provably total functions of $V^0$ are the $\mathrm{AC}^0$ functions.

### Watch out

Do not read "$S^1_2$ proves $\forall x \, \exists y \, A$" as enough when $A$ is an arbitrary bounded formula.
The tautology example above has a provable $\forall \exists$ form, and its witness is polynomial-time only if $\mathrm{P} = \mathrm{NP}$.
Check first that $A$ is $\Sigma^b_1$, after the sharply bounded quantifiers are ignored.

The definability class for functions is $\Sigma^b_1$, not $\Delta^b_1$.
A function is defined by a $\Sigma^b_1$ formula with provable existence and uniqueness, and the $\Delta^b_1$ notion belongs to the predicates of part 3.
So the polynomial-time functions are the $\Sigma^b_1$-definable functions, and the polynomial-time sets are the $\Delta^b_1$-definable predicates.

## History

Buss proved the theorem in his 1985 Princeton thesis, published as the book *Bounded Arithmetic* in 1986.
He introduced the theories $S^i_2$ and $T^i_2$ there, and the proof of part 1 uses free-cut elimination and a witness predicate.
Cook's equational theory $\mathsf{PV}$ of 1975 had given a quantifier-free theory for polynomial time, and Buss gave a first-order theory with quantifiers and induction.

## Explanations

### L1 human

Some proofs that an object exists also show how to find it fast.
Buss found a system of axioms for numbers in which this is always true for a large class of statements.
If the system proves "for every $x$ there is a $y$ with a simple property", then a fast computer program finds such a $y$ from $x$.
Fast means that the number of steps is at most a fixed power of the number of digits of $x$.
Conversely, every fast program can be described inside the system and proved to give an answer.

### L2 human

Let us extract an algorithm from the proof that square roots exist, and run it on $x = 45$.
The proof uses polynomial induction, and its step passes from $\lfloor x/4 \rfloor$ to $x$.
So the extracted $f$ computes $f(\lfloor x/4 \rfloor)$, doubles it, and keeps $2 f(\lfloor x/4 \rfloor) + 1$ if its square is at most $x$.
For $x = 45$ we go down through $\lfloor 45/4 \rfloor = 11$ and $\lfloor 11/4 \rfloor = 2$, and $f(2) = 1$.
Then $f(11)$ is $2$ or $3$, and $3^2 = 9 \le 11$ gives $3$; then $f(45)$ is $6$ or $7$, and $7^2 = 49 > 45$ gives $6$.
Check: $6^2 = 36 \le 45 < 49 = 7^2$.
The recursion has about $\lvert x \rvert / 2$ steps, each a multiplication and a comparison, so the algorithm is polynomial-time.
The typical use of the theorem runs the other way: if a statement would give a fast algorithm for a hard problem, then $S^1_2$ does not prove it unless the problem is easy.

### L3 human

The theorem is the bounded-arithmetic analogue of the classical fact that the provably total functions of $\mathsf{I}\Sigma_1$ are the primitive recursive functions.
In both cases a cut-elimination argument turns a proof into a program.
Here the program is built by limited recursion on notation, which matches polynomial induction $\Sigma^b_1$-$\mathrm{PIND}$.

The hierarchy $S^1_2 \subseteq T^1_2 \subseteq S^2_2 \subseteq \cdots$ matches the hierarchy $\square^p_1 \subseteq \mathrm{PLS} \subseteq \square^p_2 \subseteq \cdots$ of search problems.
Whether the theories are distinct is the [[separation problem|PEJQDHHX8E]], and it is tied to the question whether the polynomial hierarchy collapses.
