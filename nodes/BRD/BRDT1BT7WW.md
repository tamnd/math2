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

A Craig interpolant can always be chosen so that it uses each shared relation symbol only in the way, positive or negative, that both outer sentences use it.
For example, $P c \land (P c \to Q c)$ implies $Q c \lor \neg P c$, and the interpolant $Q c$ uses $Q$ positively, as both sides do.

We work in first-order logic with equality, over a [[signature|WDVVEYD6AT]] $\sigma$ of relation, function and constant symbols.
The equality symbol $=$ is logical, and it is not one of the relation symbols of $\sigma$.
Formulas are built from atomic formulas with $\neg, \land, \lor, \to, \forall, \exists$, and other connectives are first written out.

**Polarity.**
An occurrence of a subformula in $\varphi$ is positive when it lies in the scope of an even number of negations, and negative otherwise, where the left side of each $\to$ counts as one negation.
A relation symbol $R$ is in $\operatorname{Pos}(\varphi)$ when some atomic subformula $R\,t_1 \cdots t_m$ occurs positively in $\varphi$, and in $\operatorname{Neg}(\varphi)$ when some such atomic subformula occurs negatively.

**Theorem.**
Let $\varphi$ and $\psi$ be $\sigma$-[[sentences|DKFGQTRYZE]] with $\varphi \models \psi$, in the sense of [[logical consequence|1HK0VYWTV7]].
Then there is a $\sigma$-sentence $\theta$ with the following four properties.

1. $\varphi \models \theta$ and $\theta \models \psi$.
2. $\operatorname{Pos}(\theta) \subseteq \operatorname{Pos}(\varphi) \cap \operatorname{Pos}(\psi)$.
3. $\operatorname{Neg}(\theta) \subseteq \operatorname{Neg}(\varphi) \cap \operatorname{Neg}(\psi)$.
4. Every function symbol and every constant symbol of $\theta$ occurs in $\varphi$ and in $\psi$.

Such a $\theta$ is a Lyndon interpolant, and by properties 2 to 4 it is also an interpolant in the sense of the [[Craig interpolation theorem|E2CBFNAVZY]].
The [[proof by Maehara's method|FAG05D5RT9]] proves the relational case without equality and cites the case with equality.

## Remarks

### A first Lyndon interpolant

Let $\varphi = P c \land (P c \to Q c)$ and $\psi = Q c \lor \neg P c$.
The consequence holds, since $\varphi$ forces $Q c$.
In $\varphi$ the first $P c$ is positive, the $P c$ on the left of $\to$ is negative, and $Q c$ is positive, so we read off the signs:
$$\operatorname{Pos}(\varphi) = \{ P, Q \}, \quad \operatorname{Neg}(\varphi) = \{ P \}, \quad \operatorname{Pos}(\psi) = \{ Q \}, \quad \operatorname{Neg}(\psi) = \{ P \}.$$
So a Lyndon interpolant may use $Q$ only positively and $P$ only negatively.
The sentence $Q c$ qualifies, since $\varphi \models Q c$ and $Q c \models \psi$.
Check: $P c \land Q c$ is a Craig interpolant, but not a Lyndon interpolant, because $P$ occurs positively in it and not positively in $\psi$.

### Why equality gets no sign

Let $\varphi = \forall x \, \forall y \, (x = y)$ and $\psi = \forall x \, \forall y \, (P x \to P y)$.
Then $\varphi \models \psi$, since a model of $\varphi$ has one element.
The symbol $P$ does not occur in $\varphi$, and there are no function or constant symbols.
If $=$ had to obey properties 2 and 3 like a relation symbol, $\theta$ could not contain $=$ either, since $=$ does not occur in $\psi$.
Then $\theta$ would have no atomic subformula, and even with the constants $\top$ and $\bot$ it would be equivalent to $\top$ or to $\bot$.
But $\top \not\models \psi$, by a structure with two elements and $P$ true of one of them, and $\varphi \not\models \bot$, by a structure with one element.
With $=$ free, $\theta = \varphi$ is a Lyndon interpolant.

### Why function and constant symbols get no sign

Let $\varphi = P c$ and $\psi = \neg \exists x \, (x = c \land \neg P x)$, an example from ten Cate and Comer (Example 2.7).
In every structure $\psi$ is true exactly when $P c$ is true, so $\varphi \models \psi$, and every interpolant $\theta$ is equivalent to $P c$.
In $\varphi$ the constant $c$ occurs only in a positive atomic formula, and in $\psi$ it occurs only in $x = c$, which lies in the scope of one negation.
Suppose that $\theta$ does not contain $c$, and take the universe $\{ a, b \}$ with $P$ true of $a$ only.
Interpreting $c$ as $a$ or as $b$ does not change the truth value of $\theta$, but it changes the truth value of $P c$.
So every interpolant contains $c$, and a sign condition on constant symbols would make the theorem false.

### Why each hypothesis is needed

The hypothesis $\varphi \models \psi$ is needed, since property 1 gives $\varphi \models \psi$ back.
For example, $P c$ does not imply $Q c$, and these two sentences have no interpolant.
The theorem is stated for sentences.
For formulas with free variables the same holds with one more condition: every free variable of $\theta$ is free in both $\varphi$ and $\psi$.
The conventions of the two subsections above are needed: equality must be allowed in $\theta$ with either sign, and function and constant symbols cannot carry a sign condition.

The converse holds at once.
If some $\theta$ has property 1, then $\varphi \models \theta \models \psi$ gives $\varphi \models \psi$, so $\varphi \models \psi$ holds exactly when a Lyndon interpolant exists.

### Monotone sentences

The main use of the theorem turns a semantic property into a syntactic form.
Let $\varphi$ be a $\sigma$-sentence, let $P$ be an $m$-ary relation symbol of $\sigma$, and let $P'$ be a new $m$-ary relation symbol.
Write $\varphi(P')$ for $\varphi$ with every occurrence of $P$ replaced by $P'$.
We call $\varphi$ monotone in $P$ when the following consequence holds:
$$\varphi \land \forall \bar x \, (P \bar x \to P' \bar x) \models \varphi(P').$$
**Corollary.** If $\varphi$ is monotone in $P$, then $\varphi$ is equivalent to a $\sigma$-sentence in which $P$ occurs only positively.

The hypothesis has a semantic reading.
The sentence $\varphi$ is monotone in $P$ exactly when, for any two [[structures|983GZBQYT4]] $\mathcal{A}$ and $\mathcal{B}$ that differ only in $P$ with $P^{\mathcal{A}} \subseteq P^{\mathcal{B}}$, $\mathcal{A} \models \varphi$ implies $\mathcal{B} \models \varphi$.
To see this, read a structure for $\sigma \cup \{ P' \}$ as the pair of $\mathcal{A}$, with $P$, and $\mathcal{B}$, with $P'$ in the role of $P$.
For example, $\exists x \, \neg \neg P x$ is monotone in $P$, and the corollary gives the equivalent $\exists x \, P x$.

### Monotone sentences, continued: the proof

1. Put $\alpha = \varphi \land \forall \bar x \, (P \bar x \to P' \bar x)$ and $\beta = \varphi(P')$, so $\alpha \models \beta$, and let $\theta'$ be a Lyndon interpolant.
2. The symbol $P$ does not occur in $\beta$, so by properties 2 and 3 it does not occur in $\theta'$.
3. In $\alpha$, the symbol $P'$ occurs only on the right of $\to$ inside $\forall$ and $\land$, so $P' \notin \operatorname{Neg}(\alpha)$, and by property 3, $P' \notin \operatorname{Neg}(\theta')$.
4. Let $\theta$ be $\theta'$ with $P'$ replaced by $P$.
   Renaming does not change signs, so $P \notin \operatorname{Neg}(\theta)$.
5. To show $\varphi \models \theta$, let $\mathcal{A} \models \varphi$, and expand it to $\mathcal{A}'$ with $P'^{\mathcal{A}'} = P^{\mathcal{A}}$.
   Then $\mathcal{A}' \models \alpha$, so $\mathcal{A}' \models \theta'$, and since $P'$ and $P$ agree in $\mathcal{A}'$, $\mathcal{A} \models \theta$.
6. To show $\theta \models \varphi$, let $\mathcal{B} \models \theta$, and expand it in the same way to $\mathcal{B}'$.
   Then $\mathcal{B}' \models \theta'$, so $\mathcal{B}' \models \varphi(P')$, and since $P'$ and $P$ agree, $\mathcal{B} \models \varphi$.

So $\varphi$ is equivalent to $\theta$, in which $P$ occurs only positively or not at all.

### The converse of the corollary

A sentence $\theta$ with $P \notin \operatorname{Neg}(\theta)$ is monotone in $P$, so the corollary is an equivalence.
We prove a claim by induction on formulas $\chi$.
Let $\mathcal{C}$ be a structure with $P^{\mathcal{C}} \subseteq P'^{\mathcal{C}}$, with an assignment $s$.
If $P \notin \operatorname{Neg}(\chi)$ and $\mathcal{C} \models \chi[s]$, then $\mathcal{C} \models \chi(P')[s]$; and if $P \notin \operatorname{Pos}(\chi)$ and $\mathcal{C} \models \chi(P')[s]$, then $\mathcal{C} \models \chi[s]$.

For an atomic $P \bar t$ the first part uses $P^{\mathcal{C}} \subseteq P'^{\mathcal{C}}$, and the second part is empty, since $P \in \operatorname{Pos}(P \bar t)$.
Other atomic formulas do not change.
For $\neg A$ the signs in $A$ are reversed, so the first part for $\neg A$ is the contrapositive of the second part for $A$, and conversely.
The case $A \to B$ combines this with the case of $B$, and the cases $\land$, $\lor$, $\forall$, $\exists$ keep the signs.
Now if $\mathcal{C} \models \theta \land \forall \bar x \, (P \bar x \to P' \bar x)$, the claim gives $\mathcal{C} \models \theta(P')$.

### Other consequences

The [[Craig interpolation theorem|E2CBFNAVZY]] follows, as noted after the statement.
The propositional version holds for [[propositional formulas|TRS2HY57EG]], with the signs of propositional variables in place of the signs of relation symbols, and the propositional cases of the [[proof|FAG05D5RT9]] prove it.

A version for theories follows with the [[compactness theorem|1NR3HAWG9D]].
If $S \cup T$ has no model, compactness gives finite $S_0 \subseteq S$ and $T_0 \subseteq T$ with $\bigwedge S_0 \models \neg \bigwedge T_0$.
A Lyndon interpolant $\rho$ of these two sentences is true in all models of $S$ and false in all models of $T$.
A relation symbol positive in $\rho$ is positive in a member of $S_0$ and negative in a member of $T_0$, and dually for negative ones.

### Generalizations

For formulas $\varphi$ and $\psi$ with free variables and $\models \varphi \to \psi$, there is a Lyndon interpolant whose free variables are free in both.
The theorem also holds in first-order logic without equality, when the constant $\top$ is part of the language (ten Cate and Comer, Section 2), and for relational signatures this is Part A of the [[proof|FAG05D5RT9]].

Further refinements control the quantifiers of the interpolant.
For a set $\mathcal{U}$ of unary relation symbols, a formula is $\mathcal{U}$-relativized when each quantifier has the form $\exists x \, (U x \land \cdots)$ or $\forall x \, (U x \to \cdots)$ with $U \in \mathcal{U}$.
Otto's interpolation theorem says that if $\varphi$ and $\psi$ are $\mathcal{U}$-relativized, the Lyndon interpolant can be chosen $\mathcal{U}$-relativized as well (ten Cate and Comer, Theorem 2.8).

### Watch out

The left side of $\to$ is a negative position, although no $\neg$ is written.
In $P x \to Q x$ the symbol $P$ is negative, so a student who counts only the written $\neg$ signs gets $\operatorname{Neg}(\varphi)$ wrong.

The biconditional is a second trap.
The formula $A \leftrightarrow B$ stands for $(A \to B) \land (B \to A)$, so every symbol in it occurs with both signs.
For example, $\forall x \, (P x \leftrightarrow Q x)$ has $P$ and $Q$ in both $\operatorname{Pos}$ and $\operatorname{Neg}$.

### Try it

First, compute $\operatorname{Pos}$ and $\operatorname{Neg}$ of $\neg (P c \to \neg Q c)$.
Here $P c$ sits on the left of $\to$ inside one $\neg$, so it is positive, and $Q c$ sits inside two $\neg$, so it is positive too.
So $\operatorname{Pos} = \{ P, Q \}$ and $\operatorname{Neg} = \emptyset$.

Second, find a Lyndon interpolant for $\forall x \, P x \land R c \models P c \lor \neg S c$.
The only shared relation symbol is $P$, positive on both sides, and $\theta = P c$ works.

## History

William Craig proved his interpolation theorem in 1957.
Roger Lyndon published the refinement with signs in 1959, in the paper "An interpolation theorem in the predicate calculus" in the Pacific Journal of Mathematics.
Lyndon writes there that his first proof used Gentzen's calculus and was much the same as Craig's proof, which was then unpublished.
The published proof is model-theoretic.
Lyndon's motivation was the study of sentences whose truth is preserved when one passes from an algebraic system to a homomorphic image.

## Explanations

### L1 human

Suppose that one statement implies another.
The Craig interpolation theorem gives a middle statement that uses only the words that the two statements share.
Lyndon's theorem adds a condition on how the words are used.
A word that the middle statement uses without "not" must be used without "not" in both outer statements, and a word that it uses with "not" must be used with "not" in both.
For instance, "Tom is a cat, and every cat is black" implies "Tom is black or Tom is big".
The middle statement "Tom is black" uses "black" without "not", as both outer statements do.

### L2 human

We find a Lyndon interpolant for $\varphi = \forall x \, (P x \to Q x) \land \exists x \, P x$ and $\psi = \exists x \, (Q x \lor R x)$.
The consequence holds: a model of $\varphi$ has an element in $P$, and that element is in $Q$.
In $\varphi$ the $P x$ on the left of $\to$ is negative, $Q x$ is positive, and the $P x$ in $\exists x \, P x$ is positive.
In $\psi$ both $Q$ and $R$ are positive, so we get these signs:
$$\operatorname{Pos}(\varphi) = \{ P, Q \}, \quad \operatorname{Neg}(\varphi) = \{ P \}, \quad \operatorname{Pos}(\psi) = \{ Q, R \}, \quad \operatorname{Neg}(\psi) = \emptyset.$$
So a Lyndon interpolant may use only $Q$, and only positively.
The sentence $\theta = \exists x \, Q x$ works, since $\varphi \models \exists x \, Q x$ and $\exists x \, Q x \models \psi$.

The typical use is a preservation result, as in the monotone corollary: a semantic property, such as monotonicity in $P$, gives a syntactic form, such as a sentence with $P$ only positive.

### L3 human

The theorem is a polarity-sensitive form of interpolation, and its main uses are preservation theorems.
One encodes a semantic property as a consequence between two sentences with copies of the symbols, takes an interpolant, and reads off its syntactic form from properties 2 to 4.
The monotone corollary is the simplest case of this pattern.
Lyndon's own aim was the characterization of sentences preserved under homomorphic images, and later preservation theorems follow the same pattern.

On the proof side, the sequent proof refines Maehara's proof of the [[Craig interpolation theorem|E2CBFNAVZY]].
The induction on a cut-free derivation tracks on which side of the sequent each formula stands, and a formula changes sign when it changes side.
Model-theoretic proofs, through a polarity-sensitive form of [[Robinson's joint consistency theorem|R6AN38DNBD]], give the same result without a proof calculus.
