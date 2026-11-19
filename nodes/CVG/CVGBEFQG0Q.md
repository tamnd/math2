---
tag: CVGBEFQG0Q
kind: definition
name: Definition of the Jankov formula
msc: ["03B55", "06D20"]
topics: [38EQ20GR7M]
audience: research
defines: W0CYVZ48CK
uses: [BND6A96S3D, TYYS649FAJ, 5GTQ69W47T]
sources:
  - arxiv: 1407.5823v1
    locator: Section 1.2, Definition 1.1
  - url: https://eprints.illc.uva.nl/id/document/492
    locator: Section 5.3, Theorem 95
---

## Definition

Let $A$ be a finite [[Heyting algebra|BND6A96S3D]] with a unique coatom $s_A$, the largest element below $1$.
These are exactly the finite [[subdirectly irreducible|TYYS649FAJ]] Heyting algebras.
Take a propositional variable $p_a$ for each $a \in A$.
The *diagram* of $A$ is the conjunction
$$\delta(A) = \bigwedge_{a, b \in A} \bigl( (p_{a \wedge b} \leftrightarrow p_a \wedge p_b) \wedge (p_{a \vee b} \leftrightarrow p_a \vee p_b) \wedge (p_{a \to b} \leftrightarrow (p_a \to p_b)) \bigr) \wedge \bigwedge_{a \in A} (p_{\neg a} \leftrightarrow \neg p_a).$$
The *Jankov formula*, or *characteristic formula*, of $A$ is
$$\chi(A) = \delta(A) \to p_{s_A}.$$
For a finite rooted [[Kripke frame|5GTQ69W47T]] $F$ with root $r$, the up-sets of $F$ form a finite Heyting algebra $\mathrm{Up}(F)$ with unique coatom $F \setminus \set{r}$.
The Jankov formula of $F$ is $\chi(F) = \chi(\mathrm{Up}(F))$.

## Notation

The name is also spelled Yankov.
Some authors write $J(A)$ for $\chi(A)$, and some call the premise $\delta(A)$ the positive diagram.
De Jongh's variant uses one variable for each join-irreducible element only, and gives a shorter formula with the same property.
Any formula with the property of [[the Jankov-de Jongh theorem|D25R70HQ7C]] is often called a Jankov formula of $A$.

## Remarks

1. The valuation $p_a \mapsto a$ in $A$ makes every conjunct of $\delta(A)$ equal to $1$, and sends $p_{s_A}$ to $s_A \neq 1$. So $\chi(A)$ is refuted in $A$.
2. The diagram states that the map $a \mapsto p_a$ respects the operations. A valuation that satisfies it is, after a quotient, a homomorphism from $A$; this is the core of the proof of [[the Jankov-de Jongh theorem|D25R70HQ7C]].
3. A coatom of $\mathrm{Up}(F)$ has the form $F \setminus \set{w}$ with $w$ minimal. In a rooted frame the root is the only minimal world, so the coatom is unique.
4. The formula has $|A|$ variables. It is long even for small algebras, which is why shorter equivalent formulas are used in examples.

## Explanations

### L1 human

Take a small finite table of truth values that has one value just below "true".
Write down, with one letter for each value, all the rules of its operation tables.
The Jankov formula says: if all these rules hold, then the letter for the value just below "true" is true.
It fails exactly in the structures that contain a copy of the table.

### L2 human

1. Let $A = \set{0, 1}$, the two-element Boolean algebra, with coatom $s_A = 0$.
2. The diagram contains $p_0 \leftrightarrow \neg p_1$ and $p_1 \leftrightarrow (p_0 \to p_0)$.
3. So under $\delta(A)$, $p_1$ is true and $p_0$ is false, and $\chi(A) = \delta(A) \to p_0$ amounts to $\neg \delta(A)$.
4. Substituting $\bot$ for $p_0$ and $\bot \to \bot$ for $p_1$ makes $\delta(A)$ provable, so this instance of $\chi(A)$ is equivalent to $\bot$.

The typical use is to axiomatize the largest logic that a given finite algebra or frame refutes; see [[the two-element algebra|YJV1J5PFKC]].
A trap: the algebra must have a unique coatom.
For the four-element Boolean algebra [[no formula can play this role|K7NKMKY1C2]].
