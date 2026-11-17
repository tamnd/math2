---
tag: NRJC4R4BGR
kind: example
name: A closed tableau for ∃x∀yR(x,y) → ∀y∃xR(x,y)
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
instance_of: [WGWBBVE8GX]
uses: [WGWBBVE8GX, 5SDS9T8E7J, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_analytic_tableaux
    locator: First-order tableau without unification
---

## Example

Let $L$ be a first-order language with one binary relation symbol $R$ and no constant symbols.
We show that the sentence
$$\varphi \;=\; \exists x\, \forall y\, R(x,y) \to \forall y\, \exists x\, R(x,y)$$
is [[valid|5SDS9T8E7J]], with a closed [[semantic tableau|WGWBBVE8GX]] for $\{\neg\varphi\}$.
The parameters of $L^{+}$ are $c, d, \dots$.

1. $\neg\big(\exists x\, \forall y\, R(x,y) \to \forall y\, \exists x\, R(x,y)\big)$: the root, the negation of the goal.
2. $\exists x\, \forall y\, R(x,y)$: from line 1 by $\alpha$. Line 1 has the form $\neg(\psi \to \chi)$, and its component 1 is $\psi$.
3. $\neg\forall y\, \exists x\, R(x,y)$: from line 1 by $\alpha$. This is component 2, $\neg\chi$.
4. $\forall y\, R(c,y)$: from line 2 by $\delta$. Line 2 is $\exists x\, \psi'$ with $\psi' = \forall y\, R(x,y)$, and $\delta(c) = \psi'[c/x]$. The parameter $c$ is new, because lines 1 to 3 contain no constant.
5. $\neg\exists x\, R(x,d)$: from line 3 by $\delta$. Line 3 is $\neg\forall y\, \chi'$ with $\chi' = \exists x\, R(x,y)$, and $\delta(d) = \neg\chi'[d/y]$. The parameter $d$ is new, because the only constant on lines 1 to 4 is $c$.
6. $R(c,d)$: from line 4 by $\gamma$ with $t = d$. Line 4 is $\forall y\, R(c,y)$, and $R(c,y)[d/y] = R(c,d)$.
7. $\neg R(c,d)$: from line 5 by $\gamma$ with $t = c$. Line 5 is $\neg\exists x\, R(x,d)$, and $\gamma(c) = \neg R(x,d)[c/x] = \neg R(c,d)$.
8. The only branch contains the atomic sentence $R(c,d)$ (line 6) and its negation (line 7), so it is closed.

The tableau has one branch, and the branch is closed.
So $\vdash_{\mathsf{T}} \varphi$, and by the soundness of tableaux $\varphi$ is valid.

## Remarks

The example shows the right order of the quantifier rules.
Both $\delta$ steps (lines 4 and 5) come before both $\gamma$ steps (lines 6 and 7).
Then the $\gamma$ steps can use the parameters that the $\delta$ steps made, and the two instances meet in one atomic sentence.

A direct semantic check gives the same result.
If some element $a$ has $R(a,b)$ for each $b$, then for each $b$ the element $a$ is an $x$ with $R(x,b)$.
The tableau proof follows this argument: $c$ names $a$, and $d$ names an arbitrary $b$.

The converse $\forall y\, \exists x\, R(x,y) \to \exists x\, \forall y\, R(x,y)$ is not valid.
In the structure with domain $\{0, 1\}$ and $R = \{(0,0), (1,1)\}$, each $y$ has the witness $x = y$, but no $x$ has $R(x,0)$ and $R(x,1)$.
Its tableau does not close: each $\delta$ step must use a new parameter, so the two kinds of instances never meet in a pair $R(s,t)$, $\neg R(s,t)$.

## Explanations

### L1 human

The sentence says: if one person likes everybody, then everybody is liked by somebody.
To test it, we imagine a world where one person, call her Carol, likes everybody, and yet some person, call him Dave, is liked by nobody.
Carol likes everybody, so Carol likes Dave.
Nobody likes Dave, so Carol does not like Dave.
These two facts contradict each other, so the imagined world cannot exist, and the sentence is always true.

### L2 human

The trap is to apply the $\delta$ rule to line 3 with the parameter $c$ again, to get $\neg\exists x\, R(x,c)$.
This step is not allowed, because $c$ is already on the branch at line 4.
In this example the forbidden step would still lead to a closed branch, but the same shortcut proves false sentences in other cases; see [[the δ freshness non-example|GYM3PHAKQ1]].
The correct tableau needs no shortcut: with $d$ new, line 4 gives $R(c,d)$ and line 5 gives $\neg R(c,d)$.
