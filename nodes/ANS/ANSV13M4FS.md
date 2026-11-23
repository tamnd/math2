---
tag: ANSV13M4FS
kind: problem
name: Lower bounds for Frege systems
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
uses: [J2BAR09TPF, 5YSE04SHFH, 3V24CYWDT6, YS1T29B00B]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
history:
  posed_by: "Stephen Cook and Robert Reckhow"
  first_stated: "1979"
  notes: "Cook and Reckhow, The relative efficiency of propositional proof systems, Journal of Symbolic Logic, 1979."
---

## Problem

Compare two numbers.
In [[resolution|6JSH907W5R]], every refutation of the pigeonhole formula with $n + 1$ pigeons and $n$ holes needs a number of clauses exponential in $n$.
In a [[Frege system|J2BAR09TPF]], the best lower bound known for any family of tautologies is only about quadratic in the size of the tautology.
The problem asks whether Frege, like resolution, has a family that needs superpolynomial size.

Fix a Frege system $\mathcal F$.
Is there a sequence of tautologies $\tau_1, \tau_2, \dots$ with $\lvert \tau_n \rvert \to \infty$ such that the least size $s_{\mathcal F}(\tau_n)$ of an $\mathcal F$-proof of $\tau_n$ is bounded by no polynomial in $\lvert \tau_n \rvert$?

The problem is open, and the same question for [[extended Frege|5YSE04SHFH]] is open too.
By [[Reckhow's theorem|YAHHWZ7XRH]], the answer does not depend on the choice of $\mathcal F$.
The measure is size, the number of symbols of a proof.

## Remarks

### What is known

The best known lower bounds on Frege size are quadratic in the size of the tautology.
For the number of lines, nothing better than a linear lower bound is known.
Weaker systems fare much better.
For [[bounded-depth Frege|41QJ1WEMJ3]] of each fixed depth $d$ there are exponential size lower bounds, for example from [[Ajtai's theorem|Q0ERK64J78]] and its later sharpenings on the pigeonhole formulas.
Those bounds have the form $2^{n^{\varepsilon_d}}$ with $\varepsilon_d$ shrinking as $d$ grows, so they say nothing about Frege, whose lines have unbounded depth.

### Why the hard examples fail

Each family that is hard for a weaker system has turned out to be easy for Frege.
The [[pigeonhole formulas|RJ571F7FF0]] need exponential size in resolution and superpolynomial size in bounded-depth Frege.
But [[Buss's theorem|VRX23FZV21]] gives them polynomial-size Frege proofs, by counting with formulas of depth $O(\log n)$.
The [[Tseitin formulas|JXTCC6KXNG]] need exponential size in resolution on expander graphs, yet Frege proves them in polynomial size by counting modulo $2$.
So a Frege lower bound needs new hard candidates, not just old ones.

### Why the methods fail

The lower bounds for resolution and [[cutting planes|KKCX2HQP2K]] come from [[feasible interpolation|59GJCM8C66]], which turns a short proof into a small circuit.
Bonet, Pitassi and Raz showed in 2000 that $\mathrm{TC}^0$-Frege has no feasible interpolation unless the Diffie-Hellman key exchange is insecure.
Frege systems p-simulate $\mathrm{TC}^0$-Frege, so the same holds for Frege.
Krajíček and Pudlák showed in 1998 that extended Frege has no feasible interpolation if RSA is secure.
A second obstacle is that the lines of a Frege proof are formulas, and no superpolynomial lower bound on formula size is known for any explicit function in $\mathrm{NP}$.
The successful methods for weak systems all rest on lower bounds for the matching weak circuit classes.

### What a solution would and would not give

A superpolynomial lower bound for Frege would not prove $\mathrm{NP} \ne \mathrm{coNP}$, since the [[Cook-Reckhow theorem|YS1T29B00B]] needs a lower bound for every proof system.
If the hard tautologies $\tau_n$ can be written down by a polynomial-time algorithm, then adding them as axioms gives a proof system with short proofs of each $\tau_n$.
Frege could not simulate that system, so Frege would not be an optimal proof system.

### Watch out

A lower bound on the number of lines and a lower bound on size are different statements.
A Frege proof of $10$ lines can have size $10^6$, so a quadratic lower bound on size does not give one on lines.
The second trap is to quote an exponential lower bound for bounded-depth Frege as a Frege bound.
It is a bound for a weaker system, and the family it uses has short Frege proofs.

## History

Cook and Reckhow posed the question in their 1979 paper, as part of the program of lower bounds for ever stronger proof systems.
The same paper gave polynomial-size extended Frege proofs of the pigeonhole formulas and asked whether Frege has them.
Buss answered that question positively in 1987.
The general problem has been open since 1979.

## Explanations

### L1 human

Frege systems are the ordinary proof systems of logic textbooks.
No one knows a family of tautologies that needs very long proofs in them.
Every candidate tried so far, such as the pigeonhole principle for $n + 1$ pigeons and $n$ holes, turned out to have proofs of moderate length.
Resolution needs a number of clauses exponential in $n$ on that principle, but Frege needs only a number of symbols polynomial in $n$.

### L2 human

We check why an exponential lower bound for depth-$d$ Frege does not settle the problem.
The exponential form of Ajtai's theorem says that depth-$d$ Frege proofs of $\neg \mathrm{PHP}^{n+1}_n$ need size $2^{n^{\varepsilon_d}}$, for some $\varepsilon_d > 0$.
Buss's theorem gives Frege proofs of the same formulas of size polynomial in $n$.
Those proofs use lines of depth about $\log n$, which grows with $n$.
So for any fixed $d$, Buss's proofs eventually exceed depth $d$, and the depth-$d$ bound does not apply to them.
The typical use of the problem is as a benchmark: each new method is judged by whether it could ever reach Frege systems.

### L3 human

Frege systems match the circuit class $\mathrm{NC}^1$, in the sense that their lines are formulas.
So a Frege lower bound sits near the frontier of circuit complexity, where lower bounds for formulas are also stuck.
On the logic side, a superpolynomial Frege lower bound for the translations of a true statement would show that the theory $\mathrm{VNC}^1$ of [[bounded arithmetic|RA380RWEC0]] does not prove it.
The question for [[extended Frege|5YSE04SHFH]] is harder still, because extended Frege p-simulates Frege.
