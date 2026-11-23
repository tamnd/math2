---
tag: X3XGDVSANT
kind: proof
name: Proof of isomorphism invariance of truth by induction
msc: ["03C07"]
topics: [NJDME6F845]
audience: ug2
proves: NDTJ2E895C
uses: [1WTCZB4DVB, YWTERZZME5, 0GG9TVW90M, 0THBK9V825]
methods: [12MQ2NJ29A]
sources:
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Theories and Their Models
---

## Proof

We push each assignment $s$ in $\mathcal{M}$ along $h$ to the assignment $h \circ s$ in $\mathcal{N}$, and we follow the clauses of [[satisfaction|1WTCZB4DVB]] by induction.
Throughout, $h \colon M \to N$ is an [[isomorphism|YWTERZZME5]] from $\mathcal{M}$ to $\mathcal{N}$.

Part 1, by [[structural induction|12MQ2NJ29A]] on the term $t$, for every assignment $s$.

1. If $t$ is a variable $x$, then $h(t^{\mathcal{M}}[s]) = h(s(x)) = (h \circ s)(x) = t^{\mathcal{N}}[h \circ s]$, by the definition of composition.
2. If $t$ is a constant symbol $c$, then $h(c^{\mathcal{M}}) = c^{\mathcal{N}}$, because $h$ preserves constants.
3. Let $t = f(t_1, \ldots, t_n)$ and $a_i = t_i^{\mathcal{M}}[s]$.
   By the induction hypothesis, $h(a_i) = t_i^{\mathcal{N}}[h \circ s]$ for each $i$.
4. Since $h$ preserves $f$, we get $h(t^{\mathcal{M}}[s]) = h(f^{\mathcal{M}}(a_1, \ldots, a_n)) = f^{\mathcal{N}}(h(a_1), \ldots, h(a_n))$.
5. By step 3, the right side equals $f^{\mathcal{N}}(t_1^{\mathcal{N}}[h \circ s], \ldots, t_n^{\mathcal{N}}[h \circ s])$, which is $t^{\mathcal{N}}[h \circ s]$.

Part 2, by induction on $\varphi$.
The claim for $\varphi$ is that $\mathcal{M} \models \varphi[s]$ if and only if $\mathcal{N} \models \varphi[h \circ s]$, for every assignment $s$ in $\mathcal{M}$.

6. Let $\varphi = R(t_1, \ldots, t_n)$ and $a_i = t_i^{\mathcal{M}}[s]$.
   Then $\mathcal{M} \models \varphi[s]$ means $(a_1, \ldots, a_n) \in R^{\mathcal{M}}$.
7. Since $h$ preserves and reflects $R$, this holds if and only if $(h(a_1), \ldots, h(a_n)) \in R^{\mathcal{N}}$.
8. By part 1, $h(a_i) = t_i^{\mathcal{N}}[h \circ s]$, so the last condition says $\mathcal{N} \models \varphi[h \circ s]$.
9. Let $\varphi$ be $t_1 = t_2$.
   Then $\mathcal{M} \models \varphi[s]$ means $t_1^{\mathcal{M}}[s] = t_2^{\mathcal{M}}[s]$.
10. Since $h$ is injective, this holds if and only if $h(t_1^{\mathcal{M}}[s]) = h(t_2^{\mathcal{M}}[s])$.
11. By part 1, this says $t_1^{\mathcal{N}}[h \circ s] = t_2^{\mathcal{N}}[h \circ s]$, that is, $\mathcal{N} \models \varphi[h \circ s]$.
12. For $\neg \psi$ and $\psi \mathbin{\square} \chi$, the induction hypothesis gives the parts the same truth values under $s$ in $\mathcal{M}$ and under $h \circ s$ in $\mathcal{N}$.
    The clause for the connective then gives the claim.
13. Let $\varphi = \forall x \, \psi$, and let $a \in M$.
    The assignments $h \circ (s[x \mapsto a])$ and $(h \circ s)[x \mapsto h(a)]$ are equal, because both send $x$ to $h(a)$ and each $y \neq x$ to $h(s(y))$.
14. So the induction hypothesis for $\psi$ gives $\mathcal{M} \models \psi[s[x \mapsto a]]$ if and only if $\mathcal{N} \models \psi[(h \circ s)[x \mapsto h(a)]]$.
15. Suppose $\mathcal{M} \models \varphi[s]$, and let $b \in N$.
    Since $h$ is surjective, $b = h(a)$ for some $a \in M$.
16. By the clause for $\forall$, $\mathcal{M} \models \psi[s[x \mapsto a]]$, and step 14 gives $\mathcal{N} \models \psi[(h \circ s)[x \mapsto b]]$.
17. Since $b \in N$ was arbitrary, $\mathcal{N} \models \varphi[h \circ s]$.
18. Conversely, suppose $\mathcal{N} \models \varphi[h \circ s]$, and let $a \in M$.
    Then $(h \circ s)[x \mapsto h(a)]$ satisfies $\psi$, so step 14 gives $\mathcal{M} \models \psi[s[x \mapsto a]]$, and hence $\mathcal{M} \models \varphi[s]$.
19. Let $\varphi = \exists x \, \psi$.
    If $a \in M$ is a witness for $\mathcal{M} \models \varphi[s]$, then $h(a)$ is a witness for $\mathcal{N} \models \varphi[h \circ s]$, by step 14.
20. If $b \in N$ is a witness for $\mathcal{N} \models \varphi[h \circ s]$, write $b = h(a)$ by surjectivity.
    Then $a$ is a witness for $\mathcal{M} \models \varphi[s]$, by step 14.

Part 3.

21. Let $\sigma$ be a sentence and $s$ any assignment in $\mathcal{M}$.
    By part 2, $\mathcal{M} \models \sigma[s]$ if and only if $\mathcal{N} \models \sigma[h \circ s]$.
22. By the [[coincidence lemma|FM580NZ9W6]], a sentence is true in a structure exactly when one assignment satisfies it, since domains are nonempty and all assignments agree on a sentence.
    So $\mathcal{M} \models \sigma$ if and only if $\mathcal{N} \models \sigma$.

This proves the lemma.

## Idea

The isomorphism carries every assignment in $\mathcal{M}$ to an assignment in $\mathcal{N}$, and the proof follows the recursion of satisfaction.
Preservation of the symbols handles terms and atomic formulas, and injectivity handles equality.
Surjectivity handles the quantifiers, because every element of $\mathcal{N}$ is the image of an element of $\mathcal{M}$, so a search through $N$ is the image of a search through $M$.

## Variants

One can prove only the direction "$\mathcal{M} \models \varphi[s]$ implies $\mathcal{N} \models \varphi[h \circ s]$", with the induction hypothesis stated for all isomorphisms at once.
The case of $\neg$ then uses the hypothesis for the inverse isomorphism $h^{-1}$, and the other direction of the lemma follows in the same way.
