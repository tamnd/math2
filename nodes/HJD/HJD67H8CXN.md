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

A [[Henkin sentence|SBMQ5QHG9W]] of $T$ is a sentence $H$ with $T \vdash H \leftrightarrow \square H$.
The modal form of Henkin's question is answered by the theorem
$$\mathsf{GL} \vdash \square(p \leftrightarrow \square p) \to \square p$$
of [[provability logic|WJK0YA4GP2]].

1. The tautology $(p \leftrightarrow \square p) \to (\square p \to p)$ holds, since $\square p \to p$ is one half of the equivalence.
2. Necessitation and the axiom $\mathrm{K}$ turn step 1 into $\square(p \leftrightarrow \square p) \to \square(\square p \to p)$.
3. [[Löb's axiom|QQ6PZFGGB3]] is $\square(\square p \to p) \to \square p$.
4. Steps 2 and 3 give $\square(p \leftrightarrow \square p) \to \square p$.
5. Adding the unboxed equivalence: from $p \leftrightarrow \square p$ and $\square p$ we get $p$. So $\mathsf{GL} \vdash (p \leftrightarrow \square p) \wedge \square(p \leftrightarrow \square p) \to p$.
6. Arithmetical reading. Let $T \vdash H \leftrightarrow \square H$. The first [[derivability condition|F6H4STF9RG]] gives $T \vdash \square(H \leftrightarrow \square H)$. The realization of step 5 with $p^* = H$ then gives $T \vdash H$.

## Remarks

Step 6 is the result of [[the diagonal Henkin sentence of PA is provable|Y8G800QGAZ]], now obtained by a modal derivation.
The unboxed hypothesis in step 5 is needed.
Take one world $1$ with no successors and $p$ false: $\square(p \leftrightarrow \square p)$ is true at $1$, but $p$ is false.
If we replace $\square p$ by $\neg \square p$, the fixed point changes from $\top$ to $\neg \square \bot$; see the [[de Jongh-Sambin fixed-point theorem|TDDX1NHG8D]].

## Explanations

### L1 human

Henkin asked about a sentence that says "I can be proved".
Such a sentence is always provable.
The modal proof has four lines: the sentence gives "if provable, then true", and Löb's axiom turns this into "provable".
So the sentence that claims its own provability is right about itself.

### L2 human

1. Assume $\square(p \leftrightarrow \square p)$.
2. Then $\square(\square p \to p)$, since the box keeps implications.
3. Löb's axiom gives $\square p$.
4. If also $p \leftrightarrow \square p$, then $p$.

The typical use is to compute the fixed point of $\square p$: it is $\top$.
A trap: the boxed equivalence alone gives $\square p$, not $p$; the unboxed equivalence is needed for $p$.
