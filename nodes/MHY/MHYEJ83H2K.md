---
tag: MHYEJ83H2K
kind: example
name: K4 proves ◇◇p → ◇p
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [XVYMEZKH7R]
uses: [XVYMEZKH7R, JS8W7PA6JK, E87G6ZTMTN, 0GJZW9JFZQ, FDFQFWPM4X]
sources:
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Example

We derive in $\mathsf{K4}$, one of the [[modal logics T, D and K4|XVYMEZKH7R]], the dual form of axiom $\mathrm{4}$:
$$\mathsf{K4} \vdash \lozenge\lozenge p \to \lozenge p.$$

1. The instance of $\mathrm{4}$ for $\neg p$ is $\square\neg p \to \square\square\neg p$.
2. Contraposition gives $\neg\square\square\neg p \to \neg\square\neg p$. The right side is $\lozenge p$.
3. By definition, $\lozenge\lozenge p$ is $\neg\square\neg\neg\square\neg p$.
4. The tautology $\neg\neg\square\neg p \leftrightarrow \square\neg p$ and the rule RE of [[normal modal logic K|JS8W7PA6JK]] give $\square\neg\neg\square\neg p \leftrightarrow \square\square\neg p$.
5. Negating both sides, $\lozenge\lozenge p \leftrightarrow \neg\square\square\neg p$.
6. Steps 2 and 5 give $\lozenge\lozenge p \to \lozenge p$.
7. Also $\mathsf{K4} \vdash \square p \to \square\square\square p$. Axiom $\mathrm{4}$ gives $\square p \to \square\square p$.
8. The instance of $\mathrm{4}$ for $\square p$ is $\square\square p \to \square\square\square p$. The chain rule with step 7 gives $\square p \to \square\square\square p$.
9. $\mathsf{K4} \nvdash \square\square p \to \square p$. The frame $(\N, <)$ is [[transitive|0GJZW9JFZQ]], so it validates $\mathsf{K4}$.
10. Put $V(p) = \set{n : n \geq 2}$. Each $m \geq 1$ has all successors at least $2$, so $\square p$ is true at $m$, and $\square\square p$ is true at $0$.
11. The successor $1$ of $0$ lacks $p$, so $\square p$ is false at $0$. By [[soundness|E87G6ZTMTN]], $\square\square p \to \square p$ is not in $\mathsf{K4}$.

## Remarks

The example shows the standard move from a box axiom to its diamond dual: substitute $\neg p$, contrapose, and remove double negations with RE.
On frames, the dual says: if $w$ reaches a $p$-world in two steps, then $w$ reaches it in one step, which is transitivity.
Step 8 iterates: $\mathsf{K4} \vdash \square p \to \square^n p$ for every $n \geq 1$, by induction on $n$.
The converse $\square\square p \to \square p$ corresponds to density: $w R v$ implies $w R u$ and $u R v$ for some $u$.
The frame $(\N, <)$ is not dense, which is why step 10 works.
On $(\mathbb{Q}, <)$, which is transitive and dense, $\square\square p \to \square p$ is valid.

## Explanations

### L1 human

In a transitive picture, a trip from $a$ to $b$ and a trip from $b$ to $c$ give a direct trip from $a$ to $c$.
"Diamond diamond $p$" says that a $p$-world can be reached in two steps.
Transitivity turns two steps into one, so "diamond $p$" follows.
The other direction can fail on the numbers $0, 1, 2, \dots$ with "smaller than".
If $p$ holds from $2$ on, then from $0$ every two-step trip ends in $p$.
But the one-step trip from $0$ to $1$ does not.

### L2 human

1. Take $W = \set{1, 2, 3}$ with $1 R 2$ and $2 R 3$ only, and $V(p) = \set{3}$.
2. At $1$, $\lozenge\lozenge p$ is true via $2$ and $3$, and $\lozenge p$ is false, since $1$ sees only $2$.
3. So the dual of $\mathrm{4}$ fails on this frame, which is not transitive, as [[common modal axiom schemata|FDFQFWPM4X]] predicts.
4. Adding the pair $(1, 3)$ makes the frame transitive, and then $\lozenge p$ is true at $1$.

The typical use of the dual is in proofs about the [[canonical model|TVE4F04KME]] and in reductions of modalities.
A trap: the dual of $\square p \to \square\square p$ is $\lozenge\lozenge p \to \lozenge p$, with the arrow from the longer string to the shorter one.
