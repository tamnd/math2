---
tag: ZVR0ZW6DF3
kind: example
name: A table of cases does not decide a quantified statement
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 05RSK4Q657
    note: the rows are instances of a predicate over an infinite domain, not all assignments of truth values to finitely many variables
uses: [05RSK4Q657, 0GHS47PDAQ, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Truth_table
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Formula_for_primes
    locator: lead section
---

## Example

Consider the statement $S$: "for every natural number $n$, the number $n^2 + n + 41$ is [[prime|01826KMG2H]]".
A student makes a table of the values of $P(n)$: "$n^2 + n + 41$ is prime" for $n = 0, 1, \dots, 39$, and finds the value $\mathsf{T}$ in every row.
We show that this table is not a [[truth table|05RSK4Q657]] of $S$ and does not decide $S$.

1. A truth table has one row for each assignment of truth values to finitely many propositional variables. The statement $S$ has no propositional variables: it is a [[universal statement|0GHS47PDAQ]] about infinitely many numbers.
2. The table checks the instances $P(0), \dots, P(39)$. For example, $P(0)$ is "$41$ is prime", $P(1)$ is "$43$ is prime" and $P(2)$ is "$47$ is prime", and each is true.
3. The statement $S$ has infinitely many instances, one for each $n$. No finite table lists all of them.
4. The instance $n = 40$ gives $40^2 + 40 + 41 = 1600 + 81 = 1681 = 41 \cdot 41$, which is not prime.
5. So $S$ is false, although every row of the table is true.

## Remarks

The example shows the limit of the truth table method.
A truth table decides a formula of propositional logic, because such a formula has only $2^n$ cases.
A statement with a quantifier over an infinite domain has infinitely many cases, and a finite list of them proves nothing about the rest.

The numbers can be checked by factoring: $40^2 + 40 + 41 = 40 \cdot 41 + 41 = 41 \cdot 41$.
In the same way, $n = 41$ gives $41^2 + 41 + 41 = 41 \cdot 43$, so this instance also fails.
For a finite domain, the method does work: a universal statement over $\set{0, 1, \dots, 39}$ is a conjunction of $40$ instances, and the table decides it.

## Explanations

### L1 human

The rule "$n^2 + n + 41$ is always prime" works for $n = 0$, $1$, $2$ and all the way to $39$.
That is forty successes in a row.
At $n = 40$ the result is $1681$, which is $41$ times $41$.
So the rule is false.
Checking many cases is not the same as checking all cases.

### L2 human

We separate the propositional part of a statement from its quantifier.

1. Write $S$ as $\forall n\, P(n)$, where $P(n)$ is an open sentence.
2. For one fixed $n$, the statement $P(n)$ is a single proposition with one truth value.
3. Formulas of the form $P(n) \to P(n)$ or $P(n) \lor \neg P(n)$ are tautologies by a truth table, with $P(n)$ as a variable.
4. The statement $\forall n\, P(n)$ itself needs a proof or a counterexample, not a table.

The typical use of this distinction is to know when a truth table can finish an argument: only for the propositional form, never for the quantifier.
A trap: a computer can check millions of instances, but it still checks a finite table, and the first failure can lie beyond it.
