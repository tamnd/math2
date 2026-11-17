---
tag: FWP8NY5VE7
kind: example
name: The theory of abelian groups
msc: ["20A15", "03C60", "20K99"]
topics: [BAZT8JJ70S]
audience: research
instance_of: [RX9MB386C5]
uses: [RX9MB386C5, 082GHNPJ53, DKFGQTRYZE, 655K8Y7VS8]
sources:
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: Some decidable theories
---

## Example

We work in the first-order language of groups with the signature $\{\cdot, {}^{-1}, e\}$, as in the [[elementary theory of groups|RX9MB386C5]].
Let $T_{\mathrm{grp}}$ be the set of the three group axioms, and let $\gamma$ be the [[sentence|DKFGQTRYZE]] $\forall x \forall y \, (x \cdot y = y \cdot x)$.
Let $T_{\mathrm{ab}}$ be the set of all sentences that follow from $T_{\mathrm{grp}} \cup \{\gamma\}$.
We check that $T_{\mathrm{ab}}$ is the theory of the class of [[abelian groups|082GHNPJ53]], and we check some of its first properties.

1. A structure satisfies $T_{\mathrm{grp}} \cup \{\gamma\}$ if and only if it is a group in which $xy = yx$ for all $x, y$. This is the definition of an abelian group.
2. By [[Gödel's completeness theorem|WQ1ZE255SF]], a sentence follows from $T_{\mathrm{grp}} \cup \{\gamma\}$ if and only if it is true in every model of these axioms. By step 1, $T_{\mathrm{ab}}$ is the set of sentences true in every abelian group.
3. The class of abelian groups is a proper subclass of the class of groups. The group $S_3$ is not abelian, because $(1\,2)(1\,3) = (1\,3\,2)$ and $(1\,3)(1\,2) = (1\,2\,3)$. So $\gamma$ is not a consequence of $T_{\mathrm{grp}}$.
4. $T_{\mathrm{ab}}$ is not a [[complete theory|655K8Y7VS8]]. The sentence $\exists x \, (x \ne e)$ is true in the abelian group $\mathbb{Z}/2\mathbb{Z}$ and false in the [[trivial group|0BNPC9850Y]], so neither this sentence nor its negation is in $T_{\mathrm{ab}}$.
5. $T_{\mathrm{ab}}$ is axiomatized by the finite set $T_{\mathrm{grp}} \cup \{\gamma\}$, so the set $T_{\mathrm{ab}}$ is [[computably enumerable|TN9G24VABN]]. By [[Szmielew's theorem|Y0753DF5R9]], it is also decidable.

## Remarks

The example shows that one extra sentence can cut out a natural class of groups.
The same construction with the sentence $\forall x \, (x^n = e)$ in place of $\gamma$ gives the theory of the groups of exponent dividing $n$.
For $n = 2$ this class lies inside the class of abelian groups: every group with $x^2 = e$ for all $x$ is abelian, since $xy = (xy)^{-1} = y^{-1}x^{-1} = yx$.
The theory of all groups is undecidable, while $T_{\mathrm{ab}}$ is decidable.
So a single extra axiom can change an undecidable theory into a decidable one.

## Explanations

### L1 human

A group is abelian when the order of a product does not matter: $xy = yx$ for all elements.
This condition is one sentence: "for every $x$ and every $y$, $x$ times $y$ equals $y$ times $x$."
The theory of abelian groups is the list of all sentences that follow from the group rules and this one extra rule.
For example, the integers with addition satisfy all of these sentences, because $2 + 3 = 3 + 2$ and the same holds for all pairs.

### L2 human

We use the theory to show that a sentence is not a consequence of commutativity.
Let $\psi$ be the sentence $\forall x \, (x \cdot x = e \to x = e)$.

1. In the abelian group $(\mathbb{Z}, +)$, the equation $x + x = 0$ gives $x = 0$. So $\mathbb{Z} \models \psi$.
2. In the abelian group $\mathbb{Z}/2\mathbb{Z}$, the element $1$ satisfies $1 + 1 = 0$ and $1 \ne 0$. So $\mathbb{Z}/2\mathbb{Z} \models \neg \psi$.
3. Since $\psi$ is false in one abelian group, $\psi \notin T_{\mathrm{ab}}$.
4. Since $\neg \psi$ is false in another abelian group, $\neg \psi \notin T_{\mathrm{ab}}$.

The typical use of this method is to show that some axioms do not decide a sentence: we give one model where the sentence is true and one model where it is false.
A trap is to confuse "$\psi \notin T_{\mathrm{ab}}$" with "$\neg \psi \in T_{\mathrm{ab}}$".
Step 4 shows that the second statement is false.
