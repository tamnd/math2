---
tag: PFKWV5SFF5
kind: statement
role: theorem
name: Savitch's theorem
msc: [68Q15]
uses: [FDNFGKEEJR, M7SDX137WE, 7RH189REV7, T9NTRY93ZT]
about: [FDNFGKEEJR]
sources:
  - url: https://en.wikipedia.org/wiki/Savitch%27s_theorem
same_as:
  wikidata: Q954210
  wikipedia: Savitch's theorem
---

## Statement

Let $s \colon \N \to \N$ be a function with $s(n) \ge \log_2 n$ for all $n \ge 1$.
Suppose that $s$ is space-constructible, that is, the binary form of $s(n)$ can be computed from $1^n$ in $O(s(n))$ space.
Then
$$\mathrm{NSPACE}(s(n)) \subseteq \mathrm{DSPACE}(s(n)^2),$$
where $\mathrm{NSPACE}$ and $\mathrm{DSPACE}$ are the classes defined by [[space complexity|FDNFGKEEJR]] of nondeterministic and deterministic Turing machines.

## Remarks

Let $N$ be a [[nondeterministic Turing machine|M7SDX137WE]] that uses space $O(s(n))$.
On an input of length $n$, it has at most $2^{c \, s(n)}$ configurations for some constant $c$.
The deterministic machine checks whether an accepting configuration can be reached from the start within $2^{c \, s(n)}$ steps.
To test reachability within $2^{t}$ steps, it tries every middle configuration and tests both halves within $2^{t-1}$ steps, reusing the same space.
The recursion has depth $O(s(n))$ and each level stores one configuration of size $O(s(n))$, which gives space $O(s(n)^2)$.
Walter Savitch proved the theorem in 1970.

Consequences: NPSPACE, defined with nondeterministic machines in polynomial space, equals [[PSPACE|T9NTRY93ZT]], since the square of a polynomial is a polynomial.
Also $\mathrm{NL} \subseteq \mathrm{DSPACE}((\log n)^2)$, where NL is the class [[NL|7RH189REV7]].

## Explanations

### L1 human

Nondeterminism, the power to guess, saves at most a square in memory.
Anything a guessing machine does with $s$ cells, an ordinary machine can do with about $s^2$ cells.
For time, by contrast, the best known simulation of guessing costs an exponential.

### L2 human

The theorem is a statement about reachability in the configuration graph, solved by divide and conquer on the path length.
It shows that polynomial space is the same with or without nondeterminism, so there is no space analogue of the P versus NP question at the polynomial level.
Whether the square is needed is open; for example, it is unknown whether $\mathrm{NL} = \mathrm{L}$.
The Immerman–Szelepcsényi theorem gives a different fact about nondeterministic space: it is closed under complement.
