---
tag: TMJJSN9PDP
kind: definition
name: ATR0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
defines: MKB74TX3Z8
uses: [K9XG0Z2N9V, 01CGSJ0GNQ, Y92NXGEQBD, 60P2XWY5QX]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical transfinite recursion ATR0
---

## Definition

We define the system $\mathsf{ATR}_0$, in which every arithmetical construction can be iterated along every countable well-ordering.

Work in $L_2$ with the codes of the [[definition of second-order arithmetic|Y92NXGEQBD]].
A *countable linear order* is a set $W$ of pairs with the following property.
The relation $\le_W = \{ (i, j) : (i, j) \in W \}$ is a linear order on its field $\mathrm{field}(W) = \{ i : (i, i) \in W \}$.
It is a *countable [[well-ordering|01CGSJ0GNQ]]*, written $\mathrm{WO}(W)$, if there is no function $f \colon \mathbb{N} \to \mathrm{field}(W)$ with $f(k + 1) <_W f(k)$ for all $k$.

For a set $H$ of pairs, let $H_j = \{ n : (n, j) \in H \}$ and $H^j = \{ (n, i) \in H : i <_W j \}$.
For an arithmetical formula $\theta(n, Y)$, a *hierarchy along $W$ for $\theta$* is a set $H$ with
$$\forall j \in \mathrm{field}(W)\; \forall n\, \big(n \in H_j \leftrightarrow \theta(n, H^j)\big).$$

*Arithmetical transfinite recursion* is the scheme: for every arithmetical formula $\theta(n, Y)$, with any parameters, and every $W$ with $\mathrm{WO}(W)$, there is a hierarchy along $W$ for $\theta$.
$\mathsf{ATR}_0$ is the subsystem of second-order arithmetic whose axioms are those of [[ACA0|K9XG0Z2N9V]] together with arithmetical transfinite recursion.

## Notation

The name abbreviates "arithmetical transfinite recursion".
$\mathrm{WO}(W)$ is a $\Pi^1_1$ formula, since it quantifies over all functions $f$.
The column $H_j$ is stage $j$ of the recursion, and $H^j$ is the record of all earlier stages.

## Remarks

The condition $\mathrm{WO}(W)$ is the only place where a set quantifier enters.
It is tested inside the model, so a model may apply the scheme to an order that it takes for a well-ordering but that is ill-founded in truth.

The step $\theta(n, H^j)$ sees all earlier stages, and not only the one just before.
This matters at limit stages, where there is no stage just before.
The formula $\theta$ must be arithmetical, so each stage is arithmetical in the earlier ones, while the hierarchy as a whole can climb far beyond the arithmetical sets.

For an example, take $W = (\mathbb{N}, <)$ and let $\theta(n, Y)$ say "$n$ is in the [[Turing jump|60P2XWY5QX]] of $Y$".
A hierarchy is then one set whose columns are, up to Turing equivalence, $\emptyset', \emptyset'', \emptyset''', \ldots$, as worked out in [[the ω-th jump example|MF6AG57W3W]].
For $W$ with a single element, a hierarchy is just the set $\{ n : \theta(n, \emptyset) \}$ in column $0$, which exists already by arithmetical comprehension.

For a case that is not an instance, a recursion whose step is "$n$ is in the hyperjump of $Y$" is not allowed, because this step is a $\Pi^1_1$ formula.
The scheme also gives no hierarchy along the order of the negative integers, which has a descending sequence.

The concept of [[ATR0|MKB74TX3Z8]] gives the models, the equivalents and the strength of the system.

## Explanations

### L1 human

Arithmetical transfinite recursion allows one to repeat an arithmetical construction along any well-ordering.
At each stage the construction may use the results of all earlier stages.
The result is one set that holds all stages, each in its own column.

### L2 human

To use the scheme, fix the step $\theta$ and the well-ordering $W$, and get all stages at once as columns of one set.
The typical step is the Turing jump, so $\mathsf{ATR}_0$ proves that the jump can be iterated along any countable well-ordering.
For $W = \omega + 1$, the top column is the jump of the whole hierarchy below it, which is $\emptyset^{(\omega + 1)}$ up to Turing equivalence.
Watch out: the scheme needs a proof of $\mathrm{WO}(W)$ inside the system, and an order that only looks well-founded is not enough.
