---
tag: GHPPQ19J6B
kind: example
name: Reduction of iterated modalities in S5
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [VC3A2VWXND]
uses: [VC3A2VWXND, ECYRK9C2ZT, JS8W7PA6JK, 12MQ2NJ29A, E87G6ZTMTN]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
---

## Example

On a universal frame, $\square p$ is true everywhere or nowhere, so any box or diamond in front of it changes nothing.
We prove the syntactic form of this fact: in the [[modal logic S5|VC3A2VWXND]], $\mathsf{S5} = \mathsf{KT5}$, a string of boxes and diamonds in front of $p$ is equivalent to its last operator.
We use RE of [[normal modal logic K|JS8W7PA6JK]] and the equivalence $\lozenge\neg p \leftrightarrow \neg\square p$, which RE gives from $\neg\neg p \leftrightarrow p$.

### Each string reduces to its last operator

1. The instance of $\mathrm{5}$ for $\neg p$ is $\lozenge\neg p \to \square\lozenge\neg p$.
2. By RE, $\lozenge\neg p \leftrightarrow \neg\square p$ and $\square\lozenge\neg p \leftrightarrow \square\neg\square p$, so step 1 becomes $\neg\square p \to \square\neg\square p$.
3. Contraposition gives $\neg\square\neg\square p \to \square p$, which is $\lozenge\square p \to \square p$.
4. The dual of $\mathrm{T}$ for $\square p$ is $\square p \to \lozenge\square p$, so $\mathsf{S5} \vdash \lozenge\square p \leftrightarrow \square p$.
5. Axiom $\mathrm{T}$ for $\lozenge p$ gives $\square\lozenge p \to \lozenge p$, and axiom $\mathrm{5}$ gives $\lozenge p \to \square\lozenge p$, so $\mathsf{S5} \vdash \square\lozenge p \leftrightarrow \lozenge p$.
6. By [[the axioms of S5|ECYRK9C2ZT]], $\mathsf{S5} \vdash \square p \to \square\square p$, and $\mathrm{T}$ for $\square p$ gives the converse, so $\mathsf{S5} \vdash \square\square p \leftrightarrow \square p$.
7. Dually, $\mathsf{S5} \vdash \lozenge\lozenge p \leftrightarrow \lozenge p$.
8. So $M N p \leftrightarrow N p$ for all $M, N \in \{ \square, \lozenge \}$, and by substitution the same holds with any formula in place of $p$.
9. Every string $M_1 \cdots M_k p$ with $k \geq 1$ is equivalent to $M_k p$, by [[induction|12MQ2NJ29A]] on $k$.
   For $k = 1$ there is nothing to show.
10. For $k > 1$, the induction hypothesis gives $M_2 \cdots M_k p \leftrightarrow M_k p$, and RE puts $M_1$ in front of both sides.
    Then step 8 gives $M_1 M_k p \leftrightarrow M_k p$.

### Six distinct modalities

With negations, duality moves each $\neg$ to the front, so each modality is equivalent to one of $p$, $\neg p$, $\square p$, $\lozenge p$, $\neg\square p$, $\neg\lozenge p$.

11. On the universal frame $W = \{ 1, 2 \}$, the valuation $V(p) = \{ 1 \}$ gives the six formulas the truth sets $\{ 1 \}$, $\{ 2 \}$, $\varnothing$, $W$, $W$, $\varnothing$.
12. This separates every pair except $\square p$ from $\neg\lozenge p$ and $\lozenge p$ from $\neg\square p$.
    The valuation $V(p) = W$ gives $\square p$ and $\lozenge p$ the set $W$, and $\neg\lozenge p$ and $\neg\square p$ the set $\varnothing$.
13. The universal frame validates $\mathsf{S5}$, so by [[soundness|E87G6ZTMTN]] different truth sets mean that the formulas are not equivalent, and the six modalities are distinct.

## Remarks

So $\mathsf{S5}$ has exactly six modalities, against fourteen in $\mathsf{S4}$.
Step 12 is needed because on a universal frame $\square p$ and $\neg\lozenge p$ are both empty unless $p$ holds everywhere or nowhere.
One valuation is enough on a frame with two classes.
Take the classes $\{ 1 \}$ and $\{ 2, 3 \}$, with $V(p) = \{ 1, 2 \}$.
The six truth sets are $\{ 1, 2 \}$, $\{ 3 \}$, $\{ 1 \}$, $W$, $\{ 2, 3 \}$ and $\varnothing$, all different.
In $\mathsf{B}$ and in $\mathsf{S4}$ the formula $\lozenge\square p \to \square p$ of step 3 is not a theorem, and the reduction stops earlier.

## Explanations

### L1 human

In $\mathsf{S5}$, "box" means "in every possible world" and "diamond" means "in some possible world".
Every world can see every other world, so the starting world does not matter.
"Possibly necessarily $p$" then says "in some world, $p$ holds in all worlds", which is just "$p$ holds in all worlds".
So any chain of boxes and diamonds is decided by its last word.

### L2 human

We reduce $\lozenge\square\lozenge\lozenge\square p$.
The last operator is $\square$, so the claim gives this equivalence:
$$\lozenge\square\lozenge\lozenge\square p \leftrightarrow \square p.$$
Check on a universal frame: $\square p$ is true everywhere or nowhere, so each operator in front of it keeps that value, and the long formula has the same truth set as $\square p$.
You use the reduction to simplify formulas of $\mathsf{S5}$, as a first step toward a normal form of modal depth at most $1$.
Watch out: the reduction concerns strings of operators in front of one formula, so $\square(p \vee \square q)$ needs a separate argument; see [[the law □(p ∨ □q) ↔ □p ∨ □q|BAV2SAADQT]].
