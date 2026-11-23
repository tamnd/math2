---
tag: 5YSE04SHFH
kind: definition
defines: 1Q046J0AW2
name: Extended Frege system
aliases: [extended-frege, ef]
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
uses: [J2BAR09TPF, 3V24CYWDT6, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: Extended Frege system
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Bounded arithmetic
---

## Definition

Write the carry of binary addition as a formula, and each carry contains the previous one twice: the carry into position $i$ unfolds to a formula of size $12 \cdot 2^{i-1} - 9$, as in [[the carry example|MKDZSQM3KE]].
On paper you would write each carry once and give it a name.
Extended Frege is a [[Frege system|J2BAR09TPF]] with exactly that permission: a proof may say "let $q$ stand for $\varphi$" and then use $q$.

Let $\mathcal F$ be a Frege system whose connectives include $\leftrightarrow$, or in which $\leftrightarrow$ is a fixed abbreviation.
An *extended Frege proof*, or EF-proof, of a formula $\tau$ is a list of formulas $\chi_1, \dots, \chi_m = \tau$ in which each line $\chi_i$ satisfies one of two conditions.

1. $\chi_i$ is the conclusion of an instance of a rule of $\mathcal F$ whose premises are among $\chi_1, \dots, \chi_{i-1}$.
2. $\chi_i$ is an *extension axiom* $q \leftrightarrow \varphi$, where $q$ is a variable that does not occur in $\varphi$, in $\chi_1, \dots, \chi_{i-1}$ or in $\tau$.

The variable $q$ in condition 2 is an *extension variable*, and it names $\varphi$.
The *size* of an EF-proof is the total number of symbols of its lines, and its *number of lines* is $m$.
The *extended Frege system* $\mathrm{EF}$ is the [[propositional proof system|3V24CYWDT6]] whose proofs are the EF-proofs.

## Notation

The system is written $\mathrm{EF}$ or $e\mathcal F$, and the least size of an EF-proof of $\tau$ is $s_{\mathrm{EF}}(\tau)$.
By the proof of [[Reckhow's theorem|YAHHWZ7XRH]], the choice of $\mathcal F$ changes sizes by at most a polynomial, so books write $\mathrm{EF}$ without naming $\mathcal F$.
Substitution Frege, with the extra rule "from $\varphi$ infer $\varphi\sigma$", is written $\mathrm{SF}$.

## Remarks

### Why each condition is there

Each condition on the new variable $q$ blocks a way to prove a falsehood.
If $q$ may occur in $\varphi$, then $p \leftrightarrow \neg p$ becomes an axiom, and since $(p \leftrightarrow \neg p) \to r$ is a tautology, modus ponens proves the variable $r$.
If $q$ may occur in $\tau$, then $q \leftrightarrow (r \lor \neg r)$ lets you prove the non-tautology $q$.
[[A self-referential definition|D30HH9YQFM]] works out both failures.
If $q$ may occur in an earlier line, a proof could define $q$ twice, as $r \lor \neg r$ and as $\neg (r \lor \neg r)$, and then derive both $q$ and $\neg q$.

### A small proof with one name

[[An extension step|9CV99XJ8J1]] proves $(a \land b) \lor \neg (a \land b)$ in five lines.
It sets $q \leftrightarrow (a \land b)$, proves $q \lor \neg q$, and then uses a fixed tautology to trade $q$ back for $a \land b$.
The final line has no extension variable, as the definition demands.
In this case the name saves nothing, but in [[the carry example|MKDZSQM3KE]] the $n$ extension axioms have at most $13 n$ symbols in all, while the unfolded carries have size at least $2^i$.

### Why it is sound

Take any assignment to the variables that are not extension variables.
Then go through the proof in order and give each extension variable $q$ the value of its $\varphi$, which uses only variables with values already fixed.
Now every extension axiom is true, every rule of $\mathcal F$ preserves truth, so every line is true, and in particular $\tau$ is true.
Since $\tau$ contains no extension variable, $\tau$ is true under every assignment to its own variables, and so it is a tautology.

### Where EF stands

$\mathrm{EF}$ p-simulates every Frege system, since a Frege proof is an EF-proof with no extension axioms.
An extension variable acts as a gate of a Boolean circuit, so EF reasons with circuits while Frege reasons with formulas.
$\mathrm{EF}$ is p-equivalent to substitution Frege $\mathrm{SF}$.
Cook and Reckhow gave polynomial-size EF-proofs of the [[pigeonhole formulas|RJ571F7FF0]] in 1979, and [[Buss's theorem|VRX23FZV21]] later did the same in Frege.
Whether Frege p-simulates $\mathrm{EF}$ is open.

### Lower bounds and logic

No superpolynomial lower bound on EF size is known.
A lower bound for $\mathrm{EF}$ would give one for Frege, so this problem is at least as hard as the [[problem for Frege systems|ANSV13M4FS]].
Krajíček and Pudlák showed in 1998 that $\mathrm{EF}$ has no feasible interpolation if the RSA cryptosystem is secure; see [[feasible interpolation|59GJCM8C66]].
On the logic side, Cook's theory $\mathrm{PV}$ of 1975 corresponds to $\mathrm{EF}$: a universal statement provable in $\mathrm{PV}$ has polynomial-size EF-proofs of its propositional translations, and $\mathrm{PV}$ proves that $\mathrm{EF}$ is sound.
See [[bounded arithmetic|RA380RWEC0]].

### Watch out

Extension adds no new tautologies, only shorter proofs.
A student who sees $q$ in a line may think that $q$ is a free variable of the theorem.
It is not, since $q$ is a local name, and it must be gone by the last line.
The count of lines can also mislead: an EF-proof with few lines may still need long extension axioms, so the measure is size.

### History

Tseitin introduced the extension rule in 1968, for resolution.
Cook and Reckhow defined extended Frege systems in 1979.

### Try it

First, is $q \leftrightarrow (q \land a)$ an extension axiom?
No, because $q$ occurs in its own defining formula.

Second, how many symbols do the extension axioms for the carries $q_1, \dots, q_4$ use?
The first has $5$ symbols and each of the other three has $13$, so they use $5 + 3 \cdot 13 = 44$ symbols.

## Explanations

### L1 human

In a long argument, mathematicians give short names to long expressions.
Extended Frege allows exactly this: "let $q$ stand for $\varphi$".
After the definition, the proof writes $q$ in place of $\varphi$.
If $\varphi$ has $1000$ symbols and appears in $50$ lines, the name saves almost $50000$ symbols.

### L2 human

We check soundness on a short proof.
Line 1 is the extension axiom $q \leftrightarrow (a \land b)$, and a later line $q \to a$ follows from it by Frege rules.
Take the assignment $a = 1$, $b = 0$, and extend it by $q = a \land b = 0$.
Then line 1 is true, so every derived line is true, and $q \to a$ is true, since $q = 0$.
The typical use of $\mathrm{EF}$ is as the propositional counterpart of polynomial-time reasoning: an argument about a polynomial-time algorithm names each intermediate value once, as extension variables do.

### L3 human

$\mathrm{EF}$ is the proof system of polynomial-time reasoning.
Its lines are in effect circuits, as Frege lines are formulas and resolution lines are clauses.
So results on $\mathrm{EF}$ and on $\mathrm{PV}$ are often proved together: a $\mathrm{PV}$-proof of a universal statement gives short EF-proofs of its translations, by the correspondence of [[bounded arithmetic|RA380RWEC0]].
In the other direction, a superpolynomial EF lower bound for the translations of a true universal statement would show that $\mathrm{PV}$ does not prove that statement.
