---
tag: 5ZPK7DC8MK
kind: example
name: Splitting a clause with a new variable
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
instance_of: [B37TYWXS74]
uses: [QN7M1JCGT9, 0JMR2HM2N2, H31CS3HK5P]
sources:
  - url: https://en.wikipedia.org/wiki/Equisatisfiability
    locator: Examples
---

## Example

A new variable can split one clause into two, and the price is that the result is only [[equisatisfiable|B37TYWXS74]] with the original, not equivalent to it.
Let
$$\varphi = p \lor q, \qquad \psi = (p \lor x) \land (\neg x \lor q),$$
where $x$ is a variable different from $p$ and $q$.
We show that $\varphi$ and $\psi$ are equisatisfiable and not [[logically equivalent|0JMR2HM2N2]].

1. Let $v$ satisfy $\varphi$.
   If $v(p) = 1$, change $v$ at $x$ to $0$; then $p \lor x$ is true by $p$, and $\neg x \lor q$ is true by $\neg x$.
2. If $v(p) = 0$, then $v(q) = 1$, since $v$ satisfies $p \lor q$.
   Change $v$ at $x$ to $1$; then $p \lor x$ is true by $x$, and $\neg x \lor q$ is true by $q$.
3. So every model of $\varphi$ becomes a model of $\psi$ after a change at $x$ only.
4. Conversely, let $v$ satisfy $\psi$.
   If $v(x) = 0$, the clause $p \lor x$ gives $v(p) = 1$, and if $v(x) = 1$, the clause $\neg x \lor q$ gives $v(q) = 1$.
5. In both cases $v$ satisfies $p \lor q$, so $\psi \models \varphi$.
6. By steps 3 and 5, $\varphi$ is satisfiable exactly when $\psi$ is.
7. The assignment $v(p) = 1$, $v(q) = 0$, $v(x) = 1$ makes $\varphi$ true and the clause $\neg x \lor q$ false, so the formulas are not equivalent.

Check: put $x = 0$ in $\psi$ to get $(p \lor 0) \land (1 \lor q)$, which has the value of $p$; put $x = 1$ to get $(p \lor 1) \land (0 \lor q)$, which has the value of $q$.
So $\psi$ can be made true exactly when $p$ or $q$ can.

## Remarks

The two directions are not alike: $\psi \models \varphi$ holds, but $\varphi \models \psi$ fails.
The variable $x$ records which disjunct of $\varphi$ is true.
[[Resolution|ZDW6N1PGJ7]] on $x$ applied to the two clauses of $\psi$ gives back the clause $p \lor q$.

Used again and again, the same step splits a long clause $\ell_1 \lor \ell_2 \lor \cdots \lor \ell_k$ into clauses of three literals:
$$(\ell_1 \lor \ell_2 \lor x_1) \land (\neg x_1 \lor \ell_3 \lor x_2) \land \cdots \land (\neg x_{k-3} \lor \ell_{k-1} \lor \ell_k) .$$
This reduces satisfiability of general clause sets to clause sets with at most three literals per clause.

Watch out.
From "$\varphi$ and $\psi$ are equisatisfiable" we must not conclude $\varphi \models \psi$; step 7 is a counterexample.

Try it.
Split $p \lor q \lor r$ with one new variable $y$ into two clauses.
One answer is $(p \lor y) \land (\neg y \lor q \lor r)$; with $y = 0$ it has the value of $p$, and with $y = 1$ the value of $q \lor r$.

## Explanations

### L1 human

"Paula comes or Quentin comes" can be split with a helper choice.
We say "Paula comes or the helper says yes", and "the helper says no or Quentin comes".
If one of the two friends comes, we can set the helper so that both new sentences are true.
If both new sentences are true, then one of the two friends comes, whatever the helper says.
But the new pair can fail when the old sentence holds, if the helper is set badly.

### L2 human

A resolution prover or a SAT solver may split long clauses in this way and still give the right answer to "satisfiable or not".
When the solver finds a model of $\psi$, we drop the value of $x$ and get a model of $\varphi$, by step 5.
When the solver reports that $\psi$ is unsatisfiable, step 3 tells us that $\varphi$ is unsatisfiable too.
