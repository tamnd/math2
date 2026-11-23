---
tag: HJD67H8CXN
kind: example
name: Henkin's sentence in GL
msc: ["03F45", "03F40"]
topics: [3E7M66WW6Q]
audience: research
instance_of: [WJK0YA4GP2]
uses: [WJK0YA4GP2, QQ6PZFGGB3, SBMQ5QHG9W, Y8G800QGAZ, F6H4STF9RG]
sources:
  - url: https://en.wikipedia.org/wiki/Löb's_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
---

## Example

A sentence that says "I am provable" is provable, and in [[provability logic|WJK0YA4GP2]] this takes four lines.
A [[Henkin sentence|SBMQ5QHG9W]] of $T$ is a sentence $H$ with $T \vdash H \leftrightarrow \square H$.
The modal form of Henkin's question is answered by the following theorem of $\mathsf{GL}$:
$$\mathsf{GL} \vdash \square(p \leftrightarrow \square p) \to \square p.$$

1. The formula $(p \leftrightarrow \square p) \to (\square p \to p)$ is a tautology, since $\square p \to p$ is one half of the equivalence.
2. Necessitation and the axiom K turn step 1 into $\square(p \leftrightarrow \square p) \to \square(\square p \to p)$.
3. [[Löb's axiom|QQ6PZFGGB3]] is $\square(\square p \to p) \to \square p$.
4. Steps 2 and 3 give $\square(p \leftrightarrow \square p) \to \square p$, by propositional logic.
5. Now add the unboxed equivalence.
   From $p \leftrightarrow \square p$ and $\square p$ we get $p$.
   So $\mathsf{GL} \vdash (p \leftrightarrow \square p) \wedge \square(p \leftrightarrow \square p) \to p$.
6. Read step 5 in arithmetic.
   Let $T \vdash H \leftrightarrow \square H$.
   The first [[derivability condition|F6H4STF9RG]] gives $T \vdash \square(H \leftrightarrow \square H)$.
   The realization of step 5 with $p^* = H$ then gives $T \vdash H$.

## Remarks

Step 6 recovers the result that [[the diagonal Henkin sentence of PA is provable|Y8G800QGAZ]], now by a modal derivation instead of a direct argument with codes.

The unboxed hypothesis in step 5 is needed.
Take one world $1$ with no successors and let $p$ be false at $1$.
Every boxed formula is true at $1$, so $\square(p \leftrightarrow \square p)$ is true there, but $p$ is false.
Check: the conclusion of step 4, $\square p$, is also true at $1$, so step 4 is not refuted, only the stronger claim $p$.

In the language of fixed points, the example says that the fixed point of $\square p$ is $\top$.
If we replace $\square p$ by $\neg \square p$, the fixed point changes from $\top$ to $\neg \square \bot$, as the [[de Jongh-Sambin fixed-point theorem|TDDX1NHG8D]] computes.
So "I am provable" is provable, while "I am not provable" is equivalent to consistency and is not provable.

## Explanations

### L1 human

Henkin asked about a sentence that says "I can be proved".
Such a sentence is always provable.
The modal proof has four lines: the sentence gives "if provable, then true", and Löb's axiom turns this into "provable".
So the sentence that claims its own provability is right about itself.

### L2 human

Assume $\square(p \leftrightarrow \square p)$.
The box keeps implications, so we get $\square(\square p \to p)$.
Löb's axiom then gives $\square p$.
If also $p \leftrightarrow \square p$ holds unboxed, then $p$ follows from $\square p$.
This is the computation of the fixed point of $\square p$, and the answer is $\top$.
Watch out: the boxed equivalence alone gives $\square p$, not $p$, and the unboxed equivalence is needed for $p$.
