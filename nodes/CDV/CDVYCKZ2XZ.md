---
tag: CDVYCKZ2XZ
kind: definition
name: Hidden Markov model
msc: [62M05, 60J10]
defines: HJVM390354
uses: [033TJBZDG0, 0F462493EA, 0THJ7416DX, 0G48PYM96Q]
sources:
  - url: https://en.wikipedia.org/wiki/Hidden_Markov_model
---

## Definition

Let $S$ and $O$ be finite sets, the *hidden states* and the *observations*.
Let $\lambda$ be a probability distribution on $S$, and let $A = (a_{ij})_{i, j \in S}$ be a [[transition matrix|0F462493EA]].
Let $E = (e_i(o))_{i \in S, o \in O}$ be a matrix with $e_i(o) \ge 0$ and $\sum_{o \in O} e_i(o) = 1$ for each $i$.
A *hidden Markov model* with these parameters is a pair of processes $(X_n, Y_n)_{n \ge 0}$ with values in $S \times O$ such that:

1. $(X_n)$ is a [[Markov chain|033TJBZDG0]] with initial law $\lambda$ and transition matrix $A$;
2. given $(X_n)_{n \ge 0}$, the variables $Y_0, Y_1, \ldots$ are [[conditionally independent|0THJ7416DX]];
3. $P(Y_n = o \mid (X_k)_{k \ge 0}) = e_{X_n}(o)$ for all $n \ge 0$ and $o \in O$.

Only $(Y_n)$ is observed.

## Remarks

The joint law is $P(X_0 = i_0, Y_0 = o_0, \ldots, X_n = i_n, Y_n = o_n) = \lambda_{i_0} e_{i_0}(o_0) \prod_{k=1}^{n} a_{i_{k-1} i_k} e_{i_k}(o_k)$.
Example: let $S = \set{F, L}$ for a fair and a loaded die, with $a_{FL} = a_{LF} = 0.05$, and let $O = \set{1, \ldots, 6}$.
Take $e_F(o) = 1/6$ for all $o$, $e_L(6) = 1/2$ and $e_L(o) = 1/10$ for $o \le 5$; each row sums to $1$, so clauses 1 to 3 define a model.
Non-example: if $Y_n$ is allowed to depend on $Y_{n-1}$ as well as on $X_n$, clause 3 fails.
The observed process $(Y_n)$ alone is in general not a [[Markov chain|0G48PYM96Q]].
The forward algorithm computes the likelihood $P(Y_0 = o_0, \ldots, Y_n = o_n)$ in time of order $n \abs{S}^2$, and the Viterbi algorithm finds a most likely hidden path.
