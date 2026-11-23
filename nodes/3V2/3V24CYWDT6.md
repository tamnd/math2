---
tag: 3V24CYWDT6
kind: definition
defines: 1Q046J0AW2
name: Propositional proof system
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
uses: [05006AJ7DZ, 3A81RHAN68, SBDQH0TJ5X, NBSD5FG7NY]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof system strength
---

## Definition

Suppose that a solver claims that the three clauses $\{p\}$, $\{\neg p, q\}$ and $\{\neg q\}$ cannot all be true.
It can back the claim with two resolution steps, $\{p\}, \{\neg p, q\} \vdash \{q\}$ and $\{q\}, \{\neg q\} \vdash \square$, and you can check both steps at a glance.
A propositional proof system is any such scheme of evidence: a fast checker that accepts evidence exactly for the true statements.

Fix a finite alphabet $\Sigma$ with at least two letters, and encode propositional formulas as strings over $\Sigma$, with the variable $p_i$ written as $p$ followed by $i$ in binary.
Let $\mathrm{TAUT} \subseteq \Sigma^*$ be the set of codes of [[tautologies|05006AJ7DZ]], and write $\lvert x \rvert$ for the length of a string $x$.
A *propositional proof system*, in the sense of Cook and Reckhow, is a function $f \colon \Sigma^* \to \Sigma^*$ with two properties.

1. $f$ is computable in [[polynomial time|3A81RHAN68]].
2. The image of $f$ is exactly $\mathrm{TAUT}$.

A string $w$ with $f(w) = \tau$ is an *$f$-proof* of $\tau$.
The *size* $s_f(\tau)$ is the least length $\lvert w \rvert$ of an $f$-proof of $\tau$.
The system $f$ is *polynomially bounded* if some polynomial $q$ gives $s_f(\tau) \le q(\lvert \tau \rvert)$ for every $\tau \in \mathrm{TAUT}$.

A proof system $g$ *p-simulates* $f$ if some polynomial-time function $h$ gives $g(h(w)) = f(w)$ for every string $w$.
It *simulates* $f$ if some polynomial $q$ gives $s_g(\tau) \le q(s_f(\tau))$ for every tautology $\tau$.
Two systems are *p-equivalent* if each p-simulates the other.
A system is *optimal* if it simulates every proof system, and *p-optimal* if it p-simulates every proof system.
A *refutation system* is defined in the same way, with the set of codes of unsatisfiable CNFs in place of $\mathrm{TAUT}$.

## Notation

Books write $s_f(\tau)$, $\mathrm{size}_f(\tau)$ or $\lvert \tau \rvert_f$ for the size of the shortest proof.
For systems whose proofs are lists of formulas, many books also count the *number of lines*, written $k_f(\tau)$ or $\lambda_f(\tau)$.
The two measures differ, since one line can be long, so a result must say which one it bounds.
The relations "$g$ p-simulates $f$" and "$g$ simulates $f$" are often written $f \le_p g$ and $f \le g$.

## Remarks

### Reading the two conditions

Condition 1 makes proofs easy to check, and it is the whole content of the word "proof".
Condition 2 has two halves.
Every value of $f$ is a tautology, which is *soundness*, and every tautology is a value of $f$, which is *completeness*.
The definition does not ask that proofs be short.
How short they can be is the subject of [[proof complexity|1Q046J0AW2]].

A system that writes proofs as lists of formulas fits the definition through a standard trick.
Let $f(w)$ be the last formula of $w$ if $w$ is a correct derivation, and the fixed tautology $p \lor \neg p$ otherwise.
That is how [[Frege systems|J2BAR09TPF]], the sequent calculus, [[extended Frege|5YSE04SHFH]], [[cutting planes|KKCX2HQP2K]] and the [[algebraic proof systems|ZERBQSTZB5]] all become proof systems in this sense.

### Three examples

The [[truth-table proof system|67MYPBSHCJ]] takes a formula with $n$ variables followed by $2^n$ padding letters.
It is a proof system, and it is not polynomially bounded, since $(x_1 \lor \neg x_1) \land \dots \land (x_n \lor \neg x_n)$ needs size above $2^n$.
[[Resolution|6JSH907W5R]] becomes a proof system for tautologies once you fix a CNF translation of $\neg \tau$, as [[resolution as a Cook-Reckhow proof system|SSJGW960SY]] checks.
A Frege system sends a correct derivation to its last line, as above.

### What fails to be a proof system

[[Checking one satisfying assignment|72CPDNTXKT]] gives a map from a pair (formula, satisfying assignment) to the formula.
It runs in polynomial time and every tautology is a value, but $p$ is also a value, so soundness fails.
The map that sends each tautology to itself and every other string to $p \lor \neg p$ has image $\mathrm{TAUT}$.
It runs in polynomial time exactly when $\mathrm{TAUT} \in \mathrm{P}$, and that is open, so it is not known to be a proof system.

### The first properties

The relation "p-simulates" is reflexive and transitive, because a composition of polynomial-time functions runs in polynomial time.
If $g$ p-simulates $f$ through $h$, then $g$ simulates $f$, since $h$ turns a shortest $f$-proof $w$ into a $g$-proof of length polynomial in $\lvert w \rvert$.
For every system $f$ there is a polynomial $t$ with $\lvert \tau \rvert \le t(s_f(\tau))$, because $f$ writes $\tau$ in time polynomial in $\lvert w \rvert$ and writes at most one letter per step.
So a polynomially bounded system $g$ with bound $q$ simulates every $f$:
$$s_g(\tau) \le q(\lvert \tau \rvert) \le q(t(s_f(\tau))).$$
A polynomially bounded system exists if and only if $\mathrm{NP} = \mathrm{coNP}$, by the [[Cook-Reckhow theorem|YS1T29B00B]].

### Optimal systems

Whether an optimal propositional proof system exists is open.
Whether a p-optimal one exists is also open.
Krajíček and Pudlák showed in 1989 that an optimal system exists if $\mathrm{NE} = \mathrm{coNE}$, and that a p-optimal system exists if $\mathrm{E} = \mathrm{NE}$.
The converses are not known.

### Watch out

The first error is to call a sound system that proves only some tautologies a proof system.
The definition asks for the image to be all of $\mathrm{TAUT}$.
The second error is to treat "simulates" and "p-simulates" as the same.
The first compares only proof sizes, while the second asks for a fast translation of proofs, which is stronger.
The third error is to read a lower bound for one system as a lower bound for a stronger one.

### History

Stephen Cook and Robert Reckhow gave the definition in 1979, in "The relative efficiency of propositional proof systems" in the Journal of Symbolic Logic.
The same paper introduced p-simulation and proved the theorem that links polynomially bounded systems with $\mathrm{NP} = \mathrm{coNP}$.

### Try it

First, is the map that sends $\tau \# a$ to $\tau$ when $a$ falsifies $\neg \tau$ a proof system?
No: it is the satisfying-assignment map again, applied to $\tau$, so any formula with one true row is a value.

Second, if $g$ p-simulates $f$ and $f$ is polynomially bounded, is $g$ polynomially bounded?
Yes, since $s_g(\tau)$ is at most a polynomial in $s_f(\tau)$, which is at most a polynomial in $\lvert \tau \rvert$.

## Explanations

### L1 human

A proof is evidence that a checker can verify quickly.
The definition allows any kind of evidence, as long as a fast program accepts evidence exactly for the true formulas.
A truth table is evidence of this kind: a formula with $3$ letters has $8$ rows, and a program checks them one by one.
A formula with $100$ letters has $2^{100}$ rows, and that evidence is far too long to write.
The main question is whether some kind of evidence is always short.

### L2 human

We check that resolution, with a fixed translation of $\neg \tau$ into a CNF $F_\tau$, is a proof system.
A proof of $\tau$ is a pair $(\tau, \pi)$, where $\pi$ is a list of clauses.
The checker $f$ computes $F_\tau$, tests that each clause of $\pi$ is a clause of $F_\tau$ or a resolvent of two earlier clauses, and tests that the last clause is empty.
These tests take polynomial time, and $f$ outputs $\tau$ if they pass and $p \lor \neg p$ if they fail.
Soundness holds because a refutation shows that $F_\tau$ is unsatisfiable, so $\tau$ is a tautology.
Completeness holds because resolution can refute every unsatisfiable CNF.
This is the typical use of the definition: name the checker, then verify speed, soundness and completeness.

### L3 human

The definition is the propositional case of a general idea: a proof system for a language $L$ is a polynomial-time function onto $L$.
For $\mathrm{TAUT}$, which is coNP-complete, short proofs for all members is the question $\mathrm{NP} = \mathrm{coNP}$.
The simulation order makes the set of proof systems a preorder, and the open questions on optimal systems ask whether this preorder has a greatest element.
Strong systems correspond to strong theories of [[bounded arithmetic|RA380RWEC0]]; for example, extended Frege corresponds to Cook's theory $\mathrm{PV}$.
