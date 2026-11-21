---
tag: AJAABP7ZAF
kind: example
name: Finite distance in a real closed field is not type-definable
aliases: [finite-distance-not-type-definable, finite-distance-classes-not-hyperimaginaries]
msc: ["03C45", "03C64", "12J15"]
topics: [SZRM3N6BXW]
audience: research
not_instance_of:
  - target: NQPCDVV3NB
    note: "the relation of being at finite distance is an invariant equivalence relation whose complement is type-definable, so if it were type-definable it would be definable, and then the finite elements would have a supremum"
uses: [N1RV9VNCE8, DSQ17TNW1C, DDY3Q3PJ6W, 0P3VCBDEE2, DTWHAW1N0V, 1NR3HAWG9D, EYTTQZ0E1S, 0G8VEZ3WTK]
sources:
  - book: isbn:9780521119559
---

## Example

Let $T = \mathrm{RCF}$, the theory of [[real closed fields|DDY3Q3PJ6W]], with [[monster model|EYTTQZ0E1S]] $\mathbb{M}$.
Say that $x$ and $y$ are *at finite distance*, written $x \sim y$, if $|x - y| < n$ for some natural number $n$.
Each $n = 1 + \cdots + 1$ is a $\emptyset$-definable element, so $\sim$ is the union of the $\emptyset$-definable relations $|x - y| < n$.
We show that $\sim$ is an [[equivalence relation|0G8VEZ3WTK]] that is not type-definable, so its classes are not [[hyperimaginaries|N1RV9VNCE8]].

1. Equivalence relation. Reflexivity and symmetry follow from $|x - x| = 0 < 1$ and $|x - y| = |y - x|$. If $|x - y| < m$ and $|y - z| < n$, then $|x - z| < m + n$.
2. Complement. The relation $x \not\sim y$ is defined by the partial type $\set{|x - y| \ge n : n \ge 1}$ over $\emptyset$.
3. Suppose $\sim$ were defined by a partial type $\pi(x, y)$ over $\emptyset$. Then $\pi \cup \set{|x - y| \ge n : n \ge 1}$ has no realization in the saturated $\mathbb{M}$, so it is inconsistent.
4. By [[compactness|1NR3HAWG9D]], some formula $\psi$ in $\pi$ and some $N$ satisfy $\psi(x, y) \to |x - y| < N$. Since $\sim$ implies $\psi$, the relation $\sim$ is defined by the formula $|x - y| < N$.
5. Let $F = \set{x : x \sim 0}$, the set of finite elements. By step 4, $F = \set{x : |x| < N}$. But $|N| < N + 1$, so $N \in F$, while $|N| < N$ fails, a contradiction.

Hence $\sim$ is not type-definable over $\emptyset$.

## Remarks

The argument is a special case of a general fact: a relation that is type-definable and has a type-definable complement is definable.
A second proof uses that $T$ is [[o-minimal|DTWHAW1N0V]].
A definable $F$ would be nonempty and bounded above by an infinite element, so it would have a supremum $s$.
If $s$ is finite, then $s + 1 \in F$; if $s$ is infinite, then $s - 1$ is a smaller upper bound.
The relation $\sim$ is invariant under all [[automorphisms|DSQ17TNW1C]] of $\mathbb{M}$, so invariance alone does not make a relation type-definable.
Compare "infinitely close", which is type-definable, see [[this example|BE6P5Y177V]]; its classes are hyperimaginaries.
The same argument shows that $\sim$ is not type-definable over any small set of parameters either.

## Explanations

### L1 human

Two numbers are at finite distance when some ordinary whole number is bigger than their difference.
In a number system with infinitely large numbers, this sorts numbers into groups, one for each "level of infinity".
To describe the rule, we need to say "less than $1$, or less than $2$, or less than $3$, and so on": an endless "or", not an endless "and".
Endless "and" lists are allowed for hyperimaginaries, but endless "or" lists are not, and this rule cannot be rewritten as an endless "and".

### L2 human

We check step 1 on concrete elements of a non-archimedean real closed field, with $\omega$ an infinite element.

1. The elements $\omega$ and $\omega + 5$ are at finite distance, since $|5| < 6$.
2. The elements $\omega$ and $2 \omega$ are not, since $|\omega| \ge n$ for every $n$.
3. Transitivity: $\omega \sim \omega + 5$ and $\omega + 5 \sim \omega + 7$, with bounds $6$ and $3$, give $\omega \sim \omega + 7$ with bound $9$.

The typical use is as the standard example of an invariant equivalence relation that is not type-definable.
A trap is to take "for some $n$" as a list of conditions, as with "infinitely close": it is a disjunction, not a conjunction.
