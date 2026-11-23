---
tag: DX4BZJ272P
kind: example
name: A KD45 model of belief is not a model of knowledge
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
not_instance_of:
  - target: EA34W4ERRE
    note: the box is true of a false proposition at the actual world, so the truth axiom of knowledge fails
uses: [RTP4HTZYK3, 1CFMP9DEE6, JDE7CN1C48, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Epistemic_modal_logic
    locator: section Axiom systems
  - url: https://en.wikipedia.org/wiki/Doxastic_logic
    locator: lead section
---

## Example

Ann is sure that her train leaves at nine, but the timetable changed and it leaves at ten.
Let $p$ say "the train leaves at nine".
A model of Ann's mind must let her be certain of $p$ while $p$ is false, so it cannot be a model of [[knowledge|EA34W4ERRE]].

Let $W = \{w, v\}$ with $p$ true at $v$ only, and let $w$ be the actual world.
Let $R = \{(w, v), (v, v)\}$, so that at both worlds Ann considers only $v$ possible.

1. $R$ is serial, since both worlds see $v$.
2. $R$ is transitive.
   The composable pairs are $(w, v)$ then $(v, v)$, and $(v, v)$ then $(v, v)$, with composites $(w, v)$ and $(v, v)$, which are in $R$.
3. $R$ is [[Euclidean|JDE7CN1C48]], since every world sees only $v$ and $v R v$ holds.
4. So the frame is a $\mathsf{KD45}$ frame, and the logic $\mathsf{KD45}$ is sound for it by [[the completeness of KD45|1CFMP9DEE6]].
5. At $w$ the only world seen is $v$, where $p$ is true, so $\square p$ is true at $w$.
6. The atom $p$ is false at $w$, so $\square p \to p$ is false at $w$.

The box behaves as belief: Ann is sure that the train leaves at nine, and she is wrong.
It is not knowledge, because the truth axiom $K \varphi \to \varphi$ fails at the actual world.

## Remarks

The truth axiom matches reflexivity, by [[the common modal axioms|FDFQFWPM4X]], and $w R w$ fails here.
The model is a correct model of [[doxastic logic|RTP4HTZYK3]]: Ann's beliefs are consistent, since she sees a world, and she is introspective about them.
If we add the pair $(w, w)$, Ann considers the true world too, so she no longer believes $p$.
But then the relation fails to be Euclidean, since $w R w$ and $w R v$ would need $v R w$.
Adding $(v, w)$ as well gives the universal relation, an $\mathsf{S5}$ frame, in which Ann neither believes nor knows $p$.

## Explanations

### L1 human

Believing is not knowing.
Ann is certain that her train leaves at nine, but it leaves at ten.
A picture of her mind has to allow her to be certain of something false.
So the rule "what you know is true" holds for knowledge but not for belief.

### L2 human

To test whether a box can be read as knowledge, look for a world that does not see itself.
At such a world $w$, let $p$ be true at all worlds seen from $w$ and false at $w$.
Then $\square p$ is true and $p$ is false at $w$, so the truth axiom fails.
Here $w$ sees only $v$, and $p$ is true exactly at $v$.
Watch out: the frame satisfies axioms $\mathsf{4}$ and $\mathsf{5}$, so introspection alone does not make a box into knowledge.

### L3 human

$\mathsf{KD45}$ and $\mathsf{S5}$ differ by reflexivity only.
A point-generated $\mathsf{KD45}$ frame is a nonempty cluster of believed worlds, possibly with a root outside the cluster that sees all of it.
Here the cluster is $\{v\}$ and the root is $w$.
Combined logics of knowledge and belief relate the two boxes, for example by $K \varphi \to B \varphi$.
