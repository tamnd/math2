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

We prove the three parts of [[the theorem|TCAYVAVAK4]].
$\mathsf{KD4}$ has the propositional tautologies, modus ponens, the [[necessitation rule|9TPXQT9625]], and the axioms $\mathsf{K}$, $\mathsf{D}$ and $\mathsf{4}$.

Part 1, a derivation in $\mathsf{KD4}$.

1. $(p \wedge \neg Bp) \to p$ is a tautology. Necessitation and $\mathsf{K}$ give $B(p \wedge \neg Bp) \to Bp$.
2. Likewise $(p \wedge \neg Bp) \to \neg Bp$ gives $B(p \wedge \neg Bp) \to B\neg Bp$.
3. Axiom $\mathsf{4}$ gives $Bp \to BBp$. With step 1, $B(p \wedge \neg Bp) \to BBp$.
4. $Bp \to (\neg Bp \to \bot)$ is a tautology. Necessitation and $\mathsf{K}$, used twice, give $BBp \to (B\neg Bp \to B\bot)$.
5. Steps 2, 3 and 4 give $B(p \wedge \neg Bp) \to B\bot$, by propositional logic.
6. Axiom $\mathsf{D}$ is $\neg B\bot$. So $\neg B(p \wedge \neg Bp)$ follows.
7. $\mathsf{KD45}$ contains $\mathsf{KD4}$, so it proves the same formula.

Part 2, the semantic form.

8. Let $M$ be a Kripke model with a serial and transitive relation $R$. Suppose $B(p \wedge \neg Bp)$ holds at $w$, for a contradiction.
9. By seriality there is $v$ with $w R v$. Then $p \wedge \neg Bp$ holds at $v$.
10. Since $\neg Bp$ holds at $v$, there is $u$ with $v R u$ and $p$ false at $u$.
11. By transitivity $w R u$. So $p \wedge \neg Bp$ holds at $u$, and $p$ is true at $u$.
12. Steps 10 and 11 contradict each other. So $B(p \wedge \neg Bp)$ is false at every world of $M$.
13. [[KD45 frames|1CFMP9DEE6]] are serial, transitive and Euclidean. So $B(p \wedge \neg Bp)$ is unsatisfiable on them.
14. Part 2 also follows from part 1 by [[soundness|E87G6ZTMTN]], since serial transitive frames validate $\mathsf{D}$ and $\mathsf{4}$.

Part 3, a model of the Moore sentence.

15. Let $W = \set{w, v}$, $R = \set{(w, v), (v, v)}$, and let $p$ be true at $w$ only.
16. $R$ is serial: both worlds see $v$. It is transitive: the composable pairs give only $(w, v)$ and $(v, v)$.
17. $R$ is Euclidean: if $x R y$ and $x R z$ then $y = z = v$, and $v R v$ holds.
18. At $w$, $p$ is true. The only successor $v$ has $p$ false, so $Bp$ is false at $w$.
19. So $p \wedge \neg Bp$ holds at $w$, on a $\mathsf{KD45}$ frame.

## Idea

Believing "$p$, and I do not believe $p$" commits the agent to $Bp$, and by introspection to $BBp$.
It also commits her to $B\neg Bp$.
So she believes both $Bp$ and its negation, which consistency forbids.
Semantically, the worlds she considers possible must all satisfy $p$, but one of them must see a world without $p$, and by transitivity she considers that world possible too.

## Variants

1. The proof of part 1 uses axiom $\mathsf{4}$ once and axiom $\mathsf{D}$ once. So it works in any normal logic containing $\mathsf{D}$ and $\mathsf{4}$, such as $\mathsf{KD4}$, $\mathsf{KD45}$ and $\mathsf{S4}$.
2. For knowledge, $\mathsf{T}$ replaces both $\mathsf{4}$ and $\mathsf{D}$: from $K\neg Kp$ one gets $\neg Kp$, contradicting $Kp$ directly.
