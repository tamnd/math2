---
tag: QM0F33QE9P
kind: statement
role: theorem
name: Chang's completeness theorem
aliases: [changs-completeness-theorem, chang-completeness-mv-algebras]
msc: ["03B50", "06D35"]
topics: [WZP584JQ06]
audience: research
about: [NFCEM44XYH]
uses: [JQ713VVD0G, AJNZJD8442]
proofs: [XDK66G0FSD]
history:
  first_stated: "Chang 1958"
  notes: "Wikipedia dates the theorem to Chang's papers of 1958 and 1959."
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Relation to Łukasiewicz logic
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: General algebraic semantics
  - book: isbn:9780792360094
---

## Statement

An MV-algebra is a structure $\langle A, \oplus, \neg, 0 \rangle$ that satisfies these identities:

1. $(x \oplus y) \oplus z = x \oplus (y \oplus z)$, $x \oplus 0 = x$ and $x \oplus y = y \oplus x$;
2. $\neg \neg x = x$ and $x \oplus \neg 0 = \neg 0$;
3. $\neg(\neg x \oplus y) \oplus y = \neg(\neg y \oplus x) \oplus x$.

The standard MV-algebra is $[0, 1]$ with $x \oplus y = \min(1, x + y)$, $\neg x = 1 - x$ and $0$.

**Theorem.**

1. An equation $s = t$ in the language $\oplus, \neg, 0$ holds in the standard MV-algebra iff it holds in every MV-algebra.
2. Equivalently, the standard MV-algebra generates the [[variety|AJNZJD8442]] of all MV-algebras.
3. A formula of [[infinite-valued Łukasiewicz logic|JQ713VVD0G]] is a $[0, 1]$-tautology iff it has value $1$ under every valuation in every MV-algebra.

## Remarks

### Why each hypothesis is needed

1. Generation is meant in the sense of varieties, not of subalgebras of powers.
   [[Chang's MV-algebra|8T4M7RN9AC]] has an element $\varepsilon \neq 0$ with $n \varepsilon \le \neg \varepsilon$ for all $n$.
   In a power of $[0, 1]$ such an element has all coordinates $0$, so Chang's algebra is not a subalgebra of a power of $[0, 1]$.
2. The algebra $[0, 1]$ cannot be replaced by a finite chain $\set{0, \tfrac{1}{n-1}, \dots, 1}$.
   That chain satisfies $x \oplus \dots \oplus x = x \oplus \dots \oplus x$ with $n$ and $n - 1$ summands, and $[0, 1]$ does not.
3. The rational chain $[0, 1] \cap \mathbb{Q}$ can replace $[0, 1]$.
   The proof gives counterexamples with rational values.

### Consequences

1. Validity in the standard MV-algebra is the same as validity in all MV-algebras, and the same as validity in all linearly ordered MV-algebras.
2. With the fact that the Lindenbaum-Tarski algebra of the Łukasiewicz axioms is an MV-algebra, item 3 gives the completeness of the axioms of [[Łukasiewicz logic|NFCEM44XYH]] for $[0, 1]$-tautologies.
3. Wikipedia lists provability, validity in all MV-algebras, validity in all linear MV-algebras and validity in $[0, 1]$ as equivalent conditions, after Hájek 1998.
4. A formula that is not a tautology fails at a rational point. So the set of tautologies is co-recursively enumerable, which also follows from its decidability.

### Converse

The converse direction of item 1 is immediate: $[0, 1]$ is an MV-algebra, so an equation that holds in every MV-algebra holds in $[0, 1]$.
The content of the theorem is the other direction.

### Generalizations

1. Wikipedia reports Mundici's categorical equivalence between MV-algebras and abelian lattice-ordered groups with strong unit.
2. For the finite-valued logics, Wikipedia reports that the right algebras are the $\mathrm{MV}_n$-algebras of Grigolia (1977).
3. SEP gives the analogous completeness of MTL with respect to MTL-chains as the first step to standard completeness, after Jenei and Montagna (2002).

## History

Wikipedia states that Chang devised MV-algebras to study many-valued logics and dates his completeness theorem to his papers of 1958 and 1959.
The first published proof of completeness of the Łukasiewicz axioms, by Rose and Rosser in 1958, was syntactic, according to SEP.
Chang's proof was algebraic.
The book of Cignoli, D'Ottaviano and Mundici is a standard modern account.

## Explanations

### L1 human

Boolean algebras obey the same equations as the two values $0$ and $1$.
Chang's theorem says the same thing for MV-algebras and the interval $[0, 1]$.
If an equation is true for all numbers in $[0, 1]$, then it is true in every MV-algebra.

### L2 human

We use the theorem to check an MV-algebra identity by a computation with real numbers.
For example, $x \oplus y = y \oplus x$ is true in $[0, 1]$, so it is true in every MV-algebra.
A less direct example is the identity $(x \to y) \lor (y \to x) = 1$, which holds in every MV-algebra because $[0, 1]$ is a chain.

A trap: the theorem does not say that every MV-algebra is a subalgebra of a power of $[0, 1]$.
Chang's MV-algebra is a counterexample, because it has nonzero infinitesimals.

### L3 human

The proof has three steps.
First, an equation that fails in an MV-algebra fails in a linearly ordered MV-algebra, by subdirect representation.
Second, a linearly ordered MV-algebra is an interval $[0, u]$ of a totally ordered abelian group, by Chang's representation.
Third, the failure involves finitely many linear inequalities with integer coefficients, and these have a rational solution.
Scale the solution so that $u = 1$, and the equation fails in $[0, 1]$.

The third step is the analytic core.
Its form explains why McNaughton functions are piecewise linear with integer coefficients.
