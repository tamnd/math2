---
tag: 3PCHE75WFM
kind: example
name: A default theory with no extension
msc: ["68T27", "03B60"]
topics: [NJB94B39QK]
audience: ug2
instance_of: [K4AYFFKY2D]
uses: [K4AYFFKY2D, 44Z7CFSJAE]
sources:
  - url: https://plato.stanford.edu/entries/logic-nonmonotonic/
    locator: Non-monotonic Logic (SEP entry), section 3.4
---

## Example

Let $\theta$ be an atom, and let $T = (\emptyset, \set{d})$ with $d = (\top : \theta)/\neg\theta$.
We show that the [[default theory|K4AYFFKY2D]] $T$ has no [[extension|44Z7CFSJAE]].

1. Let $E$ be an extension, so $\Gamma_T(E) = E$.
2. Case $\neg\theta \in E$. Then $d$ is blocked, so $\Gamma_T(E) = \mathrm{Cn}(\emptyset)$.
   The atom $\neg\theta$ is not a tautology, so $\neg\theta \notin \Gamma_T(E) = E$, a contradiction.
3. Case $\neg\theta \notin E$. Then $d$ is not blocked, and its prerequisite $\top$ is in every deductively closed set.
   So $\neg\theta \in \Gamma_T(E) = E$, a contradiction.
4. Both cases are impossible, so $T$ has no extension.

## Remarks

The default defeats itself: applying it makes its own justification inconsistent.
The default is not normal; the normal default $(\top : \theta)/\theta$ gives the extension $\mathrm{Cn}(\set{\theta})$.
If $T$ has no extension, then every sentence is a skeptical consequence and none is a credulous one.
Lukaszewicz's variant of default logic avoids this case: in it every default theory has an extension.

## Explanations

### L1 human

The rule says: "if it is consistent that $\theta$, conclude not $\theta$".
If we use the rule, we believe not $\theta$, and then the rule should not have been used.
If we do not use it, nothing stops it, so we should have used it.
There is no stable set of beliefs.

### L2 human

The proof is a case split on whether the default is blocked by the candidate extension.
Each case gives the opposite answer when we compute $\Gamma_T(E)$.
A trap is to think that every default theory has an extension; this holds for normal theories, not in general.
