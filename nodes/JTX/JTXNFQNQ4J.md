---
tag: JTXNFQNQ4J
kind: statement
role: theorem
name: Hewitt–Savage zero–one law
msc: [60F20, 60G09]
uses: [00MRN0FARV, 05RWFKVTJ7, 031TPJVS74, 073Q8Z94KG]
about: [00MRN0FARV, 4MR4YJS1ZD]
sources:
  - url: https://en.wikipedia.org/wiki/Hewitt%E2%80%93Savage_zero%E2%80%93one_law
same_as:
  wikidata: Q21051250
  wikipedia: Hewitt–Savage zero–one law
---

## Statement

Let $(S, \mathcal{S})$ be a measurable space, and let $X_1, X_2, \dots$ be [[independent and identically distributed|00MRN0FARV]] random variables with values in $S$.
Let $B \subseteq S^{\N}$ be a measurable set for the product σ-algebra.
Assume that $B$ is symmetric: for every [[permutation|05RWFKVTJ7]] $\pi$ of $\N$ that moves only finitely many indices, $(x_n)_n \in B$ if and only if $(x_{\pi(n)})_n \in B$.
Then the [[event|031TPJVS74]] $A = \set{(X_1, X_2, \dots) \in B}$ has $P(A) \in \set{0, 1}$.

## Remarks

Proof idea: approximate $A$ by an event $A_n$ that depends only on $X_1, \dots, X_n$.
Let $A_n'$ be the image of $A_n$ under the permutation that swaps the blocks $1, \dots, n$ and $n+1, \dots, 2n$.
By symmetry $A_n'$ approximates $A$ as well, and $A_n, A_n'$ are independent with equal probability.
So $P(A) = \lim P(A_n \cap A_n') = \lim P(A_n)^2 = P(A)^2$.
Every tail event is symmetric, so the theorem extends [[Kolmogorov's zero–one law|073Q8Z94KG]] in the i.i.d. case.
Example: let $X_i$ be real and $S_n = X_1 + \dots + X_n$. The event $\set{S_n \in I \text{ for infinitely many } n}$, for an interval $I$, is symmetric, because a finite permutation leaves $S_n$ unchanged for all large $n$. It is not a tail event in general, since changing $X_1$ shifts all $S_n$.
The identical distribution is needed: if $X_1$ is a fair coin and $X_n = 0$ for $n \ge 2$, then $\set{\text{some } X_n = 1}$ is symmetric and has probability $\frac{1}{2}$.

## Explanations

### L1 human

Take an infinite sequence of independent draws from one distribution.
Any event that does not care about the order of finitely many draws is either almost certain or almost impossible.
For instance, whether a random walk returns to its start infinitely often has probability $0$ or $1$.

### L2 human

The theorem is used to show that quantities such as $\limsup_n S_n$ for a random walk are almost surely constant, and to obtain the recurrence dichotomy for random walks.
Compared with [[Kolmogorov's zero–one law|073Q8Z94KG]], it needs identical distribution but covers more events, namely all events of the exchangeable σ-algebra.
In the language of [[de Finetti's theorem|W19129PVKQ]], it says that an i.i.d. sequence is an exchangeable sequence whose mixing measure is a point mass.
