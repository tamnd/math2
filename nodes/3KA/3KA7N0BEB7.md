---
tag: 3KA7N0BEB7
kind: example
name: Moore's paradox in a KD45 model
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [RTP4HTZYK3]
uses: [TCAYVAVAK4, 1CFMP9DEE6, JDE7CN1C48]
sources:
  - url: https://en.wikipedia.org/wiki/Moore%27s_paradox
    locator: section The problem
  - url: https://en.wikipedia.org/wiki/Doxastic_logic
    locator: lead section
---

## Example

Let $p$ say "it is raining".
Carl is indoors, and he is sure it is dry outside, but it is raining.

1. Let $W = \set{w, v}$, with $w$ the actual world. Let $p$ be true at $w$ and false at $v$.
2. Let $R = \set{(w, v), (v, v)}$: at both worlds Carl considers only the dry world $v$ possible.
3. $R$ is serial, transitive and [[Euclidean|JDE7CN1C48]], so the model is a $\mathsf{KD45}$ model, see [[the completeness of KD45|1CFMP9DEE6]].
4. At $w$: $p$ is true, and $Bp$ is false since $p$ fails at $v$. So the Moore sentence $p \wedge \neg Bp$ is true at $w$.
5. At $v$: $p$ is false, so $p \wedge \neg Bp$ is false at $v$.
6. $B(p \wedge \neg Bp)$ at $w$ needs $p \wedge \neg Bp$ at $v$, which fails by step 5. So Carl does not believe the Moore sentence.
7. At $v$ the same holds, since $v$ also sees only $v$.
8. Carl does believe $\neg p$ at $w$, since $p$ fails at $v$. So he also satisfies the second Moore form: $p \wedge B\neg p$ is true at $w$.

The Moore sentence is true at $w$, and Carl could even be told it.
But no $\mathsf{KD45}$ model has a world where he believes it, by [[the theorem|TCAYVAVAK4]].

## Remarks

Step 6 is an instance of a general pattern.
In a $\mathsf{KD45}$ model the worlds Carl considers possible form a cluster, and $Bp$ has one value on the whole cluster.
If he believed $p \wedge \neg Bp$, then $p$ would hold on the cluster, so $Bp$ would hold on it, contradicting $\neg Bp$.
If Carl is told the Moore sentence and believes the speaker, he must give up $\neg Bp$ at once: he comes to believe $p$, and the sentence he was told is no longer true of him.

## Explanations

### L1 human

"It is raining but I don't believe it" can be true: Carl is wrong about the weather.
Carl himself cannot believe it.
If he did, he would believe it is raining, so the second half, "I don't believe it", would be false.

### L2 human

To test whether an agent believes a formula at $w$, check it at each world $w$ sees.

1. Here $w$ sees only $v$.
2. The Moore sentence fails at $v$ because $p$ fails at $v$.
3. So the agent does not believe it.

The typical use is to separate "true about the agent" from "believed by the agent".
A trap: the Moore sentence is not a contradiction; step 4 shows it is true at $w$.

### L3 human

Moore sentences are the standard examples of truths that are not believable, and, for knowledge, of truths that are not knowable.
In dynamic epistemic logic the same sentences are unsuccessful: announcing them makes them false.
