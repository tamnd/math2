---
tag: MFGHDHGV1D
kind: statement
role: theorem
name: Soundness of the reduction axioms of public announcement logic
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: research
uses: [9465T2PWZT, EA34W4ERRE, ERG3KAQWYF, NGHWZ9Y7ZV]
about: [9465T2PWZT]
proofs: [NFFFDP1TK6]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_epistemic_logic
    locator: section Public Events
  - book: isbn:9781402058387
    locator: van Ditmarsch, van der Hoek and Kooi, Dynamic Epistemic Logic, chapter on public announcements
---

## Statement

A public announcement can always be pushed inside a formula and then removed, so announcements add no expressive power to epistemic logic.

Let $M = (W, (R_a)_{a \in \mathcal{A}}, V)$ be any [[multi-agent|ERG3KAQWYF]] [[Kripke model|NGHWZ9Y7ZV]], and let $\varphi$ be a formula of [[public announcement logic|9465T2PWZT]].
Let $M|\varphi = (W', (R'_a)_a, V')$ with $W' = \{w \in W : M, w \models \varphi\}$, $R'_a = R_a \cap (W' \times W')$ and $V'(p) = V(p) \cap W'$.
Define $M, w \models [!\varphi]\psi$ to hold when $M, w \models \varphi$ implies $M|\varphi, w \models \psi$.
Then the following formulas are true at every world of every model.

1. $[!\varphi]p \leftrightarrow (\varphi \to p)$, for atoms $p$.
2. $[!\varphi]\neg\psi \leftrightarrow (\varphi \to \neg[!\varphi]\psi)$.
3. $[!\varphi](\psi \wedge \chi) \leftrightarrow ([!\varphi]\psi \wedge [!\varphi]\chi)$.
4. $[!\varphi]K_a\psi \leftrightarrow (\varphi \to K_a[!\varphi]\psi)$.
5. $[!\varphi][!\psi]\chi \leftrightarrow [!(\varphi \wedge [!\varphi]\psi)]\chi$.

As a consequence, every formula of public announcement logic without common knowledge is equivalent to a formula of [[epistemic logic|EA34W4ERRE]] without announcements.

## Remarks

### Why each hypothesis is needed

No condition on the relations is used, so the five formulas are valid in every Kripke model.
What can fail is that $M|\varphi$ stays in an intended class of models.
$\mathsf{S5}_n$ models stay $\mathsf{S5}_n$ models, because the restriction of an equivalence relation is an equivalence relation.
Seriality is not preserved, so a $\mathsf{KD45}_n$ model can turn into a model with dead ends, and the axioms then speak about a model of a weaker logic.
The atom clause needs the valuation to be restricted and not changed, and events that change facts need other axioms.

### What it gives you

Add parts 1 to 5 as axioms to $\mathsf{S5}_n$, with the rule "from $\psi$ infer $[!\varphi]\psi$".
The result is a complete axiomatization of $\mathsf{PAL}$ over $\mathsf{S5}_n$ models.
The reason is that a $\mathsf{PAL}$ validity translates into an $\mathsf{S5}_n$ validity, which is provable, and the translation steps are provable equivalences.
The same translation shows that $\mathsf{PAL}$ validity is decidable.
Part 5 also says that two announcements in a row have the effect of a single announcement.
[[The translation example|JRHH7Z42A4]] carries out the reduction on a concrete formula.

### The converse fails for common knowledge

There is no reduction axiom of this form for common knowledge.
Some formulas $[!\varphi]C_G\psi$ have no equivalent in epistemic logic with $C_G$.
So $\mathsf{PAL}$ with common knowledge is strictly more expressive than epistemic logic with common knowledge.

### Generalizations

For an action model $\mathsf{E}$ with event $e$, the knowledge axiom becomes the following.
$$[\mathsf{E}, e]K_a\psi \leftrightarrow \Big(\mathrm{pre}(e) \to \bigwedge_{e \to_a f} K_a[\mathsf{E}, f]\psi\Big).$$
With relativized common knowledge $C_G(\varphi, \psi)$, read "$\psi$ holds along every $G$-path through $\varphi$-worlds", the reduction extends to announcements and common knowledge together.

## History

Plaza gave the reduction axioms in "Logics of public communications" (1989).
The reduction axioms for action models are due to Baltag, Moss and Solecki (1998).
Relativized common knowledge and the reduction for it are due to van Benthem, van Eijck and Kooi (2006).

## Explanations

### L1 human

After a public announcement, every question about what agents know can be answered by looking at the model before the announcement.
"After $\varphi$ is announced, Ann knows $\psi$" means "if $\varphi$ is true, Ann knows that $\psi$ would hold after the announcement".
So announcements do not let us say anything new, and they only let us say it more conveniently.

### L2 human

We read axiom 4 at a world $w$ where $\varphi$ is true.
After the announcement, Ann considers possible the worlds she saw before at which $\varphi$ holds.
So "Ann knows $\psi$ after" means that at every world she saw before, if $\varphi$ holds there, then $\psi$ holds there after the announcement.
That is $K_a[!\varphi]\psi$, since $[!\varphi]\psi$ is automatically true where $\varphi$ is false.

The typical use is to eliminate announcements from a formula, innermost first.
Watch out: in axiom 2 the antecedent $\varphi$ is needed.
At a world where $\varphi$ is false, $[!\varphi]\neg\psi$ and $[!\varphi]\psi$ are both true, so $[!\varphi]\neg\psi \leftrightarrow \neg[!\varphi]\psi$ fails there.

### L3 human

The axioms describe how the model transformer $M \mapsto M|\varphi$ acts on truth sets, clause by clause.
They are recursion equations for the weakest precondition of $\psi$ under $!\varphi$, in the sense of program semantics.
