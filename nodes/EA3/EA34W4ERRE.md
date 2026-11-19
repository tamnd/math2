---
tag: EA34W4ERRE
kind: concept
name: Epistemic logic
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
specializes: [ERG3KAQWYF]
uses: [C3RZY20ETK, ERG3KAQWYF, NGHWZ9Y7ZV, VC3A2VWXND, N60RVXSA5W, FDFQFWPM4X, 0G8VEZ3WTK, JDE7CN1C48, H9RGWCR10W, 1P2B0C7CQ4]
sources:
  - url: https://en.wikipedia.org/wiki/Epistemic_modal_logic
    locator: section The negative introspection axiom, section Axiom systems, section Multi-agent systems
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapters 2 and 3
  - url: https://plato.stanford.edu/entries/logic-epistemic/
    locator: Rendsvig and Symons, Epistemic Logic, Stanford Encyclopedia of Philosophy
same_as:
  wikipedia: Epistemic modal logic
---

## Summary

Epistemic logic is the [[modal logic|C3RZY20ETK]] of knowledge.
For each agent $a$ in a finite set $\mathcal{A}$ it has a box $K_a$, and $K_a \varphi$ reads "agent $a$ knows that $\varphi$".
A model is a [[multimodal Kripke model|ERG3KAQWYF]] with one relation $R_a$ per agent, where $w R_a v$ means "at $w$, agent $a$ cannot rule out $v$".
Then $K_a \varphi$ is true at $w$ when $\varphi$ is true at every $v$ with $w R_a v$.
The standard system is $\mathsf{S5}_n$, with each $R_a$ an [[equivalence relation|0G8VEZ3WTK]]; its axioms say that knowledge is true and that agents know what they know and what they do not know.
The last axiom, negative introspection, is widely rejected for human knowledge, and $\mathsf{S4}$ or $\mathsf{S4.2}$ are then used instead.
Epistemic logic matters because it is the basis for reasoning about communication, games and distributed protocols.

## Motivation

A distributed protocol is correct when each process acts on what it knows, and what it knows depends on the messages it has seen.
A card player plans by asking what the others know about her hand.
In both cases one reasons about knowledge of facts, and also about knowledge of other agents' knowledge.
Possible worlds give a simple picture: an agent knows a fact when it holds in every situation that she cannot tell apart from the actual one.
This picture is [[Kripke semantics|NGHWZ9Y7ZV]], so the tools of modal logic apply.

## Notation

1. $K_a \varphi$: agent $a$ knows $\varphi$. The dual $\hat K_a \varphi = \neg K_a \neg\varphi$ reads "$a$ considers $\varphi$ possible".
2. A model is $M = (W, (R_a)_{a \in \mathcal{A}}, V)$. In $\mathsf{S5}$ models one often writes $\sim_a$ for $R_a$.
3. $E_G \varphi = \bigwedge_{a \in G} K_a \varphi$: everyone in the group $G$ knows $\varphi$.
4. $C_G \varphi$: $\varphi$ is [[common knowledge|7BCMKF2P7X]] in $G$. $D_G \varphi$: $\varphi$ is distributed knowledge in $G$.
5. $\mathsf{S5}_n$, $\mathsf{S4}_n$ and $\mathsf{KD45}_n$ denote the logics with $n$ agents, each box obeying $\mathsf{S5}$, $\mathsf{S4}$ or $\mathsf{KD45}$.

## Remarks

### Examples

1. Two agents and a deal of three cards give an $\mathsf{S5}_2$ model, worked in [[the card deal example|EM6M72T720]].
2. On an $\mathsf{S4.2}$ model, an agent can fail to know $p$ without knowing that she fails, see [[the failure of negative introspection|RF03DRPGN3]].
3. Every Kripke model makes knowledge closed under logical consequence, see [[logical omniscience|TSE4F131XH]].

### Non-examples

1. A model of belief, in which an agent "knows" something false, is not a model of knowledge, see [[the doxastic non-example|DX4BZJ272P]].
2. "Agent $a$ assigns $\varphi$ probability above $0.99$" is not a box of a Kripke model. Two such facts can each pass the threshold while their conjunction fails it. A Kripke box always satisfies $K_a\varphi \wedge K_a\psi \to K_a(\varphi \wedge \psi)$.

### Basic properties

The axioms and their frame conditions, as in [[the common modal axioms|FDFQFWPM4X]]:

1. $\mathsf{K}$: $K_a(\varphi \to \psi) \to (K_a\varphi \to K_a\psi)$, valid on all frames. With necessitation it makes knowledge closed under consequence, see [[epistemic closure|H9RGWCR10W]].
2. $\mathsf{T}$: $K_a\varphi \to \varphi$, knowledge is true. It holds on reflexive frames.
3. $\mathsf{4}$: $K_a\varphi \to K_a K_a\varphi$, positive introspection. It holds on transitive frames.
4. $\mathsf{5}$: $\neg K_a\varphi \to K_a\neg K_a\varphi$, negative introspection. It holds on [[Euclidean|JDE7CN1C48]] frames.
5. A relation is reflexive and Euclidean exactly when it is an equivalence relation. So $\mathsf{K} + \mathsf{T} + \mathsf{5}$ is [[S5|VC3A2VWXND]], and $\mathsf{4}$ follows.
6. Satisfiability is NP-complete for $\mathsf{S5}_1$, PSPACE-complete for $\mathsf{S5}_n$ with $n \ge 2$, and EXPTIME-complete with common knowledge and $n \ge 2$, by [[the complexity theorem|1P2B0C7CQ4]].

### History

Hintikka's Knowledge and Belief (1962) founded epistemic logic with a possible worlds semantics.
Hintikka accepted positive introspection and rejected negative introspection, so his logic of knowledge is [[S4|N60RVXSA5W]].
Computer scientists in the 1980s, among them Halpern and Moses, adopted $\mathsf{S5}_n$ for distributed systems.
There an agent's knowledge is defined by its local state, so negative introspection holds by construction.
Stalnaker argued in 2006 that combining knowledge with belief leads to $\mathsf{S4.2}$.
Williamson argued against positive introspection in Knowledge and Its Limits (2000).

### Common errors

1. Taking $\mathsf{S5}$ as the obvious logic of knowledge. Axiom $\mathsf{5}$ makes the agent know the full extent of her ignorance, which fails when she has false beliefs. The $\mathsf{S5}$ reading fits "knowledge" defined by a local state, as in distributed systems.
2. Reading the necessitation rule as "every true fact is known". It says that every valid formula is known.
3. Reading $\neg K_a \varphi$ as $K_a \neg\varphi$. Not knowing that it rains differs from knowing that it does not rain.
4. Treating $K_a K_b \varphi$ as $K_b K_a \varphi$. The boxes of different agents do not commute in general.

## Explanations

### L1 human

Epistemic logic is a logic of "knows".
Picture all the ways the world might be.
You know a fact when it is true in every way the world might be, as far as you can tell.
If you hold the ace of spades, you know it, because every situation you consider has you holding it.
You do not know your friend's card when you can picture two situations with different cards for her.

### L2 human

We read off knowledge in a two-world model for one agent.
Let $W = \set{w, v}$, let $p$ be true at $w$ only, and let $R$ relate every world to both worlds.

1. At $w$, the agent considers both $w$ and $v$ possible.
2. $p$ fails at $v$, so $K p$ is false at $w$.
3. $\neg p$ fails at $w$, so $K \neg p$ is false at $w$ as well.
4. $\neg K p$ is true at both worlds, by the argument of step 2 at each world. So $K \neg K p$ is true at $w$: the agent knows that she does not know $p$.

The typical use is to trace who knows what after an event, by removing worlds or arrows.
A trap: step 4 used that $R$ is an equivalence relation, and it fails in models where $R$ is only reflexive and transitive.

### L3 human

Epistemic logic is [[multimodal logic|ERG3KAQWYF]] with an epistemic reading, and its completeness and complexity results are those of $\mathsf{S5}_n$ and its neighbours.
New operators come from groups: common knowledge is the box of the transitive closure of $\bigcup_{a \in G} R_a$, and distributed knowledge is the box of $\bigcap_{a \in G} R_a$.
The other new feature is change: [[dynamic epistemic logic|9465T2PWZT]] adds modalities for announcements and actions.
Logical omniscience is the main limit of the Kripke picture, and awareness or impossible-world models are proposed to avoid it.
