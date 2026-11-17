---
tag: 1VVKMP89VA
kind: example
name: The subgroups of order two of the Klein four-group are isomorphic but not conjugate
msc: ["20E45"]
topics: [E1506A5A55]
audience: ug1
not_instance_of:
  - target: 0H11ZPX4ND
    note: V4 is abelian, so each subgroup is equal to all its conjugates, and two different subgroups are never conjugate
uses: [0PMRQJVTME, 082GHNPJ53, 08MG7H8JW5]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_four-group
    locator: Permutation representation
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Conjugacy of subgroups and general subsets
---

## Example

Let $V_4 = \{e, a, b, c\}$ be the [[Klein four-group|0PMRQJVTME]].
In $V_4$, each element is its own inverse, and the product of two different elements of $\{a, b, c\}$ is the third one.
Let $H = \{e, a\}$ and $K = \{e, b\}$.
We show that $H$ and $K$ are isomorphic, but not [[conjugate subgroups|0H11ZPX4ND]].

1. $H$ and $K$ are subgroups of order $2$, because $a^2 = e$ and $b^2 = e$.
2. The map $H \to K$ with $e \mapsto e$ and $a \mapsto b$ is a [[group isomorphism|08MG7H8JW5]]. So $H \cong K$.
3. $V_4$ is an [[abelian group|082GHNPJ53]], because its multiplication table is symmetric.
4. For each $g \in V_4$ and $h \in H$, $ghg^{-1} = hgg^{-1} = h$. So $gHg^{-1} = H$ for each $g$.
5. Thus the only conjugate of $H$ is $H$ itself. Since $K \ne H$, $K$ is not a conjugate of $H$.

## Remarks

Conjugate subgroups are isomorphic, but this example shows that the converse is false.
The same thing happens in each abelian group with two different subgroups of the same order.
A non-abelian example is in the symmetric group $S_4$, with composition from right to left.
Let $V = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ and $W = \{e, (1\,2), (3\,4), (1\,2)(3\,4)\}$.
Both groups are isomorphic to $V_4$, because each has order $4$ and three elements of order $2$.
$V$ is normal in $S_4$, so its only conjugate is $V$, and $W$ is not conjugate to $V$.
$W$ is not normal: $(1\,3)W(1\,3)^{-1} = \{e, (1\,4), (2\,3), (1\,4)(2\,3)\} \ne W$.

## Explanations

### L1 human

Two subgroups can have the same shape without being related by a renaming inside the group.
In $V_4$ nothing can be renamed by conjugation, because the group is abelian.
So each subgroup stays where it is, even if another subgroup has the same shape.

### L2 human

Conjugate subgroups are isomorphic, because conjugation by $g$ is an isomorphism from $H$ to $gHg^{-1}$.
A common error is to use the converse and to conclude that two isomorphic subgroups are conjugate.
To show that two subgroups are not conjugate, look for a property that conjugation keeps and that only one of them has.
Here the property is "the subgroup is normal": $H$ is normal in $V_4$, so its only conjugate is $H$.
In the example in $S_4$, the same property separates $V$ from $W$.
