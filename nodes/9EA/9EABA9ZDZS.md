---
tag: 9EABA9ZDZS
kind: statement
role: theorem
name: Bourbaki–Witt theorem
msc: [06A06, 47H10, "03E25"]
uses: [0QV2JS9RJ3, 0S8FE7ZMFM, 0R3H5PANRQ, 04RXTQA5ZA]
about: [0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Bourbaki%E2%80%93Witt_theorem
same_as:
  wikidata: Q4950096
  wikipedia: Bourbaki–Witt theorem
---

## Statement

Let $(P, \le)$ be a nonempty [[partially ordered set|0QV2JS9RJ3]] in which every [[chain|0S8FE7ZMFM]] has a [[supremum|0R3H5PANRQ]].
Let $f \colon P \to P$ be a map with $x \le f(x)$ for every $x \in P$.
Then $f$ has a fixed point: there is $x \in P$ with $f(x) = x$.

## Remarks

The map $f$ need not be monotone; the hypothesis $x \le f(x)$ says that $f$ is *inflationary*.
Proof idea: fix $a \in P$ and let $T$ be the smallest subset of $P$ that contains $a$, is closed under $f$, and contains the supremum of each of its nonempty chains.
A careful induction shows that $T$ is a chain, so it has a supremum $s$, and $s \in T$.
Then $f(s) \in T$, so $f(s) \le s \le f(s)$ and $f(s) = s$.
The proof uses no form of the axiom of choice.
Combined with the axiom of choice, the theorem shows that such a poset has a maximal element.
Otherwise a choice of some $f(x) > x$ for each $x$ would be an inflationary map with no fixed point.
This is a standard step in the proof of [[Zorn's lemma|04RXTQA5ZA]] from the axiom of choice.
The hypothesis $x \le f(x)$ is needed: on the chain $\set{0, 1}$, where every chain has a supremum, the map swapping $0$ and $1$ has no fixed point.
The completeness hypothesis is needed too: on $\N$, the inflationary map $n \mapsto n + 1$ has no fixed point, and the chain $\N$ has no supremum.

## Explanations

### L1 human

Suppose a rule never moves any point downward, and every chain of points has a top.
Then some point is not moved at all.
The idea is to start anywhere and keep applying the rule, jumping to the top of the chain built so far whenever the steps run out.
This climb cannot go on forever, so it stops at a fixed point.

### L2 human

The theorem is a choice-free fixed-point principle for chain-complete posets.
It is a standard route to [[Zorn's lemma|04RXTQA5ZA]] from the axiom of choice, and it is used to build objects by transfinite recursion without naming ordinals.
Unlike the [[Knaster–Tarski theorem|RHXP3HA64M]], it does not need monotonicity, but it says nothing about least fixed points.
