---
tag: RTP4HTZYK3
kind: concept
name: Doxastic logic
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
specializes: [ERG3KAQWYF]
uses: [C3RZY20ETK, EA34W4ERRE, 1CFMP9DEE6, JDE7CN1C48, FDFQFWPM4X, D1TJYZZDCY, 1P2B0C7CQ4]
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

Ann is sure that her keys are in her bag, but they are on the table.
Her belief is false, yet it is consistent, and she knows that she holds it.
Doxastic logic is the [[modal logic|C3RZY20ETK]] of such belief: it lets an agent be wrong, but not incoherent.

The language has a box $B_a$ for each agent, and $B_a \varphi$ reads "agent $a$ believes that $\varphi$".
In a Kripke model, $B_a \varphi$ is true at $w$ when $\varphi$ holds at every world that $a$ takes as a candidate for the actual one at $w$.
The standard system is $\mathsf{KD45}$, the logic of serial, transitive and [[Euclidean|JDE7CN1C48]] frames, by [[the completeness of KD45|1CFMP9DEE6]].
Its axioms are $\mathsf{K}$ and the following three.
$$\neg B \bot, \qquad B \varphi \to B B \varphi, \qquad \neg B \varphi \to B \neg B \varphi.$$
Unlike knowledge in [[epistemic logic|EA34W4ERRE]], belief may be false, so the truth axiom $B \varphi \to \varphi$ is not part of the logic.

## Motivation

People act on beliefs, and beliefs can be wrong.
A model of an agent's mind must allow her to be sure of something false, so the relation of belief cannot be reflexive.
Still, a rational agent should not believe a contradiction, and she should be aware of her own beliefs.
These three demands (falsity allowed, consistency, introspection) pick out $\mathsf{KD45}$.

Belief is where agents go wrong, so it is the attitude that changes when they learn.
[[AGM belief revision|Y05YQN7HGQ]] studies that change from the outside, and plausibility models in [[dynamic epistemic logic|9465T2PWZT]] study it inside a Kripke model.
In game theory, the beliefs of players about each other are $\mathsf{KD45}$ boxes, often with probabilities on top.

## Notation

We write $B_a \varphi$, or $B \varphi$ for one agent; some authors write $\square_a$ or $\mathrm{Bel}_a$.
The axioms are named $\mathsf{D}$ for $\neg B \bot$, $\mathsf{4}$ for positive introspection and $\mathsf{5}$ for negative introspection.
$\mathsf{KD45}_n$ is the logic with $n$ agents, each obeying $\mathsf{KD45}$.
A Moore sentence is a formula of the form $p \wedge \neg B p$.

## Remarks

### A first model

Let $W = \{w, v_1, v_2\}$ with actual world $w$.
The atom $\mathit{bag}$ ("the keys are in the bag") is true at $v_1$ and $v_2$, and the atom $\mathit{rain}$ is true at $v_1$ only.
At every world Ann takes $v_1$ and $v_2$ as the candidates, so $R = \{(x, v_i) : x \in W, \ i = 1, 2\}$.
At $w$ she sees $v_1$ and $v_2$, where $\mathit{bag}$ holds, so $B \mathit{bag}$ is true at $w$, while $\mathit{bag}$ itself is false there.
She believes neither $\mathit{rain}$ nor $\neg \mathit{rain}$, because the two candidates disagree.
Check: $R$ is serial, and every world sees exactly $\{v_1, v_2\}$, so $R$ is transitive and Euclidean.

### The shape of a belief frame

The axioms match frame conditions by [[the common modal axioms|FDFQFWPM4X]]: $\mathsf{D}$ matches seriality, $\mathsf{4}$ transitivity and $\mathsf{5}$ the Euclidean property.
Together they force a simple shape.
A rooted $\mathsf{KD45}$ frame is a nonempty cluster in which every world sees every world, plus possibly a root outside it that sees the whole cluster.
In the first model the cluster is $\{v_1, v_2\}$ and the root is $w$.
So belief is like knowledge relative to the cluster, and the actual world may lie outside it.

Two collapse laws follow, and [[the collapse example|G7HAS0P39P]] works them in a model.
$\mathsf{KD45}$ proves $B B \varphi \leftrightarrow B \varphi$ and $B \neg B \varphi \leftrightarrow \neg B \varphi$, so iterated belief adds nothing.
Satisfiability is NP-complete for one agent and PSPACE-complete for two or more, by [[the complexity theorem|1P2B0C7CQ4]].

### Moore's paradox

In the first model, take $p = \neg \mathit{bag}$, which is true at $w$.
Ann does not believe $p$, because $p$ fails at $v_1$, so the Moore sentence $p \wedge \neg B p$ is true at $w$.
Yet she cannot believe it.
By [[the Moore sentence theorem|TCAYVAVAK4]], $\mathsf{KD45}$ proves $\neg B (p \wedge \neg B p)$ for every agent and every $p$.
[[Moore's paradox in a KD45 model|3KA7N0BEB7]] shows the same thing on a two-world model: the sentence can be true, but it cannot be believed.

### What it is not

The logic $\mathsf{K}$ alone is not a logic of rational belief.
In [[the dead-end world|75JR35MPWD]] a world without successors believes $\bot$, and with it every formula.

[[S5|VC3A2VWXND]] is not a logic of belief either, because its frames are reflexive.
Read as belief, it makes every belief true, so it erases the gap that doxastic logic exists to describe; [[the train timetable model|DX4BZJ272P]] is a belief model that no $\mathsf{S5}$ frame can match.

### Watch out

Do not read $\neg B p$ as $B \neg p$.
In the first model Ann has neither $B \mathit{rain}$ nor $B \neg \mathit{rain}$: suspending judgment is not believing the opposite.

Do not think that a Moore sentence is a contradiction.
It is true at $w$ in the first model, so it is satisfiable; what fails is believing it, or sincerely asserting it.

### History

Hintikka's Knowledge and Belief (1962) treated belief alongside knowledge with possible worlds.
G. E. Moore observed that "it is raining but I do not believe it" is absurd to assert though it may be true, and Wittgenstein gave the observation the name Moore's paradox.
$\mathsf{KD45}$ became the standard logic of belief in computer science and in game theory.

### Try it

First, in the first model, is $B B \mathit{bag}$ true at $w$?
Yes: $B \mathit{bag}$ holds at $v_1$ and $v_2$, since both see only $v_1$ and $v_2$, and $w$ sees exactly those worlds.

Second, prove $B \neg B p \to \neg B p$ in $\mathsf{KD45}$.
If $B \neg B p$ and $B p$, then axiom $\mathsf{4}$ gives $B B p$, so $B (B p \wedge \neg B p)$, which is $B \bot$ and contradicts $\mathsf{D}$.

## Explanations

### L1 human

Doxastic logic is a logic of "believes".
You believe something when it holds in every situation you think might be the real one.
Unlike knowledge, belief can be wrong: you can believe that your keys are in your bag when they are on the table.
Rational belief should still not contradict itself, and you should be aware of what you believe.

### L2 human

Here is a typical check: does axiom $\mathsf{D}$ hold in the model $W = \{w, v\}$, $R = \{(w, v), (v, v)\}$?
Every world has a successor, since $w$ sees $v$ and $v$ sees $v$.
For $B \bot$ to hold at a world, $\bot$ would have to hold at all its successors, and there is at least one, so $B \bot$ fails at both worlds.
At $w$ the agent's beliefs are exactly the formulas true at $v$, and these need not be true at $w$.
So the model describes an agent with consistent beliefs that may be false, which is the typical use of a belief model.
Watch out: one world without successors anywhere in the model is enough to make $B \bot$ satisfiable.

### L3 human

$\mathsf{KD45}$ and $\mathsf{S5}$ differ only by reflexivity, and logics that combine knowledge and belief add bridge axioms such as $K \varphi \to B \varphi$ and $B \varphi \to K B \varphi$.
Stalnaker argued in 2006 that natural bridge axioms force knowledge to be $\mathsf{S4.2}$ and make belief definable from knowledge.
Plausibility models refine $\mathsf{KD45}$ by an ordering of worlds, so that belief is truth in the most plausible worlds, and they support belief revision in [[dynamic epistemic logic|9465T2PWZT]].
