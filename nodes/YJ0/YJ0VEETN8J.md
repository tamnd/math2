---
tag: YJ0VEETN8J
kind: example
name: A formula with free variables satisfied in the natural numbers
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
instance_of: [2RBQPV02AS]
uses: [1WTCZB4DVB, 983GZBQYT4, 0MWKJ44V5A]
sources:
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Syntax and Semantics
---

## Example

Let $\mathcal{N} = (\mathbb{N}, <)$ be the [[structure|983GZBQYT4]] whose domain is the set $\mathbb{N} = \{0, 1, 2, \ldots\}$ of [[natural numbers|0MWKJ44V5A]] and whose binary relation is the usual strict order.
Let $\varphi$ be the formula $\exists z \, (x < z \wedge z < y)$, "some number lies strictly between $x$ and $y$", with free variables $x$ and $y$.
Let $s$ be an assignment with $s(x) = 1$ and $s(y) = 3$.
We show that $\mathcal{N} \models \varphi[s]$ by the clauses of [[satisfaction|1WTCZB4DVB]].

1. By the clause for $\exists z$, it is enough to find $a \in \mathbb{N}$ with $\mathcal{N} \models (x < z \wedge z < y)[s[z \mapsto a]]$.
2. Take $a = 2$.
   The variant $s[z \mapsto 2]$ sends $x$ to $1$, $y$ to $3$ and $z$ to $2$.
3. The atomic formula $x < z$ is satisfied under this variant, because $(1, 2) \in {<^{\mathcal{N}}}$.
4. The atomic formula $z < y$ is satisfied under this variant, because $(2, 3) \in {<^{\mathcal{N}}}$.
5. By the clause for $\wedge$, the conjunction is satisfied under $s[z \mapsto 2]$.
6. By step 1, $\mathcal{N} \models \varphi[s]$.

## Remarks

A formula with free variables is satisfied by some assignments and not by others.
Here the exact answer is: $\mathcal{N} \models \varphi[s]$ holds if and only if $s(y) \geq s(x) + 2$, because the natural numbers strictly between $m$ and $n$ are $m + 1, \ldots, n - 1$, and this list is nonempty exactly when $n \geq m + 2$.

With $s(x) = 1$ and $s(y) = 2$, no natural number lies strictly between $1$ and $2$, so $\varphi$ is not satisfied.
Over the domain $\mathbb{Q}$ instead of $\mathbb{N}$, the formula is satisfied by every $s$ with $s(x) < s(y)$, with the witness $(s(x) + s(y)) / 2$.
The value $s(z)$ never matters, because $z$ is bound in $\varphi$.

## Explanations

### L1 human

The formula says "there is a number strictly between $x$ and $y$".
With $x = 1$ and $y = 3$ it is true, because $2$ lies between them.
With $x = 1$ and $y = 2$ it is false for whole numbers, because nothing lies between $1$ and $2$.
So the same formula can be satisfied or not, depending on the values that we give to its free letters.

### L2 human

We find all assignments that satisfy $\varphi$ in $\mathcal{N}$.
Let $m = s(x)$ and $n = s(y)$.
If $n \geq m + 2$, the witness $z \mapsto m + 1$ works, because
$$m < m + 1 \quad \text{and} \quad m + 1 < m + 2 \leq n.$$
If $n \leq m + 1$, a witness $a$ would need $m < a < n \leq m + 1$, so $m < a < m + 1$, and no natural number does that.
So $\mathcal{N} \models \varphi[s]$ if and only if $s(y) \geq s(x) + 2$.

The typical use of this pattern is to define relations by formulas: $\varphi$ defines the set of pairs $(m, n)$ with $n \geq m + 2$.
Watch out: the clause for $\exists z$ asks for a search over all values of $z$, so testing only the value $s(z)$ is a mistake.
