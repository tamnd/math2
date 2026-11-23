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

"It rains or it snows; if it rains, the road is wet; if it snows, the road is wet; so the road is wet."
An argument is valid when no assignment of truth values makes all premises true and the conclusion false.
With $p$ for rain, $q$ for snow and $r$ for a wet road, we test
$$p \lor q, \quad p \to r, \quad q \to r \quad \text{therefore} \quad r$$
with a [[truth table|05RSK4Q657]].

1. There are $3$ variables, so there are $8$ rows.
2. For each row we compute the three premises with the tables of [[disjunction|0H5GKDTB01]] and [[material implication|0ZNX6DQ3EJ]], and mark the rows where all three are T.

| $p$ | $q$ | $r$ | $p \lor q$ | $p \to r$ | $q \to r$ | all premises T | $r$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | yes | T |
| T | T | F | T | F | F | no | F |
| T | F | T | T | T | T | yes | T |
| T | F | F | T | F | T | no | F |
| F | T | T | T | T | T | yes | T |
| F | T | F | T | T | F | no | F |
| F | F | T | F | T | T | no | T |
| F | F | F | F | T | T | no | F |

3. All premises are T in the rows TTT, TFT and FTT.
4. In each of these three rows the conclusion $r$ is T.
5. So no row has all premises T and the conclusion F, and the argument is valid.

Next we test "$p \to r$, $r$, therefore $p$" with the same method.

6. In the row with $p$ F and $r$ T, the premises $p \to r$ and $r$ are T, and the conclusion $p$ is F.
7. So this argument is not valid, and that row is a countermodel.

## Remarks

### What the two arguments are

The first argument is the logical form of [[proof by cases|0WCP0PVET6]]: if $p$ or $q$ holds, and each of them gives $r$, then $r$ holds.
The second argument is the fallacy of [[affirming the consequent|J7KFCFQRBT]], and [[affirming the consequent is not a valid deduction|2XXTDXK1ZC]] gives a mathematical instance.

### Validity is about all rows

A valid argument can have a false conclusion in a row where some premise is false, as in the row TTF.
The test is the same as the test that $((p \lor q) \land (p \to r) \land (q \to r)) \to r$ is a tautology.
In the metalanguage, the first result is written $p \lor q,\ p \to r,\ q \to r \models r$, which says that $r$ is a [[logical consequence|1HK0VYWTV7]] of the premises.
A short cut checks only the rows where the conclusion is F, here the four rows with $r$ F, and each of them has a false premise.

## Explanations

### L1 human

An argument is valid when true premises can never lead to a false conclusion.
The table checks all $8$ cases of rain, snow and a wet road.
In every case where all three premises are true, the road is wet.
So the argument never leads from true premises to a false conclusion.

### L2 human

Test "$p \to q$, $\neg q$, therefore $\neg p$" with the short cut.

1. The conclusion $\neg p$ is F only when $p$ is T.
2. In the row TT, the premise $\neg q$ is F.
3. In the row TF, the premise $p \to q$ is F.
4. In both rows with a false conclusion some premise is F, so the argument is valid.

This argument is [[modus tollens|32AQPJQQAM]], and the test decides whether a pattern of reasoning may be used in proofs.
Watch out: a valid form does not make the conclusion true.
It guarantees a true conclusion only when the premises are true.
