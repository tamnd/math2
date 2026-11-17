---
tag: 3FPFGDVQCV
kind: example
name: Checking the validity of an argument by a truth table
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [05RSK4Q657]
uses: [05RSK4Q657, 0ZNX6DQ3EJ, 0H5GKDTB01, 1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Truth_table
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Validity_(logic)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Example

An argument with premises $\varphi_1, \dots, \varphi_k$ and conclusion $\psi$ is valid when no assignment of truth values makes all premises true and the conclusion false.
We test the argument
$$p \lor q, \quad p \to r, \quad q \to r \quad \text{therefore} \quad r$$
with a [[truth table|05RSK4Q657]].

1. There are $3$ variables, so there are $8$ rows.
2. For each row we compute the three premises, using the tables of [[disjunction|0H5GKDTB01]] and [[material implication|0ZNX6DQ3EJ]], and we mark the rows where all three are true.

| $p$ | $q$ | $r$ | $p \lor q$ | $p \to r$ | $q \to r$ | all premises true | $r$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | yes | T |
| T | T | F | T | F | F | no | F |
| T | F | T | T | T | T | yes | T |
| T | F | F | T | F | T | no | F |
| F | T | T | T | T | T | yes | T |
| F | T | F | T | T | F | no | F |
| F | F | T | F | T | T | no | T |
| F | F | F | F | T | T | no | F |

3. All premises are true in the rows $\mathsf{T}\mathsf{T}\mathsf{T}$, $\mathsf{T}\mathsf{F}\mathsf{T}$ and $\mathsf{F}\mathsf{T}\mathsf{T}$.
4. In each of these three rows the conclusion $r$ is $\mathsf{T}$.
5. So no row has all premises true and the conclusion false, and the argument is valid.

Next we test the argument "$p \to r$, $r$, therefore $p$" with the same method.

6. In the row $p = \mathsf{F}$, $r = \mathsf{T}$, the premise $p \to r$ is $\mathsf{T}$, the premise $r$ is $\mathsf{T}$, and the conclusion $p$ is $\mathsf{F}$.
7. So this argument is not valid, and the row of step 6 is a countermodel.

## Remarks

The first argument is the logical form of [[proof by cases|0WCP0PVET6]]: if $p$ or $q$ holds, and each of them gives $r$, then $r$ holds.
The second argument is the fallacy of [[affirming the consequent|J7KFCFQRBT]], and the page [[affirming the consequent is not a valid deduction|2XXTDXK1ZC]] gives a mathematical instance.

Validity is a claim about all rows, not about one row.
A valid argument can have a false conclusion in a row where some premise is false, as in the row $\mathsf{T}\mathsf{T}\mathsf{F}$.
The test is the same as the test that $((p \lor q) \land (p \to r) \land (q \to r)) \to r$ is a tautology.
In the metalanguage, the first result is written $p \lor q,\ p \to r,\ q \to r \models r$, which says that $r$ is a [[logical consequence|1HK0VYWTV7]] of the premises.

A short cut checks only the rows where the conclusion is false: here the four rows with $r = \mathsf{F}$, and each of them has a false premise.

## Explanations

### L1 human

An argument is valid when true premises can never lead to a false conclusion.
"It rains or it snows; if it rains, the road is wet; if it snows, the road is wet; so the road is wet" is valid.
The table checks all $8$ cases of rain, snow and a wet road.
In every case where all three premises are true, the road is wet.
So the argument never leads from true premises to a false conclusion.

### L2 human

We test "$p \to q$, $\neg q$, therefore $\neg p$" with the short cut.

1. The conclusion $\neg p$ is false only when $p = \mathsf{T}$.
2. Row $\mathsf{T}\mathsf{T}$: the premise $\neg q$ is $\mathsf{F}$.
3. Row $\mathsf{T}\mathsf{F}$: the premise $p \to q$ is $\mathsf{F}$.
4. In both rows with a false conclusion, some premise is false, so the argument is valid.

This argument is [[modus tollens|32AQPJQQAM]].
The typical use of the test is to decide whether a pattern of reasoning may be used in proofs.
A trap: a valid form does not make the conclusion true; it guarantees a true conclusion only when the premises are true.
