---
tag: WYFEEA2SV3
kind: proof
name: Proof of Rybakov's theorem from enumerability and a cited lemma
msc: ["03B20", "03B25", "03B55"]
topics: [38EQ20GR7M]
audience: research
proves: GJN7A5DJHK
uses: [C5K35H0R4Y, JNFV2NMNFR, 480TCT5CJ9, TN9G24VABN]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Admissible_rule
    locator: Bases of admissible rules
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 4.2 Admissible rules of intuitionistic logic and arithmetic
---

## Proof

We prove item 1 from [[Iemhoff's theorem|JNFV2NMNFR]], which came later than Rybakov's proof, and item 2 from one cited lemma.
Write $\vdash$ for $\vdash_{\mathsf{IPC}}$, and reduce several premises to one by conjunction.

Part A: decidability.

1. $\mathsf{IPC}$ is decidable, by the finite model property in [[Kripke completeness|480TCT5CJ9]].
2. Fix $A$ and $B$, and let $q_1, \dots, q_m$ be their variables. Only the values $\sigma q_1, \dots, \sigma q_m$ matter, so the relevant substitutions form a [[computably enumerable|TN9G24VABN]] list.
3. $A \mathrel{|\!\sim} B$ fails iff some $\sigma$ in this list has $\vdash \sigma A$ and $\nvdash \sigma B$.
4. By step 1, each test in step 3 is decidable. So the set of non-admissible rules is computably enumerable.
5. By Iemhoff's theorem, $A \mathrel{|\!\sim} B$ iff $A \vdash_V B$. Derivations in $\vdash_V$ use $\mathsf{IPC}$ and substitution instances of the computable family $V_n$.
6. So the set of admissible rules is computably enumerable.
7. A set of rules that is computably enumerable and has a computably enumerable complement is decidable. Run both enumerations until the given rule appears in one of them.

Part B: no finite basis.

8. Lemma C, cited (Rybakov): for each $n$, the admissible rules in at most $n$ variables do not form a basis.
9. Suppose $R$ is a finite basis. Its rules contain at most $n$ variables in total, for some $n$.
10. Each rule of $R$ is admissible and has at most $n$ variables. So the admissible rules in at most $n$ variables generate every rule that $R$ generates.
11. Then the admissible rules in at most $n$ variables form a basis, which contradicts Lemma C.

## Idea

Non-admissibility has a finite witness: a substitution that turns the premise into a theorem and the conclusion into a non-theorem.
Admissibility also has a finite witness once a recursive basis is known: a derivation with the basis rules.
So the two enumerations meet, and the problem is decidable.
For item 2, every finite basis lives in finitely many variables, and Rybakov showed that no such bound is enough.

## Variants

1. Ghilardi's projective approximation gives a direct algorithm: $A \mathrel{|\!\sim} B$ iff $P \vdash B$ for every $P$ in the computable finite set $\Pi(A)$.
2. Rybakov's monograph works through the modal logic $\mathsf{Grz}$. It uses the equivalence of $A \mathrel{|\!\sim}_{\mathsf{IPC}} B$ with $T(A) \mathrel{|\!\sim}_{\mathsf{Grz}} T(B)$, for the Gödel-McKinsey-Tarski translation $T$, and a semantic criterion for admissibility in $\mathsf{Grz}$, both cited here.
