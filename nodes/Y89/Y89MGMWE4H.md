---
tag: Y89MGMWE4H
kind: statement
role: theorem
name: Van Benthem characterization theorem
msc: ["03B45", "03C95"]
topics: [SPQVNPZDTB]
audience: research
uses: [7T740SFHHV, TKFFTAX30E, DBDNYXA7ME, YW6YGBMVQY, 086QKPF0A6, 1NR3HAWG9D, RMTZ5J64FX]
about: [X27BR4YP2Y, C3RZY20ETK, 086QKPF0A6]
proofs: [AG61G22V37]
history:
  first_stated: "van Benthem, 1976, Modal correspondence theory (dissertation, University of Amsterdam)"
  notes: "Rosen proved the version over finite models in 1997."
sources:
  - url: https://en.wikipedia.org/wiki/Bisimulation
    locator: Bisimulation and modal logic
  - url: https://en.wikipedia.org/wiki/Standard_translation
    locator: Definition
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Statement

Compare two first-order statements about a world $x$ of a Kripke model.
The first, $\exists y \, (R(x, y) \wedge \forall z \, (R(y, z) \to P(z)))$, is the translation of the modal formula $\lozenge \square p$.
The second, $R(x, x)$, says that $x$ sees itself, and it is true at a loop and false at the bisimilar world of a two-cycle.
The van Benthem characterization theorem says that this is the whole difference: a first-order statement is modal exactly when bisimulation cannot change its truth value.

The correspondence language is the [[first-order|086QKPF0A6]] language with one binary relation symbol $R$ and one unary symbol $P$ for each propositional variable $p$.
A Kripke model $(W, R, V)$ is a structure for this language, with $P$ read as $V(p)$.
The [[standard translation|YW6YGBMVQY]] $\mathrm{ST}_x$ sends $p$ to $P(x)$, commutes with $\neg$ and $\wedge$, and sends $\lozenge \varphi$ to $\exists y \, (R(x, y) \wedge \mathrm{ST}_y(\varphi))$.
A formula $\alpha(x)$ with one free variable is *invariant under bisimulation* if $\mathfrak{M} \models \alpha[w] \iff \mathfrak{M}' \models \alpha[w']$ whenever $\mathfrak{M}, w \mathrel{\underline{\leftrightarrow}} \mathfrak{M}', w'$.

**Theorem.** A first-order formula $\alpha(x)$ of the correspondence language is invariant under [[bisimulation|7T740SFHHV]] if and only if $\alpha(x)$ is equivalent on all models to $\mathrm{ST}_x(\varphi)$ for some modal formula $\varphi$.

**Rosen's theorem.** A first-order formula $\alpha(x)$ is invariant under bisimulation between finite models if and only if $\alpha(x)$ is equivalent on all finite models to $\mathrm{ST}_x(\varphi)$ for some modal formula $\varphi$.

The [[proof|AG61G22V37]] covers the first theorem; Rosen's theorem needs other methods, and we cite it without proof.

## Remarks

### Why each hypothesis is needed

Invariance cannot be dropped.
The formula $R(x, x)$ is first-order, but it is true at a reflexive point and false at a bisimilar world of a two-cycle, as [[the loop and two-cycle example|2D9T8ERY94]] shows.
So it is equivalent to no modal formula.

First-order definability cannot be dropped either.
The property "some world reachable from $x$ in finitely many steps satisfies $p$" is invariant under bisimulation, but it is not first-order, and it is equivalent to no $\mathrm{ST}_x(\varphi)$.
A modal formula of depth $d$ cannot see a $p$-world at distance $d + 1$ along a path.

The class of models matters.
Over finite models both the hypothesis and the conclusion are weaker, so Rosen's theorem and the first theorem do not imply each other.
The proof of the first theorem fails there, because it uses the [[compactness theorem|1NR3HAWG9D]].

### What it gives you

The modal language is, up to equivalence, the bisimulation-invariant fragment of first-order logic.
So the definition of modal logic by syntax and its definition by invariance agree.
To show that a first-order property of worlds is not modal, it suffices to find two bisimilar worlds that differ on it.
And every bisimulation-invariant $\alpha(x)$ is equivalent to a formula with only two variables, since standard translations can reuse $x$ and $y$.

### The converse

The theorem is an equivalence, and the direction from right to left is the easy one.
The formula $\mathrm{ST}_x(\varphi)$ expresses the truth of $\varphi$, and $\varphi$ is invariant by [[bisimulation invariance|TKFFTAX30E]].

### Generalizations

The Janin-Walukiewicz theorem says that the modal mu-calculus is the bisimulation-invariant fragment of [[monadic second-order logic|3WHQFSHR58]].
The [[guarded fragment|Y7YS1C3GAE]] of first-order logic is characterized by invariance under guarded bisimulation.
For multimodal languages the same theorem holds with one relation symbol for each modality.

### Watch out

Invariance must be checked across two different models, not only between worlds of one model.
A formula can give the same value to all bisimilar worlds of one model and still fail invariance.
For example, $R(x, x)$ agrees on all bisimilar pairs inside a single loop, but the loop and the two-cycle separate it.

## History

Johan van Benthem proved the theorem in his 1976 dissertation "Modal correspondence theory" at the University of Amsterdam.
Eric Rosen proved the version over finite models in 1997.

## Explanations

### L1 human

First-order logic can say many things about a network of points and arrows.
Some of these things never change when you replace the network by another one that looks the same from inside.
The theorem says that exactly these statements can already be written in the simpler modal language.
"Some arrow leads to a point that has an arrow" survives such a replacement, and it is the modal formula $\lozenge \lozenge \top$.
"There is an arrow from this point to itself" does not survive, and it is not modal.

### L2 human

Is "$x$ has two different successors" modal?
In first-order form it reads
$$\beta(x) = \exists y \, \exists z \, (R(x, y) \wedge R(x, z) \wedge y \neq z).$$
Take $a$ with successors $b$ and $c$, and $x_0$ with the one successor $y_0$, with no true variables.
The relation $\{(a, x_0), (b, y_0), (c, y_0)\}$ is a bisimulation.
Then $\beta$ holds at $a$ and fails at $x_0$, so $\beta$ is not invariant, and by the theorem it is equivalent to no modal formula.
Compare $\alpha(x) = \exists y \, (R(x, y) \wedge \forall z \, (R(y, z) \to P(z)))$, which is $\mathrm{ST}_x(\lozenge \square p)$ with $z$ in place of $x$ inside, and so is invariant.
This is the typical use: a candidate property is modal only if it survives every bisimulation.

### L3 human

The theorem is a preservation theorem in the style of the Łoś-Tarski theorem: a semantic closure condition on first-order formulas matches a syntactic fragment.
Its proof uses compactness and saturation, so it does not transfer to finite models, and Rosen's theorem needs different methods; Martin Otto later gave a proof of both versions by locality.
The pattern recurs across logic: invariance characterizes the mu-calculus inside monadic second-order logic, the guarded fragment under guarded bisimulation, and first-order logic itself in Lindström's theorem.
