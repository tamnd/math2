---
tag: 4PZM5GJTR5
kind: statement
role: theorem
name: Gödel's second incompleteness theorem
aliases: [second-incompleteness-theorem]
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: grad
uses: [MPSCREYC3M, 92SWXST1ZM, VM8TQ70CVJ, NB2BCZR40F, 4NBAX3VRQ7, F6H4STF9RG, 3PRW76471J, X9WYNYE29C]
about: [VM8TQ70CVJ, 4NBAX3VRQ7]
history:
  first_stated: "Gödel, 1931, Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I"
  notes: "Gödel gave only an outline of the proof. The first full published proof is in the second volume of Hilbert and Bernays, Grundlagen der Mathematik, 1939."
sources:
  - url: https://en.wikipedia.org/wiki/Gödel's_incompleteness_theorems
    locator: Second incompleteness theorem
  - book: isbn:9780521857840
  - book: isbn:9780521701464
  - url: https://builds.openlogicproject.org/
    locator: "Part: Incompleteness"
---

## Statement

The second theorem says that $\mathsf{PA}$ cannot prove the sentence "no number codes a $\mathsf{PA}$-proof of $0 = 1$".
The same holds for every consistent theory with computable axioms that contains $\mathsf{PA}$: it cannot prove the sentence that expresses its own consistency.

Let $T$ be a [[first-order theory|92SWXST1ZM]] in the language $\{0, S, +, \cdot\}$ that contains [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$.
Let the axioms of $T$ be defined by a $\Sigma_1$ formula $\alpha(x)$ that defines a decidable set of sentences in $\mathbb{N}$.
Let $\mathrm{Prov}_T$ be the standard [[provability predicate|NB2BCZR40F]] built from $\alpha$, and let the [[consistency statement|4NBAX3VRQ7]] of $T$ be
$$\mathrm{Con}(T) := \neg \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner).$$

**Theorem (Gödel).**

1. If $T$ is [[consistent|VM8TQ70CVJ]], then $T \nvdash \mathrm{Con}(T)$.
2. $T \vdash \mathrm{Con}(T) \leftrightarrow G_T$, where $G_T$ is the Gödel sentence of [[the first incompleteness theorem|X9WYNYE29C]].
3. Formalized form: $T \vdash \mathrm{Con}(T) \to \neg \mathrm{Prov}_T(\ulcorner \mathrm{Con}(T) \urcorner)$.

The [[proof of the second incompleteness theorem|4S9W7VVKT9]] derives all three parts from the [[derivability conditions|F6H4STF9RG]].

## Remarks

### One sentence about numbers

Code every finite string of symbols by a number, as in [[Gödel numbering|MFJXPAF0R0]].
Then "$\mathsf{PA}$ never proves $0 = 1$" becomes a claim about numbers: no number is the code of a $\mathsf{PA}$-proof whose last line is $0 = S0$.
Each single number can be checked by a finite computation, and $\mathsf{PA}$ proves the result of each check.
The second theorem says that $\mathsf{PA}$ cannot prove the claim for all numbers at once.
The claim is a $\Pi_1$ sentence, and it is true, as [[the example on Con(PA)|23M4TSTPN8]] shows.

### Why the theorem holds

The first theorem gives a sentence $G$ that says "$G$ is not provable", and it shows: if $T$ is consistent, then $T \nvdash G$.
That argument is elementary, so $T$ can carry it out about itself.
The result is $T \vdash \mathrm{Con}(T) \to G$.
Now a proof of $\mathrm{Con}(T)$ in $T$ would give a proof of $G$ in $T$, and the first theorem forbids that.
The derivability conditions are exactly what makes "$T$ can carry out the argument" precise.

### Why each hypothesis is needed

Consistency is needed because an inconsistent theory proves every sentence, $\mathrm{Con}(T)$ included.

The provability predicate must satisfy the derivability conditions.
The [[Rosser provability predicate|Z0H1KA8ZHT]] defines the same set of theorems in $\mathbb{N}$ when $T$ is consistent, yet $T$ proves the consistency statement built from it.

The axiom formula matters too.
Feferman built a $\Pi_1$ formula $\alpha^*$ that defines exactly the axioms of $\mathsf{PA}$ in $\mathbb{N}$, and $\mathsf{PA}$ proves the consistency statement built from $\alpha^*$.
So the theorem is about a formula that presents the axioms, not only about a set of axioms.

"Contains $\mathsf{PA}$" can be weakened, because the proof needs only D2 and D3 inside $T$.
These hold in every extension of $\mathsf{I}\Sigma_1$, the [[fragment of Peano arithmetic|T70PYM1F36]] with induction for $\Sigma_1$ formulas.

Computable axioms are needed for $\mathrm{Con}(T)$ to be defined at all.
[[True arithmetic|DX0KPMH4QZ]] is consistent, but its set of axioms has no $\Sigma_1$ definition, and no arithmetic definition at all.

### What it gives you

If $T$ is consistent, then $\mathrm{Con}(T)$ is a true $\Pi_1$ sentence that $T$ does not prove.
So $T + \neg \mathrm{Con}(T)$ is consistent, and for $\mathsf{PA}$ this theory is [[consistent but ω-inconsistent|FK06QR6A44]].
A proof of $\mathrm{Con}(\mathsf{PA})$ must use means that go beyond $\mathsf{PA}$.
[[Gentzen's consistency proof|QPV0HNP22S]] uses primitive recursive arithmetic with induction along the ordinal $\varepsilon_0$, and $\mathsf{PA}$ does not prove that induction.
In the same way, if $\mathsf{ZFC}$ is consistent, it does not prove $\mathrm{Con}(\mathsf{ZFC})$, so it does not prove that a set model of $\mathsf{ZFC}$ exists.

[[Hilbert's program|P1RW6JWX73]] asked for a finitary proof of the consistency of mathematics.
If the finitary methods can be formalized inside $\mathsf{PA}$, the theorem rules out such a proof of $\mathrm{Con}(\mathsf{PA})$.

### The converse and a false converse

The converse of part 1 holds: if $T \nvdash \mathrm{Con}(T)$, then $T$ is consistent, because an inconsistent theory proves every sentence.
Another converse fails.
A theory that proves $\neg \mathrm{Con}(T)$ need not be inconsistent, and $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is the standard example.

### Generalizations

The theorem holds in every language for a consistent theory that interprets $\mathsf{I}\Sigma_1$ and has a $\Sigma_1$ axiom formula, for example $\mathsf{ZFC}$.
[[Löb's theorem|3HD30YG3DG]] contains it as a special case.
If $T \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \varphi$, then $T \vdash \varphi$, and the case $\varphi := (0 = S0)$ is the second theorem.
Below $\mathsf{I}\Sigma_1$ the picture changes: Willard's [[self-verifying theories|D8SGFVA3RT]] are weak theories that prove a form of their own consistency.

### Watch out

Do not read the theorem as "$\mathrm{Con}(T)$ is doubtful".
The sentence $\mathrm{Con}(\mathsf{PA})$ is true, and [[ZFC proves it|1KSQAD4BWM]].
What fails is a proof inside $\mathsf{PA}$ itself.
Do not drop the words "built from $\alpha$" either.
For the Rosser predicate or for Feferman's $\alpha^*$, a consistency statement is provable, so the claim "no consistent $T$ proves any sentence that says $T$ is consistent" is false as stated.

### Try it

Does $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ prove its own consistency statement?
No, if it is consistent: it is a theory with a $\Sigma_1$ axiom formula that contains $\mathsf{PA}$, so the theorem applies to it.

Is $\mathrm{Con}(T)$ provable in $T + \mathrm{Con}(T)$?
Yes, as an axiom, and this does not contradict the theorem, because $T + \mathrm{Con}(T)$ is a different theory with its own consistency statement.

## History

Gödel stated the second theorem in his 1931 paper "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I", and gave only an outline of the proof.
The first full published proof is in the second volume of Hilbert and Bernays, Grundlagen der Mathematik, in 1939.
Their proof isolated conditions on the provability predicate, and Löb gave these derivability conditions their present short form in 1955.
Feferman showed in 1960, in "Arithmetization of metamathematics in a general setting", that the theorem depends on the formula that presents the axioms.

## Explanations

### L1 human

Suppose a computer can check proofs from a list of axioms for arithmetic, and the axioms never lead to a contradiction.
The statement "these axioms never prove $0 = 1$" can be written as a statement about whole numbers.
Gödel showed that the axioms cannot prove that statement.
So if you want to trust the axioms, the reasons must come from outside them, for example from a stronger theory.

### L2 human

We follow the argument for $T = \mathsf{PA}$ and its Gödel sentence $G$, with $\mathsf{PA} \vdash G \leftrightarrow \neg \mathrm{Prov}(\ulcorner G \urcorner)$.
The first theorem gives the implication "if $\mathsf{PA}$ is consistent, then $\mathsf{PA} \nvdash G$".
Its proof uses only coding and finite checks, and the derivability conditions let $\mathsf{PA}$ repeat it, so
$$\mathsf{PA} \vdash \mathrm{Con}(\mathsf{PA}) \to \neg \mathrm{Prov}(\ulcorner G \urcorner).$$
The right side is equivalent to $G$, so $\mathsf{PA} \vdash \mathrm{Con}(\mathsf{PA}) \to G$.
If $\mathsf{PA}$ proved $\mathrm{Con}(\mathsf{PA})$, it would prove $G$, which the first theorem forbids.
The typical use is to show that a statement which implies $\mathrm{Con}(T)$ is not provable in $T$.
For example, $\mathsf{ZFC}$ proves that a set model of $\mathsf{ZFC}$ gives $\mathrm{Con}(\mathsf{ZFC})$, so a consistent $\mathsf{ZFC}$ cannot prove that such a model exists.

### L3 human

In [[provability logic|WJK0YA4GP2]] the formalized form is the formula $\neg \square \bot \to \neg \square \neg \square \bot$, a theorem of the modal logic $\mathsf{GL}$.
Unlike the first theorem, which is about the set of theorems, the second theorem is intensional: it depends on how the axioms are presented.
Consistency statements order theories by strength, and [[Gentzen's consistency proof|QPV0HNP22S]] started ordinal analysis, which measures that strength by ordinals.
The [[reflection principles|NB485KFXKV]] and the [[Turing and Feferman progressions|F7Z4BV2KHD]] build on the second theorem by adding consistency statements again and again.
