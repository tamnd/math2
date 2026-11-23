---
tag: Y0JTZXBRT5
kind: definition
name: Δ0, Σn and Πn formulas
msc: ["03F30", "03D55"]
topics: [QHCRN4JVG0]
audience: grad
defines: GE43CSZTS9
uses: [329ZG1Z0G5, 2CHENV4DCC, CV2E6JZHVP, EDRV3N0SA3]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: The arithmetical hierarchy of formulas
  - book: isbn:9780521857840
---

## Definition

The classes $\Delta_0$, $\Sigma_n$ and $\Pi_n$ sort formulas by their bounded quantifiers and by the alternations of their unbounded quantifiers.
Let $L_A$ be the [[language of arithmetic|329ZG1Z0G5]], with bounded quantifiers as defined there.

1. The class $\Delta_0$ is the smallest set of [[formulas|2CHENV4DCC]] of $L_A$ that contains the atomic formulas and is closed under $\neg$, $\land$, $\lor$, $\to$, and the bounded quantifiers $\forall x < t$, $\exists x < t$, $\forall x \le t$ and $\exists x \le t$, for terms $t$ in which $x$ does not occur.
2. We put $\Sigma_0 = \Pi_0 = \Delta_0$.
3. For $n \ge 0$, a formula is $\Sigma_{n+1}$ if it has the form $\exists x_1 \cdots \exists x_k\, \varphi$ with $k \ge 0$ and $\varphi \in \Pi_n$.
4. For $n \ge 0$, a formula is $\Pi_{n+1}$ if it has the form $\forall x_1 \cdots \forall x_k\, \varphi$ with $k \ge 0$ and $\varphi \in \Sigma_n$.
5. Let $T$ be an $L_A$-theory.
   A formula $\psi$ is $\Sigma_n$ in $T$ if $T \vdash \psi \leftrightarrow \varphi$ for some $\varphi \in \Sigma_n$ with the same free variables, and likewise for $\Pi_n$.
   It is $\Delta_n$ in $T$ if it is both $\Sigma_n$ in $T$ and $\Pi_n$ in $T$.
6. A formula is $\Sigma_n$, $\Pi_n$ or $\Delta_n$ in $\mathfrak{N}$ if item 5 holds with "$\mathfrak{N} \models \forall \vec{x}\,(\psi \leftrightarrow \varphi)$" in place of "$T \vdash \psi \leftrightarrow \varphi$".

## Notation

The classes of items 1 to 4 are classes of formulas, fixed by their shape.
A set $A \subseteq \mathbb{N}^k$ is $\Sigma^0_n$, $\Pi^0_n$ or $\Delta^0_n$ when some formula of the matching class in $\mathfrak{N}$ defines it.
These are the set classes of the [[arithmetical hierarchy|CV2E6JZHVP]].
Many books write $\Sigma^0_n$ for the formula class as well, and we keep the superscript for sets.

## Remarks

Item 1 asks that the bounding term $t$ not contain $x$, so that the bound is known before the search starts.
For example, $\exists x < S x\,(x = x)$ is not a bounded quantifier, since its bound moves with $x$.

Items 3 and 4 allow $k = 0$, so an empty block is permitted.
This gives $\Sigma_n \cup \Pi_n \subseteq \Sigma_{n+1} \cap \Pi_{n+1}$.
They also allow $k \ge 2$, so a block such as $\exists x\, \exists y$ counts as one alternation.
For example, $\exists x\, \exists y\, \forall z\,(x + z = y)$ is $\Sigma_2$, and $\forall z\, \exists x\,(z < x)$ is $\Pi_2$.

Items 3 and 4 put unbounded quantifiers only in a block in front.
So a formula such as $\exists x\, \delta \land \forall y\, \delta'$ is in no class as written, unless its quantifiers are bounded.

Items 5 and 6 give the semantic notions, which depend on a theory or on the standard model.
Membership in $\Delta_0$ is checked by [[induction on formulas|EDRV3N0SA3]], and it is decidable.
The [[concept page|GE43CSZTS9]] states the closure properties and the link with computability.

## Explanations

### L1 human

The definition sorts formulas by their quantifiers.
Formulas whose quantifiers are all "below some number" form the class $\Delta_0$.
Putting a block of "there is" in front of a formula of class $\Pi_n$ gives class $\Sigma_{n+1}$.
Putting a block of "for all" in front of a formula of class $\Sigma_n$ gives class $\Pi_{n+1}$.

### L2 human

We classify $\varphi := \exists z\, \forall u < z\, \exists v\,(u + v = z)$.
The atomic formula $u + v = z$ is $\Delta_0$, and $\exists v\,(u + v = z)$ is $\Sigma_1$ because its quantifier is unbounded.
Next, $\forall u < z$ puts a bounded quantifier in front of a $\Sigma_1$ formula, so the result is in no class of items 1 to 4 as written.
In $\mathfrak{N}$, however, $\exists v\,(u + v = z)$ is equivalent to $\exists v \le z\,(u + v = z)$, since $v \le u + v$.
With this change the inner part is $\Delta_0$, and $\varphi$ is $\Sigma_1$ in $\mathfrak{N}$.
The typical use of the definition is to check the hypothesis "$\varphi$ is $\Sigma_1$" of a theorem such as $\Sigma_1$-completeness.
The trap is the middle step, since a bounded quantifier in front of an unbounded one gives no formula of the hierarchy as written.
