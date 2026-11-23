---
tag: NFCEM44XYH
kind: concept
name: Łukasiewicz infinite-valued logic
aliases: [lukasiewicz-infinite-valued-logic, lukasiewicz-logic]
msc: ["03B50", "03B52"]
topics: [WZP584JQ06]
audience: research
uses: [DWYCKAKXZD, 1CE2TGM6MQ, P7E926JK13]
sources:
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: Axioms; Real-valued semantics; General algebraic semantics; Complexity
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 3. Łukasiewicz logic
  - url: https://plato.stanford.edu/entries/lukasiewicz/
    locator: 5.3 More than Three Values; 5.4 Axioms and Definitions
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.4 A continuum of truth values; 4.2 When is a logic finite-valued?
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Relation to Łukasiewicz logic
  - book: isbn:9780792360094
---

## Summary

Suppose "the soup is hot" has truth value $0.7$ and "the soup is safe to eat" has value $0.4$.
Łukasiewicz's implication gives "if hot then safe" the value
$$\min(1, 1 - 0.7 + 0.4) = 0.7.$$
The implication is fully true when the antecedent is no truer than the consequent, and it loses exactly the drop $0.3$ otherwise.
Łukasiewicz infinite-valued logic is the logic of this rule on all of $[0, 1]$.

Exactly, $\mathrm{Ł}_\infty$ is the logic of the matrix on $[0, 1]$ with $\neg x = 1 - x$, $x \to y = \min(1, 1 - x + y)$ and the designated value $1$; see [[the definition|JQ713VVD0G]].
Four axiom schemas with modus ponens prove exactly its tautologies.
Its formulas define exactly the continuous piecewise linear functions with integer coefficients, by [[McNaughton's theorem|E11A9H8Z7Q]], and its algebras are the [[MV-algebras|8T4M7RN9AC]].

## Motivation

Łukasiewicz first used three values for future contingents, in [[Ł3|1CE2TGM6MQ]], and then allowed any number of values with the same formulas.
A continuum of values suits vague predicates, where "hot" or "tall" can hold to any degree.
So $\mathrm{Ł}_\infty$ is the oldest [[fuzzy logic|8DH4QM6AX8]], and it is the logic of the Łukasiewicz t-norm.

The logic also has a clean algebraic theory.
It stands to MV-algebras as classical logic stands to Boolean algebras, and [[Chang's completeness theorem|QM0F33QE9P]] makes this exact.
Later, [[Pavelka logic|YG62F8YC0P]] adds truth constants to it, and the [[arithmetical complexity of first-order Łukasiewicz logic|VAHH1505Z0]] shows what goes wrong with quantifiers.

## Notation

We write $x \oplus y = \min(1, x + y)$ and $x \odot y = \max(0, x + y - 1)$ for strong disjunction and strong conjunction.
Other texts write $\otimes$ or $\&$ for $\odot$; the [[topic|WZP584JQ06]] fixes $\odot$ throughout.
Weak conjunction and disjunction are $\min$ and $\max$, written $\land$ and $\lor$.
We write $\varphi^n$ for $\varphi \odot \dots \odot \varphi$ with $n$ factors, and $n\varphi$ for $\varphi \oplus \dots \oplus \varphi$.

## Remarks

### Three computations

Strong conjunction is not idempotent.
At $p = \tfrac12$ the [[contraction formula|D0S5PRXVZM]] $p \to (p \odot p)$ gets a value below $1$:
$$\tfrac12 \odot \tfrac12 = \max(0, 0) = 0, \qquad \tfrac12 \to 0 = \min(1, \tfrac12) = \tfrac12.$$

Disjunction is definable from implication.
The formula $(p \to q) \to q$ has [[the value max(x, y)|DG496EV8FE]] in both cases of the order.
At $x = 0.8$ and $y = 0.3$ we get $0.8 \to 0.3 = 0.5$, and then $0.5 \to 0.3 = 0.8$.

Double negation holds, since $1 - (1 - x) = x$ for every $x$.
So $\neg\neg p \leftrightarrow p$ is a tautology, unlike in Gödel logic.

### The finite and the infinite

The $n$-valued logics $\mathrm{Ł}_n$ use the same tables on $\{0, \tfrac{1}{n-1}, \dots, 1\}$, and [[Ł3|1CE2TGM6MQ]] is $\mathrm{Ł}_3$.
Every tautology of $\mathrm{Ł}_\infty$ is a tautology of each $\mathrm{Ł}_n$, because the $n$ values form a subalgebra of $[0, 1]$.
The converse also holds for the intersection: a formula valid in every $\mathrm{Ł}_n$ takes the value $1$ at every rational point.
The operations are continuous, so it takes the value $1$ everywhere.
So $\mathrm{Ł}_\infty$ is the intersection of the finite-valued logics, not their union.

### Completeness, weak and strong

A formula is a theorem of the Łukasiewicz axioms with modus ponens exactly when it is a $[0, 1]$-tautology.
The same holds for consequence from a finite set of premises.
It fails for infinite sets, and here is the standard witness.
Let $\Gamma = \{\neg p \to p^n : n \ge 1\}$.
If $v(p) = x < 1$, then $p^n = 0$ for large $n$, and $\neg p \to 0$ has the value $x < 1$.
So every model of $\Gamma$ has $v(p) = 1$, and $\Gamma \models p$.

But a proof uses only finitely many premises, and each finite part fails to give $p$.
For the premises with $n \le N$, take $p = \tfrac{N}{N+1}$, so that $p^n = \tfrac{N + 1 - n}{N + 1} \ge \tfrac{1}{N+1} = 1 - p$.
Then each premise has the value $1$ while $p$ does not, so $\Gamma \not\vdash p$.

### What it is not

Classical logic is not $\mathrm{Ł}_\infty$: the law $p \lor \neg p$ has the value $\max(\tfrac12, \tfrac12) = \tfrac12$ at $p = \tfrac12$.
Gödel and product logic are not $\mathrm{Ł}_\infty$ either, because [[double negation fails in them|XXVXP0S5Q0]].
At $x = 0.5$ the Gödel negation gives $\neg 0.5 = 0$ and $\neg 0 = 1$, so $\neg\neg 0.5 = 1 \ne 0.5$.

### Watch out

Do not use $\land$ where $\odot$ is meant.
Modus ponens in degrees reads $x \odot (x \to y) \le y$.
The version with $\min$ fails: at $x = 0.6$ and $y = 0.2$ we get $x \to y = 0.6$, and $\min(0.6, 0.6) = 0.6 > 0.2$.
Check: $0.6 \odot 0.6 = 0.2$, which is at most $y$.
A second trap is to read $p \odot p$ as a product: at $p = \tfrac12$ it is $0$, not $\tfrac14$.

### History

Łukasiewicz and Tarski presented the infinite-valued logic in their joint paper of 1930, and Łukasiewicz conjectured that his axioms are complete.
Wajsberg claimed a proof, but did not publish it.
Rose and Rosser published the first proof of completeness in 1958.
Chang introduced MV-algebras in 1958 and gave an algebraic proof of completeness in 1959.
McNaughton described the definable functions in 1951, and Mundici showed in 1987 that the tautology problem is coNP-complete.

### Try it

First, compute $0.9 \to 0.5$ and $0.5 \to 0.9$.
The first is $\min(1, 0.6) = 0.6$ and the second is $\min(1, 1.4) = 1$.

Second, at which values is $p \oplus p = 1$?
We need $\min(1, 2x) = 1$, so exactly at $x \ge \tfrac12$.

## Explanations

### L1 human

The truth values are all numbers from $0$ to $1$.
"Not $x$" is $1 - x$.
"If $x$ then $y$" is fully true when $x \le y$, and otherwise it loses exactly the amount by which $x$ exceeds $y$.
With $x = 0.7$ and $y = 0.4$ it loses $0.3$ and has the value $0.7$.
A formula is a law when it gets the value $1$ for every choice of values.

### L2 human

We check that $p \to (q \to p)$ is a tautology.
Let $v(p) = x$ and $v(q) = y$, and compute the inner implication first:
$$v(q \to p) = \min(1, 1 - y + x) \ge x.$$
The inner value is at least $x$, so the outer implication has antecedent at most its consequent:
$$v(p \to (q \to p)) = \min(1, 1 - x + v(q \to p)) = 1.$$
Check at $x = 0.9$, $y = 1$: $q \to p = 0.9$ and $0.9 \to 0.9 = 1$.
This is the typical method: compute a piecewise linear function and show that it is $1$ everywhere.

### L3 human

$\mathrm{Ł}_\infty$ is algebraizable, and its equivalent algebraic semantics is the variety of MV-algebras, which $[0, 1]$ generates.
Mundici's functor $\Gamma$ turns abelian lattice-ordered groups with a strong unit into MV-algebras, and it is an equivalence of categories.
The free MV-algebra on $n$ generators is the algebra of McNaughton functions on $[0, 1]^n$.
Among the three basic t-norm logics, $\mathrm{Ł}_\infty$ is the only one whose implication is continuous, and this is why it admits [[Pavelka-style completeness|YG62F8YC0P]].
