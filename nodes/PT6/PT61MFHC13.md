---
tag: PT61MFHC13
kind: concept
name: Significance of the incompleteness theorems
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: grad
uses: [X9WYNYE29C, 4PZM5GJTR5, DH9RQ61GVD, 4NBAX3VRQ7, 3K1AKGXF8A, MPSCREYC3M, 69TTX21TRJ, YRV6SYK2BY, P1RW6JWX73, QPV0HNP22S]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Discussion and implications
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Examples of undecidable statements
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Minds and machines
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Appeals to the incompleteness theorems in other fields
---

## Summary

The [[first incompleteness theorem|X9WYNYE29C]], in Rosser's form, says exactly this.
If $T$ is a consistent theory with a decidable set of axioms that contains [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$, then some sentence $\varphi$ of its language has $T \nvdash \varphi$ and $T \nvdash \neg \varphi$.
A typical misquote is "Gödel proved that there are mathematical truths that can never be proved".

The theorem does not say that.
It does not say that mathematics is incomplete, and it does not say that some truths are unknowable.
It says that each single theory of this kind misses some sentence, and a stronger theory can prove the missed sentence.
The [[second incompleteness theorem|4PZM5GJTR5]] says that such a theory, if it also has enough induction (for example $T \supseteq \mathsf{PA}$), does not prove its own [[consistency statement|4NBAX3VRQ7]] $\mathrm{Con}(T)$.
Both theorems limit what one effectively given theory can prove, and both have exact hypotheses that their popular versions leave out.

## Motivation

The theorems are among the most quoted results of mathematics outside mathematics, and many of these quotations are wrong.
A correct reading needs the exact hypotheses: consistency, a decidable or computably enumerable set of axioms, and enough arithmetic.
It also needs the exact conclusion: unprovability in one fixed theory, not unprovability in every theory, and not falsehood.
Inside mathematics, the theorems answered a central question of [[Hilbert's program|P1RW6JWX73]] and started the study of independence in arithmetic.

## Notation

We write $T \vdash \varphi$ when $\varphi$ is provable in the formal theory $T$, and "true" means true in the standard model $\mathbb{N}$.
A Gödel sentence of $T$ is a sentence $G_T$ with $T \vdash G_T \leftrightarrow \neg \mathrm{Prov}_T(\ulcorner G_T \urcorner)$; it is equivalent to a $\Pi_1$ sentence.
$\mathrm{Th}(\mathbb{N})$ is the set of all sentences of arithmetic that are true in $\mathbb{N}$.

## Remarks

### Consistency proofs and Hilbert's program

$\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$, and $\mathsf{ZFC} \nvdash \mathrm{Con}(\mathsf{ZFC})$ if $\mathsf{ZFC}$ is consistent.
So a consistency proof for $\mathsf{PA}$ must use some principle that $\mathsf{PA}$ does not prove.
Hilbert's program in its original form asked for a finitary consistency proof for all of mathematics.
If finitary reasoning can be formalized in $\mathsf{PA}$, the second theorem shows that this cannot succeed.

[[Gentzen's consistency proof|QPV0HNP22S]] proves $\mathrm{Con}(\mathsf{PA})$ in a weak theory together with transfinite induction up to the ordinal $\varepsilon_0$.
This does not contradict the second theorem, because that induction is not provable in $\mathsf{PA}$.

### Independence in ordinary mathematics

The Gödel sentence has no mathematical content beyond its self-reference, but later work found natural independent statements.
The [[Paris-Harrington theorem|509ZWA0R26]] (1977) gives a true strengthening of the finite Ramsey theorem that $\mathsf{PA}$ does not prove.
[[Goodstein's theorem|XQMNJF241J]] is true and not provable in $\mathsf{PA}$, by Kirby and Paris (1982).
Friedman showed that [[Kruskal's tree theorem|XVHKCX4F5Y]] is not provable in the system $\mathsf{ATR}_0$ of second-order arithmetic.
Their unprovability is shown by models of arithmetic and by ordinal analysis, not by self-reference.

The theorems also produce concrete unprovable statements.
By the solution of [[Hilbert's tenth problem|X8TVJSVTD4]], each consistent theory with a decidable set of axioms that contains $\mathsf{Q}$ misses some true statement "this polynomial equation has no solution in natural numbers".
Chaitin showed that each such theory has a number $c$ such that it proves no sentence "the [[Kolmogorov complexity|8PY3K6NCKF]] of $s$ is greater than $c$", although such sentences are true for all but finitely many strings $s$.

### Misreadings about truth

The claim "some truths of arithmetic can never be proved" is false as a reading of the theorems.
Each fixed theory $T$ misses some truths, but each truth is provable in some consistent theory.
For $T \supseteq \mathsf{PA}$, the Gödel sentence $G_T$ is provable in $T + \mathrm{Con}(T)$, because $T \vdash \mathrm{Con}(T) \to G_T$.
In general a true sentence $\varphi$ is provable in $\mathsf{PA} + \varphi$, which is consistent because its axioms are true.

The claim "arithmetic is incomplete" confuses a theory with the truth.
The theory $\mathrm{Th}(\mathbb{N})$ is complete and consistent; it has no decidable set of axioms, so the theorems do not apply to it, as shown in [[true arithmetic has no decidable axiom set|69TTX21TRJ]].

The claim "mathematics might be inconsistent, and Gödel showed we cannot know" is also wrong.
The second theorem says that $T$ cannot prove $\mathrm{Con}(T)$, not that $T$ might be inconsistent, and other theories can prove $\mathrm{Con}(T)$.
A proof of $\mathrm{Con}(T)$ inside $T$ would give no extra confidence anyway, because an inconsistent $T$ proves everything.

### Misreadings about other systems

The theorems need enough arithmetic.
[[Presburger arithmetic|4W0E9G7PPV]], the theory of [[real closed fields|DDY3Q3PJ6W]] and [[Tarski's axioms|14DWEDXWCC]] for elementary geometry are complete and decidable theories with effective axioms.

The [[continuum hypothesis|0MN2MER9WN]] is independent of [[ZFC|0HE5WDQ9FJ]] by the work of Gödel and Cohen, who built models of $\mathsf{ZFC}$ in which it holds and in which it fails.
This is a different phenomenon: it is not a Gödel sentence, and its independence is not proved by self-reference.

Claims that the theorems apply to legal systems, theologies, physical theories or any system of thought use them where a formal theory, effective axioms and enough arithmetic have no clear meaning.
Torkel Franzén's book "Gödel's Theorem: An Incomplete Guide to Its Use and Abuse" (2005) discusses many such claims.
Lucas and Penrose argued from the theorems that human mathematical understanding is not mechanical.
These arguments are disputed, and they depend on assumptions about minds that the theorems do not supply.

### The rules you can use

The theorems are about provability in a fixed formal theory: if $T$ is consistent, $G_T$ is unprovable in $T$, and if $T$ is also sound, $G_T$ is true.
The hypotheses cannot be dropped.
Without effective axioms, $\mathrm{Th}(\mathbb{N})$ is complete; without enough arithmetic, there are complete decidable theories; without consistency, $T$ proves everything.
The theorems apply again to every consistent effective extension of $T$, such as $T + G_T$ or $T + \mathrm{Con}(T)$.
The first theorem is the arithmetic shadow of [[Tarski's undefinability theorem|YRV6SYK2BY]]: provability in $T$ is definable in arithmetic and truth is not, so the two differ.
The second theorem depends on how consistency is expressed.
With the standard provability predicate it holds, but Feferman (1960) showed that other formulas for the same axioms give consistency statements that the theory does prove.

### History

Gödel published both theorems in 1931, in "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I".
His first theorem assumed $\omega$-consistency, and Rosser (1936) reduced this hypothesis to consistency.
Hilbert and Bernays (1939) isolated the derivability conditions behind the second theorem, and Löb (1955) refined them.
Gentzen published his consistency proof for $\mathsf{PA}$ in 1936.
Lucas published "Minds, Machines and Gödel" in 1961, and Penrose took up the argument in "The Emperor's New Mind" (1989).
The Paris-Harrington theorem (1977) was the first widely accepted natural combinatorial statement independent of $\mathsf{PA}$.

### Watch out

Do not forget the hypothesis of effective axioms.
Every consistent theory has a complete consistent extension, by Lindenbaum's lemma, and the theorems say only that such an extension has no decidable set of axioms.
Do not read "unprovable in $T$" as "false" or as "unprovable".
Do not mix up incompleteness of a theory with Gödel's completeness theorem, which says that first-order logic proves every sentence true in all models.

### Try it

Is "there is a true sentence that $\mathsf{PA}$ does not prove" a correct use?
Yes: $G_{\mathsf{PA}}$ is one, and Goodstein's theorem is another.

Is "the theory of real closed fields is incomplete, by Gödel" a correct use?
No: the natural numbers are not definable in it, so it does not contain $\mathsf{Q}$ in the required sense, and it is complete.

Is "$\mathsf{PA}$ cannot be proved consistent" a correct use?
No: Gentzen proved it with transfinite induction up to $\varepsilon_0$; only a proof inside $\mathsf{PA}$ is excluded.

## Explanations

### L1 human

Gödel proved two theorems about lists of axioms for arithmetic that a computer can check.
The first says that such a list, if it has no contradiction, leaves some statement neither proved nor disproved.
The second says that such a list cannot prove its own freedom from contradiction.
These theorems are often quoted to say that "some truths can never be known" or "every system is incomplete", and those quotations are wrong.
Each statement missed by one list can be proved by a bigger list, and some useful theories, such as the theory of real numbers with addition and multiplication, are complete.
Some natural statements about numbers, for example Goodstein's theorem about a sequence that grows and then falls to zero, are not provable from the usual axioms of arithmetic.

### L2 human

Test the claim "there is a true sentence that no theory proves" against the exact first theorem for $T = \mathsf{PA}$.
The theorem gives a sentence $G_{\mathsf{PA}}$ that $\mathsf{PA}$ does not prove.
Since $\mathsf{PA}$ is sound, $G_{\mathsf{PA}}$ is true.
But $\mathsf{PA} \vdash \mathrm{Con}(\mathsf{PA}) \to G_{\mathsf{PA}}$, so $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ proves it.
So the claim does not follow from the theorem.
The typical use of the theorems in a discussion is to check each claim that cites Gödel against the three hypotheses and the exact conclusion.
Watch out: the first theorem needs a decidable set of axioms, and the set of all true sentences is complete exactly because it has none.

### L3 human

For mathematical logic the theorems opened several programs.
Proof theory measures theories by their consistency strength and their provable ordinals, and reverse mathematics locates theorems on a scale of subsystems of second-order arithmetic.
The second theorem makes consistency strength a measure of theories: $U$ is stronger than $T$ when $U$ proves $\mathrm{Con}(T)$.
In practice natural theories, including the extensions of set theory by large cardinal axioms, are ordered by this measure.
In philosophy, the theorems bear on formalism, on the question whether mathematical truth exceeds provability in any fixed system, and on the minds and machines debate.
These discussions use the theorems as premises together with further assumptions that the theorems do not supply.
