---
tag: G7HAS0P39P
kind: example
name: Iterated belief collapses in KD45
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [RTP4HTZYK3]
uses: [1CFMP9DEE6, JDE7CN1C48, FDFQFWPM4X, GHPPQ19J6B]
sources:
  - url: https://en.wikipedia.org/wiki/Doxastic_logic
    locator: lead section
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 3
---

## Example

For a rational believer, "I believe that I believe it" should say no more than "I believe it".
In [[doxastic logic|RTP4HTZYK3]] this is a pair of theorems of $\mathsf{KD45}$.
$$B B p \leftrightarrow B p \qquad\text{and}\qquad B \neg B p \leftrightarrow \neg B p.$$
We check both on serial, transitive, [[Euclidean|JDE7CN1C48]] frames, which suffices by [[the completeness of KD45|1CFMP9DEE6]].
Fix a model on such a frame and a world $w$.

1. $B p \to B B p$ is axiom $\mathsf{4}$, valid on transitive frames.
2. For $B B p \to B p$, let $B B p$ hold at $w$, and let $w R u$.
   The Euclidean property applied to $w R u$ and $w R u$ gives $u R u$.
3. $B B p$ at $w$ gives $B p$ at $u$, and $u R u$ then gives $p$ at $u$.
   This holds for every $u$ with $w R u$, so $B p$ holds at $w$.
4. $\neg B p \to B \neg B p$ is axiom $\mathsf{5}$, valid on Euclidean frames.
5. For $B \neg B p \to \neg B p$, let $B \neg B p$ hold at $w$, and use seriality to pick $v$ with $w R v$.
   Then $\neg B p$ holds at $v$, so some $u$ has $v R u$ and $p$ false at $u$.
6. By transitivity $w R u$, so $B p$ fails at $w$.

So the agent believes that she believes $p$ exactly when she believes $p$, and believes that she does not believe $p$ exactly when she does not.

## Remarks

Step 3 uses only the Euclidean property, and step 6 uses seriality and transitivity.
Without seriality, step 6 fails: at a world with no successors, $B \neg B p$ and $B p$ are both true.
And $B B p \to B p$ is not a theorem of $\mathsf{K4}$.
On the transitive frame with one arrow $w R v$ and $p$ false at $v$, the dead end $v$ has $B p$ vacuously, so $B B p$ holds at $w$ while $B p$ fails there.

In a $\mathsf{KD45}$ frame, $w R v$ implies that $v$ sees exactly the worlds that $w$ sees, by transitivity and the Euclidean property.
So a formula that starts with $B$ has the same value at $w$ and at every world that $w$ sees.
Hence every string of $B$s and negations in front of $p$ is equivalent to one of $p$, $\neg p$, $B p$, $\neg B p$, $B \neg p$ and $\neg B \neg p$.
This mirrors [[the reduction of modalities in S5|GHPPQ19J6B]].

## Explanations

### L1 human

For a rational believer, "I believe that I believe it" says no more than "I believe it".
"I believe that I do not believe it" says no more than "I do not believe it".
Taller towers of beliefs about one's own beliefs add nothing new.

### L2 human

The key frame fact is step 2: in a Euclidean frame, every world that $w$ sees also sees itself.
So on the set of worlds seen from $w$ the relation is reflexive, and there belief behaves like knowledge: $B p$ at a seen world gives $p$ at that world.
The typical use is to shorten long belief prefixes, for example to reduce $B B B \neg B p$ to $\neg B p$ in three steps.
Watch out: $B p \to p$ is still not valid, since $w$ itself need not see itself.

### L3 human

A rooted $\mathsf{KD45}$ frame is a cluster with an optional root, and on the cluster the box is an $\mathsf{S5}$ box.
That is why the modal structure of $\mathsf{KD45}$ is as flat as that of $\mathsf{S5}$, even though $\mathsf{KD45}$ lacks the truth axiom.
