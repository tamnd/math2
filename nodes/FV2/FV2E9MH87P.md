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

Let $f$ be the [[truth-table system|67MYPBSHCJ]].
For a tautology $\tau$ with $n(\tau)$ distinct variables, its $f$-proofs are the words $\tau \# 1^{2^{n(\tau)}}$.
So $\tau$ has exactly one $f$-proof, and $s_f(\tau) = \abs{\tau} + 1 + 2^{n(\tau)}$.

**Algorithm.** Given $\tau$, count its distinct variables, and output $\tau \# 1^{2^{n(\tau)}}$.

**Analysis.**

1. Counting the variables takes time polynomial in $\abs{\tau}$.
2. Writing the output takes time $O(\abs{\tau} + 2^{n(\tau)})$.
3. Both are at most polynomial in $\abs{\tau} + s_f(\tau)$, since $2^{n(\tau)} \le s_f(\tau)$.
4. So $f$ is [[automatizable|WBECDG163W]] with a linear bound $t$, up to the cost of step 1.

The algorithm does not check that $\tau$ is a tautology, and it does not need to: automatizability only asks for correct output on tautologies.
If one wants the output to be checked, then evaluating $\tau$ under all $2^{n(\tau)}$ assignments also takes time polynomial in $\abs{\tau} + s_f(\tau)$.

## Remarks

- The system is automatizable because its proofs are long. The length $s_f(\tau)$ already pays for the search.
- So automatizability alone says nothing about short proofs. The truth-table system is not [[polynomially bounded|3V24CYWDT6]], since $\bigvee_{i \le n} (p_i \lor \neg p_i)$ has size linear in $n$ and its only proof has size about $2^n$.
- The interesting question is automatizability for systems with short proofs, such as [[resolution|6JSH907W5R]].

## Explanations

### L1 human

In the truth-table system, the proof of a formula is a long list of marks, one for each way to set its letters.
A program can write this proof at once, without any search.
So the program is fast compared with the length of the proof.

### L2 human

The definition of automatizability measures time against $\abs{\tau} + s_f(\tau)$.
For the truth-table system this sum is at least $2^{n(\tau)}$, so the algorithm may spend exponential time in $n(\tau)$.
A trap is to conclude that truth tables are a good proof system.
They are automatizable but exponentially long, while systems with short proofs, such as resolution, are hard to automate by the [[Atserias-Müller theorem|W7FP9TZMVP]].
