---
tag: 9DD1FWC8YF
kind: example
name: A satisfiable infinite chain of implications
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [QN7M1JCGT9]
uses: [H31CS3HK5P, 0NMG7W7Q11, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Satisfiability
    locator: Reduction of validity to satisfiability
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Example

An infinite set of formulas has no finite truth table, but one well-chosen assignment can still show that it is [[satisfiable|QN7M1JCGT9]].
Let $p_0, p_1, p_2, \ldots$ be distinct propositional variables, and let
$$\Gamma = \{ p_0 \} \cup \{ p_n \to p_{n+1} : n \geq 0 \} .$$
We show that $\Gamma$ is satisfiable, and that every assignment that satisfies it makes every $p_n$ true.

1. Let $v$ be the assignment with $v(p_n) = 1$ for every $n$.
2. The member $p_0$ has $\bar v(p_0) = 1$.
3. Each member $p_n \to p_{n+1}$ has a true consequent $p_{n+1}$, so it is true by the table of [[implication|0NMG7W7Q11]].
4. So $v$ satisfies $\Gamma$, and $\Gamma$ is satisfiable.
5. Now let $w$ be any assignment that satisfies $\Gamma$.
   We show $w(p_n) = 1$ by [[induction|0ASJVEFA9J]] on $n$.
6. Base: $w(p_0) = 1$, because $p_0 \in \Gamma$.
7. Step: if $w(p_n) = 1$, then $w(p_{n+1}) = 1$, because $\bar w(p_n \to p_{n+1}) = 1$, and an implication with a true antecedent and a false consequent is false.

Check: for $n = 0$, step 7 reads "$w(p_0) = 1$ and $p_0 \to p_1$ true give $w(p_1) = 1$", which is modus ponens.

## Remarks

One assignment and one induction replace the infinite table.
Every finite subset is also satisfiable, since a subset of a satisfiable set is satisfiable.

If we add the member $\neg p_{17}$, the set becomes unsatisfiable by step 7.
A finite subset of that larger set is unsatisfiable only when it contains $\neg p_{17}$, $p_0$ and all seventeen links $p_0 \to p_1$, ..., $p_{16} \to p_{17}$.
If one link $p_k \to p_{k+1}$ is missing, make $p_0, \ldots, p_k$ true and every later variable false.
This fits the [[compactness theorem|4X9126SEMM]]: an unsatisfiable set has a finite unsatisfiable subset.

Watch out.
"Each member is satisfiable" is not the same as "the set is satisfiable".
Here the set is satisfiable, but the reason is the single assignment of step 1, not the fact that each member alone can be made true.

Try it.
Is $\Gamma \cup \{ \neg p_0 \lor \neg p_1 \}$ satisfiable?
No: steps 6 and 7 force $p_0 = p_1 = 1$, and then the new member is $0 \lor 0 = 0$.

## Explanations

### L1 human

Picture an endless row of dominoes.
The first one falls, and each one that falls knocks over the next.
These rules can all hold together: every domino falls.
In fact they force this, since each domino is pushed by the one before it.

### L2 human

We check one finite part of the set with care.

1. Take $\Delta = \{ p_0, \; p_0 \to p_1, \; p_1 \to p_2 \}$.
2. An assignment that satisfies $\Delta$ has $w(p_0) = 1$, then $w(p_1) = 1$, then $w(p_2) = 1$.
3. The assignment with $w(p_0) = w(p_1) = w(p_2) = 1$ satisfies $\Delta$.
4. So $\Delta$ is satisfiable, and $\Delta \models p_2$.

To show that an infinite set is satisfiable, describe one assignment and check every member with a general argument.
