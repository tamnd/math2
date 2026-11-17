---
tag: BRDT1BT7WW
kind: statement
role: theorem
name: Lyndon interpolation theorem
aliases: [lyndons-interpolation-theorem, craig-lyndon-interpolation-theorem]
msc: ["03C40", "03B10", "03F05"]
topics: [FBWW4J1XWG]
audience: research
uses: [DKFGQTRYZE, 1HK0VYWTV7, WDVVEYD6AT, 983GZBQYT4, E2CBFNAVZY]
about: [1HK0VYWTV7]
sources:
  - wikipedia: en:2056790@r1321826961
    locator: Craig interpolation, section Lyndon's interpolation theorem
    note: adopted
    mention: wikipedia://en/2056790#BUCI
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: Lyndon's interpolation theorem
  - doi: 10.2140/pjm.1959.9.129
    locator: Section 5, Interpolation theorem
  - arxiv: 2510.03822v1
    locator: Section 2, Definition 2.4, Theorem 2.5, Example 2.7 and Theorem 2.8
history:
  first_stated: "Roger Lyndon, 1959"
  notes: "Roger Lyndon, An interpolation theorem in the predicate calculus, Pacific Journal of Mathematics 9 (1959), pages 129 to 142."
inventory: [CWW1NZDZSW]
---

## Statement

We work in first-order logic with equality, over a [[signature|WDVVEYD6AT]] $\sigma$ of relation, function and constant symbols.
The equality symbol $=$ is logical, and it is not one of the relation symbols of $\sigma$.
Formulas are built from atomic formulas with $\neg, \land, \lor, \to, \forall, \exists$; other connectives are first written out.

**Polarity.**
An occurrence of a subformula in $\varphi$ is positive when it lies in the scope of an even number of negations, and negative otherwise.
Here the left side of each $\to$ counts as one negation.
A relation symbol $R$ is in $\operatorname{Pos}(\varphi)$ when some atomic subformula $R\,t_1 \cdots t_m$ occurs positively in $\varphi$.
It is in $\operatorname{Neg}(\varphi)$ when some such atomic subformula occurs negatively.
A relation symbol can be in both sets, in one, or in neither.

**Theorem.**
Let $\varphi$ and $\psi$ be $\sigma$-[[sentences|DKFGQTRYZE]] with $\varphi \models \psi$, in the sense of [[logical consequence|1HK0VYWTV7]].
Then there is a $\sigma$-sentence $\theta$ with the following four properties.

1. $\varphi \models \theta$ and $\theta \models \psi$.
2. $\operatorname{Pos}(\theta) \subseteq \operatorname{Pos}(\varphi) \cap \operatorname{Pos}(\psi)$.
3. $\operatorname{Neg}(\theta) \subseteq \operatorname{Neg}(\varphi) \cap \operatorname{Neg}(\psi)$.
4. Every function symbol and every constant symbol of $\theta$ occurs in $\varphi$ and in $\psi$.

The equality symbol may occur in $\theta$ with either sign.
Such a $\theta$ is a Lyndon interpolant, and by properties 2 and 3 it is also an interpolant in the sense of the [[Craig interpolation theorem|E2CBFNAVZY]].

The [[proof by Maehara's method|FAG05D5RT9]] proves the case of relational signatures without equality, reduces function symbols to the case with equality, and cites that case.

## Remarks

### An example

Let $\varphi = P c \land (P c \to Q c)$ and $\psi = Q c \lor \neg P c$.

1. Then $\varphi \models \psi$, since $\varphi$ forces $Q c$.
2. In $\varphi$, the first $P c$ is positive, the $P c$ on the left of $\to$ is negative, and $Q c$ is positive. So $\operatorname{Pos}(\varphi) = \{P, Q\}$ and $\operatorname{Neg}(\varphi) = \{P\}$.
3. In $\psi$, $Q c$ is positive and $P c$ is negative. So $\operatorname{Pos}(\psi) = \{Q\}$ and $\operatorname{Neg}(\psi) = \{P\}$.
4. So a Lyndon interpolant may use $Q$ only positively and $P$ only negatively.
5. The sentence $Q c$ is a Lyndon interpolant: $\varphi \models Q c$ and $Q c \models \psi$.
6. The sentence $P c \land Q c$ is a Craig interpolant, but not a Lyndon interpolant, because $P$ occurs positively in it and not positively in $\psi$.

### Conventions on equality and on function symbols

The equality symbol must be free in $\theta$.
Let $\varphi = \forall x \, \forall y \, (x = y)$ and $\psi = \forall x \, \forall y \, (P x \to P y)$.

1. Then $\varphi \models \psi$, since a model of $\varphi$ has one element.
2. The symbol $P$ does not occur in $\varphi$, and there are no function or constant symbols. If $=$ had to obey properties 2 and 3 like a relation symbol, $\theta$ could not contain $=$ either, since $=$ does not occur in $\psi$.
3. Then $\theta$ would have no atomic subformula. Even with the constants $\top$ and $\bot$ added, it would be equivalent to $\top$ or to $\bot$.
4. But $\top \not\models \psi$, by a structure with two elements and $P$ true of one of them, and $\varphi \not\models \bot$, by a structure with one element.
5. With $=$ free, $\theta = \varphi$ is a Lyndon interpolant.

Function and constant symbols get no sign.
Let $\varphi = P c$ and $\psi = \neg \exists x \, (x = c \land \neg P x)$; this example is taken from ten Cate and Comer (Example 2.7).

1. In every structure, $\psi$ is true exactly when $P c$ is true. So $\varphi \models \psi$, and every interpolant $\theta$ is equivalent to $P c$.
2. In $\varphi$, the constant $c$ occurs only in a positive atomic formula. In $\psi$, it occurs only in $x = c$, which is in the scope of one negation.
3. Suppose that $\theta$ does not contain $c$. Take the universe $\{a, b\}$ with $P$ true of $a$ only. Interpreting $c$ as $a$ or as $b$ does not change the truth value of $\theta$.
4. But it changes the truth value of $P c$. So every interpolant contains $c$, and a sign condition on constant symbols would make the theorem false.

### Why each hypothesis is needed

- The hypothesis $\varphi \models \psi$ is needed, since property 1 gives $\varphi \models \psi$. For example, $P c$ and $Q c$ have no interpolant.
- The theorem is stated for sentences. For formulas with free variables the same holds with one more condition: every free variable of $\theta$ is free in $\varphi$ and in $\psi$.
- The conventions above are needed: equality must be allowed in $\theta$, and function and constant symbols cannot carry a sign condition.

### Converse

The converse holds and is immediate.
If some $\theta$ has property 1, then $\varphi \models \theta \models \psi$ gives $\varphi \models \psi$.
So $\varphi \models \psi$ holds exactly when a Lyndon interpolant exists.

### Consequences

- The [[Craig interpolation theorem|E2CBFNAVZY]] follows, as shown after the statement.
- The propositional version holds: a Lyndon interpolant exists for [[propositional formulas|TRS2HY57EG]], with the signs of propositional variables in place of the signs of relation symbols. The propositional cases of the [[proof|FAG05D5RT9]] prove it.
- The version for theories in the article on Craig interpolation follows with the [[compactness theorem|1NR3HAWG9D]].
  If $S \cup T$ has no model, compactness gives finite $S_0 \subseteq S$ and $T_0 \subseteq T$ with $\bigwedge S_0 \models \neg \bigwedge T_0$.
  A Lyndon interpolant $\rho$ of these two sentences is true in all models of $S$ and false in all models of $T$.
  A relation symbol positive in $\rho$ is positive in a member of $S_0$ and negative in a member of $T_0$, and dually for negative ones.

**Corollary (monotone sentences).**
Let $\varphi$ be a $\sigma$-sentence, let $P$ be an $m$-ary relation symbol of $\sigma$, and let $P'$ be a new $m$-ary relation symbol.
Write $\varphi(P')$ for $\varphi$ with every occurrence of $P$ replaced by $P'$.
Call $\varphi$ monotone in $P$ when
$$\varphi \land \forall \bar x \, (P \bar x \to P' \bar x) \models \varphi(P').$$
If $\varphi$ is monotone in $P$, then $\varphi$ is equivalent to a $\sigma$-sentence in which $P$ occurs only positively.

1. Put $\alpha = \varphi \land \forall \bar x \, (P \bar x \to P' \bar x)$ and $\beta = \varphi(P')$. By hypothesis $\alpha \models \beta$.
2. Let $\theta'$ be a Lyndon interpolant: $\alpha \models \theta' \models \beta$, with properties 2 to 4.
3. The symbol $P$ does not occur in $\beta$. By properties 2 and 3, $P$ does not occur in $\theta'$.
4. In $\alpha$, the symbol $P'$ occurs only in $P' \bar x$, on the right of $\to$, inside $\forall$ and $\land$. So $P'$ is not in $\operatorname{Neg}(\alpha)$, and by property 3 it is not in $\operatorname{Neg}(\theta')$.
5. Let $\theta$ be $\theta'$ with $P'$ replaced by $P$. Then $\theta$ is a $\sigma$-sentence, and $P \notin \operatorname{Neg}(\theta)$, because renaming a symbol does not change signs.
6. We show $\varphi \models \theta$. Let $\mathcal{A} \models \varphi$, and expand $\mathcal{A}$ to $\mathcal{A}'$ by $P'^{\mathcal{A}'} = P^{\mathcal{A}}$. Then $\mathcal{A}' \models \alpha$, so $\mathcal{A}' \models \theta'$.
7. Since $P'$ and $P$ have the same interpretation in $\mathcal{A}'$, the sentences $\theta'$ and $\theta$ have the same truth value in $\mathcal{A}'$. So $\mathcal{A} \models \theta$.
8. We show $\theta \models \varphi$. Let $\mathcal{B} \models \theta$, and expand $\mathcal{B}$ to $\mathcal{B}'$ by $P'^{\mathcal{B}'} = P^{\mathcal{B}}$. As in step 7, $\mathcal{B}' \models \theta'$, so $\mathcal{B}' \models \beta = \varphi(P')$.
9. Again $P'$ and $P$ have the same interpretation, so $\mathcal{B}' \models \varphi$, and $\mathcal{B} \models \varphi$.
10. So $\varphi$ is equivalent to $\theta$, and $P$ occurs only positively in $\theta$, or not at all.

The hypothesis of the corollary has a semantic reading.
The sentence $\varphi$ is monotone in $P$ exactly when, for any two [[structures|983GZBQYT4]] $\mathcal{A}$ and $\mathcal{B}$ that differ only in $P$ with $P^{\mathcal{A}} \subseteq P^{\mathcal{B}}$, $\mathcal{A} \models \varphi$ implies $\mathcal{B} \models \varphi$.
To see this, read a structure for $\sigma \cup \{P'\}$ as the pair of $\mathcal{A}$, with $P$, and $\mathcal{B}$, with $P'$ in the role of $P$.

The converse of the corollary also holds.

1. Claim: let $\chi$ be a formula, and let $\mathcal{C}$ be a structure with $P^{\mathcal{C}} \subseteq P'^{\mathcal{C}}$, with an assignment $s$. If $P \notin \operatorname{Neg}(\chi)$ and $\mathcal{C} \models \chi[s]$, then $\mathcal{C} \models \chi(P')[s]$. If $P \notin \operatorname{Pos}(\chi)$ and $\mathcal{C} \models \chi(P')[s]$, then $\mathcal{C} \models \chi[s]$.
2. We prove both parts together by induction on $\chi$. For atomic $P \bar t$ the first part uses $P^{\mathcal{C}} \subseteq P'^{\mathcal{C}}$; the second part is empty, since $P \in \operatorname{Pos}(P \bar t)$. Other atomic formulas do not change.
3. For $\neg A$, the signs in $A$ are reversed, so the first part for $\neg A$ is the contrapositive of the second part for $A$, and conversely. The case of $A \to B$ combines this with the case of $B$.
4. The cases $\land$, $\lor$, $\forall$, $\exists$ keep the signs, and they follow from the induction hypothesis for each assignment.
5. Now let $P \notin \operatorname{Neg}(\theta)$ and $\theta$ equivalent to $\varphi$. If $\mathcal{C} \models \varphi \land \forall \bar x \, (P \bar x \to P' \bar x)$, then $\mathcal{C} \models \theta$, so $\mathcal{C} \models \theta(P')$ by step 1. Since $\theta(P')$ is equivalent to $\varphi(P')$, $\varphi$ is monotone in $P$.

### Generalizations

- For formulas $\varphi$ and $\psi$ with free variables and $\models \varphi \to \psi$, there is a Lyndon interpolant $\theta$ whose free variables are free in both $\varphi$ and $\psi$.
- The theorem holds in first-order logic without equality as well, when the constant $\top$ is part of the language (ten Cate and Comer, Section 2). For relational signatures this is Part A of the [[proof|FAG05D5RT9]].
- Further refinements control the quantifiers of the interpolant. Call a formula $\mathcal{U}$-relativized, for a set $\mathcal{U}$ of unary relation symbols, when each quantifier has the form $\exists x \, (U x \land \cdots)$ or $\forall x \, (U x \to \cdots)$ with $U \in \mathcal{U}$. Otto's interpolation theorem says that if $\varphi$ and $\psi$ are $\mathcal{U}$-relativized, the Lyndon interpolant can be chosen $\mathcal{U}$-relativized as well (ten Cate and Comer, Theorem 2.8).

## History

William Craig proved his interpolation theorem in 1957.
Roger Lyndon published the refinement with signs in 1959, in the paper "An interpolation theorem in the predicate calculus" in the Pacific Journal of Mathematics.
Lyndon writes there that his first proof used Gentzen's calculus and was much the same as Craig's proof, then unpublished.
The published proof is model-theoretic.
Lyndon's motivation was the study of sentences whose truth is preserved when one passes from an algebraic system to a homomorphic image.

## Explanations

### L1 human

Suppose that one statement implies another.
The Craig interpolation theorem gives a middle statement that uses only the words that the two statements share.
Lyndon's theorem adds a condition on how the words are used.
A word that the middle statement uses without "not" must be used without "not" in both outer statements.
A word that it uses with "not" must be used with "not" in both.
For instance, "Tom is a cat, and every cat is black" implies "Tom is black or Tom is big".
The middle statement "Tom is black" uses "black" without "not", as both outer statements do.

### L2 human

We find a Lyndon interpolant for $\varphi = \forall x \, (P x \to Q x) \land \exists x \, P x$ and $\psi = \exists x \, (Q x \lor R x)$.

1. The consequence holds: a model of $\varphi$ has an element in $P$, and that element is in $Q$.
2. In $\varphi$, the $P x$ on the left of $\to$ is negative, $Q x$ is positive, and the $P x$ in $\exists x \, P x$ is positive. So $\operatorname{Pos}(\varphi) = \{P, Q\}$ and $\operatorname{Neg}(\varphi) = \{P\}$.
3. In $\psi$, both $Q$ and $R$ are positive, so $\operatorname{Pos}(\psi) = \{Q, R\}$ and $\operatorname{Neg}(\psi) = \emptyset$.
4. A Lyndon interpolant may use only $Q$, and only positively.
5. The sentence $\theta = \exists x \, Q x$ works: $\varphi \models \exists x \, Q x$ by step 1, and $\exists x \, Q x \models \psi$.

The typical use is a preservation result: from a semantic property, such as monotonicity in $P$, the theorem gives a syntactic form, such as a sentence with $P$ only positive.
A trap is the sign of the left side of $\to$: the hypothesis $P x$ in $P x \to Q x$ is a negative occurrence, although no $\neg$ is written.
A second trap is $\leftrightarrow$: the formula $A \leftrightarrow B$ stands for $(A \to B) \land (B \to A)$, so every symbol in it occurs with both signs.

### L3 human

The theorem is a polarity-sensitive form of interpolation, and its main uses are preservation theorems.
The monotone corollary is one of them.
Lyndon's own aim was the characterization of sentences preserved under homomorphic images, and later preservation theorems follow the same pattern.
One encodes a semantic property as a consequence between two sentences with copies of the symbols, takes an interpolant, and reads off its syntactic form from properties 2 to 4.

On the proof side, the sequent proof refines Maehara's proof of the [[Craig interpolation theorem|E2CBFNAVZY]]: the induction on a cut-free derivation tracks on which side of the sequent each formula stands, and a formula changes sign when it changes side.
Model-theoretic proofs, through a polarity-sensitive form of [[Robinson's joint consistency theorem|~6d43779a]], give the same result without a proof calculus.
