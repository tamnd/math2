---
tag: ~fadab0bc
kind: statement
role: theorem
name: A Moore sentence cannot be believed in KD45
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
uses: [RTP4HTZYK3, 1CFMP9DEE6, FDFQFWPM4X, JDE7CN1C48, 9TPXQT9625]
about: [RTP4HTZYK3]
proofs: [~f58fe59d]
sources:
  - url: https://en.wikipedia.org/wiki/Moore%27s_paradox
    locator: section The problem
  - url: https://en.wikipedia.org/wiki/Doxastic_logic
    locator: lead section
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 3
---

## Statement

Let $B$ be the box of [[doxastic logic|RTP4HTZYK3]], and let $p$ be an atom.

1. $\mathsf{KD4} \vdash \neg B(p \wedge \neg Bp)$, and hence $\mathsf{KD45} \vdash \neg B(p \wedge \neg Bp)$.
2. Equivalently, $B(p \wedge \neg Bp)$ is false at every world of every serial transitive Kripke model. In particular it is unsatisfiable on $\mathsf{KD45}$ frames.
3. The Moore sentence $p \wedge \neg Bp$ itself is satisfiable on a $\mathsf{KD45}$ frame.

## Remarks

### Why each hypothesis is needed

1. Axiom $\mathsf{D}$, seriality. Without it, a world with no successors satisfies $B\chi$ for every $\chi$. So $B(p \wedge \neg Bp)$ is satisfiable in $\mathsf{K45}$.
2. Axiom $\mathsf{4}$, transitivity. Take $W = \set{w, v, u}$ and $R = \set{(w, v), (v, u), (u, u)}$, with $p$ true at $v$ only. The frame is serial.
   At $v$, $p$ holds and $Bp$ fails since $u$ lacks $p$.
   So $B(p \wedge \neg Bp)$ holds at $w$, and $\mathsf{KD}$ does not prove part 1.
3. Axiom $\mathsf{5}$ is not needed for parts 1 and 2. It is part of $\mathsf{KD45}$, the logic in which the result is usually stated.

### Consequences

1. In $\mathsf{KD45}$ the agent can never come to believe a true Moore sentence about herself. This is the logical core of Moore's paradox.
2. A Moore sentence can be true but not believed, so belief is not closed under "being true about oneself".
3. In [[public announcement logic|~0c910f5d]], announcing $p \wedge \neg K_a p$ to $a$ makes it false. Such sentences are unsuccessful updates.

### Generalizations

1. The second Moore form $p \wedge B\neg p$ also cannot be believed in $\mathsf{KD45}$. From $B(p \wedge B\neg p)$ one gets $Bp$ and $BB\neg p$, hence $B\neg p$, by [[the collapse of iterated belief|~71039b6a]], and then $B\bot$.
2. For knowledge, axiom $\mathsf{T}$ alone suffices: $\mathsf{T} \vdash \neg K(p \wedge \neg Kp)$. From $K(p \wedge \neg Kp)$ one gets $Kp$ and $K\neg Kp$, and $\mathsf{T}$ turns the second into $\neg Kp$.
   This is the key step in the proof of Fitch's paradox of knowability.

## History

Moore noted the absurdity of asserting "it is raining but I do not believe it", and the name Moore's paradox is attributed to Wittgenstein.
Hintikka's Knowledge and Belief (1962) gave the doxastic logic analysis: such sentences are consistent but cannot be consistently believed.

## Explanations

### L1 human

The sentence "it is raining and I do not believe it is raining" can be true.
But you cannot believe it.
If you believed it, you would believe it is raining, and you would also believe that you do not believe it.
A rational believer who knows her own mind cannot hold both.

### L2 human

We see where each axiom enters.

1. $\mathsf{K}$ splits $B(p \wedge \neg Bp)$ into $Bp$ and $B\neg Bp$.
2. $\mathsf{4}$ turns $Bp$ into $BBp$.
3. $\mathsf{K}$ joins $BBp$ and $B\neg Bp$ into $B(Bp \wedge \neg Bp)$, that is, $B\bot$.
4. $\mathsf{D}$ rules out $B\bot$.

The typical use is to show that a formula is consistent yet unbelievable.
A trap: the theorem concerns the agent's own beliefs; "it is raining and Bob does not believe it" can be believed by Ann.

### L3 human

In a $\mathsf{KD45}$ model, belief is truth throughout the agent's cluster of doxastic alternatives, and $\neg Bp$ is constant on that cluster.
So inside the cluster, $p \wedge \neg Bp$ would need $p$ everywhere and $p$ false somewhere.
This is the semantic shadow of the syntactic proof, and it is what [[the proof|~f58fe59d]] makes precise.
