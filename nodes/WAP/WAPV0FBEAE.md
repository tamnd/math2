---
tag: WAPV0FBEAE
kind: example
name: "The formulas (p and q) implies r and (p implies r) and (q implies r) are not equivalent"
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 0JMR2HM2N2
    note: the two formulas differ in the row p true, q false, r false, and in the row p false, q true, r false
uses: [0JMR2HM2N2, 05RSK4Q657, 0NMG7W7Q11, 025YZN3VJW]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_equivalence
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Example

Let $p$, $q$ and $r$ be propositional variables, and consider the two formulas
$$\varphi = (p \land q) \to r \qquad \text{and} \qquad \psi = (p \to r) \land (q \to r).$$
We show that $\varphi$ and $\psi$ are not [[logically equivalent|0JMR2HM2N2]].
One valuation under which they have different truth values is enough.

1. Take the valuation $p = \mathrm{T}$, $q = \mathrm{F}$, $r = \mathrm{F}$.
2. By the definition of [[conjunction|025YZN3VJW]], $p \land q$ is $\mathrm{T} \land \mathrm{F}$, which is F.
3. An [[implication|0NMG7W7Q11]] with a false hypothesis is true, so $\varphi = (p \land q) \to r$ is T.
4. The implication $p \to r$ is $\mathrm{T} \to \mathrm{F}$, which is F.
5. A conjunction with a false part is false, so $\psi = (p \to r) \land (q \to r)$ is F.
6. By steps 3 and 5, $\varphi$ is true and $\psi$ is false under this valuation, so $\varphi \not\equiv \psi$.

The whole [[truth table|05RSK4Q657]] shows the two rows where the formulas differ.

| $p$ | $q$ | $r$ | $\varphi = (p \land q) \to r$ | $\psi = (p \to r) \land (q \to r)$ |
|---|---|---|---|---|
| T | T | T | T | T |
| T | T | F | F | F |
| T | F | T | T | T |
| T | F | F | T | F |
| F | T | T | T | T |
| F | T | F | T | F |
| F | F | T | T | T |
| F | F | F | T | T |

## Remarks

The two formulas agree in six of the eight rows, so a check of a few rows can miss the difference.
In every row where $\psi$ is true, $\varphi$ is also true.
So $\varphi$ is a logical consequence of $\psi$, but $\psi$ is not a logical consequence of $\varphi$.

The correct equivalences are these two.
$$(p \lor q) \to r \;\equiv\; (p \to r) \land (q \to r)$$
$$(p \land q) \to r \;\equiv\; (p \to r) \lor (q \to r)$$
The first one is on the page [[a conditional with a disjunctive hypothesis|FM28G5WGAZ]].
In the second one, the conjunction in the hypothesis turns into a disjunction of implications.

## Explanations

### L1 human

Take the rule "if a student has a ticket and an identity card, the student may enter".
Compare it with the rule "a student with a ticket may enter, and a student with an identity card may enter".
A student who has a ticket but no identity card may not enter under the first rule.
Under the second rule, the same student may enter.
So the two rules are different, and the formulas behind them are not equivalent.

### L2 human

We test the claim "if $n$ is divisible by $2$ and by $3$, then $n$ is divisible by $6$".
We compare it with the pair "if $2 \mid n$, then $6 \mid n$" and "if $3 \mid n$, then $6 \mid n$".

1. The first claim is true for every integer $n$, because $2$ and $3$ are coprime.
2. The pair of claims is false: $n = 2$ is divisible by $2$ but not by $6$.
3. This is the row $p = \mathrm{T}$, $q = \mathrm{F}$, $r = \mathrm{F}$ of the table, with $p$ "$2$ divides $n$", $q$ "$3$ divides $n$" and $r$ "$6$ divides $n$".

The typical use of such a non-equivalence is a warning: a theorem with two hypotheses cannot be split into two theorems with one hypothesis each.
A trap is the analogy with the disjunctive hypothesis, where the split is correct.
