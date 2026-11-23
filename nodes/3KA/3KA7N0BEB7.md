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

Carl is indoors and sure that it is dry outside, but it is raining.
So the sentence "it is raining and Carl does not believe that it is raining" is true.
We build a model of [[doxastic logic|RTP4HTZYK3]] in which this Moore sentence is true and yet Carl cannot believe it.

Let $p$ say "it is raining".
Let $W = \{w, v\}$ with actual world $w$, and let $p$ be true at $w$ and false at $v$.
Let $R = \{(w, v), (v, v)\}$, so that at both worlds Carl considers only the dry world $v$ possible.

1. $R$ is serial, transitive and [[Euclidean|JDE7CN1C48]], since every world sees exactly $\{v\}$ and $v R v$ holds.
   So the model is a $\mathsf{KD45}$ model, and the logic is sound for it by [[the completeness of KD45|1CFMP9DEE6]].
2. At $w$ the atom $p$ is true, and $B p$ is false because $p$ fails at $v$.
   So the Moore sentence $p \wedge \neg B p$ is true at $w$.
3. At $v$ the atom $p$ is false, so $p \wedge \neg B p$ is false at $v$.
4. $B (p \wedge \neg B p)$ at $w$ needs $p \wedge \neg B p$ at $v$, which fails by step 3.
   So Carl does not believe the Moore sentence at $w$, and by the same argument not at $v$.
5. Carl does believe $\neg p$ at $w$, since $p$ fails at $v$.
   So the second Moore form $p \wedge B \neg p$ is also true at $w$.

The Moore sentence is true at $w$, but Carl does not believe it, and by [[the theorem|TCAYVAVAK4]] no $\mathsf{KD45}$ model has a world where anyone believes it.

## Remarks

Step 4 is an instance of a general pattern.
In a $\mathsf{KD45}$ model the worlds that Carl considers possible form a cluster, and $B p$ has one value on the whole cluster.
If he believed $p \wedge \neg B p$, then $p$ would hold on the cluster, so $B p$ would hold on it, which contradicts $\neg B p$ there.

Now suppose a friend tells Carl the Moore sentence, and he trusts her.
He must then believe $p$, so the second conjunct $\neg B p$ is no longer true of him.
The sentence he was told becomes false by being accepted, which is the pattern studied in [[announcing a Moore sentence|Z13C7EBPXB]].
If we change the model so that $p$ is true at $v$ as well, Carl believes $p$, and the Moore sentence is false at both worlds.

## Explanations

### L1 human

"It is raining but Carl does not believe it" can be true, because Carl is wrong about the weather.
Carl himself cannot believe it.
If he did, he would believe that it is raining, so the second half, "Carl does not believe it", would be false.

### L2 human

To test whether an agent believes a formula at $w$, check the formula at each world that $w$ sees.
Here $w$ sees only $v$, and the Moore sentence fails at $v$ because $p$ fails there, so Carl does not believe it.
The typical use is to separate what is true about an agent from what the agent believes.
Watch out: the Moore sentence is not a contradiction, since step 2 shows that it is true at $w$.

### L3 human

Moore sentences are the standard examples of truths that cannot be believed, and, for knowledge, of truths that cannot be known.
That second reading drives [[Fitch's paradox of knowability|HVCW7QYXSW]].
In dynamic epistemic logic the same sentences are unsuccessful formulas: announcing them makes them false.
