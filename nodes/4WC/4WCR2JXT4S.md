---
tag: 4WCR2JXT4S
kind: example
name: Merging existential quantifiers in a Σ1 formula
msc: ["03F30", "03D55"]
topics: [QHCRN4JVG0]
audience: grad
instance_of: [GE43CSZTS9]
uses: [Y0JTZXBRT5, 329ZG1Z0G5]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: The arithmetical hierarchy of formulas
  - book: isbn:9780521857840
---

## Example

Two searches for witnesses can always be run as one search for a common bound.
Let $\delta(x, y, \vec{z})$ be a $\Delta_0$ formula, and let $w$ be a variable that does not occur in $\delta$.
We show that the $\Sigma_1$ formula $\exists x\, \exists y\, \delta$ is equivalent in $\mathfrak{N}$ to the formula
$$\exists w\, \exists x \le w\, \exists y \le w\; \delta(x, y, \vec{z}),$$
which has a single unbounded quantifier in front of a $\Delta_0$ formula.

1. The part $\exists x \le w\, \exists y \le w\, \delta$ is $\Delta_0$, by item 1 of the [[definition|Y0JTZXBRT5]], because the bound $w$ is a variable different from $x$ and $y$.
2. Fix values $\vec{c}$ of $\vec{z}$, and suppose that $\mathfrak{N} \models \delta(a, b, \vec{c})$ for some $a, b \in \mathbb{N}$.
3. Put $w = \max(a, b)$.
   Then $a \le w$ and $b \le w$, so the right-hand formula holds with witnesses $w$, $a$ and $b$.
4. Conversely, witnesses $w$, $x$ and $y$ for the right-hand formula give $\mathfrak{N} \models \delta(x, y, \vec{c})$, so the left-hand formula holds.
5. So the two formulas define the same relation of $\vec{z}$ in $\mathfrak{N}$.

A concrete case is "$x$ is a sum of two squares", $\exists a\, \exists b\,(a \cdot a + b \cdot b = x)$.

6. Here the bound $w$ can even be replaced by $x$, because $a \cdot a + b \cdot b = x$ gives $a \le a \cdot a \le x$ and in the same way $b \le x$.
7. So the formula is equivalent in $\mathfrak{N}$ to the $\Delta_0$ formula $\exists a \le x\, \exists b \le x\,(a \cdot a + b \cdot b = x)$.
8. For $x = 13$, the witnesses $a = 2$ and $b = 3$ work, since $4 + 9 = 13$.
   For $x = 7$, the squares up to $7$ are $0$, $1$ and $4$, and no two of them add to $7$, so the bounded search fails.

## Remarks

The example shows that the number of unbounded existential quantifiers in a $\Sigma_1$ formula does not matter, because one suffices.
The same argument merges any block $\exists x_1 \cdots \exists x_k$, with $w = \max(x_1, \ldots, x_k)$.
Step 6 shows more: when the witnesses are bounded by a free variable, the $\Sigma_1$ formula is even $\Delta_0$ in $\mathfrak{N}$.

What changes inside a theory $T$?
The proof used only that any two numbers have a common upper bound.
So the equivalence holds in $T$ when $T$ proves $\forall x\, \forall y\, \exists w\,(x \le w \land y \le w)$, and $\mathsf{PA}$ proves this with $w = x + y$.

## Explanations

### L1 human

"There are $a$ and $b$ with some property" says the same as "there is a bound $w$, and below it there are $a$ and $b$ with the property".
If $a$ and $b$ exist, the larger of the two is such a bound.
So two searches can be done as one search for $w$, followed by a finite check below $w$.

### L2 human

We merge the quantifiers in $\exists x\, \exists y\,(x \cdot y = \overline{12} \land \overline{1} < x \land x < y)$.
The part after the quantifiers has no quantifiers, so it is $\Delta_0$.
The merged formula is
$$\exists w\, \exists x \le w\, \exists y \le w\,(x \cdot y = \overline{12} \land \overline{1} < x \land x < y).$$
In $\mathfrak{N}$ the pair $x = 2$, $y = 6$ works, and $w = 6$ bounds it.
The pair $x = 3$, $y = 4$ also works, with $w = 4$.
The typical use of merging is to put every $\Sigma_1$ formula in the form $\exists w\, \delta$ with $\delta$ in $\Delta_0$, as in the [[representability theorem|BJF29XET83]].
The trap is to forget the theory: the equivalence is a fact about $\mathfrak{N}$, and inside a theory it needs the common bound as a theorem.
