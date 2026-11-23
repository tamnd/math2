---
tag: XQD2D1T45M
kind: example
name: Paraconsistent weak Kleene logic fails explosion and disjunctive syllogism
msc: ["03B50", "03B53"]
topics: [WZP584JQ06]
audience: grad
instance_of: [BCK5QXQXA6]
uses: [PJA9JVQ5XN, 05006AJ7DZ]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: "2.2 From two to three truth values: gaps and gluts"
---

## Example

Work in [[PWK|PJA9JVQ5XN]], the weak Kleene tables with the designated values $\tfrac12$ and $1$.
Take the valuation $v(p) = \tfrac12$ and $v(q) = 0$.

1. $v(p \land \neg p) = \tfrac12$, since $p$ has the value $\tfrac12$, and this value is designated.
2. $v(q) = 0$ is not designated, so explosion $p \land \neg p \models q$ fails.
3. $v(p) = \tfrac12$ is designated.
4. $v(\neg p \lor q) = \tfrac12$, since $p$ occurs in it, and this value is designated.
5. With $v(q) = 0$ from step 2, disjunctive syllogism $p, \neg p \lor q \models q$ fails.
6. Since $p \to q$ is $\neg p \lor q$, modus ponens $p, p \to q \models q$ fails by the same valuation.

So $\mathsf{PWK}$ is a [[paraconsistent logic|C7YWCR87QJ]].

## Remarks

The tautologies of $\mathsf{PWK}$ are exactly the classical [[tautologies|05006AJ7DZ]].
Let $\varphi$ be a classical tautology and take a valuation.
If it gives some variable of $\varphi$ the value $\tfrac12$, then $\varphi$ has the value $\tfrac12$, which is designated.
Otherwise the valuation is classical on $\varphi$, and $\varphi$ has the value $1$.
Conversely, at a classical valuation a $\mathsf{PWK}$ tautology has a classical designated value, which must be $1$.
So $\mathsf{PWK}$ changes the valid inferences of classical logic but keeps its tautologies.

## Explanations

### L1 human

In this logic, a meaningless statement is acceptable.
"$p$ and not $p$" can be acceptable when $p$ is meaningless.
That does not force every other statement to be acceptable, so a contradiction does not entail everything.

### L2 human

To refute a $\mathsf{PWK}$ inference, find a variable that occurs in every premise but not in the conclusion.
Give it the value $\tfrac12$, so every premise becomes $\tfrac12$.
Then give the variables of the conclusion classical values that make it $0$.
The typical use is this recipe for refuting inferences.
Watch out: the recipe needs a variable shared by all premises and absent from the conclusion, and $p \models p \lor q$ is valid.
