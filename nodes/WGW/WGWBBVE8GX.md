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

A semantic tableau tests a sentence by trying to build a world in which the sentence is false.
It breaks sentences into simpler pieces, one case per branch, and when every case ends in a contradiction, the sentence is proved.
Here is a complete tableau for $\forall x\, P(x) \to \exists x\, P(x)$:
$$\begin{array}{rll} 1. & \neg(\forall x\, P(x) \to \exists x\, P(x)) & \text{the negated goal} \\ 2. & \forall x\, P(x) & \alpha \text{ from line 1} \\ 3. & \neg \exists x\, P(x) & \alpha \text{ from line 1} \\ 4. & P(c) & \gamma \text{ from line 2 with } t = c \\ 5. & \neg P(c) & \gamma \text{ from line 3 with } t = c \end{array}$$
Check: lines 4 and 5 are a sentence and its negation, so the only branch is closed.
The parameter $c$ names some element, and that step is sound because every [[structure|983GZBQYT4]] has a nonempty domain.

In general, a tableau for a set $\Gamma$ of [[sentences|DKFGQTRYZE]] of a [[first-order|086QKPF0A6]] language $L$ is a finite tree whose nodes carry sentences of $L^{+}$, the language $L$ with countably many new constant symbols called parameters.
The tree starts with members of $\Gamma$ and grows by the premise rule and four rules for the types $\alpha$, $\beta$, $\gamma$ and $\delta$ listed under Notation.
A branch is closed when it contains a sentence $\chi$ and its negation $\neg\chi$, and the tableau is closed when every branch is closed.
We write $\Gamma \vdash_{\mathsf{T}} \varphi$ when some tableau for $\Gamma \cup \{ \neg\varphi \}$ is closed.
Tableaux are sound and complete, so $\Gamma \vdash_{\mathsf{T}} \varphi$ holds exactly when $\Gamma \models \varphi$.

## Motivation

To show that a sentence $\varphi$ is [[valid|5SDS9T8E7J]], we can try to build a structure in which $\neg\varphi$ is true and watch the attempt fail.
A true sentence forces simpler sentences to be true.
If $\varphi \wedge \psi$ is true, then $\varphi$ and $\psi$ are true, and if $\varphi \vee \psi$ is true, then one of them is true, so we try both cases.
If $\exists x\, \varphi$ is true, some element is a witness, and we give this unknown witness a new name.
If $\forall x\, \varphi$ is true, then $\varphi[t/x]$ is true for every closed term $t$ that we have.
A tableau writes these forced sentences down, one branch for each case.

The method is analytic.
Each sentence on a tableau is a part of a sentence above it, or an instance of such a part.
So the search for a proof only takes the goal apart, and it never has to guess a new formula.
This is the main difference from a [[Hilbert-style calculus|N95HV0VWSM]], where a proof can need axiom instances that are not parts of the goal.
When the search fails, the open branch is a [[Hintikka set|RJNDEG07R1]], and it describes a countermodel.

## Notation

We use unsigned formulas with $\neg$ and Smullyan's uniform notation.
The connectives are $\neg, \wedge, \vee, \to$, and $\leftrightarrow$ is an abbreviation.
An atomic sentence or its negation is a literal, and every other sentence has exactly one of the four types below.

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

Here $\varphi[t/x]$ is the [[substitution|NCDZ969V7X]] of $t$ for the free occurrences of $x$, and a closed term is always free for $x$.
An $\alpha$ sentence is true when both components are true, and a $\beta$ sentence is true when at least one is true.
A $\gamma$ sentence has universal force, and a $\delta$ sentence has existential force.
Signed tableaux write $T\varphi$ and $F\varphi$ in place of $\varphi$ and $\neg\varphi$, and introductory books often say "truth tree".

## Remarks

### The rules in full

Fix a first-order language $L$ without the equality symbol, and let $L^{+}$ add a countable set of parameters.
The tableaux for a set $\Gamma$ of sentences of $L$ are the finite labeled trees that these rules make.

1. Start: a single branch whose nodes carry members of $\Gamma$ is a tableau.
2. Premise rule: add any $\sigma \in \Gamma$ at the end of a branch.
3. $\alpha$ rule: if an $\alpha$ sentence is on a branch, add $\alpha_1$ and then $\alpha_2$ at its end.
4. $\beta$ rule: if a $\beta$ sentence is on a branch, give the end of the branch two children, one with $\beta_1$ and one with $\beta_2$.
5. $\gamma$ rule: if a $\gamma$ sentence is on a branch, add $\gamma(t)$ for any closed term $t$ of $L^{+}$.
6. $\delta$ rule: if a $\delta$ sentence is on a branch, add $\delta(c)$, where the parameter $c$ does not occur on that branch.

A rule acts on a whole sentence, never on a part of one.
A sentence stays on the branch after a rule uses it, so one $\gamma$ sentence can give many instances.
A closed branch is not extended further.

### Three more closed tableaux

The sentence $P(c) \vee \neg P(c)$ is valid.
Its negation $\neg(P(c) \vee \neg P(c))$ gives $\neg P(c)$ and $\neg\neg P(c)$ by $\alpha$, and $\neg\neg P(c)$ gives $P(c)$ by $\alpha$.
The branch closes on $P(c)$ and $\neg P(c)$.

For $\forall x\, P(x) \to (P(c) \wedge P(d))$, one $\gamma$ sentence is used twice.
The negation gives $\forall x\, P(x)$ and $\neg(P(c) \wedge P(d))$ by $\alpha$, and the $\beta$ rule splits the second into $\neg P(c)$ and $\neg P(d)$.
On the left branch, $\gamma$ with $t = c$ gives $P(c)$, and on the right branch $\gamma$ with $t = d$ gives $P(d)$.
Both branches close.

The [[closed tableau for ∃x∀yR(x,y) → ∀y∃xR(x,y)|NRJC4R4BGR]] uses two $\delta$ steps and two $\gamma$ steps.
It shows why we apply the $\delta$ rules first: the $\gamma$ rules can then reuse the parameters that the $\delta$ rules made.
The L2 explanation below works one more tableau line by line.

### What is not a tableau

The [[tableau that breaks the freshness condition|GYM3PHAKQ1]] reuses an old parameter in a $\delta$ step.
It "closes" for the negation of $\exists x\, P(x) \to \forall x\, P(x)$, and that negation is satisfiable, so the tree cannot be a tableau.

A calculus in which each $\gamma$ sentence gives only one instance is not complete.
The set $\{ \forall x(P(x) \to P(f(x))), P(c), \neg P(f(f(c))) \}$ is unsatisfiable, but a closed tableau needs both instances $t = c$ and $t = f(c)$ on one branch.

The branch $P(c), \neg P(d)$ is not closed.
Closure needs a sentence and its own negation, and $P(d)$ is a different sentence from $P(c)$.

### Why a closed tableau proves something

Soundness says that if some tableau for $\Gamma$ is closed, then $\Gamma$ is not [[satisfiable|QN7M1JCGT9]].
The proof follows one property through the construction: some branch $B$ has an $L^{+}$-structure that is a model of $\Gamma \cup B$.

If $\Gamma$ has a model $\mathcal{M}$, the start tableau has the property, because we can give the parameters any values in $M$.
The premise rule and the $\alpha$ rule keep it, since the same model works.
The $\beta$ rule keeps it, because the model makes $\beta_1$ or $\beta_2$ true, and we follow that child.
The $\gamma$ rule keeps it, because a model of $\forall x\, \varphi$ is a model of every $\varphi[t/x]$ with $t$ closed.
The $\delta$ rule keeps it, because $c$ is not on the branch and not in $\Gamma$, so we can move the value of $c$ to a witness without changing any other truth value.
A closed branch has no model, so a closed tableau lacks the property, and $\Gamma$ has no model.
The general [[soundness|4A84VHDTHV]] theorem for first-order proof systems belongs to the next sub-area.

### Systematic tableaux

To prove completeness we need a tableau that does every possible piece of work.
Let $L$ be countable, list the closed terms of $L^{+}$ as $t_1, t_2, \dots$, and list $\Gamma$ as $\sigma_1, \sigma_2, \dots$.
The systematic tableau starts with $\sigma_1$ and runs through stages $n = 1, 2, \dots$, and it never extends a branch that contains a pair $A, \neg A$ with $A$ atomic.

1. Take the unprocessed node of least depth, the leftmost if there are several, and let $\psi$ be its sentence.
2. On each open branch through it, apply the $\alpha$, $\beta$ or $\delta$ rule to $\psi$, with the first parameter not on the branch for $\delta$.
3. If $\psi$ is a $\gamma$ sentence, add $\gamma(t_j)$ for the least $j$ with $\gamma(t_j)$ not yet on the branch, and then a new copy of $\psi$.
4. Mark the node as processed, and add $\sigma_{n+1}$ at the end of each open branch if it exists.

The copy in step 3 makes the procedure return to $\psi$ later, so every instance is added in time.
There are at most $2^k$ nodes at depth $k$, so every node is processed at some finite stage.

### Systematic tableaux, continued: completeness

Let $\Gamma$ be a countable set of sentences of $L$.
If $\Gamma$ is unsatisfiable, then its systematic tableau closes after finitely many stages.
So every unsatisfiable set has a closed tableau, and $\Gamma \models \varphi$ gives $\Gamma \vdash_{\mathsf{T}} \varphi$.

1. Suppose the systematic tableau has an open branch $B$, and let $H$ be the set of its sentences.
2. Then $H$ is a [[Hintikka set|RJNDEG07R1]] for $L^{+}$.
   No atomic $A$ and $\neg A$ are both on $B$, every $\alpha$, $\beta$ and $\delta$ sentence was processed, and every $\gamma$ sentence was processed infinitely often, so all of $\gamma(t_1), \gamma(t_2), \dots$ are on $B$.
3. By [[Hintikka's lemma|2A6QP78XN3]], $H$ has a model, and $\Gamma \subseteq H$ by step 4 of the construction, so $\Gamma$ is satisfiable.
4. So if $\Gamma$ is unsatisfiable, every branch is closed and finite.
   A tree with at most two children at each node and no infinite branch is finite by König's lemma, so the tableau is an ordinary finite tableau.

The model in step 3 has the closed terms of $L^{+}$ as its domain, so a satisfiable countable set has a countable model.
In this way tableaux prove [[Gödel's completeness theorem|WQ1ZE255SF]] and the [[compactness theorem|1NR3HAWG9D]] for countable languages.

### When the search does not stop

The systematic tableau for a satisfiable set can run forever.
For the invalid sentence $\forall y\, \exists x\, R(x,y) \to \exists x\, \forall y\, R(x,y)$, every $\gamma$ step gives a new $\delta$ sentence, every $\delta$ step adds a new parameter, and the branch never ends.
No method can avoid this in general, because by [[Church's theorem|VA6BNNY2YC]] validity in first-order logic is undecidable.

A closed tableau for $\{ \sigma_1, \dots, \sigma_n \}$, read from the leaves to the root, is a cut-free derivation of the sequent $\sigma_1, \dots, \sigma_n \Rightarrow$ in the [[sequent calculus|W72CA3R9MP]].
The [[equivalence of proof systems|A9AAHN4BMH]] shows that tableaux prove the same sentences as the Hilbert, natural deduction and sequent systems.

### Watch out

The most common error is to reuse an old parameter in the $\delta$ rule.
From $\exists x\, P(x)$ and $\neg\forall x\, P(x)$ we may write $P(c)$, but then the second sentence needs a new name, $\neg P(d)$, and not $\neg P(c)$.
The witness of $\exists x\, \varphi$ can differ from every element named before, as the [[unsound "tableau"|GYM3PHAKQ1]] shows.

The second error is to treat a $\gamma$ sentence as used up.
The same $\forall x\, \varphi$ may need instances for $c$, for $d$ and for $f(c)$ on one branch.

The third error is to apply a rule inside a sentence.
The sentence $\forall x\, P(x) \to Q(c)$ is a $\beta$ sentence, not a $\gamma$ sentence, so the $\gamma$ rule does not give $P(c) \to Q(c)$, and that sentence does not even follow from it.

### History

Evert Willem Beth and Jaakko Hintikka introduced semantic tableaux independently in 1955, and Stig Kanger gave a related method.
Hintikka worked with sets of sentences that describe a model, now called [[Hintikka sets|RJNDEG07R1]].
Raymond Smullyan's book First-Order Logic (1968) gave the analytic tableaux with the uniform $\alpha, \beta, \gamma, \delta$ notation used here.

### Try it

First, give a closed tableau for $\neg\exists x\, P(x) \to \forall x\, \neg P(x)$.
The negation gives $\neg\exists x\, P(x)$ and $\neg\forall x\, \neg P(x)$, then $\delta$ gives $\neg\neg P(c)$ and $\alpha$ gives $P(c)$, and $\gamma$ with $t = c$ gives $\neg P(c)$, so the branch closes.

Second, explain why $P(c), \neg P(c) \vee Q(c)$ does not close at once.
The second sentence is a $\beta$ sentence, so the branch splits: the left branch $\neg P(c)$ closes, and the right branch $Q(c)$ stays open.

## Explanations

### L1 human

A tableau tests an argument by trying to break it.
Take the claim "all cats are animals and Tom is a cat, so Tom is an animal".
To break it, imagine a world where all cats are animals, Tom is a cat, and Tom is not an animal.
From "all cats are animals" we get "if Tom is a cat, then Tom is an animal".
An "if" sentence gives two cases: Tom is not a cat, or Tom is an animal.
The first case contradicts "Tom is a cat", and the second contradicts "Tom is not an animal".
Every case fails, so no such world exists, and the argument is correct.

### L2 human

We show that $\forall x(P(x) \to Q(x)) \to (\forall x\, P(x) \to \forall x\, Q(x))$ is valid with a closed tableau for its negation.

1. $\neg\big(\forall x(P(x) \to Q(x)) \to (\forall x\, P(x) \to \forall x\, Q(x))\big)$: the negated goal.
2. $\forall x(P(x) \to Q(x))$: from line 1 by $\alpha$.
3. $\neg(\forall x\, P(x) \to \forall x\, Q(x))$: from line 1 by $\alpha$.
4. $\forall x\, P(x)$ and then $\neg\forall x\, Q(x)$: from line 3 by $\alpha$.
5. $\neg Q(c)$: from $\neg\forall x\, Q(x)$ by $\delta$, and $c$ is new because no constant occurs above.
6. $P(c) \to Q(c)$: from line 2 by $\gamma$ with $t = c$.
7. $P(c)$: from $\forall x\, P(x)$ by $\gamma$ with $t = c$.
8. Split line 6 by $\beta$: the left branch $\neg P(c)$ closes with line 7, and the right branch $Q(c)$ closes with line 5.

Both branches are closed, so the sentence is valid by soundness.
The order of work is the usual one: $\alpha$ first, then $\delta$ for new parameters, then $\gamma$ with the parameters on the branch, and $\beta$ last, since each split doubles the work.
Watch the order of lines 5 and 6.
If we apply $\gamma$ to line 2 with $c$ first, then $c$ is on the branch, and the $\delta$ step must use a new $d$, which costs a second $\gamma$ step with $t = d$.

### L3 human

A tableau is a cut-free sequent proof written upside down.
Under the translation of $\neg\varphi$ on the left into $\varphi$ on the right, the $\alpha, \beta, \gamma, \delta$ rules are the left and right rules of [[LK|PZX9J3VEMT]].
The completeness proof through [[Hintikka sets|RJNDEG07R1]] is a model existence argument that builds a [[Herbrand structure|HKW429DSDK]] from an open branch.
It gives completeness, compactness and the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]] for countable languages at once, and it needs no maximal consistent sets.

For automated proof search, the $\gamma$ rule is the hard part, because it asks which term to use.
Free-variable tableaux delay the choice: they instantiate with a new free variable, replace the $\delta$ rule by [[Skolem functions|GCPQGMJYEV]], and close branches by [[unification|RJJ9D0WF53]].
This is the idea behind [[first-order resolution|DEB3CF4Z2D]] as well, and connection tableaux are a common method of [[automated theorem proving|A51M1KK9DJ]].
Tableaux also adapt to modal, intuitionistic and many-valued logics, where a branch describes a Kripke model or a many-valued valuation.
