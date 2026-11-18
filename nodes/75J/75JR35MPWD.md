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

Let $W = \set{w}$ and $R = \emptyset$: the single world sees nothing.
Read the box as belief, $B$.

1. $B\varphi$ at $w$ needs $\varphi$ at every successor of $w$. There are none, so $B\varphi$ is true at $w$ for every formula $\varphi$.
2. In particular $B\bot$ is true at $w$: the agent believes a contradiction.
3. Also $Bp$ and $B\neg p$ are both true at $w$.
4. $R$ is transitive and Euclidean, since there are no pairs to check. So the frame is a frame of $\mathsf{K45}$.
5. $R$ is not serial, and axiom $\mathsf{D}$, $\neg B\bot$, fails at $w$.

So this is a model of [[the logic K|JS8W7PA6JK]], and even of $\mathsf{K45}$, but not of rational belief.

## Remarks

Seriality is exactly what rules out such worlds, by [[the common modal axioms|FDFQFWPM4X]].
The example also shows why [[the Moore sentence theorem|TCAYVAVAK4]] needs axiom $\mathsf{D}$: at $w$, the agent believes $p \wedge \neg Bp$ along with everything else.
In deontic logic the same dead end means a situation in which everything is obligatory, and $\mathsf{D}$ again excludes it.

## Explanations

### L1 human

Belief in a Kripke model means "true in every world I think possible".
If the agent thinks no world is possible, the condition holds for every sentence.
Then she believes everything, including contradictions.
A rational believer always thinks at least one world is possible.

### L2 human

To check axiom $\mathsf{D}$ in a finite model, look for a world without arrows.

1. If every world has an outgoing arrow, $\mathsf{D}$ holds at every world.
2. If some world has none, $B\bot$ is true there and $\mathsf{D}$ fails.

The typical use is to show that a proposed model of belief is not consistent.
A trap: vacuous truth is still truth, so "believes everything" is a real consequence of having no alternatives.

### L3 human

$\mathsf{K45}$ is the logic of transitive Euclidean frames, and its rooted frames are either a cluster with an optional root or a single dead end.
Adding $\mathsf{D}$ removes the dead end, which gives $\mathsf{KD45}$.
