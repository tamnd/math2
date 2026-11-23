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

Compare the rule "a student with a ticket and an identity card may enter" with the pair of rules "a student with a ticket may enter" and "a student with an identity card may enter".
With $p$ for "has a ticket", $q$ for "has an identity card" and $r$ for "may enter", the two are
$$\varphi = (p \land q) \to r \qquad \text{and} \qquad \psi = (p \to r) \land (q \to r).$$
We show that $\varphi$ and $\psi$ are not [[logically equivalent|0JMR2HM2N2]].
One valuation under which they have different truth values is enough.

1. Take the valuation $p$ T, $q$ F, $r$ F: a student with a ticket, without a card, who may not enter.
2. By the definition of [[conjunction|025YZN3VJW]], $p \land q$ is $\mathrm{T} \land \mathrm{F}$, which is F.
3. An [[implication|0NMG7W7Q11]] with a false hypothesis is true, so $\varphi$ is T.
4. The implication $p \to r$ is $\mathrm{T} \to \mathrm{F}$, which is F.
5. A conjunction with a false part is false, so $\psi$ is F.
6. Under this valuation $\varphi$ is true and $\psi$ is false, so $\varphi \not\equiv \psi$.

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

Two correct equivalences sit next to this failure:
$$(p \lor q) \to r \;\equiv\; (p \to r) \land (q \to r), \qquad (p \land q) \to r \;\equiv\; (p \to r) \lor (q \to r).$$
The first one is [[the disjunctive hypothesis example|FM28G5WGAZ]].
In the second one, the "and" in the hypothesis turns into an "or" between the two implications.
Check it in the row TFF: the right side is $\mathrm{F} \lor \mathrm{T}$, which is T, the same as $\varphi$.

## Explanations

### L1 human

Under the rule "ticket and card, then you may enter", a student with a ticket but no card is not let in, and nobody breaks the rule.
Under the pair of rules "ticket, then enter" and "card, then enter", the same student must be let in.
So the two rule books give different answers for one student, and the formulas behind them are not equivalent.

### L2 human

Compare the claim "if $2 \mid n$ and $3 \mid n$, then $6 \mid n$" with the pair "if $2 \mid n$, then $6 \mid n$" and "if $3 \mid n$, then $6 \mid n$".

1. The first claim is true for every integer $n$, because $2$ and $3$ are coprime.
2. The pair is false: $n = 2$ is divisible by $2$ but not by $6$.
3. With $p$ for "$2 \mid n$", $q$ for "$3 \mid n$" and $r$ for "$6 \mid n$", the number $n = 2$ gives the row $p$ T, $q$ F, $r$ F of the table.

A theorem with two hypotheses cannot be split into two theorems with one hypothesis each.
Watch out for the analogy with a hypothesis "$p$ or $q$", where the split into two implications is correct.
