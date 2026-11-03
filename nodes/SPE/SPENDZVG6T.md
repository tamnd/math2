---
tag: SPENDZVG6T
kind: definition
name: Quantum complexity class BQP
msc: [68Q12, 68Q15, 81P68]
defines: VP21SFE7ZA
uses: [E1P61VYRRD, ESPYW94XGR]
sources:
  - url: https://en.wikipedia.org/wiki/BQP
---

## Definition

Let $L \subseteq \set{0,1}^*$ be a language.
The language $L$ is in *BQP* if there are a [[quantum Turing machine|E1P61VYRRD]] $M$ and a polynomial $p$ with these properties.

1. On every input $x$, the machine $M$ halts after at most $p(\abs{x})$ steps, and its output is then measured.
2. If $x \in L$, the measurement gives $1$ with probability at least $2/3$.
3. If $x \notin L$, the measurement gives $1$ with probability at most $1/3$.

The amplitudes of $M$ are required to be efficiently computable complex numbers.

## Remarks

An equivalent definition uses uniform families of quantum circuits.
A language $L$ is in BQP exactly when some classical polynomial-time algorithm does the following.
On input $1^n$ it outputs a quantum circuit $C_n$ of polynomial size that decides $L$ on inputs of length $n$ with error at most $1/3$.

Example: every language in P is in BQP.
A reversible version of a deterministic polynomial-time computation can be run on a quantum machine, and it gives the right answer with probability $1$.

Non-example: if in clause 2 one only asks for probability greater than $1/2$, with no gap from $1/2$, one gets the class PP, which contains BQP.
With bounded error, repeating $M$ and taking the majority makes the error exponentially small, which is why $1/3$ can be replaced by any constant below $1/2$.

Known inclusions are $\mathrm{BPP} \subseteq \mathrm{BQP} \subseteq \mathrm{PP} \subseteq \mathrm{PSPACE}$.
