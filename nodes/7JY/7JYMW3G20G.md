---
tag: 7JYMW3G20G
kind: example
name: Interpolation by elimination of the private variables
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
not_instance_of:
  - target: 59GJCM8C66
    note: "The elimination interpolant always exists, but computing it takes time exponential in the number of private variables, while the refutation has linear size."
uses: [TRS2HY57EG, YHGCN7BBEP, 6JSH907W5R]
sources:
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: Proof of Craig's interpolation theorem
---

## Example

Fix $m \geq 1$, a shared variable $p$, and private variables $q_1, \dots, q_m$ of $A$.
Take these two CNFs:
$$A_m = \{q_1, \ \dots, \ q_m, \ \neg q_1 \vee \cdots \vee \neg q_m \vee p\}, \qquad B = \{\neg p\}.$$
The proof of [[Craig's theorem|TRS2HY57EG]] gives the interpolant $E_m(p) = \bigvee_{c} A_m(p, c)$, where $c$ runs over all $2^m$ assignments of $q_1, \dots, q_m$.
We check that this way of interpolating is correct but not feasible.

1. A short refutation exists.
   Resolve the long clause with $q_1$, the result with $q_2$, and so on up to $q_m$, which leaves the clause $p$.
   One more step with $\neg p$ gives the empty clause.
   The refutation has $m + 2$ axioms and $m + 1$ resolvents, so $L = 2m + 3$ clauses.
2. The elimination interpolant is correct.
   By its definition, $E_m(a) = 1$ exactly when $A_m(a, q)$ is satisfiable.
   So $E_m(a) = 0$ means that $A_m(a, q)$ fails.
   And $E_m(a) = 1$ forces $a = 1$, where $B(1) = \{\neg 1\}$ fails.
3. The elimination interpolant is expensive.
   Written out, $E_m$ has $2^m$ disjuncts, and evaluating it by trying all $c$ takes $2^m$ evaluations of $A_m$.
   That is exponential in $L$.
4. A feasible interpolant exists.
   The [[interpolation theorem for resolution|YHGCN7BBEP]] applied to the refutation of step 1 gives a circuit with at most $4L = 8m + 12$ gates, and it computes $p$.

So elimination gives an interpolant, but not one of size polynomial in the refutation, and it is not an instance of feasible interpolation.

## Remarks

The example separates two questions.
Craig's theorem answers "is there an interpolant?", and the answer is always yes.
Feasible interpolation answers "is there an interpolant of size polynomial in a given refutation?".

Only $c = (1, \dots, 1)$ satisfies the unit clauses $q_1, \dots, q_m$, so $E_m$ is equivalent to the single variable $p$.
The elimination formula is large although a one-variable interpolant exists, because elimination never looks at the refutation.

What if $m$ is fixed?
Then elimination costs a constant factor $2^m$, and for this fixed $m$ it is feasible.
The failure is in the growth with $m$.

## Explanations

### L1 human

One way to find which side fails is to try every value of the private switches of $A$.
With $m$ private switches there are $2^m$ settings to try.
The proof of the conflict has only about $2m$ lines.
So this way takes far more work than the size of the proof, and it does not use the proof at all.

### L2 human

Compare the two methods for small and large $m$.
For $m = 3$, the refutation has $2 \cdot 3 + 3 = 9$ clauses, and elimination tries the $8$ assignments of $q_1, q_2, q_3$.
For $m = 30$, the refutation has $63$ clauses, while elimination tries $2^{30}$, more than $10^9$, assignments.
The comparison shows why feasible interpolation is a property of the proof system: it must read the interpolant off the refutation.
Watch out: a large interpolant formula does not mean that no small interpolant exists, as $E_m \equiv p$ shows.
