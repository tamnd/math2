---
tag: DFDWDKV0PG
kind: example
name: A satisfiable set of three clauses
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [QN7M1JCGT9]
uses: [H31CS3HK5P, 0F72FK8EKB, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Satisfiability
    locator: Propositional satisfiability for classical logic
---

## Example

To show that a set is [[satisfiable|QN7M1JCGT9]] we need only one assignment, and often the formulas force it step by step.
Let
$$\Gamma = \{ p \lor q, \; \neg p \lor r, \; \neg q \} .$$
We find an assignment that satisfies $\Gamma$, and we show that it is the only one on $p$, $q$, $r$.

1. The member $\neg q$ is true only when $v(q) = 0$.
2. With $v(q) = 0$, the member $p \lor q$ is true only when $v(p) = 1$, by the table of [[disjunction|0F72FK8EKB]].
3. With $v(p) = 1$, the disjunct $\neg p$ has the value $0$, so the member $\neg p \lor r$ is true only when $v(r) = 1$.
4. Take $v(p) = 1$, $v(q) = 0$, $v(r) = 1$.
   Then $\bar v(p \lor q) = 1$, $\bar v(\neg p \lor r) = 0 \lor 1 = 1$ and $\bar v(\neg q) = 1$.
5. So $v$ satisfies $\Gamma$, and $\Gamma$ is satisfiable.
6. Steps 1 to 3 show that every satisfying assignment has these three values, so it is the only one on $p$, $q$, $r$.

Check: of the $8$ rows, the $4$ with $q = 1$ fail $\neg q$, the $2$ with $p = q = 0$ fail $p \lor q$, and of the last $2$ only $r = 1$ makes $\neg p \lor r$ true.

## Remarks

Each step above uses a member with only one literal left that can still be true, and forces that literal.
This is unit propagation, the basic step of the [[DPLL algorithm|K7R9D390SP]].
The three members are clauses, so $\Gamma$ is a formula in [[conjunctive normal form|0B3D4C8YF2]].

If we add the member $\neg r$, the set becomes unsatisfiable, since step 3 forces $v(r) = 1$.
If we remove the member $\neg q$, the set has more satisfying assignments, for example $v(p) = 0$, $v(q) = 1$ with any value of $r$.

Watch out.
One satisfying assignment proves satisfiability, but one failed guess proves nothing.
To show that a set is unsatisfiable, we need an argument about all assignments, as in steps 1 to 3.

Try it.
Is $\{ p \lor q, \; \neg p \lor r, \; \neg r \}$ satisfiable?
Yes: $\neg r$ forces $r = 0$, then $\neg p \lor r$ forces $p = 0$, then $p \lor q$ forces $q = 1$, and $p = 0$, $q = 1$, $r = 0$ works.

## Explanations

### L1 human

Three friends plan a party.
Paul or Quinn must bring food.
If Paul brings food, Rita brings drinks.
Quinn cannot bring food.
Then Paul brings food, and so Rita brings drinks, and every wish is met.

### L2 human

We use the same set to test a consequence.

1. Step 6 of the example shows that every assignment satisfying $\Gamma$ has $v(r) = 1$.
2. So $\Gamma \models r$.
3. By the reduction of consequence to satisfiability, $\Gamma \cup \{ \neg r \}$ is unsatisfiable.

So one search answers two questions: it finds a model of $\Gamma$, and it shows that $\Gamma$ forces $r$.
