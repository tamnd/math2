---
tag: R6AN38DNBD
kind: statement
role: theorem
name: Robinson's joint consistency theorem
aliases: [robinson-joint-consistency-theorem, robinson-consistency-theorem, joint-consistency-theorem]
msc: ["03C07", "03C40"]
topics: [FBWW4J1XWG]
audience: ug3
about: [VM8TQ70CVJ, 655K8Y7VS8]
uses: [VM8TQ70CVJ, 655K8Y7VS8, DKFGQTRYZE, WDVVEYD6AT, MVCH6N9SNW, AVD7T7J063]
history:
  first_stated: "Abraham Robinson, 1956, in 'A result on consistency and its application to the theory of definition'"
sources:
  - url: https://en.wikipedia.org/wiki/Robinson%27s_joint_consistency_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Robinson%27s_joint_consistency_theorem
    locator: Proof
  - url: https://builds.openlogicproject.org/
    locator: Interpolation
---

## Statement

Two consistent theories in different languages can be combined into one consistent theory, as long as nothing in their shared language tells them apart.
For example, a theory about an order with a coloring $P$ and a theory about the same kind of order with a function $f$ can live in one structure, when both contain the same complete theory of the order.

Let $L_1$ and $L_2$ be first-order languages with equality, given by [[signatures|WDVVEYD6AT]], and let $L_0 = L_1 \cap L_2$ be the language of their common symbols.
Derivability $\vdash$ is in the Hilbert system $H$ of the [[soundness theorem|AVD7T7J063]].
Let $\Gamma$ be a set of [[sentences|DKFGQTRYZE]] of $L_1$, and let $\Sigma$ be a set of sentences of $L_2$.
A sentence $\theta$ of $L_0$ separates $\Gamma$ from $\Sigma$ when $\Gamma \vdash \theta$ and $\Sigma \vdash \neg \theta$.

**Theorem (Robinson).**

1. Separation form: if no sentence of $L_0$ separates $\Gamma$ from $\Sigma$, then $\Gamma \cup \Sigma$ has a [[model|MVCH6N9SNW]], and so it is [[consistent|VM8TQ70CVJ]].
2. Classical form: let $T$ be a [[complete theory|655K8Y7VS8]] in $L_0$, that is, a consistent set of sentences of $L_0$ that derives $\sigma$ or $\neg \sigma$ for each sentence $\sigma$ of $L_0$.
   If $\Gamma \supseteq T$ and $\Sigma \supseteq T$ are consistent, then $\Gamma \cup \Sigma$ is consistent.

Two proofs are given: [[a direct proof by a joint Henkin construction|VNABTNK13X]] and [[a proof from Craig's interpolation theorem|V36AHEN7ZE]].

## Remarks

### A first joint model

Let $L_0 = \{ < \}$, and let $T$ be the theory of dense linear orders without endpoints, which is complete.
Let $L_1 = \{ <, P \}$, and let $\Gamma$ be $T$ together with the sentence that both $P$ and its complement are dense:
$$\forall x \, \forall y \, \big(x < y \to \exists z \, (x < z \land z < y \land P z) \land \exists z \, (x < z \land z < y \land \neg P z)\big).$$
It is consistent, because the rationals with $P$ the dyadic rationals are a model.
Let $L_2 = \{ <, f \}$, and let $\Sigma$ be $T$ together with "$f$ is increasing and $f(x) > x$ for all $x$".
It is consistent, because the reals with $f(x) = x + 1$ are a model.
The two witnesses are different structures, but part 2 gives one dense order that carries both a dense and codense $P$ and an increasing $f$ that moves every point up.
Check: the shared language is $\{ < \}$, and both sets contain the complete theory $T$, so the hypothesis holds.

### Why each hypothesis is needed

The completeness of $T$ in part 2 is needed.
Let $L_0 = L_1 = L_2$ have no non-logical symbols, and take $T = \emptyset$ with
$$\Gamma = \{ \exists x \, \exists y \, \neg (x = y) \}, \qquad \Sigma = \{ \forall x \, \forall y \, (x = y) \}.$$
Both sets are consistent, but their union is not.
The theory $T$ does not decide the $L_0$-sentence $\forall x \, \forall y \, (x = y)$, and this sentence separates $\Sigma$ from $\Gamma$.

The consistency of $\Gamma$ and $\Sigma$ in part 2 is needed, since an inconsistent set has no consistent superset.
The restriction of $\theta$ to the common symbols is the heart of part 1.
If $\theta$ could use a symbol of $L_1$ outside $L_2$, then $\Sigma$ could never derive $\neg \theta$ unless it were inconsistent, so the condition would say nothing about $\Sigma$.

### Part 1 gives part 2

Suppose $\Gamma$ and $\Sigma$ extend a complete $L_0$-theory $T$ and are consistent, and suppose that $\theta \in L_0$ separates them.
If $T \vdash \theta$, then $\Sigma \vdash \theta$ and $\Sigma \vdash \neg \theta$, so $\Sigma$ is inconsistent.
If $T \vdash \neg \theta$, then $\Gamma \vdash \theta$ and $\Gamma \vdash \neg \theta$, so $\Gamma$ is inconsistent.
Both cases contradict the hypothesis, so no sentence separates the two sets, and part 1 gives a model of $\Gamma \cup \Sigma$.

### What it gives you

[[Craig's interpolation theorem|E2CBFNAVZY]] follows from part 1, by [[a short proof|JP8J5RJM6W]], and the [[Beth definability theorem|RJBDSA2ETP]] follows in turn; Robinson's own application was to the theory of definition.

The theorem also joins models.
Let $\mathcal{M}$ be an $L_1$-structure and $\mathcal{N}$ an $L_2$-structure whose reducts to $L_0$ are elementarily equivalent.
Part 2 with $T = \mathrm{Th}_{L_0}(\mathcal{M})$ gives a structure for $L_1 \cup L_2$ that satisfies $\mathrm{Th}(\mathcal{M}) \cup \mathrm{Th}(\mathcal{N})$.
The first joint model above is a case of this, with $\mathcal{M}$ the rationals with the dyadics and $\mathcal{N}$ the reals with $x + 1$.

### The converse and generalizations

The converse of part 1 holds.
If $\Gamma \cup \Sigma$ has a model $\mathcal{A}$ and $\Gamma \vdash \theta$, then $\mathcal{A} \models \theta$ by soundness, so $\Sigma \nvdash \neg \theta$.
So $\Gamma \cup \Sigma$ is consistent if and only if no sentence of $L_0$ separates $\Gamma$ from $\Sigma$.

Part 1 holds for languages of every cardinality, and the joint Henkin proof extends by transfinite recursion.
Many-sorted logic has the same theorem.

### Watch out

A common slip is to apply part 2 to two consistent extensions of an incomplete theory.
The example with $\Gamma = \{ \exists x \, \exists y \, \neg (x = y) \}$ and $\Sigma = \{ \forall x \, \forall y \, (x = y) \}$ shows the failure: both extend the empty theory, and they disagree about the size of the universe.
The correct move is to check that the two sets agree on every sentence of the shared language, which completeness of $T$ guarantees.

Remember also that equality is shared even when $L_0$ has no symbols, so sentences about the number of elements always belong to the common language.

### Try it

First, let $L_0 = \{ < \}$, let $\Gamma$ say "$<$ is a linear order with a least element and $c$ is that least element", and let $\Sigma$ say "$<$ is a linear order with no least element".
Is $\Gamma \cup \Sigma$ consistent?
No: the $L_0$-sentence $\exists x \, \forall y \, \neg (y < x)$ separates them.

Second, explain why part 2 applies to any two consistent expansions of the theory of the infinite set in the empty language.
The theory saying "there are at least $n$ elements" for every $n$ is complete, so if both sets contain it, their union is consistent.

## History

Abraham Robinson published the theorem in 1956, in a paper on consistency and the theory of definition.
He used it to give a new proof of Beth's definability theorem.
Craig's interpolation theorem of 1957 is equivalent to it, given the compactness theorem.

## Explanations

### L1 human

Two people describe the same world, each in their own words.
Each description makes sense alone.
If the two descriptions never disagree on anything that both people can say, then the two descriptions together still make sense.
For example, one person speaks of colors on a line of points and the other speaks of moving the points to the right.
They share only the words "left of" and "right of", and if they agree about everything those words can say, one line of points can carry both stories.

### L2 human

We use the theorem to show that a theory in a larger language does not change what is true in a smaller one.
Let $T$ be a complete $L_0$-theory, and let $\Gamma \supseteq T$ be a consistent $L_1$-theory.
Suppose $\Gamma \vdash \sigma$ for an $L_0$-sentence $\sigma$.
Because $T$ is complete, $T \vdash \sigma$ or $T \vdash \neg \sigma$.
If $T \vdash \neg \sigma$, then $\Gamma \vdash \neg \sigma$ and $\Gamma$ is inconsistent, which is false.
So $T \vdash \sigma$: an expansion of a complete theory proves no new sentences of the old language.

Robinson's theorem goes one step further.
Two such expansions, in languages that share only $L_0$, can be satisfied together, as the joint model of the first subsection shows.
The trap is to forget completeness, as the Watch out shows.

### L3 human

The theorem is an amalgamation property for theories along the square of languages $L_0$, $L_1$, $L_2$ and $L_1 \cup L_2$.
It is equivalent to Craig interpolation over the compactness theorem.
Robinson's own use, a proof of Beth's theorem, shows its role: it turns a semantic hypothesis about two expansions into a syntactic conclusion in the common language.
The [[joint Henkin construction|VNABTNK13X]] builds the amalgam directly, by running the [[Henkin construction|RY8KRKR097]] on both sides at once.
