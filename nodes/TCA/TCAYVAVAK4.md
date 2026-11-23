---
tag: TCAYVAVAK4
kind: statement
role: theorem
name: A Moore sentence cannot be believed in KD45
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
uses: [RTP4HTZYK3, 1CFMP9DEE6, FDFQFWPM4X, JDE7CN1C48, 9TPXQT9625]
about: [RTP4HTZYK3]
proofs: [F9PNV3HSVA]
sources:
  - url: https://en.wikipedia.org/wiki/Moore%27s_paradox
    locator: section The problem
  - url: https://en.wikipedia.org/wiki/Doxastic_logic
    locator: lead section
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 3
---

## Statement

A consistent and introspective believer can never believe "$p$, and I do not believe $p$", although that sentence can be true.

Let $B$ be the box of [[doxastic logic|RTP4HTZYK3]], and let $p$ be an atom.

1. $\mathsf{KD4} \vdash \neg B (p \wedge \neg B p)$, and hence $\mathsf{KD45} \vdash \neg B (p \wedge \neg B p)$.
2. Semantically, $B (p \wedge \neg B p)$ is false at every world of every Kripke model whose relation is serial and transitive.
   In particular it is unsatisfiable on $\mathsf{KD45}$ frames.
3. The Moore sentence $p \wedge \neg B p$ itself is satisfiable on a $\mathsf{KD45}$ frame.

## Remarks

### Why each hypothesis is needed

Axiom $\mathsf{D}$, seriality, cannot be dropped.
At a world with no successors, $B \chi$ is true for every $\chi$, so $B (p \wedge \neg B p)$ is satisfiable in $\mathsf{K45}$, as [[the dead-end world|75JR35MPWD]] shows.

Axiom $\mathsf{4}$, transitivity, cannot be dropped either.
Take $W = \{w, v, u\}$ and $R = \{(w, v), (v, u), (u, u)\}$, with $p$ true at $v$ only, which is a serial frame.
At $v$ the atom $p$ holds and $B p$ fails, because $u$ lacks $p$, so the Moore sentence holds at $v$.
Since $w$ sees only $v$, $B (p \wedge \neg B p)$ holds at $w$, and $\mathsf{KD}$ does not prove part 1.

Axiom $\mathsf{5}$ plays no role in parts 1 and 2.
It is included because $\mathsf{KD45}$ is the logic in which the result is usually stated.

### What it gives you

In $\mathsf{KD45}$ an agent can never come to believe a true Moore sentence about herself, which is the logical core of Moore's paradox.
So a sentence can be true of an agent and still be closed to her belief.
[[Moore's paradox in a KD45 model|3KA7N0BEB7]] shows both halves in a two-world model.
In [[public announcement logic|9465T2PWZT]] the analogue is that announcing $p \wedge \neg K_a p$ to $a$ makes it false, as in [[the Moore announcement example|Z13C7EBPXB]].

### Generalizations

The second Moore form $p \wedge B \neg p$ cannot be believed in $\mathsf{KD45}$ either.
From $B (p \wedge B \neg p)$ we get $B p$ and $B B \neg p$, then $B \neg p$ by [[the collapse of iterated belief|G7HAS0P39P]], and then $B \bot$.
This form needs axiom $\mathsf{5}$, since the collapse $B B \varphi \to B \varphi$ uses the Euclidean property.

For knowledge, axiom $\mathsf{T}$ alone suffices: $\mathsf{KT} \vdash \neg K (p \wedge \neg K p)$.
From $K (p \wedge \neg K p)$ we get $K p$ and $K \neg K p$, and $\mathsf{T}$ turns the second into $\neg K p$.
This is the step on which [[Fitch's paradox of knowability|HVCW7QYXSW]] turns.

## History

George Edward Moore noted the absurdity of asserting "it is raining but I do not believe it", and Wittgenstein gave the observation the name Moore's paradox.
Hintikka's Knowledge and Belief (1962) gave the analysis in doxastic logic: such sentences are consistent, but they cannot be consistently believed.

## Explanations

### L1 human

The sentence "it is raining and I do not believe it is raining" can be true.
But you cannot believe it.
If you believed it, you would believe that it is raining, and you would also believe that you do not believe it.
A believer who is consistent and knows her own mind cannot hold both.

### L2 human

Here is where each axiom enters the derivation of part 1.
Axiom $\mathsf{K}$ splits $B (p \wedge \neg B p)$ into $B p$ and $B \neg B p$.
Axiom $\mathsf{4}$ turns $B p$ into $B B p$.
Axiom $\mathsf{K}$ joins $B B p$ and $B \neg B p$ into the following.
$$B (B p \wedge \neg B p), \text{ that is, } B \bot.$$
Axiom $\mathsf{D}$ then rules out $B \bot$.
The typical use is to show that a formula is consistent yet cannot be believed.
Watch out: the theorem concerns the agent's own beliefs, and Ann can believe "it is raining and Bob does not believe it".

### L3 human

In a $\mathsf{KD45}$ model, belief is truth throughout the agent's cluster of doxastic alternatives, and $\neg B p$ is constant on that cluster.
So inside the cluster, $p \wedge \neg B p$ would need $p$ everywhere and $p$ false somewhere.
That is the semantic shadow of the derivation, and [[the proof|F9PNV3HSVA]] makes it precise.
