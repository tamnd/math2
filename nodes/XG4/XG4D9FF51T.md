---
tag: XG4D9FF51T
kind: example
name: Sturmian word
msc: [68R15, 37B10]
illustrates: [2Q1J7RZ4TK]
uses: [YJ961M051W, 080T2TXVQV, 0SC8T7548D]
sources:
  - url: https://en.wikipedia.org/wiki/Sturmian_word
same_as:
  wikidata: Q3325046
  wikipedia: Sturmian word
---

## Example

A Sturmian word is an infinite word $s = s_0 s_1 s_2 \cdots$ over $\set{0, 1}$ that has exactly $n + 1$ distinct factors of length $n$ for every $n \ge 0$.
A factor of length $n$ is a block $s_i s_{i+1} \cdots s_{i+n-1}$.
Equivalently, there are an [[irrational number|080T2TXVQV]] $\alpha \in (0, 1)$ and a real $\rho$ with the following property.
For all $n$, $s_n = \floor{(n+1)\alpha + \rho} - \floor{n \alpha + \rho}$, or the same holds with $\ceil{\cdot}$ in place of $\floor{\cdot}$.
Then $s_n = 1$ exactly when the point $n\alpha + \rho$ of the circle $\R/\Z$ lies in a fixed arc of length $\alpha$.
So $s$ codes the [[irrational rotation|2Q1J7RZ4TK]] by $\alpha$.

The Fibonacci word is the main instance.
Define $S_0 = 0$, $S_1 = 01$ and $S_{k} = S_{k-1} S_{k-2}$ for $k \ge 2$.
Each $S_{k-1}$ is a prefix of $S_k$, and the limit is
$$f = 0100101001001010010100100101 \cdots .$$
Check for small $n$: the factors of length $1$ are $0, 1$, and those of length $2$ are $00, 01, 10$, since $11$ never occurs.
So there are $2$ and $3$ of them, as required.
For $k \ge 1$ the word $S_k$ has $F_k$ zeros and $F_{k-1}$ ones, with $F_k$ the Fibonacci numbers ($F_0 = F_1 = 1$).
So the frequency of the letter $1$ is $\lim F_{k-1}/F_{k+1} = 1/\varphi^2$, where $\varphi$ is the [[golden ratio|0SC8T7548D]].

## Remarks

A word with at most $n$ factors of length $n$ for some $n$ is eventually periodic, by a theorem of Morse and Hedlund.
So Sturmian words are the aperiodic words of the lowest possible complexity.
The closure of the shift orbit of a Sturmian word is a minimal shift space on which the shift has zero entropy.

## Explanations

### L1 human

Draw a straight line of irrational slope across a grid of squares.
Write $0$ each time the line crosses a vertical grid line and $1$ each time it crosses a horizontal one.
The resulting word is Sturmian: it never repeats periodically, yet it is as simple as a non-repeating word can be.
The Fibonacci word, built by gluing the two previous words together, is the best known example.
