---
tag: TJ9JJADSEQ
kind: example
name: Chisholm's paradox
msc: ["03B45"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [7B74J6J5JV]
uses: [7B74J6J5JV, RKTY59QFQ9, 6BQ71KQ6QT]
aliases: [contrary-to-duty-paradox]
sources:
  - url: https://en.wikipedia.org/wiki/Deontic_logic
    locator: Dyadic deontic logic
  - url: https://www.iep.utm.edu/contrary-to-duty-paradox/
    locator: Contrary-to-Duty Paradox, Internet Encyclopedia of Philosophy
---

## Example

Let $h$ be "Jones goes to help the neighbors" and $t$ be "Jones tells them that he is coming".
Here are four sentences and their direct translations into [[standard deontic logic|7B74J6J5JV]].

1. Jones ought to go: $Oh$.
2. It ought to be that if he goes, he tells them: $O(h \to t)$.
3. If he does not go, he ought not to tell them: $\neg h \to O\neg t$.
4. He does not go: $\neg h$.

Sentence 3 is a contrary-to-duty obligation, since it says what to do once the duty of sentence 1 is broken.
The four sentences seem consistent, and none seems to follow from the others.
We show that no direct translation into $\mathsf{SDL}$ has both properties.

5. From sentence 2, the axiom $\mathrm{K}$ gives $Oh \to Ot$, and sentence 1 then gives $Ot$.
6. From sentences 3 and 4, modus ponens gives $O\neg t$.
7. The conjunction $Ot \wedge O\neg t$ contradicts the theorem $\neg(Ot \wedge O\neg t)$ of [[the derived laws|RKTY59QFQ9]].
   So the set is inconsistent.
8. Replace sentence 2 by $h \to Ot$.
   This follows from sentence 4 by propositional logic, since $\neg h$ makes the implication true, so the set is no longer independent.
9. Replace sentence 3 by $O(\neg h \to \neg t)$.
   The formula $h \to (\neg h \to \neg t)$ is a tautology, so necessitation and $\mathrm{K}$ give $Oh \to O(\neg h \to \neg t)$.
10. So the new sentence 3 follows from sentence 1, and again the set is not independent.
11. The last combination, $h \to Ot$ together with $O(\neg h \to \neg t)$, fails independence by step 8.

## Remarks

The example shows that the one-place operator $O$ cannot express conditional obligation in all four sentences at once.
The standard answer is dyadic deontic logic, with a two-place operator $O(q \mid p)$ for "$q$ is obligatory given $p$".
The four sentences become $O(h \mid \top)$, $O(t \mid h)$, $O(\neg t \mid \neg h)$ and $\neg h$.
In Hansson's semantics the worlds are ranked by betterness, and $O(q \mid p)$ holds when every best $p$-world is a $q$-world.

Let us check that the dyadic version is consistent.
Write $ht$ for the world where both atoms are true, and put a bar over a false atom.
Rank the four worlds as follows, best first, and let the actual world be $\bar h \bar t$.
$$ht \; > \; \bar h \bar t \; > \; h \bar t \; > \; \bar h t$$
The best world overall is $ht$, so $O(h \mid \top)$ holds.
The best $h$-world is $ht$, so $O(t \mid h)$ holds.
The best $\neg h$-world is $\bar h \bar t$, so $O(\neg t \mid \neg h)$ holds.
Finally $\neg h$ is true at the actual world, so all four sentences hold together.

Chisholm published the paradox in 1963.

## Explanations

### L1 human

Jones should help his neighbors, and if he goes, he should call ahead.
If he does not go, he should not call, since a call would make them wait for nothing.
In fact he does not go.
These four rules sound fine together.
But in the simplest logic of "ought" they either clash, or one of them follows from the others.
The fix is to let "ought" depend on the situation: what is best if he goes, and what is best if he does not.

### L2 human

We check step 9 in [[Kripke semantics|6BQ71KQ6QT]].
Suppose that $w \models Oh$ in a serial model, so that every ideal world $v$ of $w$ satisfies $h$.
At such a $v$ the antecedent $\neg h$ is false, so $\neg h \to \neg t$ is true.
So $w \models O(\neg h \to \neg t)$, as the derivation claimed.
This shows why $O(\neg h \to \neg t)$ is a poor contrary-to-duty rule.
Since $h$ holds in all ideal worlds, the formula says nothing about the non-ideal worlds where $\neg h$ is true, and those are the worlds the rule is for.
The typical use of the example is as a benchmark: a logic of conditional obligation must make the four sentences consistent and independent.
