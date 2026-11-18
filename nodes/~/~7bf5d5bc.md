---
tag: ~7bf5d5bc
kind: example
name: The truth-table proof system
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
instance_of: [~8ae21f34, 1Q046J0AW2]
uses: [~8ae21f34, 05006AJ7DZ, 3A81RHAN68]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
  - url: https://en.wikipedia.org/wiki/Truth_table
    locator: lead section
---

## Example

For a formula $\tau$, let $n(\tau)$ be the number of distinct variables of $\tau$.
Define $f \colon \Sigma^* \to \Sigma^*$ as follows.

1. If $w = \tau \# 1^{2^{n(\tau)}}$, a formula followed by a separator and $2^{n(\tau)}$ letters $1$, then $f$ evaluates $\tau$ under each of the $2^{n(\tau)}$ assignments.
2. If every assignment makes $\tau$ true, then $f(w) = \tau$.
3. In every other case, $f(w) = p \lor \neg p$.

The function $f$ is a [[propositional proof system|~8ae21f34]].

- *Polynomial time.* There are $2^{n(\tau)} \le \abs{w}$ assignments, and each evaluation takes time polynomial in $\abs{\tau} \le \abs{w}$. So $f$ runs in time polynomial in $\abs{w}$.
- *Soundness.* Every value of $f$ is $p \lor \neg p$ or a formula that is true under all assignments, so every value is a [[tautology|05006AJ7DZ]].
- *Completeness.* For a tautology $\tau$, the string $\tau \# 1^{2^{n(\tau)}}$ is an $f$-proof of $\tau$.

The padding $1^{2^{n(\tau)}}$ is the proof: it buys the time that the checker needs.

*Not polynomially bounded.* Let $\tau_n = (x_1 \lor \neg x_1) \land \cdots \land (x_n \lor \neg x_n)$.
Its length is linear in $n$, up to the length of the indices.
Every $f$-proof of $\tau_n$ has the form $\tau_n \# 1^{2^n}$, of length more than $2^n$.
So $s_f(\tau_n) > 2^n$, and no polynomial bounds $s_f$.

## Remarks

The truth-table system shows that the definition asks for proofs that are easy to check, and not for proofs that are short.
Its size $s_f(\tau)$ is about $2^{n(\tau)}$, so exponential size is the trivial upper bound on proof size.
The systems of interest, such as resolution and Frege systems, give short proofs of some families on which $f$ is exponential, such as $\tau_n$.

## Explanations

### L1 human

A truth table checks a formula row by row, one row for each assignment of true and false to the variables.
In this proof system, the proof is just a long string that gives the checker enough time to check all rows.
For a formula with $3$ variables the proof has $8$ padding letters, and for $50$ variables it has $2^{50}$, about $10^{15}$.

### L2 human

We write the proof of $\tau = p \lor \neg p$.

1. $\tau$ has one variable, so $n(\tau) = 1$ and the padding has $2^1 = 2$ letters.
2. The proof is $w = (p \lor \neg p) \# 11$.
3. $f$ evaluates $\tau$ at $p = 0$ and at $p = 1$, and both values are $1$.
4. So $f(w) = p \lor \neg p$.

The typical use of the example is as the base case of the definition: every proof system improves on it for some formulas, or it does not.
A trap: the length of $\tau$ is not the measure; the size $s_f(\tau)$ counts the padding.
