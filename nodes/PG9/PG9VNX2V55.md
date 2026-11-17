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
$$\varphi \;=\; (\exists x\, P(x) \wedge \exists x\, Q(x)) \to \exists x\,(P(x) \wedge Q(x))$$
with a [[semantic tableau|WGWBBVE8GX]] for $\{\neg\varphi\}$.
We apply every rule that can add something new, with the $\gamma$ rule used for each parameter on the branch.

1. $\neg\big((\exists x\, P(x) \wedge \exists x\, Q(x)) \to \exists x\,(P(x) \wedge Q(x))\big)$: the root.
2. $\exists x\, P(x) \wedge \exists x\, Q(x)$: from line 1 by $\alpha$ (component 1 of $\neg(\psi \to \chi)$).
3. $\neg\exists x\,(P(x) \wedge Q(x))$: from line 1 by $\alpha$ (component 2).
4. $\exists x\, P(x)$: from line 2 by $\alpha$.
5. $\exists x\, Q(x)$: from line 2 by $\alpha$.
6. $P(c)$: from line 4 by $\delta$, with $c$ new, since lines 1 to 5 contain no constant.
7. $Q(d)$: from line 5 by $\delta$, with $d$ new, since $c$ is on the branch and $d \neq c$.
8. $\neg(P(c) \wedge Q(c))$: from line 3 by $\gamma$ with $t = c$.
9. $\neg(P(d) \wedge Q(d))$: from line 3 by $\gamma$ with $t = d$.
10. Branch 1 (left, from line 8 by $\beta$): $\neg P(c)$. It closes with line 6.
11. Branch 2 (right, from line 8 by $\beta$): $\neg Q(c)$. It is open.
12. Branch 2.1 (left, from line 9 by $\beta$, below line 11): $\neg P(d)$. It is open.
13. Branch 2.2 (right, from line 9 by $\beta$, below line 11): $\neg Q(d)$. It closes with line 7.

Branch 2.1 is open.
Its set of sentences is $H = \{$lines 1 to 9, $\neg Q(c)$, $\neg P(d)\}$.
We check that $H$ is a [[Hintikka set|RJNDEG07R1]] for the language $L'$ with the symbols $P, Q, c, d$; the closed terms of $L'$ are $c$ and $d$.

1. No clash: the atomic sentences in $H$ are $P(c)$ and $Q(d)$, and the negated atomic sentences are $\neg Q(c)$ and $\neg P(d)$. No atomic sentence occurs with its negation.
2. $\alpha$ sentences: line 1 has its components 2 and 3 in $H$, and line 2 has its components 4 and 5 in $H$.
3. $\beta$ sentences: line 8 has the component $\neg Q(c)$ in $H$, and line 9 has the component $\neg P(d)$ in $H$.
4. $\gamma$ sentences: line 3 has the instances for both closed terms, $c$ (line 8) and $d$ (line 9).
5. $\delta$ sentences: line 4 has the instance $P(c)$ and line 5 has the instance $Q(d)$.

So the branch is finished: each rule would only repeat a sentence that is already on it.
[[Hintikka's lemma|2A6QP78XN3]] gives a model: the domain is $\{c, d\}$, $P$ is true of exactly the elements whose atom is in $H$, so $P^{\mathcal{M}} = \{c\}$, and $Q^{\mathcal{M}} = \{d\}$.
We check the model directly: $\exists x\, P(x)$ holds with $x = c$, and $\exists x\, Q(x)$ holds with $x = d$.
No element has both properties, because $c \notin Q^{\mathcal{M}}$ and $d \notin P^{\mathcal{M}}$.
So the antecedent of $\varphi$ is true and its consequent is false, and $\varphi$ is not [[valid|5SDS9T8E7J]].

## Remarks

The countermodel is a [[structure|983GZBQYT4]] with two elements: one element with $P$ only, one element with $Q$ only.
In everyday words, "something is red and something is round" does not give "something is red and round".

The tableau is finite here because the language has no function symbols and only two $\delta$ steps occur.
With the sentence $\forall y\, \exists x\, R(x,y) \to \exists x\, \forall y\, R(x,y)$ in place of $\varphi$, the $\delta$ steps never stop, and the open branch is infinite.
The open branch then gives an infinite countermodel, and a small countermodel must be found by other means, for example the domain $\{0, 1\}$ with $R = \{(0,0), (1,1)\}$.

If the conclusion is changed to $\exists x\, P(x)$, the sentence becomes valid, and the tableau for its negation closes.

## Explanations

### L1 human

Suppose that some ball is red and some ball is round.
We ask if some ball must then be both red and round.
The tableau tries to build a world where the answer is no, and it succeeds.
The world has two balls: ball $c$ is red but not round, and ball $d$ is round but not red.
This small world shows that the conclusion does not follow.

### L2 human

The method to read a countermodel from an open branch has three steps.

1. Take the closed terms on the branch as the elements of the domain.
2. Make an atomic sentence true when it is on the branch, and false otherwise.
3. Check that each sentence on the branch is true, from the short sentences to the long ones.

The trap is to read a model from a branch that is open but not finished.
A branch is a Hintikka set only when every rule has done its work on it, and every $\gamma$ sentence has its instance for every closed term.
An open branch that is not finished can belong to an unsatisfiable set.
For example, in the [[closed tableau for ∃x∀yR(x,y) → ∀y∃xR(x,y)|NRJC4R4BGR]], the branch is still open after line 5, and yet its root has no model.
