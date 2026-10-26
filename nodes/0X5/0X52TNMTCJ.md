---
tag: 0X52TNMTCJ
kind: statement
role: theorem
name: Tietze extension theorem
aliases: [tietze-urysohn-extension-theorem]
msc: [54C20]
uses: [0AJ646N339, 01EY3VR7ZD, 0SY9ECQ19Q, 0D2MXBV21T]
sources:
  - url: https://en.wikipedia.org/wiki/Tietze_extension_theorem
    locator: Formal statement
same_as:
  wikidata: Q1346677
  wikipedia: Tietze extension theorem
---

## Statement

Let $X$ be a [[normal space|0AJ646N339]], let $A \subseteq X$ be [[closed|0G5AV9Q4RR]], and let $f \colon A \to \mathbb{R}$ be [[continuous|0SY9ECQ19Q]] for the subspace topology on $A$.
Then there is a continuous $F \colon X \to \mathbb{R}$ whose [[restriction|0D2MXBV21T]] to $A$ is $f$.
If also $|f(a)| \le M$ for all $a \in A$, then one can choose $F$ with $|F(x)| \le M$ for all $x \in X$.

## Remarks

The proof applies [[Urysohn's lemma|01EY3VR7ZD]] many times and sums a uniformly convergent series of functions.
The converse holds: if each continuous function from each closed subset to $\mathbb{R}$ extends, then $X$ is normal.
The closedness of $A$ is needed: the function $\sin(1/x)$ on $(0, 1]$ has no continuous extension to $[0, 1]$.

## Explanations

### L1 human

On a normal space, each continuous real function on a closed set can be extended to the whole space, without losing continuity.
You can also keep the same bound on the function.
