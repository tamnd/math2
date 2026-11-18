---
tag: RTP4HTZYK3
kind: concept
name: Doxastic logic
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
specializes: [ERG3KAQWYF]
uses: [C3RZY20ETK, ~8b9604fb, 1CFMP9DEE6, JDE7CN1C48, FDFQFWPM4X, D1TJYZZDCY, 1P2B0C7CQ4]
sources:
  - url: https://en.wikipedia.org/wiki/Doxastic_logic
    locator: lead section, section Types of reasoners
  - url: https://en.wikipedia.org/wiki/Moore%27s_paradox
    locator: section The problem
  - url: https://en.wikipedia.org/wiki/Epistemic_modal_logic
    locator: section Axiom systems
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 3
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section D
    note: adopted
    mention: wikipedia://en/76765067#TG4A
    sections: [Summary]
same_as:
  wikipedia: Doxastic logic
inventory: [9BFQGV4DPG]
---

## Summary

Doxastic logic is a branch of [[modal logic|C3RZY20ETK]] that deals with the logic of belief, modeling the beliefs of rational agents.
It has a box $B_a$ for each agent, and $B_a\varphi$ reads "agent $a$ believes that $\varphi$".
The standard system is $\mathsf{KD45}$, the logic of serial, transitive and Euclidean frames, by [[the completeness of KD45|1CFMP9DEE6]].
Its axioms say that beliefs are consistent and that the agent knows what she believes and what she does not believe.
Unlike knowledge in [[epistemic logic|~8b9604fb]], belief may be false, so the truth axiom $B\varphi \to \varphi$ is dropped.
Doxastic logic matters because it separates what an agent takes to be true from what is true, which is needed for belief revision, games and deception.

## Motivation

People act on beliefs, and beliefs can be wrong.
A model of an agent's mind must allow her to be sure of something false, so the box of belief cannot be reflexive.
Still, a rational agent should not believe a contradiction, and should be aware of her own beliefs.
These three demands, falsity allowed, consistency and introspection, pick out $\mathsf{KD45}$.
In a Kripke model, $B_a\varphi$ at $w$ says that $\varphi$ holds in all worlds that $a$ regards as candidates for the actual one at $w$.

## Notation

1. $B_a\varphi$: agent $a$ believes $\varphi$. Some authors write $\square_a$ or $\mathrm{Bel}_a$.
2. The axioms: $\mathsf{D}$ is $\neg B\bot$, $\mathsf{4}$ is $B\varphi \to BB\varphi$, $\mathsf{5}$ is $\neg B\varphi \to B\neg B\varphi$.
3. $\mathsf{KD45}_n$ is the logic with $n$ agents, each obeying $\mathsf{KD45}$.
4. A Moore sentence is a formula of the form $p \wedge \neg Bp$.

## Remarks

### Examples

1. "It is raining, but I do not believe that it is raining" is consistent, but no $\mathsf{KD45}$ agent can believe it, by [[the Moore sentence theorem|~fadab0bc]]. The model is in [[Moore's paradox in KD45|~bf93db5c]].
2. In $\mathsf{KD45}$, believing that one believes is the same as believing, see [[the collapse of iterated belief|~71039b6a]].
3. A $\mathsf{KD45}$ model in which the agent holds a false belief is [[the train timetable example|~1fa3a926]].

### Non-examples

1. In the logic $\mathsf{K}$ a world without successors believes $\bot$, so $\mathsf{K}$ alone is not a logic of rational belief, see [[the dead-end world|~44f73073]].
2. A model of [[S5|VC3A2VWXND]] is a model of knowledge. Read as belief it is too strong, since then every belief is true.

### Basic properties

1. Frame correspondences, by [[the common modal axioms|FDFQFWPM4X]]: $\mathsf{D}$ holds on serial frames, $\mathsf{4}$ on transitive frames, $\mathsf{5}$ on [[Euclidean|JDE7CN1C48]] frames.
2. $\mathsf{KD45}$ is a [[normal modal logic|D1TJYZZDCY]], sound and complete for serial, transitive, Euclidean frames.
3. A rooted $\mathsf{KD45}$ frame is a nonempty cluster, in which every world sees every world, plus possibly a root outside it that sees the whole cluster.
4. $\mathsf{KD45} \vdash \neg B(p \wedge \neg Bp)$: a Moore sentence cannot be believed.
5. $\mathsf{KD45} \vdash BBp \leftrightarrow Bp$ and $\mathsf{KD45} \vdash B\neg Bp \leftrightarrow \neg Bp$.
6. $\mathsf{KD45} \nvdash Bp \to p$: belief can be false.
7. Satisfiability of $\mathsf{KD45}$ is NP-complete for one agent and PSPACE-complete for two or more, by [[the complexity theorem|1P2B0C7CQ4]].

### History

Hintikka's Knowledge and Belief (1962) treated belief alongside knowledge.
Moore observed that "it is raining but I do not believe it" is absurd to assert though it may be true, and the name Moore's paradox is attributed to Wittgenstein.
The system $\mathsf{KD45}$ became the standard logic of belief in the computer science and game theory literature.
Logics combining knowledge and belief add bridge axioms such as $K\varphi \to B\varphi$ and $B\varphi \to KB\varphi$.

### Common errors

1. Using $\mathsf{T}$ for belief. Then all beliefs are true, and belief collapses into knowledge.
2. Reading $\neg Bp$ as $B\neg p$. Suspending judgment on $p$ differs from believing $\neg p$.
3. Thinking that a Moore sentence is contradictory. It is satisfiable; what fails is believing it.

## Explanations

### L1 human

Doxastic logic is a logic of "believes".
You believe something when it holds in every situation you think might be the real one.
Unlike knowledge, belief can be wrong: you can believe your keys are in your bag when they are on the table.
Rational belief should not contradict itself, and you should be aware of what you believe.

### L2 human

We check axiom $\mathsf{D}$ in a model.
Let $W = \set{w, v}$ and $R = \set{(w, v), (v, v)}$.

1. Every world has a successor: $w$ sees $v$, and $v$ sees $v$.
2. $B\bot$ at a world would need $\bot$ at all its successors, so it fails at both worlds. So $\neg B\bot$ holds.
3. At $w$, the agent's beliefs are the formulas true at $v$, and these need not be true at $w$.

The typical use is to build a model of an agent with false but consistent beliefs.
A trap: seriality is about the agent's own world too; one dead-end world is enough to make $B\bot$ satisfiable.

### L3 human

$\mathsf{KD45}$ and $\mathsf{S5}$ differ by reflexivity, and belief is often modelled as knowledge "relative to the cluster".
Plausibility models refine $\mathsf{KD45}$ with an ordering of worlds, and support belief revision in [[dynamic epistemic logic|~0c910f5d]].
Stalnaker argued in 2006 that natural bridge axioms between knowledge and belief force knowledge to be $\mathsf{S4.2}$ and belief to be definable from it.
