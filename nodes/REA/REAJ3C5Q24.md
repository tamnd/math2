---
tag: REAJ3C5Q24
kind: proof
name: Proof of Łoś's theorem by induction on formulas
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: ug2
proves: AGYBSTD7BG
uses: [AX9Q86GB8M, VFPGADHJYA, J64Y3JC0RE, HYJ10AF6RT, 6D3WA7N2W4, 0HTGB13FE2]
methods: [12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Łoś's theorem
  - book: isbn:9780387987606
---

## Proof

Write $\mathcal{M} = \prod_{i \in I} \mathcal{M}_i / \mathcal{U}$ and $[\![ \varphi(a) ]\!] = \set{i \in I : \mathcal{M}_i \models \varphi(a(i))}$ for a tuple $a = (a_1, \dots, a_n)$ of elements of $\prod_{i \in I} M_i$.
Every formula is equivalent to one built from atomic formulas with $\neg$, $\land$ and $\exists$, so we treat only these cases.
We prove by [[structural induction|12MQ2NJ29A]] on $\varphi$ the claim: for every tuple $a$, $\mathcal{M} \models \varphi([a])$ if and only if $[\![ \varphi(a) ]\!] \in \mathcal{U}$.

1. *Terms.* For a [[term|6D3WA7N2W4]] $t$, the value $t^{\mathcal{M}}([a])$ is the class of $i \mapsto t^{\mathcal{M}_i}(a(i))$. This follows by induction on $t$ from clauses 1 and 3 of the [[definition|VFPGADHJYA]].
2. *Equations.* By step 1, $t_1([a]) = t_2([a])$ holds in $\mathcal{M}$ exactly when the two functions agree on a set in $\mathcal{U}$, that is, when $[\![ t_1(a) = t_2(a) ]\!] \in \mathcal{U}$.
3. *Relations.* By step 1 and clause 2 of the definition, $R(t_1, \dots, t_k)$ holds in $\mathcal{M}$ at $[a]$ exactly when its truth set lies in $\mathcal{U}$.
4. *Negation.* $[\![ \neg\varphi(a) ]\!] = I \setminus [\![ \varphi(a) ]\!]$. An [[ultrafilter|J64Y3JC0RE]] contains exactly one of a set and its complement.
5. So $[\![ \neg\varphi(a) ]\!] \in \mathcal{U}$ if and only if $[\![ \varphi(a) ]\!] \notin \mathcal{U}$. By the induction hypothesis, this holds if and only if $\mathcal{M} \not\models \varphi([a])$, that is, $\mathcal{M} \models \neg\varphi([a])$.
6. *Conjunction.* $[\![ (\varphi \land \psi)(a) ]\!] = [\![ \varphi(a) ]\!] \cap [\![ \psi(a) ]\!]$. A filter contains an intersection of two sets if and only if it contains both sets, since it is closed under intersections and supersets.
7. With the induction hypothesis for $\varphi$ and $\psi$, this gives the claim for $\varphi \land \psi$.
8. *Existential quantifier, forward.* Suppose $\mathcal{M} \models \exists y \, \psi([a], y)$. Then $\mathcal{M} \models \psi([a], [b])$ for some $b$, and $[\![ \psi(a, b) ]\!] \in \mathcal{U}$ by the induction hypothesis.
9. Each $i$ in $[\![ \psi(a, b) ]\!]$ lies in $X = [\![ \exists y \, \psi(a, y) ]\!]$, with witness $b(i)$. So $X \in \mathcal{U}$, because $\mathcal{U}$ is closed under supersets.
10. *Existential quantifier, backward.* Suppose $X \in \mathcal{U}$. For $i \in X$ choose $b(i) \in M_i$ with $\mathcal{M}_i \models \psi(a(i), b(i))$, and for $i \notin X$ choose any $b(i) \in M_i$.
11. This choice of one element in each of the nonempty sets uses the [[axiom of choice|0HTGB13FE2]].
12. Then $[\![ \psi(a, b) ]\!] \supseteq X$ lies in $\mathcal{U}$. The induction hypothesis gives $\mathcal{M} \models \psi([a], [b])$, so $\mathcal{M} \models \exists y \, \psi([a], y)$.

Steps 2 to 12 cover every way to build a formula, so the claim holds for every first-order formula.
For a sentence, the tuple $a$ is empty, and the claim is the statement for sentences.

## Idea

Truth in the ultraproduct is computed coordinatewise and then read off along $\mathcal{U}$.
Atomic formulas work by the definition, conjunction by closure under intersection, and negation by the ultrafilter property.
For an existential formula, witnesses in the factors are glued into one witness by the axiom of choice.

## Variants

The same induction with a filter in place of $\mathcal{U}$ fails only at negation, and it shows that [[Horn formulas are preserved by reduced products|FHZPY6GVPG]].
The [[Feferman-Vaught theorem|RYMZZ2AWFT]] gives another route: truth in a reduced product depends on the truth sets through the Boolean algebra $\mathcal{P}(I) / \mathcal{U}$, which is the two-element algebra.
In the Boolean-valued view, the ultraproduct is the quotient of a $\mathcal{P}(I)$-valued structure by the ultrafilter, and Łoś's theorem is the fact that this quotient respects all connectives and quantifiers.
