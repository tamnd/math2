---
tag: VRA3B0V8CD
kind: example
name: The cross product is not associative
msc: ["08A02", "15A72"]
topics: [BAZT8JJ70S, VKVAJ94SKZ]
audience: school
not_instance_of:
  - target: 0K8F7PVDMX
    note: (i × i) × j = 0, but i × (i × j) = -j
uses: [0N5N15HWZ7, 0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Algebraic properties
---

## Example

The [[cross product|0N5N15HWZ7]] is a [[binary operation|0M418FE7BB]] on $\mathbb{R}^3$.
Let $\mathbf{i}, \mathbf{j}, \mathbf{k}$ be the standard basis vectors.
We use the rules $\mathbf{v} \times \mathbf{v} = \mathbf{0}$ for each vector $\mathbf{v}$, $\mathbf{i} \times \mathbf{j} = \mathbf{k}$ and $\mathbf{i} \times \mathbf{k} = -\mathbf{j}$.
We show that the cross product is not [[associative|0K8F7PVDMX]].

1. Take $\mathbf{a} = \mathbf{i}$, $\mathbf{b} = \mathbf{i}$, $\mathbf{c} = \mathbf{j}$.
2. $(\mathbf{i} \times \mathbf{i}) \times \mathbf{j} = \mathbf{0} \times \mathbf{j} = \mathbf{0}$.
3. $\mathbf{i} \times (\mathbf{i} \times \mathbf{j}) = \mathbf{i} \times \mathbf{k} = -\mathbf{j}$.
4. Since $\mathbf{0} \neq -\mathbf{j}$, the law fails for this triple, so the cross product is not associative.

## Remarks

The rule $\mathbf{i} \times \mathbf{k} = -\mathbf{j}$ comes from $\mathbf{k} \times \mathbf{i} = \mathbf{j}$ and the rule $\mathbf{u} \times \mathbf{v} = -(\mathbf{v} \times \mathbf{u})$.
For all vectors, the [[vector triple product formula|03FTB26QYD]] $\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}$ holds.
With it, the difference of the two groupings is $\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) - (\mathbf{a} \times \mathbf{b}) \times \mathbf{c} = (\mathbf{b} \cdot \mathbf{c})\mathbf{a} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}$.
For the triple above, this is $0 \cdot \mathbf{i} - 1 \cdot \mathbf{j} = -\mathbf{j}$, as in steps 2 and 3.
In place of associativity, the cross product satisfies the [[Jacobi identity|ZKFN197MBR]] $\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) + \mathbf{b} \times (\mathbf{c} \times \mathbf{a}) + \mathbf{c} \times (\mathbf{a} \times \mathbf{b}) = \mathbf{0}$, so $\mathbb{R}^3$ with the cross product is a [[Lie algebra|5JJYBJ6A8K]].
The cross product is not [[commutative|099E72KTF8]] either: $\mathbf{j} \times \mathbf{i} = -\mathbf{k}$.

## Explanations

### L1 human

The cross product takes two arrows in space and gives a third arrow.
The cross product of an arrow with itself is the zero arrow.
So if we first take $\mathbf{i} \times \mathbf{i}$, we get zero, and the final answer is zero.
If we first take $\mathbf{i} \times \mathbf{j}$, we get $\mathbf{k}$, and $\mathbf{i} \times \mathbf{k}$ is not zero.
The brackets changed the answer.

### L2 human

A good triple for a failure of associativity often uses a repeated element, because $\mathbf{v} \times \mathbf{v} = \mathbf{0}$ makes one grouping zero.
The general identity in the Remarks shows that the two groupings agree exactly when $(\mathbf{b} \cdot \mathbf{c})\mathbf{a} = (\mathbf{a} \cdot \mathbf{b})\mathbf{c}$.
For example, they agree when $\mathbf{b}$ is perpendicular to both $\mathbf{a}$ and $\mathbf{c}$.
A trap is to test only such triples, for example $\mathbf{i}, \mathbf{j}, \mathbf{i}$.
