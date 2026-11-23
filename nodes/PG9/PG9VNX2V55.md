---
tag: PG9VNX2V55
kind: example
name: An open tableau gives a countermodel
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
instance_of: [WGWBBVE8GX]
uses: [WGWBBVE8GX, RJNDEG07R1, 2A6QP78XN3, 983GZBQYT4, 5SDS9T8E7J]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_analytic_tableaux
    locator: First-order tableau without unification
  - url: https://en.wikipedia.org/wiki/Hintikka_set
    locator: lead section
---

## Example

Let $L$ have two unary relation symbols $P$ and $Q$ and no constant symbols.
We test the sentence
$$\varphi = (\exists x\, P(x) \wedge \exists x\, Q(x)) \to \exists x\,(P(x) \wedge Q(x))$$
with a [[semantic tableau|WGWBBVE8GX]] for $\{ \neg\varphi \}$.
We apply every rule that can add something new, and we use the $\gamma$ rule for each parameter on the branch.

1. $\neg\big((\exists x\, P(x) \wedge \exists x\, Q(x)) \to \exists x\,(P(x) \wedge Q(x))\big)$: the root.
2. $\exists x\, P(x) \wedge \exists x\, Q(x)$: from line 1 by $\alpha$.
3. $\neg\exists x\,(P(x) \wedge Q(x))$: from line 1 by $\alpha$.
4. $\exists x\, P(x)$: from line 2 by $\alpha$.
5. $\exists x\, Q(x)$: from line 2 by $\alpha$.
6. $P(c)$: from line 4 by $\delta$, with $c$ new, since lines 1 to 5 contain no constant.
7. $Q(d)$: from line 5 by $\delta$, with $d$ new, since $c$ is already on the branch.
8. $\neg(P(c) \wedge Q(c))$: from line 3 by $\gamma$ with $t = c$.
9. $\neg(P(d) \wedge Q(d))$: from line 3 by $\gamma$ with $t = d$.
10. Split line 8 by $\beta$: the left branch $\neg P(c)$ closes with line 6, and the right branch $\neg Q(c)$ stays open.
11. Below $\neg Q(c)$, split line 9 by $\beta$: the left branch $\neg P(d)$ stays open, and the right branch $\neg Q(d)$ closes with line 7.

So one branch stays open, the branch through $\neg Q(c)$ and $\neg P(d)$.
Its set of sentences is $H$, which is lines 1 to 9 together with $\neg Q(c)$ and $\neg P(d)$.
We check that $H$ is a [[Hintikka set|RJNDEG07R1]] for the language with the symbols $P, Q, c, d$, whose closed terms are $c$ and $d$.

1. No clash: the atoms in $H$ are $P(c)$ and $Q(d)$, and the negated atoms are $\neg Q(c)$ and $\neg P(d)$.
2. The $\alpha$ sentences: line 1 has its components 2 and 3 in $H$, and line 2 has its components 4 and 5.
3. The $\beta$ sentences: line 8 has the component $\neg Q(c)$ in $H$, and line 9 has the component $\neg P(d)$.
4. The $\gamma$ sentence: line 3 has its instances for both closed terms, lines 8 and 9.
5. The $\delta$ sentences: line 4 has the instance $P(c)$, and line 5 has the instance $Q(d)$.

So the branch is finished, since every rule would only repeat a sentence already on it.
[[Hintikka's lemma|2A6QP78XN3]] gives the model $\mathcal{M}$ with domain $\{ c, d \}$, $P^{\mathcal{M}} = \{ c \}$ and $Q^{\mathcal{M}} = \{ d \}$.
Check: $\exists x\, P(x)$ holds with $x = c$, and $\exists x\, Q(x)$ holds with $x = d$.
No element has both properties, because $c \notin Q^{\mathcal{M}}$ and $d \notin P^{\mathcal{M}}$.
So the antecedent of $\varphi$ is true and its consequent is false, and $\varphi$ is not [[valid|5SDS9T8E7J]].

## Remarks

### What the countermodel says

The countermodel is a [[structure|983GZBQYT4]] with two elements, one with $P$ only and one with $Q$ only.
In everyday words, "something is red and something is round" does not give "something is red and round".
If we change the conclusion to $\exists x\, P(x)$, the sentence becomes valid, and the tableau for its negation closes.

### When the open branch is infinite

The tableau is finite here because the language has no function symbols and only two $\delta$ steps occur.
For $\forall y\, \exists x\, R(x,y) \to \exists x\, \forall y\, R(x,y)$ the $\delta$ steps never stop, and the open branch of the systematic tableau is infinite.
That branch gives an infinite countermodel.
A small countermodel must be found by other means, for example the domain $\{ 0, 1 \}$ with $R = \{ (0,0), (1,1) \}$.

## Explanations

### L1 human

Suppose that some ball is red and some ball is round.
Must some ball be both red and round?
The tableau tries to build a world where the answer is no, and it succeeds.
The world has two balls: ball $c$ is red but not round, and ball $d$ is round but not red.
This small world shows that the conclusion does not follow.

### L2 human

To read a countermodel from a finished open branch, take three steps.

1. Take the closed terms on the branch as the elements of the domain.
2. Make an atomic sentence true when it is on the branch, and false otherwise.
3. Check that each sentence on the branch is true, from the short sentences to the long ones.

Watch out: read a model only from a finished branch.
A branch is a Hintikka set only when every rule has done its work on it, and every $\gamma$ sentence has its instance for every closed term.
An open branch that is not finished can belong to an unsatisfiable set.
For example, in the [[closed tableau for ∃x∀yR(x,y) → ∀y∃xR(x,y)|NRJC4R4BGR]], the branch is still open after line 5, and yet its root has no model.
