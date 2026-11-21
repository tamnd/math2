---
tag: A7CTMV6M39
kind: example
name: The Lindenbaum-Tarski algebra on two variables has sixteen elements
msc: ["03G05", "03B05"]
topics: [QYA4H5Y7VR]
audience: grad
instance_of: [QC9M3Q8B8Q]
uses: [MGCVQXXQJH, J2GTJ8FKF2, 1MF0TVHDZD]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum–Tarski_algebra
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Free_Boolean_algebra
    locator: lead section
---

## Example

Let $P = \set{p, q}$ and $T = \emptyset$, and let $\mathbf{L}$ be the [[Lindenbaum-Tarski algebra|MGCVQXXQJH]] of classical logic over $P$.
We show that $\mathbf{L}$ has exactly $16$ elements, and we list them.

1. Each formula $\varphi$ in $p$, $q$ has a truth function $\set{0, 1}^2 \to \set{0, 1}$.
   There are $2^4 = 16$ such functions, since there are four rows and two values in each row.
2. If $\varphi$ and $\psi$ have the same truth function, then $\varphi \to \psi$ and $\psi \to \varphi$ are tautologies.
   By [[the algebraic completeness theorem|J2GTJ8FKF2]], both are derivable, so $[\varphi] = [\psi]$.
3. If $[\varphi] = [\psi]$, then $\varphi \to \psi$ and $\psi \to \varphi$ are derivable, so they are tautologies by soundness.
   So $\varphi$ and $\psi$ have the same truth function.
4. So the classes correspond one to one to the truth functions that formulas realize.
5. Every one of the 16 functions is realized; the table gives one formula for each.
   The column lists the values at $(p, q) = (1,1), (1,0), (0,1), (0,0)$, in this order.

| values | formula | values | formula |
|---|---|---|---|
| 0000 | $\bot$ | 1111 | $\top$ |
| 1000 | $p \land q$ | 0111 | $\neg(p \land q)$ |
| 0100 | $p \land \neg q$ | 1011 | $p \to q$ |
| 0010 | $\neg p \land q$ | 1101 | $q \to p$ |
| 0001 | $\neg p \land \neg q$ | 1110 | $p \lor q$ |
| 1100 | $p$ | 0011 | $\neg p$ |
| 1010 | $q$ | 0101 | $\neg q$ |
| 1001 | $(p \to q) \land (q \to p)$ | 0110 | $\neg((p \to q) \land (q \to p))$ |

6. The four atoms are the classes with one $1$ in the column: $[p \land q]$, $[p \land \neg q]$, $[\neg p \land q]$, $[\neg p \land \neg q]$.
7. Each class is the join of the atoms below it; for example $[p \to q] = [p \land q] \lor [\neg p \land q] \lor [\neg p \land \neg q]$.
8. So $\mathbf{L}$ is isomorphic to the power set of a four-element set, by the map that sends a class to its set of rows with value $1$.

So $\mathbf{L}$ has $16$ elements, and it is the [[free Boolean algebra|1MF0TVHDZD]] on the two generators $[p]$ and $[q]$.

## Remarks

1. The example shows how the completeness theorem counts the classes: there is one class for each truth function.
2. With $n$ variables there are $2^n$ rows and $2^{2^n}$ classes; for $n = 1, 2, 3$ this gives $4$, $16$, $256$.
3. With a nonempty theory there are fewer classes; see [[the theory with one axiom|PV510K3H9H]].
4. Without completeness, step 2 needs a derivation for each of the pairs, which is long but finite.

## Explanations

### L1 human

With two letters $p$ and $q$, a truth table has four rows.
In each row a formula is true or false, so a formula gives a pattern of four answers.
There are $2 \times 2 \times 2 \times 2 = 16$ patterns.
Formulas with the same pattern are proved equivalent, so there are sixteen boxes.

### L2 human

1. Compute the pattern of $\neg p \lor q$, which is $\neg \neg p \to q$.
2. At $(1, 1)$ the value is $1$; at $(1, 0)$ it is $0$; at $(0, 1)$ it is $1$; at $(0, 0)$ it is $1$.
3. The pattern is $1011$, the same as for $p \to q$.
4. So $[\neg p \lor q] = [p \to q]$ in $\mathbf{L}$.
5. The pattern $1011$ has three ones, so this class is the join of three atoms.

The typical use: to decide if two formulas are provably equivalent, compare their truth tables.
The trap: this test works for classical logic only; in intuitionistic logic $[\neg p \lor q] \ne [p \to q]$.
