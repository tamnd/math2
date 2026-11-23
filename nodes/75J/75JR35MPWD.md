---
tag: 75JR35MPWD
kind: example
name: A dead-end world believes a contradiction
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
not_instance_of:
  - target: RTP4HTZYK3
    note: at a world with no successors the box makes the agent believe the contradiction, so the model violates the consistency axiom D of rational belief
uses: [JS8W7PA6JK, FDFQFWPM4X, TCAYVAVAK4]
sources:
  - url: https://en.wikipedia.org/wiki/Epistemic_modal_logic
    locator: section Axiom systems
  - url: https://en.wikipedia.org/wiki/Doxastic_logic
    locator: lead section
---

## Example

An agent who considers no situation possible believes everything, including contradictions.
This is the simplest model that shows why [[doxastic logic|RTP4HTZYK3]] needs axiom $\mathsf{D}$.

Let $W = \{w\}$ and $R = \emptyset$, so the single world sees nothing, and read the box as belief $B$.

1. $B \varphi$ at $w$ needs $\varphi$ at every successor of $w$.
   There are none, so $B \varphi$ is true at $w$ for every formula $\varphi$.
2. In particular $B \bot$ is true at $w$, so the agent believes a contradiction.
   Also $B p$ and $B \neg p$ are both true at $w$.
3. $R$ is transitive and Euclidean, since there are no pairs to check, so the frame is a frame of $\mathsf{K45}$.
4. $R$ is not serial, and axiom $\mathsf{D}$, which is $\neg B \bot$, fails at $w$.

So the model is a model of [[the logic K|JS8W7PA6JK]], and even of $\mathsf{K45}$, but not of rational belief.

## Remarks

Seriality is exactly the frame condition that rules out such worlds, by [[the common modal axioms|FDFQFWPM4X]].
The model also shows why [[the Moore sentence theorem|TCAYVAVAK4]] needs axiom $\mathsf{D}$: at $w$ the agent believes $p \wedge \neg B p$ along with everything else.

If we add the single pair $(w, w)$, the frame becomes serial, and in fact an $\mathsf{S5}$ frame.
Then the agent believes exactly the formulas true at $w$, and $B \bot$ fails.
In [[deontic logic|7B74J6J5JV]] the same dead end is a situation in which everything is obligatory, and $\mathsf{D}$ excludes it there too.

## Explanations

### L1 human

Belief in a Kripke model means "true in every world I think possible".
If the agent thinks that no world is possible, the condition holds for every sentence.
Then she believes everything, including contradictions.
A rational believer always thinks that at least one world is possible.

### L2 human

To check axiom $\mathsf{D}$ in a finite model, look for a world without outgoing arrows.
If every world has one, $\mathsf{D}$ holds at every world, and if some world has none, $B \bot$ is true there.
The typical use is to show that a proposed model of belief is inconsistent somewhere.
Watch out: vacuous truth is still truth, so "believes everything" is a real consequence of having no alternatives.

### L3 human

$\mathsf{K45}$ is the logic of transitive Euclidean frames, and each of its rooted frames is either a single dead end or a cluster with an optional root.
Adding $\mathsf{D}$ removes the dead end, which gives $\mathsf{KD45}$.
