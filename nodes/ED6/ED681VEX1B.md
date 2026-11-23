---
tag: ED681VEX1B
kind: example
name: The stages of a non-monotone operator give no fixed point
msc: ["03F15", "03D70"]
topics: [XTTKZTYDSD]
audience: research
not_instance_of:
  - target: 5C4YBXQV15
    note: the variable X occurs negatively, so the stages do not grow and their union is not a fixed point
  - target: DBD64TH52D
    note: the operator has no fixed point at all
uses: [5C4YBXQV15, VF1N6N8ECC, TA0AAMRY00, 0A7KV2WB7A, DBD64TH52D]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed-point_logic
    locator: Partial fixed-point logic
  - url: https://en.wikipedia.org/wiki/Fixed-point_logic
    locator: Inflationary fixed-point logic
---

## Example

Let $A(X, x) = \neg X(x)$, so the operator is $\Gamma(S) = \mathbb{N} \setminus S$, the [[operator not X|VF1N6N8ECC]].
It sends the empty set to $\mathbb{N}$ and $\mathbb{N}$ to the empty set.
We compute three kinds of stages and show that none of them gives a fixed point.

1. $\Gamma$ is not [[monotone|0A7KV2WB7A]]: $\emptyset \subseteq \mathbb{N}$, but $\Gamma(\emptyset) = \mathbb{N}$ is not contained in $\Gamma(\mathbb{N}) = \emptyset$.
2. $\Gamma$ has no fixed point, since $\Gamma(S) = S$ would give $0 \in S$ if and only if $0 \notin S$.
3. Cumulative stages, as for [[local predicativity|5C4YBXQV15]], are $I^\alpha = \Gamma(I^{<\alpha})$.
   Then $I^0 = \Gamma(\emptyset) = \mathbb{N}$.
4. For $\alpha \ge 1$, the union $I^{<\alpha}$ contains $I^0 = \mathbb{N}$, so $I^{<\alpha} = \mathbb{N}$ and $I^\alpha = \Gamma(\mathbb{N}) = \emptyset$.
5. So the stages are $\mathbb{N}, \emptyset, \emptyset, \ldots$, and their union $\mathbb{N}$ is not a fixed point, because $\Gamma(\mathbb{N}) = \emptyset$.
6. Iterated stages are $P_0 = \emptyset$ and $P_{i+1} = \Gamma(P_i)$.
   Then $P_1 = \mathbb{N}$, $P_2 = \emptyset$, $P_3 = \mathbb{N}$, and the sequence has period $2$, so it has no limit and gives no fixed point.
7. Inflationary stages are $Q_0 = \emptyset$ and $Q_{i+1} = Q_i \cup \Gamma(Q_i)$.
   Then $Q_i = \mathbb{N}$ for all $i \ge 1$, so the sequence becomes constant, but $\mathbb{N}$ is not a fixed point of $\Gamma$.
8. So no kind of stages gives a [[least fixed point|DBD64TH52D]], as step 2 predicts.

## Remarks

The stage construction needs monotonicity.
For a monotone operator, $I^\alpha \subseteq I^\beta$ for $\alpha \le \beta$, each element has a well-defined stage, and the union of all stages is the least fixed point, as in the [[order of type ω+1|TA0AAMRY00]].
Here the number $0$ enters at stage $0$ and leaves at stage $1$, so it has no stage in the sense of local predicativity.

Positivity is sufficient for monotonicity, but it is not necessary.
For $A(X, x) = X(x) \vee \neg X(x)$ the operator is constant, $\Gamma(S) = \mathbb{N}$, so it is monotone although $X$ occurs negatively.
The inflationary stages always become constant, and for a monotone operator their limit is the least fixed point.

## Explanations

### L1 human

Take the rule "a number belongs to the next list exactly when it is missing from the current list".
Start with an empty list: the rule puts every number in.
Apply the rule again: now every number is present, so the rule takes every number out.
The list jumps between "all numbers" and "no numbers" forever, and it never settles.

### L2 human

We compare with the operator $\Gamma'(S) = \{ 0 \} \cup \{ n + 1 : n \in S \}$, which is monotone.

1. Cumulative stages: $I^0 = \{ 0 \}$, $I^1 = \{ 0, 1 \}$, and $I^k = \{ 0, \ldots, k \}$.
2. Their union is $\mathbb{N}$, and $\Gamma'(\mathbb{N}) = \mathbb{N}$, so the union is a fixed point.
3. For $\Gamma$ of the example, step 4 gives $I^1 = \emptyset$, which is smaller than $I^0$.
4. The stages of $\Gamma'$ only grow, and the stages of $\Gamma$ shrink after the first step.

The typical use of the example is to explain why the theories of inductive definitions require $X$-positive formulas.
The trap is to think that the inflationary stages repair the problem: they become constant, but their limit need not be a fixed point.
