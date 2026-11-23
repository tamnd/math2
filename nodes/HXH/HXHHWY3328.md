---
tag: HXHHWY3328
kind: topic
name: Gödel's incompleteness theorems and related limits
msc: ["03F40"]
topics: [DYJ0KGTPMR]
---

## Summary

Take the liar sentence "this sentence is false" and replace "false" by "not provable in $\mathsf{PA}$".
The result is no longer a paradox.
If $\mathsf{PA}$ is consistent, the sentence cannot be proved, and so what it says is true.
Gödel showed in 1931 that this sentence can be written in the language of arithmetic, and the theory of these limits on formal proof is a part of [[mathematical logic|DYJ0KGTPMR]].

The first step is to code formulas and proofs by numbers.
Checking a proof is then a computation on numbers, and arithmetic can express "$y$ codes a proof of the formula with code $x$".
The diagonal lemma then gives, for every property that arithmetic can express, a sentence that says of itself that it has the property.

Applied to "not provable", the lemma gives the first incompleteness theorem.
A consistent, computably axiomatized theory that contains Robinson arithmetic leaves a true $\Pi_1$ sentence unproved, and Rosser showed in 1936 that it leaves some sentence undecided.
Formalizing that argument inside the theory gives the second theorem, that the theory does not prove its own consistency.
Applied to "not true", the lemma gives Tarski's theorem that arithmetical truth is not definable in arithmetic.
Applied to "if I am provable, then $0 = 1$", it gives Löb's theorem.

The later results measure what adding consistency and soundness statements achieves: reflection principles, ordinal progressions of theories, and shorter proofs in stronger theories.
The theorems are about formal theories, one at a time, and the last entry discusses what they do not show.

## Remarks

### Reading order

1. [[Gödel numbering|MFJXPAF0R0]]: turn symbols, formulas and proofs into numbers.
2. [[Arithmetization of syntax|6M12VR1GT6]]: check syntax by computations that $\mathsf{Q}$ proves.
3. [[Provability predicate|NB2BCZR40F]]: write "$x$ is provable in $T$" as the $\Sigma_1$ formula $\mathrm{Prov}_T(x)$.
4. [[Derivability conditions|F6H4STF9RG]]: learn what the second theorem needs from $\mathrm{Prov}_T$.
5. [[Diagonal lemma|3PRW76471J]]: build sentences that talk about themselves.
6. [[ω-consistency|4S29X1GTV4]]: see the hypothesis of Gödel's original proof.
7. [[Gödel's first incompleteness theorem|X9WYNYE29C]]: see why the Gödel sentence is undecided.
8. [[Rosser's theorem|DH9RQ61GVD]]: get incompleteness from consistency alone.
9. [[Negation completeness|319P85G2C1]]: learn the property that the first theorem refutes.
10. [[Gödel's second incompleteness theorem|4PZM5GJTR5]]: see why $T$ does not prove its own consistency statement.
11. [[Consistency statement|4NBAX3VRQ7]]: see how $\mathrm{Con}(T)$ depends on its formula.
12. [[Tarski's undefinability theorem|YRV6SYK2BY]]: see why arithmetic cannot define its own truth.
13. [[Partial truth predicates|Y2MF1EZAM7]]: define truth for $\Sigma_n$ sentences, one level at a time.
14. [[Löb's theorem|3HD30YG3DG]]: learn when $T$ proves $\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \varphi$.
15. [[Henkin sentence|SBMQ5QHG9W]]: see why a sentence that says it is provable is provable.
16. [[Reflection principles|NB485KFXKV]]: strengthen $\mathrm{Con}(T)$ to soundness schemes.
17. [[Turing and Feferman progressions|F7Z4BV2KHD]]: iterate consistency and reflection along ordinal notations.
18. [[Gödel's speed-up theorem|37X5XBDBNX]]: see how stronger theories shorten proofs.
19. [[Self-verifying theories|D8SGFVA3RT]]: meet weak theories that prove a form of their own consistency.
20. [[Significance of the incompleteness theorems|PT61MFHC13]]: separate what the theorems prove from misreadings.

### Prerequisites

- [[First-order languages and syntax|PSRDJXRW53]]: terms, formulas, sentences and proofs.
- [[Gödel's completeness theorem|WQ1ZE255SF]]: a sentence is provable exactly when it is true in all models.
- [[Formal arithmetic and its fragments|QHCRN4JVG0]]: [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$ and Peano arithmetic.
- [[Computably enumerable sets|TN9G24VABN]] and the [[undecidability of the halting problem|Z7TN2B35B0]].

### History

Gödel announced the first theorem in Königsberg in 1930 and published both theorems in 1931, in "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I".
Tarski's theorem on truth appeared in Polish in 1933 and in German in 1936.
Rosser removed the hypothesis of $\omega$-consistency in 1936.
Hilbert and Bernays gave the first full proof of the second theorem in 1939, and Löb stated the derivability conditions in their usual form in 1955, together with his theorem.
Feferman showed in 1960 how consistency statements depend on the formula that presents the axioms.
