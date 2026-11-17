---
tag: BZ1J60WBEB
kind: example
name: The prenex form of continuity
msc: ["03B10", "26A15"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [CS82V969DE]
uses: [CS82V969DE, ME9J33BFNC, YEJP7292A2, 7CVJCQKY41]
sources:
  - url: https://en.wikipedia.org/wiki/Prenex_normal_form
    locator: Conversion to prenex form
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: lead section
---

## Example

We use the formula $\mathrm{Cont}(a)$ of [[continuity of a real function|YEJP7292A2]], over the signature of ordered fields with a unary function symbol $f$.
Write $A$ for $(-\delta < x - a \land x - a < \delta)$ and $B$ for $(-\varepsilon < f(x) - f(a) \land f(x) - f(a) < \varepsilon)$.
Then
$$\mathrm{Cont}(a) = \forall \varepsilon \, \big(0 < \varepsilon \to \exists \delta \, (0 < \delta \land \forall x \, (A \to B))\big).$$
We compute a [[prenex form|CS82V969DE]] of $\forall a \, \mathrm{Cont}(a)$.

1. The variable $x$ is not free in $0 < \delta$. The rule $\alpha \land \forall x \, \beta \equiv \forall x \, (\alpha \land \beta)$ gives $0 < \delta \land \forall x \, (A \to B) \equiv \forall x \, (0 < \delta \land (A \to B))$.
2. The variable $\delta$ is not free in $0 < \varepsilon$. The rule $\alpha \to \exists \delta \, \beta \equiv \exists \delta \, (\alpha \to \beta)$ moves $\exists \delta$ out of the consequent.
3. In the same way, the rule $\alpha \to \forall x \, \beta \equiv \forall x \, (\alpha \to \beta)$ moves $\forall x$ out, because $x$ is not free in $0 < \varepsilon$.
4. By steps 1 to 3, $\mathrm{Cont}(a) \equiv \forall \varepsilon \, \exists \delta \, \forall x \, \mu$ with the quantifier-free matrix $\mu = 0 < \varepsilon \to (0 < \delta \land (A \to B))$.
5. So $\forall a \, \mathrm{Cont}(a) \equiv \forall a \, \forall \varepsilon \, \exists \delta \, \forall x \, \mu$. Its prefix type is $\forall \forall \exists \forall$, with three blocks, so it is a $\Pi_3$ form.
6. Each rule in steps 1 to 3 has the side condition that the moved variable is not free in the other part. All bound variables are distinct from $a$ and from each other, so no renaming is needed.

So "$f$ is continuous" has the prenex form $\forall a \, \forall \varepsilon \, \exists \delta \, \forall x \, \mu$.

## Remarks

The negation "$f$ is not continuous" has the prenex form $\exists a \, \exists \varepsilon \, \forall \delta \, \exists x \, \neg \mu$, with each quantifier changed to its dual.
Uniform continuity has the prenex form $\forall \varepsilon \, \exists \delta \, \forall a \, \forall x \, \mu$.
The two prefixes differ only in the place of $\forall a$, which shows how the [[order of quantifiers|0FYQMKFE77]] changes the meaning.
In arithmetic, the same count of blocks gives the levels of the [[arithmetical hierarchy|7CVJCQKY41]].

## Explanations

### L1 human

The definition of continuity says: "for every point and every error there is a tolerance such that for every input, a condition holds".
In prenex form, all the "for every" and "there is" phrases stand at the front, in this order.
The condition at the end has no more quantifiers.

### L2 human

We check the step $0 < \varepsilon \to \exists \delta \, \gamma \equiv \exists \delta \, (0 < \varepsilon \to \gamma)$ directly, for fixed values of $\varepsilon$ and $a$.

1. If $0 < \varepsilon$ is false, both sides are true. The right side needs one value of $\delta$, and the domain is nonempty.
2. If $0 < \varepsilon$ is true, both sides say that some $\delta$ satisfies $\gamma$.

The typical use is to negate a definition mechanically, as in the remark.
A trap: the side condition matters.
The rule would fail for $0 < \delta \to \exists \delta \, \gamma$, where $\delta$ is free on the left.
