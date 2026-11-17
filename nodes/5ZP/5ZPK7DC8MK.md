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

Let $\varphi = p \lor q$ and $\psi = (p \lor x) \land (\neg x \lor q)$, where $x$ is a variable different from $p$ and $q$.
We show that $\varphi$ and $\psi$ are equisatisfiable and not [[logically equivalent|0JMR2HM2N2]].

1. Let $v$ satisfy $\varphi$. If $v(p) = 1$, change $v$ at $x$ to $0$: then $p \lor x$ is true by $p$, and $\neg x \lor q$ is true by $\neg x$.
2. If $v(p) = 0$, then $v(q) = 1$, since $v$ satisfies $p \lor q$. Change $v$ at $x$ to $1$: then $p \lor x$ is true by $x$, and $\neg x \lor q$ is true by $q$.
3. So every assignment that satisfies $\varphi$ becomes, after a change at $x$ only, an assignment that satisfies $\psi$.
4. Conversely, let $v$ satisfy $\psi$. If $v(x) = 0$, the clause $p \lor x$ gives $v(p) = 1$. If $v(x) = 1$, the clause $\neg x \lor q$ gives $v(q) = 1$.
5. In both cases $v$ satisfies $p \lor q$. So $\psi \models \varphi$, and every assignment that satisfies $\psi$ satisfies $\varphi$.
6. By steps 3 and 5, $\varphi$ is satisfiable if and only if $\psi$ is, so they are equisatisfiable.
7. The assignment $v(p) = 1$, $v(q) = 0$, $v(x) = 1$ makes $\varphi$ true and the clause $\neg x \lor q$ false. So $\bar v(\varphi) = 1$ and $\bar v(\psi) = 0$, and the formulas are not equivalent.

## Remarks

The example shows the asymmetry of the usual satisfiability-preserving steps: $\psi \models \varphi$ holds, but $\varphi \models \psi$ fails.
The variable $x$ records which disjunct of $\varphi$ is true.
Applied again and again, the same step splits a long clause $\ell_1 \lor \ell_2 \lor \cdots \lor \ell_k$ into clauses of three literals, $(\ell_1 \lor \ell_2 \lor x_1) \land (\neg x_1 \lor \ell_3 \lor x_2) \land \cdots$, which reduces satisfiability of general clause sets to clause sets with at most three literals per clause.
In the other direction, a resolution step on $x$ applied to the two clauses of $\psi$ gives back the clause $p \lor q$.

## Explanations

### L1 human

"Paula comes or Quentin comes" can be split with a helper choice.
We say: "Paula comes or the helper says yes", and "the helper says no or Quentin comes".
If one of the two friends comes, we can set the helper so that both new sentences are true.
If both new sentences are true, then one of the two friends comes, whatever the helper says.
But the new pair can fail when the old sentence holds, if the helper is set badly.

### L2 human

We check equisatisfiability with a truth table on $x$ alone.

1. Put $x = 0$: then $\psi$ becomes $(p \lor 0) \land (1 \lor q)$, which has the value of $p$.
2. Put $x = 1$: then $\psi$ becomes $(p \lor 1) \land (0 \lor q)$, which has the value of $q$.
3. So $\psi$ is satisfiable exactly when $p$ or $q$ can be made true, that is, when $p \lor q$ is satisfiable.

The typical use: a resolution prover or a solver may split long clauses in this way and still give the right answer to "satisfiable or not".
A trap: from "$\varphi$ and $\psi$ are equisatisfiable" one must not conclude that $\varphi \models \psi$; step 7 of the example is a counterexample.
