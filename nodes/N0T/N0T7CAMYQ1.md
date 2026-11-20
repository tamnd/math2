---
tag: N0T7CAMYQ1
kind: example
name: The theory of infinite sets is complete
msc: ["03C07", "03C35"]
topics: [AY09KYSW81]
audience: ug2
instance_of: [655K8Y7VS8]
uses: [655K8Y7VS8, KFWXHKBHYT, ZR7Y5C235P, 1JJCGNX240, PZMGQMDN25, 8GBH6BWXPZ]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_theory
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Example

Let $L = \emptyset$ be the empty signature, so an $L$-structure is a nonempty set.
For $n \ge 2$ let $\lambda_n = \exists x_1 \cdots \exists x_n \bigwedge_{i < j} \neg(x_i = x_j)$, "there are at least $n$ elements".
Let $T_\infty = \set{\lambda_n : n \ge 2}$, the [[theory of infinite sets|KFWXHKBHYT]].
We check that $T_\infty$ is [[complete|655K8Y7VS8]].

1. $T_\infty$ is satisfiable: $\N$ satisfies every $\lambda_n$.
2. The models of $T_\infty$ are exactly the infinite sets. So $T_\infty$ has no finite models.
3. Let $\kappa$ be an infinite cardinal and let $A$, $B$ be models of size $\kappa$. There is a bijection $f \colon A \to B$.
4. In the empty signature, a bijection is an [[isomorphism|PZMGQMDN25]], since there are no symbols to respect. So $T_\infty$ is [[$\kappa$-categorical|1JJCGNX240]] for every infinite $\kappa$.
5. By the [[Łoś-Vaught test|ZR7Y5C235P]] with $\kappa = \aleph_0 \ge \abs{L}$, $T_\infty$ is complete.

So any two infinite sets satisfy the same sentences of pure equality, by the [[characterization of complete theories|8GBH6BWXPZ]].

## Remarks

The theory of a finite set with $n$ elements is axiomatized by the single sentence $\lambda_n \land \neg\lambda_{n+1}$ (with $\lambda_1$ read as $\exists x \, (x = x)$), and it is also complete.
So the complete theories in the empty signature are exactly these finite ones and $T_\infty$.
Since $T_\infty$ is complete and has a computable list of axioms, it is decidable; see [[this example|1886MXD8S5]].
The theory $\set{\lambda_n : n \ge 2}$ is not equivalent to any finite subset of it: the finite subset $\set{\lambda_2, \dots, \lambda_n}$ has the finite model with $n$ elements.

## Explanations

### L1 human

With no symbols except equality, all we can say about a set is how many elements it has, up to "at least $n$".
Every infinite set has at least $n$ elements for every $n$.
So all infinite sets give the same answers, and the theory of infinite sets answers every question.

### L2 human

We check that $\sigma = \forall x \, \exists y \, \neg(x = y)$ follows from $T_\infty$.

1. Let $A \models T_\infty$ and $a \in A$.
2. $A \models \lambda_2$, so $A$ has two distinct elements $b \ne c$.
3. At least one of $b$ and $c$ is not $a$; take it as $y$.
4. So $A \models \sigma$.

The typical use of the example is as the simplest complete theory with infinite models.
A trap is to think that "the set is infinite" is one sentence; it needs the infinite list $\lambda_2, \lambda_3, \dots$.
