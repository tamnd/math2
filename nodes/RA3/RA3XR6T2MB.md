---
tag: RA3XR6T2MB
kind: definition
name: NTU method
msc: [80A19, 80A20]
defines: KFNKGT1QQ9
uses: [97ASA870TV, J821AD6YTE]
sources:
  - url: https://en.wikipedia.org/wiki/NTU_method
---

## Definition

Consider the two-stream [[heat exchanger|97ASA870TV]] model with heat capacity rates $C_h$ and $C_c$, overall [[heat transfer coefficient|J821AD6YTE]] $U$, area $A$, and inlet temperatures $T_{h,i} > T_{c,i}$.
Let $C_{\min} = \min(C_h, C_c)$, $C_{\max} = \max(C_h, C_c)$ and $C_r = C_{\min} / C_{\max}$.

1. The largest possible heat rate is $q_{\max} = C_{\min} (T_{h,i} - T_{c,i})$.
2. The *effectiveness* of the exchanger is $\varepsilon = q / q_{\max}$, where $q$ is its actual heat rate.
3. The *number of transfer units* is $\mathrm{NTU} = U A / C_{\min}$.

The *NTU method* computes $q = \varepsilon \, q_{\max}$, where $\varepsilon = \varepsilon(\mathrm{NTU}, C_r)$ is the function obtained by solving the model for the given flow arrangement.

## Remarks

The standard effectiveness relations are as follows.
For parallel flow, $\varepsilon = \dfrac{1 - e^{-\mathrm{NTU}(1 + C_r)}}{1 + C_r}$.
For counterflow with $C_r < 1$, $\varepsilon = \dfrac{1 - e^{-\mathrm{NTU}(1 - C_r)}}{1 - C_r \, e^{-\mathrm{NTU}(1 - C_r)}}$, and for $C_r = 1$, $\varepsilon = \mathrm{NTU}/(1 + \mathrm{NTU})$.
In the limit $C_r = 0$, as for a stream that condenses or boils, $\varepsilon = 1 - e^{-\mathrm{NTU}}$ for every arrangement.

Example: counterflow with $C_r = 0.5$ and $\mathrm{NTU} = 2$ gives $\varepsilon = (1 - e^{-1})/(1 - 0.5 e^{-1}) \approx 0.632/0.816 \approx 0.77$.
So the exchanger transfers about $77$ percent of $q_{\max}$.

Non-example: if $T_{h,i} = T_{c,i}$, then $q_{\max} = 0$ and clause 2 does not define an effectiveness.

Always $0 \le \varepsilon \le 1$, and $\varepsilon$ increases with $\mathrm{NTU}$.
