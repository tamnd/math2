---
tag: W5AW31K5TA
kind: example
name: Independence of the first and second axioms of L
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
instance_of: [729RCBPAM3]
uses: [729RCBPAM3, 1MGMQX43B8, 0Y0MQYST0M]
sources:
  - book: isbn:9781482237726
    locator: Chapter 1
  - url: https://en.wikipedia.org/wiki/Independence_(mathematical_logic)
    locator: Complete (strong) independence
---

## Example

In the [[Hilbert system|1MGMQX43B8]] L, we show that A1 is not derivable from A2 and A3, and that A2 is not derivable from A1 and A3, with [[modus ponens|0Y0MQYST0M]] as the rule.
We use the matrix method of [[independence of axioms|729RCBPAM3]] with three values $0$, $1$, $u$ and the designated value $1$.
In both matrices every value of $a \to b$ is $0$ or $1$.

The matrix M1 for A1 has the following tables, with the row for $a$ and the column for $b$.

| $a \to b$ | $b = 0$ | $b = 1$ | $b = u$ | $\neg a$ |
|---|---|---|---|---|
| $a = 0$ | 1 | 1 | 1 | 1 |
| $a = 1$ | 0 | 1 | 0 | 0 |
| $a = u$ | 0 | 1 | 0 | $u$ |

So in M1, $a \to b = 1$ exactly when $a = 0$ or $b = 1$.

1. Modus ponens preserves $1$ in M1: if $a = 1$ and $a \to b = 1$, then $b = 1$ by the row $a = 1$.
2. A2 always takes the value $1$ in M1. If not, its antecedent $a \to (b \to c)$ is $1$ and its consequent is $0$, so $a \to b = 1$ and $a \to c = 0$.
3. From $a \to c = 0$ we get $a \neq 0$ and $c \neq 1$. Then $a \to b = 1$ gives $b = 1$, and $a \to (b \to c) = 1$ gives $b \to c = 1$, so $c = 1$, a contradiction.
4. A3 always takes the value $1$ in M1. If not, $\neg b \to \neg a = 1$, $\neg b \to a = 1$ and $b \neq 1$, so $b$ is $0$ or $u$, and $\neg b$ is $1$ or $u$.
5. In both cases $\neg b \neq 0$, so $\neg a = 1$ and $a = 1$. But $\neg a = 1$ gives $a = 0$, a contradiction.
6. A1 fails in M1: at $\varphi = u$, $\psi = 1$ we get $\psi \to \varphi = 1 \to u = 0$, and $u \to 0 = 0$.
7. By induction on derivations, every formula derivable from A2 and A3 always takes the value $1$ in M1. So A1 is not derivable from A2 and A3.

The matrix M2 for A2 has the following tables.

| $a \to b$ | $b = 0$ | $b = 1$ | $b = u$ | $\neg a$ |
|---|---|---|---|---|
| $a = 0$ | 1 | 1 | 1 | 1 |
| $a = 1$ | 0 | 1 | 0 | 0 |
| $a = u$ | 1 | 1 | 0 | 1 |

8. Modus ponens preserves $1$ in M2, by the row $a = 1$, as in step 1.
9. A1 always takes the value $1$ in M2. For $a = 0$ the row of $0$ gives $1$. For $a = 1$, the column $b = 1$ gives $b \to 1 = 1$, and $1 \to 1 = 1$. For $a = u$, the value $b \to u$ is $0$ or $1$, and $u \to 0 = u \to 1 = 1$.
10. A3 always takes the value $1$ in M2. If not, $\neg b \to \neg a = 1$, $\neg b \to a = 1$ and $b \neq 1$. Then $b$ is $0$ or $u$, so $\neg b = 1$.
11. From $1 \to a = 1$ we get $a = 1$, so $\neg a = 0$ and $\neg b \to \neg a = 1 \to 0 = 0$, a contradiction.
12. A2 fails in M2 at $\varphi = u$, $\psi = 0$, $\chi = u$: the antecedent is $u \to (0 \to u) = u \to 1 = 1$, and the consequent is $(u \to 0) \to (u \to u) = 1 \to 0 = 0$, so A2 takes the value $1 \to 0 = 0$.
13. So A2 is not derivable from A1 and A3.

## Remarks

Together with the [[independence of the third axiom|16P6A7750Q]], the example shows that each axiom schema of L is independent of the other two.
Two values are not enough for A1 and A2: with two values and the usual reading of $\to$, A1 and A2 are tautologies and always take the value $1$.
In both matrices $u \to u = 0$, so $p \to p$ fails, and the derivation of $p \to p$ needs both A1 and A2.
The tables were checked for all $3^3 = 27$ assignments by a computer, in addition to the arguments above.
If one entry changes, the argument can break: in M1, setting $1 \to u = 1$ makes modus ponens lead from $1$ to the undesignated value $u$.

## Explanations

### L1 human

We want to show that each of the first two axiom patterns is really needed.
For each one we invent a strange logic with three truth values: false, true, and a third value.
In the strange logic the other two axioms are always true and modus ponens keeps truth, but the chosen axiom is not always true.
So the chosen axiom cannot be proved from the other two.

### L2 human

We check the failure of A1 in M1 with the formula $p \to (q \to p)$.

1. Assign $p = u$ and $q = 1$.
2. The row $a = 1$ gives $q \to p = 1 \to u = 0$.
3. The row $a = u$ gives $p \to (q \to p) = u \to 0 = 0$.
4. The value $0$ is not designated, so this instance of A1 is not derivable from A2 and A3.

The typical use of such matrices is to show that an axiom list is minimal, or that a theorem needs a given axiom.
A trap is to check the axioms only at the values $0$ and $1$: the failures above happen only when the third value $u$ occurs.
