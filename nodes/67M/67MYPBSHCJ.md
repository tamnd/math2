---
tag: 67MYPBSHCJ
kind: example
name: The truth-table proof system
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
instance_of: [3V24CYWDT6, 1Q046J0AW2]
uses: [3V24CYWDT6, 05006AJ7DZ, 3A81RHAN68]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
  - url: https://en.wikipedia.org/wiki/Truth_table
    locator: lead section
---

## Example

Start with $\tau = p \lor \neg p$.
It has one variable, so its truth table has $2$ rows, and its proof in the truth-table system is the string
$$w = (p \lor \neg p) \, \# \, 11.$$
The two letters $1$ after the separator $\#$ are padding, one for each row.
They carry no information, but they give the checker the time that it needs.

In general, write $n(\tau)$ for the number of distinct variables of a formula $\tau$, and define $f$ on strings as follows.

1. If $w = \tau \# 1^{2^{n(\tau)}}$, then $f$ evaluates $\tau$ under each of the $2^{n(\tau)}$ assignments.
2. If every assignment makes $\tau$ true, then $f(w) = \tau$.
3. In every other case, $f(w) = p \lor \neg p$.

We check that $f$ is a [[propositional proof system|3V24CYWDT6]].

1. *Polynomial time.*
   There are $2^{n(\tau)} \le \lvert w \rvert$ assignments, and each evaluation takes time polynomial in $\lvert \tau \rvert \le \lvert w \rvert$.
   So $f$ runs in time polynomial in $\lvert w \rvert$, and in [[polynomial time|3A81RHAN68]] in the sense of the definition.
2. *Soundness.*
   Every value of $f$ is $p \lor \neg p$ or a formula that every assignment makes true, so every value is a [[tautology|05006AJ7DZ]].
3. *Completeness.*
   For a tautology $\tau$, the string $\tau \# 1^{2^{n(\tau)}}$ is an $f$-proof of $\tau$.

Now we show that $f$ is not polynomially bounded.
Let $\tau_n = (x_1 \lor \neg x_1) \land \dots \land (x_n \lor \neg x_n)$, a formula of length $O(n \log n)$ when indices are written in binary.
For $n \ge 2$, the only $f$-proof of $\tau_n$ is $\tau_n \# 1^{2^n}$, since every other string goes to $p \lor \neg p$.
So the size of the shortest proof is
$$s_f(\tau_n) > 2^n,$$
and no polynomial in $\lvert \tau_n \rvert$ bounds it.

## Remarks

The example shows what the definition of a proof system asks for.
It asks for proofs that are easy to check, and it does not ask for short proofs.
The measure here is size in symbols, and it is about $2^{n(\tau)}$, so every tautology has a proof of exponential size and exponential size is the trivial upper bound.

Every system of interest beats the table on some family.
A [[Frege system|J2BAR09TPF]] proves $\tau_n$ with $O(n)$ lines: a fixed number of lines prove each $x_i \lor \neg x_i$, and a fixed number more join each new conjunct by $\land$.
So the table and Frege differ by an exponential factor on $\tau_n$.
If you add a variable that does not occur in $\tau$, nothing changes, because $n(\tau)$ counts only the variables of $\tau$.
Watch out: the length of $\tau$ is not the measure, since the size $s_f(\tau)$ counts the padding.

## Explanations

### L1 human

A truth table checks a formula one row at a time, with a row for each way to set the letters true or false.
In this proof system the proof is just a long string of padding, which gives the checker time to go through all the rows.
A formula with $3$ letters has $8$ rows and $8$ padding letters.
A formula with $50$ letters has $2^{50}$ rows, about $10^{15}$, which no one can write down.

### L2 human

We check one proof and reject one string.

1. Take $\tau = p \to (q \to p)$, with $n(\tau) = 2$, and the string $w = \tau \# 1111$.
2. The four assignments $(p, q) = (0,0), (0,1), (1,0), (1,1)$ all make $\tau$ true, because $\tau$ is false only when $p = 1$ and $q \to p$ is false, which needs $p = 0$.
3. So $f(w) = \tau$, and $w$ has $4$ padding letters.
4. The string $\tau \# 111$ has the wrong padding, so $f$ maps it to $p \lor \neg p$, and it is not a proof of $\tau$.

The typical use of the truth-table system is as a baseline.
The upper bound $2^n$ holds for free, so the question for each real system is how far below $2^n$ its shortest proofs can go.
