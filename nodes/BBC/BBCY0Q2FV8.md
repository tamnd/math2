---
tag: BBCY0Q2FV8
kind: definition
name: BPP
msc: [68Q15, 68Q10, 68W20]
defines: PTD7E1PKV4
uses: [K99S0Q0814, ESPYW94XGR, 5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/BPP_(complexity)
---

## Definition

A language $L \subseteq \set{0,1}^*$ is in *BPP* if there are a polynomial $p$ and a [[probabilistic Turing machine|K99S0Q0814]] $M$ such that:

1. on every input $x$ and for every outcome of its coin flips, $M$ halts within $p(\abs{x})$ steps and outputs $0$ or $1$;
2. for every $x \in L$, $\Pr[M(x) = 1] \ge 2/3$;
3. for every $x \notin L$, $\Pr[M(x) = 1] \le 1/3$.

The probabilities are over the fair coin flips of $M$.

## Remarks

Example: let $L$ be the set of triples $(A, B, C)$ of $n \times n$ matrices over $\F_2$ with $AB = C$.
The machine $M$ picks two independent uniform vectors $r \in \F_2^n$ and accepts if $A(Br) = Cr$ for both, which takes $O(n^2)$ steps for each.
If $AB = C$, then $M$ always accepts.
If $AB \ne C$, then $D = AB - C$ has a nonzero row, and $Dr = 0$ for at most half of the vectors $r$, so $M$ accepts with probability at most $1/4$.
So $L$ is in BPP; this test is Freivalds' algorithm.

Non-example: a machine that accepts each $x \in L$ with probability $1/2 + 2^{-\abs{x}}$ and each $x \notin L$ with probability $1/2$ fails clause 2.
Machines with such a vanishing gap define the class PP, which contains BPP.

The constants $2/3$ and $1/3$ can be replaced by $1/2 + \varepsilon$ and $1/2 - \varepsilon$ for any fixed $\varepsilon > 0$, or by $1 - 2^{-q(n)}$ and $2^{-q(n)}$ for any polynomial $q$.
This follows by running $M$ many times and taking the majority vote, with the Chernoff bound.
Equivalently, $L \in \mathrm{BPP}$ if there are a polynomial-time deterministic machine $V$ and a polynomial $p$ with the following property.
For every $x$ and a uniform $r \in \set{0,1}^{p(\abs{x})}$, the output $V(x, r)$ is $1$ if $x \in L$ and $0$ if $x \notin L$ with probability at least $2/3$.
