---
tag: NYJX5QXX1T
kind: statement
role: theorem
name: Post's theorem
msc: [03D55, 03D30]
uses: [7CVJCQKY41, TN9G24VABN, 60P2XWY5QX, PA4PYQ1PZ0, JTAH37JTHD]
about: [7CVJCQKY41, 60P2XWY5QX]
sources:
  - url: https://en.wikipedia.org/wiki/Post's_theorem
same_as:
  wikidata: Q3007384
  wikipedia: Post's theorem
---

## Statement

Let $\emptyset^{(0)} = \emptyset$, and let $\emptyset^{(n+1)}$ be the [[Turing jump|60P2XWY5QX]] of $\emptyset^{(n)}$.
Let $A \subseteq \N$ and $n \in \N$.

1. $A$ is $\Sigma^0_{n+1}$ in the [[arithmetical hierarchy|7CVJCQKY41]] if and only if $A$ is [[computably enumerable|TN9G24VABN]] relative to the oracle $\emptyset^{(n)}$.
2. If $n \ge 1$, the set $\emptyset^{(n)}$ is $\Sigma^0_n$-complete: it is $\Sigma^0_n$, and every $\Sigma^0_n$ set is [[many-one reducible|JTAH37JTHD]] to it.
3. $A$ is $\Delta^0_{n+1}$ if and only if $A$ is [[Turing reducible|PA4PYQ1PZ0]] to $\emptyset^{(n)}$.

## Remarks

The proof is by induction on $n$.
For $n = 0$, part 1 says that $\Sigma^0_1$ sets are the computably enumerable sets, which follows from Kleene's normal form.
For the inductive step, an existential quantifier over a set computable from $\emptyset^{(n)}$ is a search with that oracle.
A $\Pi^0_n$ condition can be answered by one question to $\emptyset^{(n)}$, by the completeness in part 2.

Example: the set of programs that compute total functions is $\Pi^0_2$, so it is computable from $\emptyset''$.

## Explanations

### L1 human

The Turing jump of a set is the halting problem for machines that may consult that set.
Post's theorem says that each extra quantifier alternation in a definition corresponds to one more jump.
So the logical complexity of a definition matches the computational complexity of deciding the set.

### L2 human

The theorem is the bridge between definability in arithmetic and relative computability.
It shows that the arithmetical hierarchy is proper, because $\emptyset^{(n+1)}$ is not computable from $\emptyset^{(n)}$.
In computability arguments, one often bounds the quantifier complexity of a set to know which oracle can decide it.
Iterating the jump through computable ordinals beyond $\omega$ leads to the [[hyperarithmetical sets|NS1HWGTD8E]].
