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

We use the formula $\mathrm{Cont}(a)$ for [[continuity of a real function|YEJP7292A2]] at $a$, over the signature of ordered fields with a unary function symbol $f$.
Write $A$ for $(-\delta < x - a \land x - a < \delta)$ and $B$ for $(-\varepsilon < f(x) - f(a) \land f(x) - f(a) < \varepsilon)$.
Then
$$\mathrm{Cont}(a) = \forall \varepsilon \, \Big( 0 < \varepsilon \to \exists \delta \, \big( 0 < \delta \land \forall x \, (A \to B) \big) \Big).$$
We compute a [[prenex form|CS82V969DE]] of $\forall a \, \mathrm{Cont}(a)$, working from the inside out.

1. The variable $x$ is not free in $0 < \delta$, so the rule $\alpha \land \forall x \, \beta \equiv \forall x \, (\alpha \land \beta)$ gives
   $$0 < \delta \land \forall x \, (A \to B) \;\equiv\; \forall x \, \big( 0 < \delta \land (A \to B) \big).$$
2. The variable $\delta$ is not free in $0 < \varepsilon$, so the rule $\alpha \to \exists \delta \, \beta \equiv \exists \delta \, (\alpha \to \beta)$ moves $\exists \delta$ out of the consequent.
3. In the same way, $x$ is not free in $0 < \varepsilon$, so the rule $\alpha \to \forall x \, \beta \equiv \forall x \, (\alpha \to \beta)$ moves $\forall x$ out.
4. Steps 1 to 3 give $\mathrm{Cont}(a) \equiv \forall \varepsilon \, \exists \delta \, \forall x \, \mu$, with the quantifier-free matrix
   $$\mu = 0 < \varepsilon \to \big( 0 < \delta \land (A \to B) \big).$$
5. So $\forall a \, \mathrm{Cont}(a) \equiv \forall a \, \forall \varepsilon \, \exists \delta \, \forall x \, \mu$.
   Its prefix type $\forall \forall \exists \forall$ has three blocks and starts with $\forall$, so it is a $\Pi_3$ form.
6. Each rule had the side condition that the moved variable is not free in the other part.
   All bound variables differ from each other and from $a$, so no renaming was needed.

So "$f$ is continuous" has the prenex form $\forall a \, \forall \varepsilon \, \exists \delta \, \forall x \, \mu$.

## Remarks

The negation "$f$ is not continuous" now comes out mechanically.
Change each quantifier to its dual and negate the matrix:
$$\exists a \, \exists \varepsilon \, \forall \delta \, \exists x \, \neg \mu.$$
Uniform continuity has the prenex form $\forall \varepsilon \, \exists \delta \, \forall a \, \forall x \, \mu$.
The two prefixes differ only in the place of $\forall a$, which shows how the [[order of quantifiers|0FYQMKFE77]] changes the meaning.
In arithmetic, the same count of blocks gives the levels of the [[arithmetical hierarchy|7CVJCQKY41]].

## Explanations

### L1 human

The definition of continuity reads: "for every point and every error bound there is a tolerance such that, for every input, a condition holds".
In prenex form all the "for every" and "there is" phrases stand at the front, in exactly this order.
The condition at the end has no more quantifiers.

### L2 human

We check step 2 directly: $0 < \varepsilon \to \exists \delta \, \gamma$ is equivalent to $\exists \delta \, (0 < \varepsilon \to \gamma)$, for fixed values of $\varepsilon$ and $a$.
If $0 < \varepsilon$ is false, both sides are true; the right side needs one value of $\delta$, and the domain is nonempty.
If $0 < \varepsilon$ is true, both sides say that some $\delta$ satisfies $\gamma$.
The typical use of a prenex form is to negate a definition without error, as in the remark.
Watch out for the side condition.
The rule would fail for $0 < \delta \to \exists \delta \, \gamma$, where $\delta$ is free on the left, and there you must first rename the bound $\delta$.
