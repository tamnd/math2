---
tag: EE8XHVGJ0R
kind: example
name: Conjunctive normal form of (p → q) → r
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [0B3D4C8YF2]
uses: [07C4A8Y18K, 0JMR2HM2N2, 09PKJKA6J0, 0NFAGWH84K]
sources:
  - url: https://en.wikipedia.org/wiki/Conjunctive_normal_form
    locator: Conversion by syntactic means
---

## Example

We put $\varphi = (p \to q) \to r$ into [[conjunctive normal form|07C4A8Y18K]] with the laws of logic.
Each step replaces a part of the formula by a [[logically equivalent|0JMR2HM2N2]] part, so the truth table never changes.

1. Remove the outer implication with $\alpha \to \beta \equiv \neg\alpha \lor \beta$:
$$\varphi \equiv \neg(p \to q) \lor r.$$
2. Remove the inner implication in the same way:
$$\varphi \equiv \neg(\neg p \lor q) \lor r.$$
3. Apply [[De Morgan's law|09PKJKA6J0]] $\neg(\alpha \lor \beta) \equiv \neg\alpha \land \neg\beta$, and then the [[double negation law|0NFAGWH84K]]:
$$\varphi \equiv (\neg\neg p \land \neg q) \lor r \equiv (p \land \neg q) \lor r.$$
   This is negation normal form, and it is also a disjunctive normal form.
4. Distribute with $(\alpha \land \beta) \lor \gamma \equiv (\alpha \lor \gamma) \land (\beta \lor \gamma)$:
$$\varphi \equiv (p \lor r) \land (\neg q \lor r).$$
   This is a conjunction of the two clauses $\{ p, r \}$ and $\{ \neg q, r \}$, so it is in CNF.

Now we check the result against the truth table.

5. The formula $\varphi$ is false exactly when $p \to q$ is true and $r$ is false.
   With $r = 0$, the implication $p \to q$ is true at $(p, q) = (0, 0), (0, 1), (1, 1)$, so $\varphi$ is false at $(0, 0, 0)$, $(0, 1, 0)$ and $(1, 1, 0)$.
6. At $(0, 0, 0)$ and $(0, 1, 0)$ the clause $p \lor r$ is false, and at $(1, 1, 0)$ the clause $\neg q \lor r$ is false.
7. At the other five rows, either $r = 1$ and both clauses are true, or the row is $(1, 0, 0)$, where $p = 1$ and $\neg q = 1$ make both clauses true.

## Remarks

The two clauses can be read as rules: "if $r$ is false, then $p$ is true" and "if $r$ is false, then $q$ is false".
The truth-table method gives instead the full CNF, with one clause for each of the three false rows:
$$(p \lor q \lor r) \land (p \lor \neg q \lor r) \land (\neg p \lor \neg q \lor r).$$
The CNF found with the laws is shorter, which shows that a formula has more than one CNF.

Moving the brackets changes the answer.
The formula $p \to (q \to r)$ is not equivalent to $\varphi$, because $\to$ is not associative.
At $p = q = r = 0$, the formula $(p \to q) \to r$ is false, while $p \to (q \to r)$ is true.
The second formula has the one-clause CNF $\neg p \lor \neg q \lor r$.

## Explanations

### L1 human

The formula "if ($p$ implies $q$), then $r$" can be rewritten as two simple rules.
The first rule is "$p$ or $r$", and the second rule is "not $q$, or $r$".
The formula is true exactly when both rules hold.
We find the rules by removing the arrows and moving the negations inward.

### L2 human

The method has a fixed order: first remove $\to$, then move $\neg$ inward, then distribute.
The order matters, because De Morgan's law can only move a negation past $\land$ and $\lor$, not past an arrow.
Watch out at step 1: the outer arrow must be rewritten with its whole antecedent, so $\neg(p \to q)$ appears, not $\neg p \to q$.
At $p = 0$, $q = 0$ the first is false and the second is false too, but at $p = 0$, $q = 1$ the first is false and the second is true, so the two are not equivalent.
