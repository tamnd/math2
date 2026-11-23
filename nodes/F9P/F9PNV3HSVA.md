---
tag: F9PNV3HSVA
kind: proof
name: Proof that a Moore sentence cannot be believed in KD45
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
proves: TCAYVAVAK4
uses: [RTP4HTZYK3, 9TPXQT9625, FDFQFWPM4X, 1CFMP9DEE6, E87G6ZTMTN]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Moore%27s_paradox
    locator: section The problem
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 3
---

## Proof

We derive $B \bot$ from $B (p \wedge \neg B p)$ in $\mathsf{KD4}$, then repeat the argument on frames, and then give a model of the Moore sentence.
These are the three parts of [[the theorem|TCAYVAVAK4]].
The system $\mathsf{KD4}$ has the propositional tautologies, modus ponens, the [[necessitation rule|9TPXQT9625]], and the axioms $\mathsf{K}$, $\mathsf{D}$ and $\mathsf{4}$.

Part 1, a derivation in $\mathsf{KD4}$.

1. The formula $(p \wedge \neg B p) \to p$ is a tautology, so necessitation and $\mathsf{K}$ give $B (p \wedge \neg B p) \to B p$.
2. In the same way the tautology $(p \wedge \neg B p) \to \neg B p$ gives $B (p \wedge \neg B p) \to B \neg B p$.
3. Axiom $\mathsf{4}$ gives $B p \to B B p$, and with step 1 we get $B (p \wedge \neg B p) \to B B p$.
4. The formula $B p \to (\neg B p \to \bot)$ is a tautology, so necessitation and $\mathsf{K}$, used twice, give $B B p \to (B \neg B p \to B \bot)$.
5. Steps 2, 3 and 4 give $B (p \wedge \neg B p) \to B \bot$ by propositional logic.
6. Axiom $\mathsf{D}$ is $\neg B \bot$, so $\neg B (p \wedge \neg B p)$ follows by propositional logic.
7. $\mathsf{KD45}$ contains $\mathsf{KD4}$, so it proves the same formula.

Part 2, the semantic form.

8. Let $M$ be a Kripke model with a serial and transitive relation $R$, and suppose for a contradiction that $B (p \wedge \neg B p)$ holds at $w$.
9. By seriality there is $v$ with $w R v$, and then $p \wedge \neg B p$ holds at $v$.
10. Since $\neg B p$ holds at $v$, there is $u$ with $v R u$ and $p$ false at $u$.
11. By transitivity $w R u$, so $p \wedge \neg B p$ holds at $u$, and $p$ is true at $u$.
12. Steps 10 and 11 contradict each other, so $B (p \wedge \neg B p)$ is false at every world of $M$.
13. [[KD45 frames|1CFMP9DEE6]] are serial and transitive, so the formula is unsatisfiable on them.
    Part 2 also follows from part 1 by [[soundness|E87G6ZTMTN]], since serial transitive frames validate $\mathsf{D}$ and $\mathsf{4}$.

Part 3, a model of the Moore sentence.

14. Let $W = \{w, v\}$ and $R = \{(w, v), (v, v)\}$, with $p$ true at $w$ only.
15. $R$ is serial, since both worlds see $v$, and transitive, since the composable pairs give only $(w, v)$ and $(v, v)$.
16. $R$ is Euclidean, since $x R y$ and $x R z$ force $y = z = v$, and $v R v$ holds.
17. At $w$ the atom $p$ is true, and the only successor $v$ has $p$ false, so $B p$ is false at $w$.
    So $p \wedge \neg B p$ holds at $w$, on a $\mathsf{KD45}$ frame.

This proves the three parts of the theorem.

## Idea

Believing "$p$, and I do not believe $p$" commits the agent to $B p$, and by introspection to $B B p$.
It also commits her to $B \neg B p$, so she believes both $B p$ and its negation, which consistency forbids.
On frames the same story reads: every world she considers possible has $p$, one of them sees a world without $p$, and by transitivity she considers that world possible too.

## Variants

The derivation of part 1 uses axiom $\mathsf{4}$ once and axiom $\mathsf{D}$ once.
So it works in every normal logic that contains $\mathsf{D}$ and $\mathsf{4}$, such as $\mathsf{KD4}$, $\mathsf{KD45}$ and $\mathsf{S4}$.

For knowledge there is a shorter route, in which $\mathsf{T}$ replaces both $\mathsf{4}$ and $\mathsf{D}$.
From $K (p \wedge \neg K p)$ we get $K p$ and $K \neg K p$, and $\mathsf{T}$ turns the second into $\neg K p$, which contradicts the first.
