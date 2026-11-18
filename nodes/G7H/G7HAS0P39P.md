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

We show on serial, transitive, [[Euclidean|JDE7CN1C48]] frames that
$$BBp \leftrightarrow Bp \qquad\text{and}\qquad B\neg Bp \leftrightarrow \neg Bp.$$
By [[the completeness of KD45|1CFMP9DEE6]], both are theorems of $\mathsf{KD45}$.
Fix a model on such a frame and a world $w$.

1. $Bp \to BBp$ is axiom $\mathsf{4}$, valid on transitive frames.
2. For $BBp \to Bp$, let $BBp$ hold at $w$, and let $w R u$.
3. The relation is Euclidean, and $w R u$, $w R u$ give $u R u$.
4. $BBp$ at $w$ gives $Bp$ at $u$. Since $u R u$, $p$ holds at $u$. So $Bp$ holds at $w$.
5. $\neg Bp \to B\neg Bp$ is axiom $\mathsf{5}$, valid on Euclidean frames.
6. For $B\neg Bp \to \neg Bp$, let $B\neg Bp$ hold at $w$. By seriality pick $v$ with $w R v$.
7. $\neg Bp$ holds at $v$, so some $u$ has $v R u$ and $p$ false at $u$.
8. By transitivity $w R u$. So $Bp$ fails at $w$.

So the agent believes that she believes $p$ exactly when she believes $p$, and believes that she does not believe $p$ exactly when she does not.

## Remarks

Step 4 uses only the Euclidean property, and step 8 uses seriality and transitivity.
Without seriality, step 8 fails: at a world with no successors, $B\neg Bp$ is true and $Bp$ is true as well.
In a $\mathsf{KD45}$ frame, $w R v$ implies that $v$ sees exactly the worlds that $w$ sees, by transitivity and the Euclidean property.
So a formula that starts with $B$ has the same value at $w$ and at every world $w$ sees.
Hence every string of $B$s and negations in front of $p$ is equivalent to one of $p$, $\neg p$, $Bp$, $\neg Bp$, $B\neg p$, $\neg B\neg p$, much as in [[the reduction of modalities in S5|GHPPQ19J6B]].
$BBp \to Bp$ is not a theorem of $\mathsf{K4}$: on the two-world chain $w R v$ with $p$ false at $v$, $Bp$ holds vacuously at the dead end $v$, so $BBp$ holds at $w$, but $Bp$ fails at $w$.

## Explanations

### L1 human

For a rational believer, "I believe that I believe it" says no more than "I believe it".
"I believe that I do not believe it" says no more than "I do not believe it".
Higher towers of beliefs about one's own beliefs add nothing.

### L2 human

The key frame fact is step 3: in a Euclidean frame, every world that $w$ sees sees itself.

1. So the worlds seen from $w$ form a set on which $R$ is reflexive.
2. On that set, belief behaves like knowledge: $Bp$ at a seen world implies $p$ there.

The typical use is to reduce long belief prefixes, for example $BBB\neg Bp$ to $\neg Bp$.
A trap: $Bp \to p$ is still not valid, since $w$ itself need not see itself.

### L3 human

The rooted $\mathsf{KD45}$ frames are clusters with an optional root, and on the cluster the box is an $\mathsf{S5}$ box.
That is why the modal structure of $\mathsf{KD45}$ is as flat as that of $\mathsf{S5}$, even though $\mathsf{KD45}$ lacks the truth axiom.
