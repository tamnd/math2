---
tag: ~ff75fedd
kind: example
name: A satisfiable infinite chain of implications
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [QN7M1JCGT9]
uses: [~41f42e3d, 0NMG7W7Q11, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Satisfiability
    locator: Reduction of validity to satisfiability
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Example

Let $p_0, p_1, p_2, \ldots$ be distinct propositional variables, and let $\Gamma = \set{p_0} \cup \set{p_n \to p_{n+1} : n \ge 0}$.
We show that $\Gamma$ is satisfiable, and that every assignment that satisfies it makes every $p_n$ true.

1. Let $v$ be the assignment with $v(p_n) = 1$ for every $n$.
2. The member $p_0$ has $\bar v(p_0) = 1$.
3. Each member $p_n \to p_{n+1}$ has a true consequent $p_{n+1}$, so it is true by the truth table of [[implication|0NMG7W7Q11]].
4. So $v$ satisfies $\Gamma$, and $\Gamma$ is satisfiable.
5. Now let $w$ be any assignment that satisfies $\Gamma$. We show $w(p_n) = 1$ by [[induction|0ASJVEFA9J]] on $n$.
6. Base: $w(p_0) = 1$, because $p_0 \in \Gamma$.
7. Step: if $w(p_n) = 1$, then $w(p_{n+1}) = 1$, because $\bar w(p_n \to p_{n+1}) = 1$ and an implication with a true antecedent and a false consequent is false.

## Remarks

The set is infinite, so no truth table can check it, but one assignment and an induction suffice.
Every finite subset is also satisfiable, by step 4 and the fact that subsets of satisfiable sets are satisfiable.
If we add the member $\neg p_{17}$, the set becomes unsatisfiable by step 7.
A finite subset of that larger set is unsatisfiable only when it contains $\neg p_{17}$, $p_0$ and all seventeen links $p_0 \to p_1$, ..., $p_{16} \to p_{17}$.
This fits the compactness theorem: an unsatisfiable set has a finite unsatisfiable subset.

## Explanations

### L1 human

Picture an endless row of dominoes.
The first one falls, and each one that falls knocks over the next.
These rules can all hold together: every domino falls.
In fact they force this, since each domino is pushed by the one before it.

### L2 human

We check one finite part of the set with care.

1. Take $\Delta = \set{p_0, \; p_0 \to p_1, \; p_1 \to p_2}$.
2. An assignment that satisfies $\Delta$ has $w(p_0) = 1$, then $w(p_1) = 1$, then $w(p_2) = 1$.
3. The assignment with $w(p_0) = w(p_1) = w(p_2) = 1$ satisfies $\Delta$.
4. So $\Delta$ is satisfiable, and $\Delta \models p_2$.

The typical use: an infinite set is satisfiable when we can describe one assignment and check every member with a general argument.
A trap: "each member is satisfiable" is not the same as "the set is satisfiable"; here the set is satisfiable, but the reason is the single assignment of step 1 of the example.
