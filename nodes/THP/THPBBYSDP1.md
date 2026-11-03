---
tag: THPBBYSDP1
kind: statement
role: theorem
name: Natural proofs barrier
msc: [68Q17, 68Q06, 94A60]
uses: [P0A5DVRYDW, 4PGX7PHJCK, 0X05GS525E]
about: [4PGX7PHJCK]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_proof
same_as:
  wikidata: Q6980761
  wikipedia: Natural proof
---

## Statement

For $n \ge 1$ let $F_n$ be the set of [[Boolean functions|0X05GS525E]] $f \colon \set{0,1}^n \to \set{0,1}$, and write $N = 2^n$.
A *combinatorial property* is a sequence $\mathcal{C} = (C_n)$ with $C_n \subseteq F_n$.
It is *P/poly-natural* if some $C_n^* \subseteq C_n$ satisfies:

1. (constructivity) membership $f \in C_n^*$ is decided by Boolean circuits of size polynomial in $N$ that read the truth table of $f$;
2. (largeness) $\abs{C_n^*} \ge 2^{-O(n)} \abs{F_n}$.

It is *useful against P/poly* if every sequence $f_n \in F_n$ with $f_n \in C_n$ for infinitely many $n$ has circuit size not bounded by any polynomial in $n$.

Assume that, for some $\varepsilon > 0$, there is a family of pseudorandom functions computed by polynomial-size circuits with the following hardness.
No circuit of size $2^{n^\varepsilon}$ distinguishes them from a uniformly random function with advantage at least $2^{-n^\varepsilon}$.
Then no P/poly-natural property is useful against [[P/poly|P0A5DVRYDW]].

## Remarks

The idea of the proof is that a natural property useful against P/poly would itself be a distinguisher.
Pseudorandom functions have small circuits, so they lie outside $C_n^*$, while a random function lies in $C_n^*$ with probability at least $2^{-O(n)}$.
The constructive test for $C_n^*$ then tells the two apart, in time polynomial in $N = 2^n$, which contradicts the hardness assumption.
The hypothesis is believed true; it follows from strong enough versions of standard cryptographic assumptions, such as the hardness of factoring.

Most known [[circuit lower bounds|4PGX7PHJCK]], such as [[parity not in AC0|W6T7X0QCFH]], are proved through properties that are natural in this sense, against weaker circuit classes.
So the theorem says that proving $\mathrm{NP} \not\subseteq \mathrm{P/poly}$ needs an argument of a different kind.

## Explanations

### L1 human

To prove that a function is hard to compute, one usually finds a property that the function has and that every easy function lacks.
Razborov and Rudich noticed that the known properties are easy to test and are shared by many functions.
They showed that such a property, if it worked against all polynomial-size circuits, would break good pseudorandom functions.
Since cryptographers believe such functions exist, the usual style of argument should not separate NP from polynomial-size circuits.

### L2 human

The barrier appeared in 1994 in a paper of Alexander Razborov and Steven Rudich.
It explains why the progress on lower bounds for restricted classes, such as AC0 and monotone circuits, did not extend to general circuits.
Together with [[relativization|BST2RKE12N]] and algebrization, it is one of the main known obstacles to proving $\mathrm{P} \ne \mathrm{NP}$.
Some lower bounds avoid it, for example those proved by diagonalisation, which use no large property.
