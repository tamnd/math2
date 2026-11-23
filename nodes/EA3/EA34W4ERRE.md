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

A coin lies under a cup, showing heads.
Ann has lifted the cup and Bob has not, so Ann knows the coin shows heads and Bob does not.
Bob does know one thing about Ann, though: she knows which side is up, whichever side it is.
Epistemic logic is the [[modal logic|C3RZY20ETK]] that makes such statements exact, including statements about what agents know of each other's knowledge.

For each agent $a$ in a finite set $\mathcal{A}$ the language has a box $K_a$, and $K_a \varphi$ reads "agent $a$ knows that $\varphi$".
A model is a [[multimodal Kripke model|ERG3KAQWYF]] $M = (W, (R_a)_{a \in \mathcal{A}}, V)$, where $w R_a v$ means that at $w$ agent $a$ cannot rule out $v$.
The truth clause is the usual one for a box:
$$M, w \models K_a \varphi \iff M, v \models \varphi \text{ for every } v \text{ with } w R_a v.$$
The standard system is $\mathsf{S5}_n$, in which every $R_a$ is an [[equivalence relation|0G8VEZ3WTK]].
Its axioms say that knowledge is true, and that each agent knows what she knows and what she does not know.

## Motivation

A distributed protocol is correct when each process acts on what it knows, and what a process knows depends on the messages it has seen.
A card player plans by asking what the others know about her hand, and what they think she knows about theirs.
In both cases we reason about facts, about knowledge of facts, and about knowledge of other agents' knowledge.
Possible worlds give a simple picture of all three: an agent knows a fact when it holds in every situation that she cannot tell apart from the actual one.
That picture is [[Kripke semantics|NGHWZ9Y7ZV]], so the methods of modal logic (correspondence, completeness, complexity) apply at once.

Epistemic logic is the base of the rest of the epistemic part of the sub-area.
[[Common knowledge|7BCMKF2P7X]] adds a group operator, [[doxastic logic|RTP4HTZYK3]] weakens knowledge to belief, and [[dynamic epistemic logic|9465T2PWZT]] lets announcements change the model.
The [[muddy children puzzle|BG9TYCJ7HP]] uses all of these at once.

## Notation

We write $K_a \varphi$ for "$a$ knows $\varphi$", and $\hat K_a \varphi = \neg K_a \neg \varphi$ for "$a$ considers $\varphi$ possible".
In $\mathsf{S5}$ models many books write $\sim_a$ for $R_a$, to stress that it is an indistinguishability relation.
For a group $G$, $E_G \varphi$ is $\bigwedge_{a \in G} K_a \varphi$ ("everyone in $G$ knows"), $C_G \varphi$ is common knowledge and $D_G \varphi$ is distributed knowledge.
The names $\mathsf{S5}_n$, $\mathsf{S4}_n$ and $\mathsf{KD45}_n$ denote the logics with $n$ agents in which each box obeys $\mathsf{S5}$, $\mathsf{S4}$ or $\mathsf{KD45}$.
Watch the letter $K$: it names both the knowledge box and the minimal modal logic $\mathsf{K}$, which is a different thing.

## Remarks

### A first model

Let $W = \{h, t\}$, with the atom $\mathit{heads}$ true at $h$ only, and let $h$ be the actual world.
Ann has looked, so she can tell the worlds apart, and Bob has not:
$$R_a = \{(h, h), (t, t)\}, \qquad R_b = \{(h, h), (h, t), (t, h), (t, t)\}.$$
At $h$ Ann sees only $h$, so $K_a \mathit{heads}$ is true.
Bob sees $h$ and $t$, and $\mathit{heads}$ fails at $t$, so $K_b \mathit{heads}$ is false.
Now take $\chi = K_a \mathit{heads} \vee K_a \neg \mathit{heads}$, "Ann knows whether it is heads".
At $h$ the first disjunct holds, and at $t$ the second holds, since Ann sees only $t$ there.
So $\chi$ is true at both worlds that Bob sees, and $K_b \chi$ is true at $h$.
Check: $K_a \neg K_b \mathit{heads}$ is also true at $h$, because Ann sees only $h$ and Bob does not know heads there.

A richer model with three cards and two players is worked in [[the card deal example|EM6M72T720]].
There each player knows her own card, and neither knows the other's.

### The axioms and their frames

Each axiom of $\mathsf{S5}$ matches a property of the relation, as in [[the common modal axioms|FDFQFWPM4X]].
Axiom $\mathsf{K}$, $K_a(\varphi \to \psi) \to (K_a \varphi \to K_a \psi)$, holds on every frame, and with the necessitation rule it makes knowledge closed under consequence; this is [[epistemic closure|H9RGWCR10W]].
Axiom $\mathsf{T}$, $K_a \varphi \to \varphi$, says that knowledge is true, and it matches reflexivity.
Axiom $\mathsf{4}$, $K_a \varphi \to K_a K_a \varphi$, is positive introspection, and it matches transitivity.
Axiom $\mathsf{5}$, $\neg K_a \varphi \to K_a \neg K_a \varphi$, is negative introspection, and it matches the [[Euclidean|JDE7CN1C48]] property.

A reflexive Euclidean relation is an equivalence relation, so $\mathsf{K} + \mathsf{T} + \mathsf{5}$ is already [[S5|VC3A2VWXND]] and proves $\mathsf{4}$.
Hintikka's choice was [[S4|N60RVXSA5W]], and Stalnaker later argued for $\mathsf{S4.2}$, which adds $\hat K_a K_a \varphi \to K_a \hat K_a \varphi$ and matches directed preorders.
The [[stopped clock model|RF03DRPGN3]] shows an $\mathsf{S4.2}$ agent who does not know, and does not know that she does not know.

### Several agents and groups

With two or more agents, new facts appear that no single box can state.
In the coin model Bob knows something about Ann's knowledge, and nested formulas such as $K_a K_b \varphi$ describe such chains.
The pooled information of a group is distributed knowledge $D_G$, the box of $\bigcap_{a \in G} R_a$.
In [[the pooled information example|2C84ZDGE7K]] each agent holds half of an argument, so the group knows a fact that neither member knows.

Complexity grows with the number of agents.
Satisfiability is NP-complete for $\mathsf{S5}_1$, PSPACE-complete for $\mathsf{S5}_n$ with $n \ge 2$, and EXPTIME-complete once common knowledge is added with $n \ge 2$, by [[the complexity theorem|1P2B0C7CQ4]].

### What it is not

A model of belief is not a model of knowledge.
In [[the train timetable model|DX4BZJ272P]] Ann is sure her train leaves at nine and she is wrong, so the truth axiom fails at the actual world.
The relation there is serial, transitive and Euclidean, but not reflexive.

"Agent $a$ gives $\varphi$ probability at least $0.9$" is not a Kripke box either.
Take ten equally likely worlds, with $\varphi$ false only at world 1 and $\psi$ false only at world 2.
Both have probability $0.9$, but $\varphi \wedge \psi$ has probability $0.8$, while every Kripke box satisfies $K_a \varphi \wedge K_a \psi \to K_a (\varphi \wedge \psi)$.

### Watch out

The most common slip is to take $\mathsf{S5}$ as the obvious logic of knowledge.
Axiom $\mathsf{5}$ makes the agent know the full extent of her ignorance, and that fails as soon as she can mistake a bad case for a good one, as with the stopped clock.
The $\mathsf{S5}$ reading fits knowledge defined by a local state, as for processes in a distributed system, and it is far less plausible for people.

Two smaller slips are worth naming.
The formula $\neg K_a \varphi$ is not $K_a \neg \varphi$: in the coin model $\neg K_b \mathit{heads}$ holds at $h$, but $K_b \neg \mathit{heads}$ fails there.
The necessitation rule does not say that every true fact is known, only that every valid formula is known; [[logical omniscience|TSE4F131XH]] works out what that costs.

### History

Hintikka's Knowledge and Belief (1962) founded epistemic logic with a possible worlds semantics.
He accepted positive introspection and rejected negative introspection, so his logic of knowledge is $\mathsf{S4}$.
In the 1980s computer scientists, among them Halpern and Moses, adopted $\mathsf{S5}_n$ for distributed systems, where knowledge is defined by local states.
Williamson argued against positive introspection in Knowledge and Its Limits (2000), and Stalnaker argued for $\mathsf{S4.2}$ in 2006.

### Try it

First, in the coin model, is $K_b \neg K_a \mathit{heads}$ true at $h$?
No: at $h$ itself Ann knows heads, so $\neg K_a \mathit{heads}$ fails at a world that Bob sees.

Second, show that a reflexive Euclidean relation is transitive.
If $x R y$, then $x R y$ and $x R x$ give $y R x$ by the Euclidean property; if also $y R z$, then $y R x$ and $y R z$ give $x R z$.

## Explanations

### L1 human

Epistemic logic is a logic of "knows".
Picture all the ways the world might be.
You know a fact when it is true in every way the world might be, as far as you can tell.
If you hold the ace of spades, you know it, because every situation you consider has you holding it.
You do not know your friend's card when you can picture two situations with different cards for her.
You can still know that she knows her own card, because that is true in every situation you picture.

### L2 human

Here is a typical check: in a two-world model for one agent, does the agent know that she does not know $p$?
Let $W = \{w, v\}$, let $p$ be true at $w$ only, and let $R$ relate every world to both worlds.
At $w$ the agent sees $v$, where $p$ fails, so $K p$ is false at $w$, and by the same argument it is false at $v$.
So $\neg K p$ holds at both worlds, and since $w$ sees both,
$$M, w \models K \neg K p.$$
The agent knows that she does not know $p$, and the reason is that $R$ is an equivalence relation.
If we remove the pair $(w, v)$ and keep $(v, w)$, the relation is still reflexive and transitive, but then $K p$ holds at $w$, and $K \neg K p$ fails at $v$, because $v$ sees $w$.
That is the stopped clock pattern: in $\mathsf{S4}$ models, ignorance need not be known.

### L3 human

Epistemic logic is [[multimodal logic|ERG3KAQWYF]] with an epistemic reading, and its completeness and complexity results are those of $\mathsf{S5}_n$ and its neighbors.
Group operators come from operations on relations: common knowledge is the box of the transitive closure of $\bigcup_{a \in G} R_a$, and distributed knowledge is the box of $\bigcap_{a \in G} R_a$.
The other new feature is change: [[dynamic epistemic logic|9465T2PWZT]] adds modalities for announcements and actions, and [[justification logic|5HKWCXEFG1]] replaces the box by explicit reasons.
Logical omniscience is the main limit of the Kripke picture, and awareness structures and impossible worlds are the standard attempts to avoid it.
In game theory the same models, with partitions in place of relations, are Aumann's information structures.
