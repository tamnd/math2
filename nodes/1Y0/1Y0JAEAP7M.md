---
tag: 1Y0JAEAP7M
kind: proof
name: Proof of the Cook-Reckhow theorem
msc: ["03F20", "68Q15"]
topics: [CBAF7J051K]
audience: research
proves: YS1T29B00B
uses: [3V24CYWDT6, SBDQH0TJ5X, NBSD5FG7NY, CTK8AH98Z1, 3QKF32ZAKN]
methods: [0NTF6DMVAP, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof size complexity
  - url: https://en.wikipedia.org/wiki/Co-NP
    locator: lead section
---

## Proof

We show that a polynomially bounded proof system is the same thing as an NP certificate for tautologies, and then we use that $\mathrm{TAUT}$ is coNP-complete.

First the fact from complexity theory.
By the [[Cook-Levin theorem|CTK8AH98Z1]], the set $\mathrm{SAT}$ of satisfiable formulas is NP-complete.
A formula $\tau$ is a tautology exactly when $\neg \tau$ is not satisfiable, and $\tau \mapsto \neg \tau$ is computable in polynomial time.
So $\mathrm{TAUT}$ is in [[coNP|NBSD5FG7NY]], and every language in coNP reduces to it in polynomial time.

### From a polynomially bounded system to NP = coNP

Let $f$ be a proof system with a polynomial bound $q$, so that every $\tau \in \mathrm{TAUT}$ has an $f$-proof $w$ with $\lvert w \rvert \le q(\lvert \tau \rvert)$.

1. Define a nondeterministic algorithm $M$.
   On input $\tau$, it guesses a string $w$ with $\lvert w \rvert \le q(\lvert \tau \rvert)$, computes $f(w)$, and accepts if $f(w) = \tau$.
2. $M$ runs in polynomial time.
   The guess has length at most $q(\lvert \tau \rvert)$, and $f$ runs in time polynomial in $\lvert w \rvert$.
3. If $\tau \in \mathrm{TAUT}$, then some guess $w$ is a short $f$-proof of $\tau$, by the bound $q$, so $M$ accepts $\tau$.
4. If $M$ accepts $\tau$, then $\tau = f(w)$ for some $w$.
   The image of $f$ is $\mathrm{TAUT}$, so $\tau \in \mathrm{TAUT}$.
5. By steps 1 to 4, $\mathrm{TAUT} \in$ [[NP|SBDQH0TJ5X]].
6. Let $L \in \mathrm{coNP}$.
   Since $\mathrm{TAUT}$ is coNP-complete, there is a polynomial-time $r$ with $x \in L$ if and only if $r(x) \in \mathrm{TAUT}$.
   Running $M$ on $r(x)$ decides $L$ nondeterministically, so $L \in \mathrm{NP}$ and $\mathrm{coNP} \subseteq \mathrm{NP}$.
7. Let $L \in \mathrm{NP}$.
   Its complement $\bar L$ is in coNP, so $\bar L \in \mathrm{NP}$ by step 6, and hence $L \in \mathrm{coNP}$.
   So $\mathrm{NP} \subseteq \mathrm{coNP}$.
8. Steps 6 and 7 give $\mathrm{NP} = \mathrm{coNP}$.

### From NP = coNP to a polynomially bounded system

Assume $\mathrm{NP} = \mathrm{coNP}$.

9. Then $\mathrm{TAUT} \in \mathrm{coNP} = \mathrm{NP}$.
   By the definition of NP, there are a polynomial $q$ and a polynomial-time algorithm $V$ such that $\tau \in \mathrm{TAUT}$ if and only if $V(\tau, w) = 1$ for some $w$ with $\lvert w \rvert \le q(\lvert \tau \rvert)$.
10. Fix a code $\langle x, y \rangle$ of pairs of strings with $\lvert \langle x, y \rangle \rvert = 2 \lvert x \rvert + 2 \lvert y \rvert + 2$.
    For example, double each letter of $x$ and of $y$, and put two different letters between them.
    Coding and decoding take polynomial time.
11. Define $f(z) = \tau$ if $z = \langle \tau, w \rangle$, $\lvert w \rvert \le q(\lvert \tau \rvert)$ and $V(\tau, w) = 1$.
    For every other string $z$, define $f(z) = p \lor \neg p$.
12. $f$ is computable in polynomial time, since it decodes $z$, compares two lengths and runs $V$ once.
13. Every value of $f$ is a tautology.
    In the first case of step 11, $V(\tau, w) = 1$ with a short $w$, so $\tau \in \mathrm{TAUT}$ by step 9, and in the second case the value is $p \lor \neg p$.
14. Every tautology is a value of $f$.
    If $\tau \in \mathrm{TAUT}$, then step 9 gives a short $w$ with $V(\tau, w) = 1$, and $f(\langle \tau, w \rangle) = \tau$.
15. By steps 12 to 14, $f$ is a [[propositional proof system|3V24CYWDT6]].
16. The proof $\langle \tau, w \rangle$ of step 14 has length at most $2 \lvert \tau \rvert + 2 q(\lvert \tau \rvert) + 2$.
    This is a polynomial in $\lvert \tau \rvert$, so $f$ is polynomially bounded.

Steps 1 to 8 and steps 9 to 16 prove the two directions of the equivalence.
$\blacksquare$

## Idea

A polynomially bounded proof system is an NP certificate in disguise: to accept a tautology, guess its short proof and run the checker.
In the other direction, an NP certificate for a tautology, paired with the formula, already is a proof, and the NP verifier is the checker.
What remains is the coNP-completeness of $\mathrm{TAUT}$, which turns "$\mathrm{TAUT} \in \mathrm{NP}$" into "$\mathrm{NP} = \mathrm{coNP}$".
The proof never looks inside any particular proof system, and that is why it says nothing about which systems have short proofs.

## Variants

The same argument shows that a nonempty language $L$ has a polynomially bounded proof system if and only if $L \in \mathrm{NP}$.
For refutation systems of CNFs, replace $\mathrm{TAUT}$ by the set of unsatisfiable CNFs.
That set is also coNP-complete, because the satisfiability of [[3-CNFs|3QKF32ZAKN]] is NP-complete, so the same two directions go through.
