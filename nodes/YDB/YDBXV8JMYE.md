---
tag: YDBXV8JMYE
kind: statement
role: theorem
name: Artin–Schreier theorem on formally real fields
msc: ["12D15", "12J15"]
uses: [0QA8CHH8MG, 2362AFNG8X, 010JCV9J4E]
about: [X32TSWJSYT, 0P3VCBDEE2]
sources:
  - url: https://en.wikipedia.org/wiki/Formally_real_field
---

## Statement

Let $F$ be a [[field|0QA8CHH8MG]].
Then $F$ has a total order that makes it an [[ordered field|010JCV9J4E]] if and only if $F$ is [[formally real|2362AFNG8X]].
That is, such an order exists if and only if $-1$ is not a sum of squares in $F$.

## Remarks

One direction is short: in an ordered field every square is nonnegative, so every sum of squares is nonnegative and cannot equal $-1$.
For the converse, let $\Sigma$ be the set of sums of squares of $F$.
If $F$ is formally real, then $\Sigma$ is closed under addition and multiplication and does not contain $-1$.
By Zorn's lemma, there is a maximal subset $P \supseteq \Sigma$ with these properties, and one shows that $P$ is the set of nonnegative elements of an ordering of $F$.
Example: $\Q(\sqrt{2})$ is formally real, and it has two orderings, one with $\sqrt{2} > 0$ and one with $\sqrt{2} < 0$.
Example: $\C$ is not formally real, since $-1 = i^2$, and so $\C$ has no field ordering.

## Explanations

### L1 human

Some fields can be ordered like the real numbers, and some cannot, like the complex numbers.
The theorem gives a simple algebraic test: a field can be ordered exactly when $-1$ is not a sum of squares.
So a purely algebraic condition decides whether an order exists.

### L2 human

The theorem is the starting point of real algebra and of the theory of real closed fields developed by Artin and Schreier.
Its proof shows more: the orderings of a formally real field correspond to the maximal subsets $P$ described above.
The same theory shows that every formally real field has an algebraic extension that is real closed.
Artin used this theory in his solution of Hilbert's seventeenth problem, which asks whether a nonnegative real polynomial is a sum of squares of rational functions.
The [[Artin–Schreier theorem|58P0EGAFVV]] on fields with algebraic closure of finite degree belongs to the same theory.
