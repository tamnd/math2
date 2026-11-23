---
tag: GE7YFZ7GPX
kind: proof
name: Proof of the prenex normal form theorem
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
proves: ME9J33BFNC
uses: [CS82V969DE, HYJ10AF6RT, 9CNGDRAMGC, NCDZ969V7X, 0JMR2HM2N2, 2RBQPV02AS]
methods: [12MQ2NJ29A, 0ASJVEFA9J, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Prenex_normal_form
    locator: Conversion to prenex form
  - book: isbn:9781482237726
    locator: Chapter 2
---

## Proof

We first list the equivalences that move one quantifier outward, then show that two prenex formulas joined by a connective have a prenex equivalent, and finally prove the theorem by induction on formulas.

All structures have nonempty domains.
We write $\varphi \equiv \chi$ for [[logical equivalence|0JMR2HM2N2]], and $Q^*$ for the dual of a quantifier $Q$, so $\forall^* = \exists$ and $\exists^* = \forall$.
In steps 4 to 7, $Q$ is $\forall$ or $\exists$, and $x \notin \operatorname{FV}(\chi)$.

1. The relation $\equiv$ is an equivalence relation, and it is preserved by $\neg$, by the binary connectives and by $\forall x$ and $\exists x$.
   The reason is that the clauses of [[satisfaction|2RBQPV02AS]] compute the truth of a compound formula from the truth of its parts.
2. If $x \notin \operatorname{FV}(\chi)$, then the truth of $\chi$ under an assignment does not depend on the value given to $x$.
   This is the coincidence lemma of [[structures, satisfaction and truth|NJDME6F845]].
3. If $y$ does not occur in $\varphi$, then $Q x \, \varphi \equiv Q y \, \varphi[y/x]$, and both sides have the free variables $\operatorname{FV}(\varphi) \setminus \{ x \}$.
   The reason is that $y$ is free for $x$ in $\varphi$, so the substitution lemma of the same topic applies.
   The [[substitution|NCDZ969V7X]] changes no quantifier, so it keeps a prenex $\varphi$ prenex.
4. $\neg Q x \, \varphi \equiv Q^* x \, \neg \varphi$.
   "Not every element satisfies $\varphi$" means "some element does not satisfy $\varphi$", and dually.
5. For $\circ \in \{ \land, \lor \}$, we have $(Q x \, \varphi) \circ \chi \equiv Q x \, (\varphi \circ \chi)$ and $\chi \circ (Q x \, \varphi) \equiv Q x \, (\chi \circ \varphi)$.
   By step 2, $\chi$ has one truth value $B$ for all values of $x$.
6. So step 5 reduces to four facts about a property $A$ of elements and a fixed truth value $B$:
   $$\forall a \, (A(a) \land B) \iff (\forall a \, A(a)) \land B, \qquad \exists a \, (A(a) \lor B) \iff (\exists a \, A(a)) \lor B,$$
   $$\forall a \, (A(a) \lor B) \iff (\forall a \, A(a)) \lor B, \qquad \exists a \, (A(a) \land B) \iff (\exists a \, A(a)) \land B.$$
   Each is checked by the two cases $B$ true and $B$ false.
   The first fact uses the nonempty domain when $B$ is false, and the second when $B$ is true; the last two hold even for an empty domain.
7. $(Q x \, \varphi) \to \chi \equiv Q^* x \, (\varphi \to \chi)$ and $\chi \to Q x \, \varphi \equiv Q x \, (\chi \to \varphi)$.
   Write $\alpha \to \beta$ as $\neg \alpha \lor \beta$, and use steps 4 and 5.
8. $\varphi \leftrightarrow \chi \equiv (\varphi \to \chi) \land (\chi \to \varphi)$ for any $\varphi$ and $\chi$, and both sides have the same free variables.
   The truth tables agree.
9. Claim: if $\psi_1$ and $\psi_2$ are prenex and $\circ \in \{ \land, \lor, \to \}$, then $\psi_1 \circ \psi_2$ is equivalent to a prenex $\psi$ with $\operatorname{FV}(\psi) = \operatorname{FV}(\psi_1) \cup \operatorname{FV}(\psi_2)$.
   We use [[induction|0ASJVEFA9J]] on the total number $m$ of quantifiers in the two prefixes.
10. If $m = 0$, then $\psi_1 \circ \psi_2$ is quantifier-free, hence prenex, and we take $\psi = \psi_1 \circ \psi_2$.
11. Let $m > 0$ and $\psi_1 = Q x \, \psi_1'$.
    Choose a variable $y$ that occurs in neither $\psi_1$ nor $\psi_2$.
    By step 3, $\psi_1 \equiv Q y \, \psi_1''$, where $\psi_1'' = \psi_1'[y/x]$ is prenex.
12. Since $y \notin \operatorname{FV}(\psi_2)$, steps 5 and 7 give $\psi_1 \circ \psi_2 \equiv Q' y \, (\psi_1'' \circ \psi_2)$, where $Q' = Q$ for $\land$ and $\lor$, and $Q' = Q^*$ for $\to$.
13. The prefixes of $\psi_1''$ and $\psi_2$ have $m - 1$ quantifiers in total.
    By the induction hypothesis, $\psi_1'' \circ \psi_2 \equiv \chi$ for a prenex $\chi$ with $\operatorname{FV}(\chi) = \operatorname{FV}(\psi_1'') \cup \operatorname{FV}(\psi_2)$.
14. Take $\psi = Q' y \, \chi$.
    It is prenex, and $\psi_1 \circ \psi_2 \equiv \psi$ by steps 1 and 12.
15. Since $y \notin \operatorname{FV}(\psi_2)$, step 3 gives
    $$\operatorname{FV}(\psi) = (\operatorname{FV}(\psi_1'') \setminus \{ y \}) \cup \operatorname{FV}(\psi_2) = \operatorname{FV}(\psi_1) \cup \operatorname{FV}(\psi_2).$$
16. If $\psi_1$ has no quantifier, then $\psi_2 = Q x \, \psi_2'$, and the same argument uses the second rules of steps 5 and 7.
    There $Q' = Q$ for all three connectives.
    This proves the claim.
17. Now we prove the theorem by [[structural induction|12MQ2NJ29A]] on the [[formula|HYJ10AF6RT]] $\varphi$.
    If $\varphi$ is atomic, it is prenex with an empty prefix, and we take $\psi = \varphi$.
18. Let $\varphi = Q x \, \varphi_1$.
    The induction hypothesis gives a prenex $\psi_1 \equiv \varphi_1$ with the same free variables.
    Then $Q x \, \psi_1$ is prenex, equivalent to $\varphi$ by step 1, and has the free variables of $\varphi$.
19. Let $\varphi = \neg \varphi_1$, and let $\psi_1 = Q_1 x_1 \cdots Q_n x_n \, \mu$ be a prenex equivalent of $\varphi_1$.
    Step 4 applied $n$ times, with step 1, gives $\neg \psi_1 \equiv Q_1^* x_1 \cdots Q_n^* x_n \, \neg \mu$, which is prenex with the same free variables.
20. Let $\varphi = \varphi_1 \circ \varphi_2$ with $\circ \in \{ \land, \lor, \to \}$.
    Replace $\varphi_1$ and $\varphi_2$ by prenex equivalents, by the induction hypothesis and step 1, and apply the claim of step 9.
21. Let $\varphi = \varphi_1 \leftrightarrow \varphi_2$, with prenex equivalents $\psi_1$ and $\psi_2$.
    Use step 8, and apply the claim three times: to $\psi_1 \to \psi_2$, to $\psi_2 \to \psi_1$, and to the conjunction of the two results.
22. Every step is effective: the rules are applied in a fixed order, and the new variable $y$ is the first variable in the list $v_0, v_1, \dots$ that does not occur.
    This proves part 3 of the theorem, and parts 1 and 2 hold by the induction.

## Idea

Quantifiers move outward past the connectives one at a time, using a short list of classical equivalences.
A quantifier leaves a negation or the left side of an implication only after it turns into its dual.
Before a quantifier moves, its variable is renamed to a fresh one, so that it cannot capture a free variable of the other side.
The nonempty domain is used exactly when $\forall$ moves past $\land$ or $\exists$ moves past $\lor$.

## Variants

Many books first remove $\to$ and $\leftrightarrow$, push every $\neg$ inward to the atomic formulas, and only then move the quantifiers out.
The result has a matrix in negation normal form, and the only rules needed are those of step 5.

The order in which quantifiers move out can be chosen, and a good choice gives fewer alternations.
For $\exists x \, P(x) \lor \forall y \, Q(y) \lor \exists z \, R(z)$, pulling out $\exists x$, then $\exists z$, then $\forall y$ gives the prefix $\exists x \, \exists z \, \forall y$ with one alternation, while the left-to-right order gives $\exists x \, \forall y \, \exists z$ with two.

The structural induction can be replaced by an induction on the number of connectives and quantifiers, with the same cases.
In intuitionistic logic, steps 4 and 7 fail for $\neg \forall$ and for $\forall$ in an antecedent, and no variant of this proof works.
