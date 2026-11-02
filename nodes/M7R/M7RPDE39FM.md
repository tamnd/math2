---
tag: M7RPDE39FM
kind: definition
name: Subshift of finite type
msc: [37B10]
defines: 624XDXX8FN
uses: [A1XE59ZHNM, 0Z57EC6YX3]
sources:
  - url: https://en.wikipedia.org/wiki/Subshift_of_finite_type
---

## Definition

Let $A$ be a finite set, called the alphabet.
Let $A^{\Z}$ be the set of all sequences $x = (x_i)_{i \in \Z}$ with $x_i \in A$, with the [[product topology|0Z57EC6YX3]] of the discrete topologies.
Let $\sigma \colon A^{\Z} \to A^{\Z}$ be the shift map, $\sigma(x)_i = x_{i+1}$.
A word $w = w_1 \cdots w_n$ over $A$ occurs in $x$ if $x_{i+1} \cdots x_{i+n} = w$ for some $i \in \Z$.
For a set $F$ of words, let $X_F$ be the set of all $x \in A^{\Z}$ in which no word of $F$ occurs.
A subset $X \subseteq A^{\Z}$ is a *subshift of finite type* if $X = X_F$ for some finite set $F$ of words.

## Remarks

Each $X_F$ is closed and satisfies $\sigma(X_F) = X_F$, so it is a [[shift space|A1XE59ZHNM]].
Example: the golden mean shift is $X_F$ with $A = \set{0, 1}$ and $F = \set{11}$.
It is a subshift of finite type because $F$ is finite.
Non-example: the even shift is the set of $x \in \set{0,1}^{\Z}$ in which between any two $1$s there is an even number of $0$s.
It is a shift space, but it is not of finite type.
Each word $1 0^{2n+1} 1$ is forbidden, while all its proper subwords occur in allowed sequences, so no finite list of forbidden words can exclude all of them.
Every subshift of finite type is conjugate to a vertex shift.
Given a finite set $B$ and a square $0$-$1$ matrix $M$ indexed by $B$, this is the set of $x \in B^{\Z}$ with $M_{x_i x_{i+1}} = 1$ for all $i$.
The same definition with $A^{\Z^d}$ and finite forbidden patterns gives the multidimensional subshifts of finite type.
