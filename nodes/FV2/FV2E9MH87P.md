---
tag: FV2E9MH87P
kind: example
name: The truth-table system is automatizable
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
instance_of: [WBECDG163W]
uses: [67MYPBSHCJ, WBECDG163W, 3V24CYWDT6]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Automatability
  - url: https://en.wikipedia.org/wiki/Truth_table
    locator: lead section
---

## Example

Take $\tau = (p \wedge q) \vee \neg p \vee \neg q$, a tautology with $2$ variables.
Its proof in the [[truth-table system|67MYPBSHCJ]] is the string $\tau \# 1111$, with one letter $1$ for each of the $4$ rows of the truth table.
A program can write this string by counting the variables of $\tau$ and printing $2^2$ ones, with no search at all.

Let $f$ be the truth-table system, and for a tautology $\tau$ with $n(\tau)$ distinct variables let $w_\tau = \tau \# 1^{2^{n(\tau)}}$.
Then $w_\tau$ is an $f$-proof of $\tau$, and it is the only one unless $\tau$ is the default value $p \vee \neg p$ of $f$.
So $s_f(\tau) = \lvert \tau \rvert + 1 + 2^{n(\tau)}$ for every other tautology, and $s_f(p \vee \neg p)$ is a constant.

The algorithm is: given $\tau$, count its distinct variables and output $w_\tau$.
We check that it meets the definition of [[automatizable|WBECDG163W]].

1. Counting the variables takes time polynomial in $\lvert \tau \rvert$.
2. Writing the output takes time $O(\lvert \tau \rvert + 2^{n(\tau)})$.
3. For $\tau$ other than $p \vee \neg p$ we have $2^{n(\tau)} < s_f(\tau)$, so both costs are polynomial in $\lvert \tau \rvert + s_f(\tau)$.
4. For $\tau = p \vee \neg p$ the output $w_\tau$ has constant length.

So $f$ is automatizable with a polynomial time bound $t$.

The algorithm does not check that $\tau$ is a tautology, and it does not need to, since the definition asks for correct output only on tautologies.
If one wants a checked output, evaluating $\tau$ under all $2^{n(\tau)}$ assignments also takes time polynomial in $\lvert \tau \rvert + s_f(\tau)$.

## Remarks

The system is automatizable because its proofs are long, and the length $s_f(\tau)$ already pays for the search.
So automatizability alone says nothing about short proofs.

The truth-table system is not [[polynomially bounded|3V24CYWDT6]].
The formula $\bigwedge_{i \leq n} (p_i \vee \neg p_i)$ has length $O(n \log n)$ with indices in binary, and its only proof has length more than $2^n$.

The interesting question is automatizability for systems with short proofs, such as [[resolution|6JSH907W5R]].

## Explanations

### L1 human

In the truth-table system, the proof of a formula is the formula followed by a long row of marks, one for each way to set its letters.
A program can write this proof at once, without any search.
So the program is fast compared with the length of the proof.

### L2 human

The definition of automatizability measures time against $\lvert \tau \rvert + s_f(\tau)$.
For the truth-table system this sum is at least $2^{n(\tau)}$, so the algorithm may spend time exponential in $n(\tau)$.
A trap is to conclude that truth tables are a good proof system.
They are automatizable but exponentially long, while systems with short proofs, such as resolution, are hard to automate by the [[Atserias-Müller theorem|W7FP9TZMVP]].
