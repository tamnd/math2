---
tag: HJEZHW1YQ2
kind: example
name: A bounded quantifier in front of an unbounded one is not Σ1 as written
msc: ["03F30", "03D55"]
topics: [QHCRN4JVG0]
audience: grad
not_instance_of:
  - target: GE43CSZTS9
    note: the formula ∀u<y ∃z θ has an unbounded quantifier inside a bounded one, so it lies in no class Δ0, Σn or Πn by the formation clauses
uses: [Y0JTZXBRT5, 4WCR2JXT4S]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: The arithmetical hierarchy of formulas
  - book: isbn:9780521857840
---

## Example

A formula can fail the shape test of the hierarchy and still be $\Sigma_1$ in the standard model.
Let $\theta(u, z, y)$ be a $\Delta_0$ formula, and consider
$$\varphi(y) := \forall u < y\; \exists z\; \theta(u, z, y).$$
We show that $\varphi$ is in no class of the [[definition|Y0JTZXBRT5]] as written, but that it is $\Sigma_1$ in $\mathfrak{N}$.

1. The formula $\varphi$ is not $\Delta_0$, because the quantifier $\exists z$ is unbounded.
2. It is not $\Sigma_n$ or $\Pi_n$ for $n \ge 1$, because items 3 and 4 of the definition allow unbounded quantifiers only in a block in front.
   Here an unbounded quantifier sits inside the bounded quantifier $\forall u < y$.
3. Let $\psi(y) := \exists w\; \forall u < y\; \exists z \le w\; \theta(u, z, y)$.
   Its part after $\exists w$ is $\Delta_0$, so $\psi$ is $\Sigma_1$.
4. Fix $b \in \mathbb{N}$ and suppose that $\mathfrak{N} \models \varphi(b)$.
   For each $u < b$ choose $z_u$ with $\mathfrak{N} \models \theta(u, z_u, b)$.
5. There are only $b$ values of $u$, so $w := \max \{ z_u : u < b \}$ exists, with $w := 0$ when $b = 0$.
   Then $z_u \le w$ for every $u < b$, so $\mathfrak{N} \models \psi(b)$.
6. Conversely, if $\mathfrak{N} \models \psi(b)$ with witness $w$, then each $u < b$ has some $z \le w$ that satisfies $\theta$.
   So $\mathfrak{N} \models \varphi(b)$.
7. Hence $\mathfrak{N} \models \forall y\,(\varphi \leftrightarrow \psi)$, and $\varphi$ is $\Sigma_1$ in $\mathfrak{N}$.

Step 5 is the only place where the argument uses a property of $\mathfrak{N}$ beyond logic: a finite set of numbers has a largest element.

## Remarks

The implication from $\varphi$ to $\psi$, taken for all $\Delta_0$ formulas $\theta$, is the collection schema $\mathsf{B}\Sigma_1$.
It holds in $\mathfrak{N}$ by step 5, and the fragment $\mathsf{I}\Sigma_1$ of [[Peano arithmetic|HACXBCM7SS]] proves it by induction on $y$.
[[Robinson arithmetic|3K1AKGXF8A]] has no induction, so the argument of step 5 is not available there, and $\varphi$ need not be $\Sigma_1$ in $\mathsf{Q}$.

Together with [[merging of existential quantifiers|4WCR2JXT4S]], step 5 shows that in $\mathfrak{N}$ the $\Sigma_1$ formulas are closed under bounded quantifiers, up to equivalence.
If the bounded quantifier were unbounded, as in $\forall u\, \exists z\, \theta$, the argument would fail, since infinitely many witnesses need not have a common bound.
For example, $\forall u\, \exists z\,(u < z)$ is true, but no single $w$ bounds a $z$ above every $u$.

## Explanations

### L1 human

"For every $u$ below $y$ there is some $z$" is not of the simple form "there is something, and then a finite check".
But for finitely many $u$, the chosen values $z$ have a largest one, $w$.
So the statement says the same as "there is a $w$ such that every $u$ below $y$ has some $z$ at most $w$".
This second statement has the simple form.

### L2 human

We check steps 4 and 5 for $\theta(u, z, y) := (u + u = z)$ and $y = 3$.
The sentence $\varphi(\overline{3})$ says that every $u < 3$ has a double $z$, which is true.
The witnesses are $z_0 = 0$, $z_1 = 2$ and $z_2 = 4$, and their maximum is $w = 4$.
Check: $\forall u < 3\, \exists z \le 4\,(u + u = z)$ holds, so $\psi(\overline{3})$ holds with witness $w = 4$.
The typical use of this argument is the proof that the graph of a function defined by primitive recursion is $\Sigma_1$, where a bounded quantifier over the steps of the recursion sits in front of existential witnesses.
The trap is to think that the equivalence is logical, since it uses the fact that finitely many witnesses have a common bound.
