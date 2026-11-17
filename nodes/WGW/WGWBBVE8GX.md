---
tag: WGWBBVE8GX
kind: concept
name: Semantic tableaux
aliases: [analytic-tableaux, method-of-analytic-tableaux, truth-trees]
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
uses: [086QKPF0A6, DKFGQTRYZE, NCDZ969V7X, 983GZBQYT4, 2RBQPV02AS, QN7M1JCGT9, 1HK0VYWTV7, 2A6QP78XN3]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_analytic_tableaux
    locator: First-order tableau without unification
  - url: https://en.wikipedia.org/wiki/Method_of_analytic_tableaux
    locator: Uniform notation
  - url: https://en.wikipedia.org/wiki/Method_of_analytic_tableaux
    locator: History
---

## Summary

A semantic tableau (or analytic tableau) for a set $\Gamma$ of [[sentences|DKFGQTRYZE]] of a [[first-order|086QKPF0A6]] language $L$ is a finite tree whose nodes carry sentences of $L^{+}$, the language $L$ with countably many new constant symbols called parameters.
The tree starts with members of $\Gamma$ and grows by five rules, each applied on one branch.
The premise rule adds a member of $\Gamma$, and an $\alpha$ sentence adds $\alpha_1$ and $\alpha_2$.
A $\beta$ sentence splits the branch into a branch with $\beta_1$ and a branch with $\beta_2$.
A $\gamma$ sentence adds $\gamma(t)$ for any closed term $t$ of $L^{+}$.
A $\delta$ sentence adds $\delta(c)$ for a parameter $c$ that does not occur on the branch.
A branch is closed when it contains a sentence $\chi$ and its negation $\neg\chi$, and the tableau is closed when each of its branches is closed.
We write $\Gamma \vdash_{\mathsf{T}} \varphi$ when some tableau for $\Gamma \cup \{\neg\varphi\}$ is closed.
Tableaux are sound and complete, so $\Gamma \vdash_{\mathsf{T}} \varphi$ holds exactly when $\Gamma \models \varphi$, and an open systematic tableau describes a countermodel.

## Motivation

To show that a sentence $\varphi$ is [[valid|5SDS9T8E7J]], we can try to build a [[structure|983GZBQYT4]] in which $\neg\varphi$ is true, and watch the attempt fail.
A sentence that is true in a structure forces simpler sentences to be true there.
For example, if $\varphi \wedge \psi$ is true, then $\varphi$ and $\psi$ are true; if $\varphi \vee \psi$ is true, then one of them is true, and we must try both cases.
If $\exists x\, \varphi$ is true, then some element is a witness, and we give this unknown witness a new name $c$.
If $\forall x\, \varphi$ is true, then $\varphi[t/x]$ is true for each closed term $t$ that we have.
A tableau writes down these forced sentences, one branch for each case.
If each branch contains a sentence and its negation, then no case is possible, and $\neg\varphi$ has no model.
If some branch never meets a contradiction, then its sentences describe a structure in which $\neg\varphi$ is true.

The method is analytic: each sentence on a tableau is a subformula of a sentence above it, or an instance of such a subformula.
So the search for a proof only takes the given sentence apart, and it never has to guess a new formula.
This is the difference from a [[Hilbert-style calculus|N95HV0VWSM]], where a proof can need axiom instances that are not parts of the goal.

## Notation

We use unsigned formulas with the negation sign $\neg$, and the uniform notation of Smullyan.
The connectives are $\neg, \wedge, \vee, \to$ and the quantifiers are $\forall, \exists$; the biconditional is an abbreviation.
Each sentence that is not atomic and not the negation of an atomic sentence (a literal) has exactly one of four types.

| Type | Sentence | Component 1 | Component 2 |
|---|---|---|---|
| $\alpha$ | $\varphi \wedge \psi$ | $\varphi$ | $\psi$ |
| $\alpha$ | $\neg(\varphi \vee \psi)$ | $\neg\varphi$ | $\neg\psi$ |
| $\alpha$ | $\neg(\varphi \to \psi)$ | $\varphi$ | $\neg\psi$ |
| $\alpha$ | $\neg\neg\varphi$ | $\varphi$ | $\varphi$ |
| $\beta$ | $\varphi \vee \psi$ | $\varphi$ | $\psi$ |
| $\beta$ | $\neg(\varphi \wedge \psi)$ | $\neg\varphi$ | $\neg\psi$ |
| $\beta$ | $\varphi \to \psi$ | $\neg\varphi$ | $\psi$ |

| Type | Sentence | Instance |
|---|---|---|
| $\gamma$ | $\forall x\, \varphi$ | $\gamma(t) = \varphi[t/x]$, for any closed term $t$ |
| $\gamma$ | $\neg\exists x\, \varphi$ | $\gamma(t) = \neg\varphi[t/x]$, for any closed term $t$ |
| $\delta$ | $\exists x\, \varphi$ | $\delta(c) = \varphi[c/x]$, for a new parameter $c$ |
| $\delta$ | $\neg\forall x\, \varphi$ | $\delta(c) = \neg\varphi[c/x]$, for a new parameter $c$ |

Here $\varphi[t/x]$ is the [[substitution|NCDZ969V7X]] of $t$ for the free occurrences of $x$; a closed term is substitutable for $x$ in each formula.
In words: an $\alpha$ sentence is true when both components are true, and a $\beta$ sentence is true when at least one component is true.
A $\gamma$ sentence is universal in force and a $\delta$ sentence is existential in force.

We write a tableau as numbered lines.
Each line gives a sentence, the rule and the line that the rule uses.
A split is written in words, for example "Branch 1 (left, from line 4 by $\beta$)".
The notation $\Gamma \vdash_{\mathsf{T}} \varphi$ is used for sentences only.

Other notations in the literature: signed tableaux use the labels $T\varphi$ and $F\varphi$ in place of $\varphi$ and $\neg\varphi$; Beth wrote his tableaux in two columns ("true" and "false"); the name "truth tree" is common in introductory books.

## Remarks

### The rules in full

Fix a first-order language $L$ without the equality symbol, and let $L^{+}$ be $L$ with a countable set of new constant symbols, the parameters.
Let $\Gamma$ be a set of sentences of $L$.
The tableaux for $\Gamma$ are the finite labelled trees that the following rules make.

1. Start: a tree with one branch, whose nodes carry members of $\Gamma$, is a tableau for $\Gamma$.
2. Premise rule: if $\sigma \in \Gamma$, then we can add $\sigma$ at the end of a branch.
3. $\alpha$ rule: if an $\alpha$ sentence is on a branch, then we can add $\alpha_1$ and then $\alpha_2$ at the end of the branch.
4. $\beta$ rule: if a $\beta$ sentence is on a branch, then we can give the end of the branch two children, one with $\beta_1$ and one with $\beta_2$.
5. $\gamma$ rule: if a $\gamma$ sentence is on a branch, then we can add $\gamma(t)$ at the end of the branch, for any closed term $t$ of $L^{+}$.
6. $\delta$ rule: if a $\delta$ sentence is on a branch, then we can add $\delta(c)$ at the end of the branch, where the parameter $c$ does not occur on the branch.

A rule acts on a whole sentence of the branch, never on a part of a sentence.
A sentence stays on the branch after a rule uses it, and the $\gamma$ rule can use the same $\gamma$ sentence many times with different terms.
A closed branch is not extended further.

### Examples

- The sentence $P(c) \vee \neg P(c)$ is valid. The tableau has the lines 1: $\neg(P(c) \vee \neg P(c))$; 2: $\neg P(c)$ (from 1 by $\alpha$); 3: $\neg\neg P(c)$ (from 1 by $\alpha$); 4: $P(c)$ (from 3 by $\alpha$). It closes on lines 2 and 4.
- For $\forall x\, P(x) \to (P(c) \wedge P(d))$ the $\gamma$ sentence is used twice. The lines are 1: the negation; 2: $\forall x\, P(x)$; 3: $\neg(P(c) \wedge P(d))$ (both from 1 by $\alpha$). Branch 1 (left, from line 3 by $\beta$) has $\neg P(c)$ and then $P(c)$ from line 2 by $\gamma$ with $t = c$, and closes. Branch 2 (right) has $\neg P(d)$ and then $P(d)$ from line 2 by $\gamma$ with $t = d$, and closes.
- The sentence $\forall x(P(x) \to Q(x)) \to (\forall x\, P(x) \to \forall x\, Q(x))$ has a closed tableau with one $\delta$ step and one $\beta$ split; the L2 explanation below checks it line by line.
- [[A closed tableau for ∃x∀yR(x,y) → ∀y∃xR(x,y)|NRJC4R4BGR]] shows why the $\delta$ rules come before the $\gamma$ rules in a good proof.
- [[An open tableau gives a countermodel|PG9VNX2V55]] treats the invalid sentence $(\exists x\, P(x) \wedge \exists x\, Q(x)) \to \exists x(P(x) \wedge Q(x))$, and reads a two-element countermodel from the open branch.

### Non-examples

- [[A tableau that breaks the freshness condition of the δ rule|GYM3PHAKQ1]] reuses an old parameter in a $\delta$ step. It "closes" for the satisfiable negation of $\exists x\, P(x) \to \forall x\, P(x)$, so it is not a tableau.
- A calculus in which each $\gamma$ sentence can be used only once is not complete. The set $\{\forall x(P(x) \to P(f(x))),\ P(c),\ \neg P(f(f(c)))\}$ is unsatisfiable. Its closed tableau needs the two instances with $t = c$ and $t = f(c)$ on the same branch, and with only one instance some branch stays open.
- The branch $P(c), \neg P(d)$ is not closed. The closure condition needs a sentence and its own negation, and $P(d)$ is a different sentence from $P(c)$.

### Basic properties

**Soundness.** If some tableau for $\Gamma$ is closed, then $\Gamma$ is not [[satisfiable|QN7M1JCGT9]].
The proof shows that each rule keeps the following property: some branch $B$ has a model of $\Gamma \cup B$ (an $L^{+}$-structure).
The start tableau has this property when $\Gamma$ has a model $\mathcal{M}$: we give the parameters any values in $M$.
The premise rule and the $\alpha$ rule keep the property, because the same model works.
The $\beta$ rule keeps it, because the model makes $\beta_1$ or $\beta_2$ true, and we take that child.
The $\gamma$ rule keeps it, because a model of $\forall x\, \varphi$ is a model of $\varphi[t/x]$ for each closed term $t$.
The $\delta$ rule keeps it, because $c$ does not occur on the branch: we change only the value of $c$ to a witness of $\exists x\, \varphi$, and each sentence of $\Gamma \cup B$ keeps its truth value.
A closed branch has no model, so a closed tableau does not have the property, and $\Gamma$ has no model.
In particular, $\Gamma \vdash_{\mathsf{T}} \varphi$ gives $\Gamma \models \varphi$.
The general [[soundness|4A84VHDTHV]] theorem for first-order proof systems is part of the next sub-area.

**Systematic tableaux.** Let $L$ be countable, so that the closed terms $t_1, t_2, t_3, \dots$ of $L^{+}$ and the members $\sigma_1, \sigma_2, \dots$ of $\Gamma$ can be listed.
Let $\Gamma$ be nonempty.
The systematic tableau for $\Gamma$ starts with one node that carries $\sigma_1$, and it is the limit of the following stages $n = 1, 2, 3, \dots$.
A closed branch (one with an atomic sentence $A$ and $\neg A$) is never extended.

1. Take the first node that the procedure has not yet processed, if there is one: the node of least depth, and the leftmost among those. Let $\psi$ be its sentence.
2. For each open branch $B$ through this node: if $\psi$ is an $\alpha$ sentence, add $\alpha_1, \alpha_2$; if $\psi$ is a $\beta$ sentence, split into $\beta_1$ and $\beta_2$; if $\psi$ is a $\delta$ sentence, add $\delta(c)$ for the first parameter $c$ that is not on $B$.
3. If $\psi$ is a $\gamma$ sentence, add to each such $B$ the instance $\gamma(t_j)$ for the least $j$ with $\gamma(t_j)$ not on $B$, and then a new copy of $\psi$. The copy makes the procedure return to $\psi$ later.
4. Mark the node as processed. A literal needs no work.
5. Add $\sigma_n$ at the end of each open branch, if $\Gamma$ has an $n$-th member.

Each node has at most two children, so there are only finitely many nodes at each depth.
Each stage processes an unprocessed node of least depth.
So a node of depth $k$ waits at most until the finitely many nodes of depth at most $k$ are processed, and each node is processed at some finite stage.

**Completeness of systematic tableaux.** Let $\Gamma$ be a countable set of sentences of $L$.
If $\Gamma$ is unsatisfiable, then the systematic tableau for $\Gamma$ is closed, and it is closed after finitely many stages.
So each unsatisfiable set has a closed tableau, and $\Gamma \models \varphi$ gives $\Gamma \vdash_{\mathsf{T}} \varphi$.
For a valid sentence $\varphi$ this says that $\{\neg\varphi\}$ has a closed tableau.

The proof has four steps.

1. Suppose that the systematic tableau has an open branch $B$, and let $H$ be the set of sentences on $B$.
2. $H$ is a [[Hintikka set|RJNDEG07R1]] for $L^{+}$. No atomic $A$ and $\neg A$ are both on $B$, because $B$ is open. Each $\alpha$, $\beta$ or $\delta$ sentence on $B$ is processed at some stage, and that stage puts its components or its instance on $B$. Each $\gamma$ sentence on $B$ is processed infinitely often, because each processing adds a new copy, and so $\gamma(t_1), \gamma(t_2), \dots$ are all on $B$.
3. By [[Hintikka's lemma|2A6QP78XN3]], $H$ has a model. Stage 5 puts each member of $\Gamma$ on $B$, so $\Gamma \subseteq H$, and the model restricted to $L$ is a model of $\Gamma$.
4. So if $\Gamma$ is unsatisfiable, then each branch is closed. Each closed branch is finite, and a tree with finitely many children at each node and only finite branches is finite (König's lemma). So the tableau is finished after finitely many stages, and it is an ordinary finite tableau.

The proof also shows that closure on atomic sentences is enough: the systematic tableau closes branches only on a pair $A, \neg A$ with $A$ atomic.
The open branch gives a model whose domain is the set of closed terms of $L^{+}$, so a satisfiable countable set has a countable model.
With this, tableaux give a proof of [[Gödel's completeness theorem|WQ1ZE255SF]] and of the [[compactness theorem|1NR3HAWG9D]] for countable languages.

**No decision procedure.** The systematic tableau for a satisfiable set can run forever.
For the invalid sentence $\forall y\, \exists x\, R(x,y) \to \exists x\, \forall y\, R(x,y)$, each $\delta$ step adds a new parameter, and the $\gamma$ steps then use it, so the branch never ends.
This is unavoidable in general: by [[Church's theorem|VA6BNNY2YC]], validity in first-order logic is undecidable.

**Relation to other systems.** A closed tableau for $\{\sigma_1, \dots, \sigma_n\}$ is, read from the leaves to the root, a cut-free derivation of the sequent $\sigma_1, \dots, \sigma_n \Rightarrow$ in the [[sequent calculus|W72CA3R9MP]], with the signs moved across the arrow.
The [[equivalence of proof systems|A9AAHN4BMH]] shows that tableaux prove the same sentences as the Hilbert, natural deduction and sequent systems.

### History

Evert Willem Beth and Jaakko Hintikka introduced semantic tableaux independently in 1955, and Stig Kanger gave a related method.
Hintikka's version worked with sets of sentences that describe a model, and these sets are now called [[Hintikka sets|RJNDEG07R1]].
Raymond Smullyan's book First-Order Logic (1968) gave the analytic tableaux in the form of this page, with the uniform $\alpha, \beta, \gamma, \delta$ notation.

### Common errors

1. Reuse of an old parameter in the $\delta$ rule. The witness of $\exists x\, \varphi$ can be a different element from each element named before; see [[the unsound "tableau"|GYM3PHAKQ1]].
2. A $\gamma$ sentence is not used up. The same $\forall x\, \varphi$ can need several instances on one branch.
3. A rule applies to the main connective of a whole sentence. From $\forall x\, P(x) \to Q(c)$ the $\gamma$ rule does not give $P(c) \to Q(c)$, because this sentence is a $\beta$ sentence, and $P(c) \to Q(c)$ does not follow from it.

## Explanations

### L1 human

A tableau is a way to test an argument by trying to break it.
Take the claim "all cats are animals, Tom is a cat, so Tom is an animal".
To break it, we imagine a world where all cats are animals, Tom is a cat, and Tom is not an animal.
From "all cats are animals" we get "if Tom is a cat, then Tom is an animal".
An "if" sentence gives two cases: Tom is not a cat, or Tom is an animal.
The first case contradicts "Tom is a cat", and the second case contradicts "Tom is not an animal".
Every case fails, so no such world exists, and the argument is correct.
When some case never fails, that case describes a world where the argument breaks.

### L2 human

We prove that $\forall x(P(x) \to Q(x)) \to (\forall x\, P(x) \to \forall x\, Q(x))$ is valid with a closed tableau for its negation.

1. $\neg\big(\forall x(P(x) \to Q(x)) \to (\forall x\, P(x) \to \forall x\, Q(x))\big)$: the negation of the goal.
2. $\forall x(P(x) \to Q(x))$: from line 1 by $\alpha$ (component 1 of $\neg(\varphi \to \psi)$).
3. $\neg(\forall x\, P(x) \to \forall x\, Q(x))$: from line 1 by $\alpha$ (component 2).
4. $\forall x\, P(x)$: from line 3 by $\alpha$.
5. $\neg\forall x\, Q(x)$: from line 3 by $\alpha$.
6. $\neg Q(c)$: from line 5 by $\delta$. The parameter $c$ is new, because lines 1 to 5 have no constant.
7. $P(c) \to Q(c)$: from line 2 by $\gamma$ with $t = c$.
8. $P(c)$: from line 4 by $\gamma$ with $t = c$.
9. Branch 1 (left, from line 7 by $\beta$): $\neg P(c)$. It closes with line 8.
10. Branch 2 (right, from line 7 by $\beta$): $Q(c)$. It closes with line 6.

Both branches are closed, so $\vdash_{\mathsf{T}}$ holds for this sentence, and by soundness the sentence is valid.

The typical use follows a fixed order of work.
We apply the $\alpha$ rules first, then the $\delta$ rules to get new parameters, and then the $\gamma$ rules with the parameters on the branch.
We apply the $\beta$ rules last, since each split doubles the work.
To show that a sentence is not valid, we continue until an open branch is a Hintikka set, and read off a countermodel.

The trap is the order of lines 6 and 7.
If we first apply $\gamma$ to line 2 with $t = c$, then $c$ is on the branch, and the $\delta$ rule for line 5 must use a different parameter $d$.
Then $\neg Q(d)$ and $P(c) \to Q(c)$ do not meet, and we need a second $\gamma$ step with $t = d$.
The rule forbids the shortcut "use $c$ again", since that shortcut is unsound.

### L3 human

A tableau is a cut-free sequent calculus proof written upside down, and the $\alpha, \beta, \gamma, \delta$ rules are the left and right rules of [[LK|PZX9J3VEMT]] under the translation of $\neg\varphi$ on the left into $\varphi$ on the right.
The completeness proof through [[Hintikka sets|RJNDEG07R1]] is a model existence argument: it builds a [[Herbrand structure|HKW429DSDK]] from the open branch, and it gives at the same time completeness, compactness and the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]] for countable languages.
Unlike Henkin's proof, it never needs maximal consistent sets.

For automated proof search, the $\gamma$ rule is the problem, because it asks which term to use.
Free-variable tableaux delay the choice: they add $\varphi[x'/x]$ with a new free variable $x'$, replace the $\delta$ rule by [[Skolem functions|GCPQGMJYEV]] of the free variables, and close branches by [[unification|RJJ9D0WF53]].
This is the same idea as [[first-order resolution|DEB3CF4Z2D]], and connection tableaux are a common method of [[automated theorem proving|A51M1KK9DJ]].
Tableaux also adapt to modal, intuitionistic and many-valued logics, where the branch describes a Kripke model or a many-valued valuation.
