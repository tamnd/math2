---
tag: ~6d00eafb
kind: example
name: A bounded quantifier in front of an unbounded one is not Σ1 as written
msc: ["03F30", "03D55"]
topics: [QHCRN4JVG0]
audience: grad
not_instance_of:
  - target: ~d36afe77
    note: the formula ∀u<y ∃z θ has an unbounded quantifier inside a bounded one, so it lies in no class Δ0, Σn or Πn by the formation clauses
uses: [~29cc9691, ~d54a438d]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: The arithmetical hierarchy of formulas
  - book: isbn:9780521857840
---

## Example

Let $\theta(u, z, y)$ be a $\Delta_0$ formula, and consider
$$\varphi(y) := \forall u < y\; \exists z\; \theta(u, z, y).$$
We show that $\varphi$ is in no class of the [[definition|~29cc9691]] as written, but that it is $\Sigma_1$ in $\mathfrak{N}$.

1. $\varphi$ is not $\Delta_0$, since the quantifier $\exists z$ is unbounded.
2. $\varphi$ is not $\Sigma_n$ or $\Pi_n$ for $n \ge 1$, since its first symbol is a bounded quantifier and an unbounded quantifier occurs inside it. By items 3 and 4 of the definition, unbounded quantifiers occur only in a block in front of the formula.
3. Let $\psi(y) := \exists w\; \forall u < y\; \exists z \le w\; \theta(u, z, y)$. Its matrix $\forall u < y\, \exists z \le w\, \theta$ is $\Delta_0$, so $\psi$ is $\Sigma_1$.
4. Fix $b \in \N$ and suppose $\mathfrak{N} \models \varphi(b)$. For each $u < b$ choose $z_u$ with $\mathfrak{N} \models \theta(u, z_u, b)$.
5. There are only $b$ values of $u$, so $w := \max \set{z_u : u < b}$ exists, with $w := 0$ when $b = 0$. Then $z_u \le w$ for every $u < b$, so $\mathfrak{N} \models \psi(b)$.
6. Conversely, if $\mathfrak{N} \models \psi(b)$ with witness $w$, then for each $u < b$ some $z \le w$ satisfies $\theta$. So $\mathfrak{N} \models \varphi(b)$.
7. Hence $\mathfrak{N} \models \forall y\,(\varphi \leftrightarrow \psi)$, and $\varphi$ is $\Sigma_1$ in $\mathfrak{N}$.

Step 5 is the only place where a property of $\mathfrak{N}$ beyond logic is used: a finite set of numbers has a maximum.

## Remarks

The sentence "$\forall u < y\, \exists z\, \theta \to \exists w\, \forall u < y\, \exists z \le w\, \theta$" for all $\Delta_0$ formulas $\theta$ is the collection schema $\mathsf{B}\Sigma_1$, stated for $\Sigma_1$ formulas $\exists z\, \theta$.
It holds in $\mathfrak{N}$ by step 5, and it is provable in the fragment $\mathsf{I}\Sigma_1$ of [[Peano arithmetic|~b3b2d1f3]], by induction on $y$.
In a weak theory such as [[Robinson arithmetic|3K1AKGXF8A]], step 5 has no proof by induction, so $\varphi$ is $\Sigma_1$ in $\mathfrak{N}$ without being known to be $\Sigma_1$ in the theory.
Together with [[merging of existential quantifiers|~d54a438d]], step 5 shows that in $\mathfrak{N}$ the $\Sigma_1$ formulas are closed under bounded quantifiers, up to equivalence.

## Explanations

### L1 human

"For every $u$ below $y$ there is some $z$" is not of the simple form "there is something, and then a finite check".
But for finitely many $u$, the chosen $z$'s have a largest one, $w$.
So the statement says the same as "there is a $w$ such that every $u$ below $y$ has some $z$ at most $w$".
This second statement has the simple form.

### L2 human

We check steps 4 and 5 for $\theta(u, z, y) := (u + u = z)$ and $y = 3$.

1. $\varphi(\overline{3})$ says that every $u < 3$ has a double $z$, which is true.
2. The witnesses are $z_0 = 0$, $z_1 = 2$ and $z_2 = 4$.
3. Their maximum is $w = 4$, and $\forall u < 3\, \exists z \le 4\,(u + u = z)$ holds.
4. So $\psi(\overline{3})$ holds with witness $w = 4$.

The typical use of this argument is in the proof that the graph of a function defined by primitive recursion is $\Sigma_1$, where a bounded quantifier over the steps of the recursion sits in front of existential witnesses.
A trap is to think that the equivalence is logical: it uses the fact that finitely many witnesses have a common bound, which is a property of $\mathfrak{N}$.
