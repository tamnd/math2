---
tag: MM8KDN9TBF
kind: statement
role: theorem
name: May's theorem
msc: [91B12, 91B14]
uses: [KH8ACT22FR]
about: [KH8ACT22FR, F17C7F17PM]
sources:
  - url: https://en.wikipedia.org/wiki/May%27s_theorem
same_as:
  wikidata: Q1056283
  wikipedia: May's theorem
---

## Statement

Let there be two alternatives $x, y$ and $n \ge 1$ voters.
A profile is a vector $D = (D_1, \dots, D_n) \in \set{-1, 0, 1}^n$, where $D_i = 1$ means that voter $i$ prefers $x$, $D_i = -1$ that $i$ prefers $y$, and $D_i = 0$ that $i$ is indifferent.
A *group decision function* is a map $f \colon \set{-1, 0, 1}^n \to \set{-1, 0, 1}$, with the same meaning of the values for the group.
It is:

1. *anonymous* if $f(D_{\sigma(1)}, \dots, D_{\sigma(n)}) = f(D)$ for every permutation $\sigma$ of the voters;
2. *neutral* if $f(-D) = -f(D)$ for every $D$;
3. *positively responsive* if $f(D') = 1$ whenever $f(D) \in \set{0, 1}$ and $D'$ is obtained from $D$ by raising one coordinate. Raising means a change from $-1$ to $0$ or $1$, or from $0$ to $1$, with the other coordinates unchanged.

Then $f$ is anonymous, neutral and positively responsive if and only if $f$ is simple majority rule:
$$f(D) = \sgn\left(D_1 + \cdots + D_n\right).$$

## Remarks

Simple majority rule has the three properties: the sum $D_1 + \cdots + D_n$ is symmetric, changes sign with $D$, and rises when a coordinate rises.
Conversely, anonymity means that $f$ depends only on the numbers $p$ and $m$ of voters with $D_i = 1$ and $D_i = -1$.
Neutrality gives $f = 0$ when $p = m$, since then $D$ and $-D$ have the same counts.
Starting from a tie and raising votes one at a time, positive responsiveness gives $f = 1$ when $p > m$, and neutrality then gives $f = -1$ when $p < m$.

Each condition is needed.
The dictatorship $f(D) = D_1$ is neutral, but it is neither anonymous nor positively responsive.
The rule "always $0$" is anonymous and neutral but not positively responsive.
The rule "choose $x$ unless every voter prefers $y$" is anonymous and positively responsive but not neutral.

## Explanations

### L1 human

When a group chooses between just two options, simple majority vote is the only fair rule in a precise sense.
It treats all voters alike, treats both options alike, and reacts to any extra support in the right direction.
May's theorem says that these three demands already force majority rule.

### L2 human

May's theorem is the positive counterpart of Arrow's impossibility theorem.
With two alternatives the problems of transitivity do not arise, and a short list of axioms characterizes a unique rule.
It is a model for later axiomatic characterizations, such as those of the Borda count and of approval voting.
