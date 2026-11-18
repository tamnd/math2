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

Let $\mathcal F$ be a [[Frege system|J2BAR09TPF]] whose connectives include $\leftrightarrow$, or in which $\leftrightarrow$ is a fixed abbreviation.

An *extended Frege proof* (EF-proof) of a formula $\tau$ is a finite sequence of formulas $\chi_1, \dots, \chi_m = \tau$.
Each line $\chi_i$ satisfies one of two conditions.

1. $\chi_i$ is the conclusion of an instance of a rule of $\mathcal F$ whose premises are among $\chi_1, \dots, \chi_{i-1}$.
2. $\chi_i$ is an *extension axiom* $q \leftrightarrow \varphi$, where $\varphi$ is a formula and $q$ is a variable with three properties: $q$ does not occur in $\varphi$, $q$ does not occur in $\chi_1, \dots, \chi_{i-1}$, and $q$ does not occur in $\tau$.

The variable $q$ of condition 2 is an *extension variable*, and it names the formula $\varphi$.

The *size* of an EF-proof is the total number of symbols of its lines, and the *number of lines* is $m$.
The extended Frege system $\mathrm{EF}$ is the proof system whose proofs are the EF-proofs, in the sense of a [[propositional proof system|3V24CYWDT6]].

## Notation

The system is written $\mathrm{EF}$ or $e\mathcal F$, and the least size of an EF-proof of $\tau$ is $s_{\mathrm{EF}}(\tau)$.
By the proof of [[Reckhow's theorem|YAHHWZ7XRH]], the choice of $\mathcal F$ changes the sizes by at most a polynomial, so one writes $\mathrm{EF}$ without naming $\mathcal F$.

## Remarks

### Examples

- An [[extension step in a small proof|9CV99XJ8J1]] shows the rule and the conditions on the new variable.
- [[Extension variables for the carries of binary addition|MKDZSQM3KE]] keep every line of constant size, where the unfolded carry formulas have exponential size.

### Non-examples

- [[A self-referential definition $p \leftrightarrow \neg p$|D30HH9YQFM]] is not an extension axiom, because $p$ occurs in its own definition.
- A proof in substitution Frege that uses the substitution rule is not an EF-proof, although the two systems are p-equivalent.

### Basic properties

- *Soundness.* Let $\alpha$ be an assignment to the variables of $\tau$, and give the other variables of the proof any values. Then give each extension variable $q$, in the order of the proof, the value of its $\varphi$, which contains no later extension variable. Then every extension axiom is true, every rule preserves truth, and $\tau$ is true under $\alpha$. So $\tau$ is a tautology.
- *Strength.* $\mathrm{EF}$ p-simulates every Frege system, since a Frege proof is an EF-proof without extension axioms.
- *Circuits.* An extension variable is a gate of a Boolean circuit. So the lines of an EF-proof are in effect circuits, while the lines of a Frege proof are formulas.
- *Substitution Frege.* $\mathrm{EF}$ is p-equivalent to *substitution Frege* $\mathrm{SF}$, the Frege system with the extra rule "from $\varphi$ infer $\varphi\sigma$" for every [[substitution|NCDZ969V7X]] $\sigma$.
- *Pigeonhole.* Cook and Reckhow gave polynomial-size EF-proofs of the [[pigeonhole formulas|RJ571F7FF0]] in 1979. Later Buss gave polynomial-size Frege proofs; see [[Buss's theorem|VRX23FZV21]].
- *Bounded arithmetic.* Cook's theory PV of 1975 corresponds to $\mathrm{EF}$. A universal statement provable in PV has, as a family of propositional translations, polynomial-size EF-proofs. Conversely, PV proves that $\mathrm{EF}$ is sound. The same holds for Buss's theory $S^1_2$. See [[bounded arithmetic|RA380RWEC0]].

### Lower bounds

No superpolynomial lower bound on the size of EF-proofs is known.
This is an open problem, harder than the [[problem for Frege systems|ANSV13M4FS]].
Whether Frege systems p-simulate $\mathrm{EF}$ is also open.
Krajíček and Pudlák showed in 1998 that $\mathrm{EF}$ has no feasible interpolation unless the RSA cryptosystem is insecure; see [[feasible interpolation|59GJCM8C66]].

### History

Tseitin introduced the extension rule in 1968, for resolution.
Cook and Reckhow defined extended Frege systems in 1979 and proved that their sizes do not depend on the Frege system used.

### Common errors

- The defined variable $q$ must be new. If it occurs in $\varphi$, in earlier lines or in $\tau$, the system becomes unsound.
- The final formula $\tau$ must not contain extension variables. They are local names inside the proof.
- Extension does not add new tautologies. It adds only shorter proofs.

## Explanations

### L1 human

In a long proof, mathematicians give names to long expressions.
Extended Frege allows exactly this: "let $q$ stand for $\varphi$".
After the definition, the proof can write $q$ instead of $\varphi$.
For example, if $\varphi$ has $1000$ symbols and appears in $50$ lines, the name saves almost $50000$ symbols.

### L2 human

We check soundness on a two-line proof.

1. Line 1 is $q \leftrightarrow (a \land b)$, an extension axiom with a new variable $q$.
2. Suppose a later line is $q \to a$, derived by the rules from line 1.
3. Take an assignment $a = 1$, $b = 0$. Extend it by $q = a \land b = 0$.
4. Line 1 is true, so every derived line is true, and $q \to a$ is true.

The typical use of $\mathrm{EF}$ is as the propositional counterpart of polynomial-time reasoning.
A trap: an extension variable is not a free variable of the theorem, so it may not occur in the final formula.

### L3 human

$\mathrm{EF}$ is the proof system of polynomial-time reasoning.
Its lines are circuits, as Frege lines are formulas, and the theory PV proves its soundness.
So results on $\mathrm{EF}$ and on PV are often proved together: a PV-proof of a universal statement gives short EF-proofs of its translations, by the correspondence of [[bounded arithmetic|RA380RWEC0]].
