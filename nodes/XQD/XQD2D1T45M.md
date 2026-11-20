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

Work in [[PWK|PJA9JVQ5XN]]: the weak Kleene tables with designated values $\tfrac12$ and $1$.
Take the valuation $v(p) = \tfrac12$, $v(q) = 0$.

1. $v(p \land \neg p) = \tfrac12$, since $p$ has value $\tfrac12$. This is designated.
2. $v(q) = 0$ is not designated. So explosion $p \land \neg p \models q$ fails.
3. $v(p) = \tfrac12$ is designated.
4. $v(\neg p \lor q) = \tfrac12$, since $p$ occurs in it. This is designated.
5. With $v(q) = 0$ from step 2, disjunctive syllogism $p, \neg p \lor q \models q$ fails.
6. Since $p \to q$ is $\neg p \lor q$, modus ponens $p, p \to q \models q$ fails by the same valuation.

So $\mathsf{PWK}$ is a [[paraconsistent logic|C7YWCR87QJ]].

## Remarks

1. The tautologies of $\mathsf{PWK}$ are exactly the classical [[tautologies|05006AJ7DZ]].
2. Proof of remark 1. If $\varphi$ is a classical tautology and a valuation gives some variable of $\varphi$ the value $\tfrac12$, then $\varphi$ has value $\tfrac12$, which is designated. Otherwise the valuation is classical and $\varphi$ has value $1$.
3. Conversely, a $\mathsf{PWK}$ tautology has value $1$ or $\tfrac12$ at each classical valuation, and the value there is classical, so it is $1$.
4. So $\mathsf{PWK}$ changes the valid inferences of classical logic but keeps its tautologies.

## Explanations

### L1 human

In this logic, a meaningless statement is acceptable.
"$p$ and not $p$" can be acceptable when $p$ is meaningless.
That does not force every other statement to be acceptable, so a contradiction does not prove everything.

### L2 human

1. Find a variable that occurs in every premise but not in the conclusion.
2. Give it the value $\tfrac12$, so every premise becomes $\tfrac12$.
3. Give the conclusion's variables classical values that make it $0$.

The typical use is this recipe for refuting $\mathsf{PWK}$ inferences.
A trap: the recipe needs a variable shared by all premises and absent from the conclusion; $p \models p \lor q$ is valid.
