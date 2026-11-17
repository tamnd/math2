---
tag: ~f5cfc0f6
kind: example
name: A tableau that breaks the freshness condition of the δ rule
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
not_instance_of:
  - target: ~78632a29
    note: the δ step on line 5 uses the parameter c, which already occurs on the branch, so the tree is not a tableau, and it closes for a satisfiable set
uses: [~78632a29, QN7M1JCGT9, 983GZBQYT4, 5SDS9T8E7J]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_analytic_tableaux
    locator: First-order tableau without unification
---

## Example

Let $L$ have one unary relation symbol $P$ and no constant symbols.
The sentence $\exists x\, P(x) \to \forall x\, P(x)$ is not [[valid|5SDS9T8E7J]].
In the [[structure|983GZBQYT4]] $\mathcal{M}$ with domain $M = \{0, 1\}$ and $P^{\mathcal{M}} = \{0\}$, the antecedent $\exists x\, P(x)$ is true (witness $0$) and the consequent $\forall x\, P(x)$ is false (the element $1$ fails).
So the set $\{\neg(\exists x\, P(x) \to \forall x\, P(x))\}$ is [[satisfiable|QN7M1JCGT9]].
The following tree looks like a closed [[semantic tableau|~78632a29]] for this set.

1. $\neg(\exists x\, P(x) \to \forall x\, P(x))$: the root.
2. $\exists x\, P(x)$: from line 1 by $\alpha$. This step is correct.
3. $\neg\forall x\, P(x)$: from line 1 by $\alpha$. This step is correct.
4. $P(c)$: from line 2 by $\delta$, with $c$ new. This step is correct, because lines 1 to 3 contain no constant.
5. $\neg P(c)$: from line 3 by "$\delta$" with the parameter $c$. This step breaks the rule, because $c$ occurs on line 4.
6. Lines 4 and 5 form the pair $P(c)$, $\neg P(c)$, so the single branch "closes".

If the tree were a tableau, soundness would make the root unsatisfiable, and $\exists x\, P(x) \to \forall x\, P(x)$ would be valid.
The structure $\mathcal{M}$ above shows that this is false.
So a calculus that allows step 5 is unsound, and step 5 is the only step that breaks a rule.

The correct step 5 uses a new parameter $d$ and gives $\neg P(d)$.
The branch with lines 1 to 4 and $\neg P(d)$ is then finished and open.
It has no $\gamma$ sentence; its $\alpha$ sentence has both components, its $\delta$ sentences have instances, and it has no clash.
So it is a Hintikka set for the closed terms $c, d$, and it gives the model with domain $\{c, d\}$ and $P = \{c\}$, which is $\mathcal{M}$ with new names.

## Remarks

The example shows why the $\delta$ rule needs a parameter that is new to the branch.
The sentence $\exists x\, P(x)$ says only that some element has $P$, and the sentence $\neg\forall x\, P(x)$ says only that some element lacks $P$.
Nothing says that these are the same element, so they must get different names.
A parameter that is new to the branch has no properties yet, so it can name any element, and this is why the $\delta$ rule is sound.

The same error appears in other systems as a broken eigenvariable condition.
In [[natural deduction|6KT3BJZ7D1]], the same false sentence $\exists x\, P(x) \to \forall x\, P(x)$ becomes derivable when the eigenvariable condition of $\forall$-introduction or of $\exists$-elimination is dropped.

It is enough that the parameter is new to the branch, not to the whole tableau.
Two different branches can use the same parameter in their $\delta$ steps, because no model has to make both branches true.

## Explanations

### L1 human

"Somebody in the class is tall" and "somebody in the class is not tall" can both be true.
They are true together when the class has one tall student and one short student.
The error is to call both people by the same name, say Carl.
Then we get "Carl is tall" and "Carl is not tall", which is a contradiction.
The contradiction comes from the bad naming, not from the facts.

### L2 human

The check for each $\delta$ step is mechanical.

1. Find the parameter $c$ that the step introduces.
2. List the sentences on the branch above the step.
3. Check that $c$ occurs in none of them, and that $c$ is not a symbol of $L$.

In this example, step 2 for line 5 lists lines 1 to 4, and $c$ occurs in line 4, so the check fails.
The trap is the order of work: a student who applies the $\delta$ rule to line 3 before line 2 must then use a new parameter for line 2, and the same error is possible at that point.
