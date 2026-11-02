---
tag: N383CX7WKS
kind: concept
name: Regularity theory
msc: [35B65, 35J15, 35D30]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_operator
---

## Summary

Regularity theory is the part of the theory of partial differential equations that shows that solutions are smoother than first assumed.
Typically one first obtains a [[weak solution|SJZX81A783]] in a [[Sobolev space|M4CEZ5K9HP]].
Then one proves that it has more derivatives, in Sobolev or [[Hölder spaces|P101AX1ZSC]], when the coefficients and data are smooth.
For elliptic equations the classical results are [[elliptic regularity|2PVQY9PCT4]], the [[Schauder estimates|HSEKZMAH1V]], the [[Calderón–Zygmund estimates|RYQJH4RYB4]] and the [[De Giorgi–Nash–Moser theorem|32C3D8FG9V]].
An important source of the subject is [[Hilbert's nineteenth problem|QPMM2ZPWBW]] on the analyticity of minimisers.

## Explanations

### L1 human

Existence of a solution is often easiest to prove in a weak sense, where the function may not even have classical derivatives.
Regularity theory then asks how nice this solution really is.
For the Laplace equation $\Delta u = 0$ the answer is striking: any locally integrable weak solution is smooth, and even real analytic.
In general, an elliptic operator $L$ of order $m$ with smooth coefficients gains $m$ derivatives.
If $Lu$ has $k$ derivatives in $L^2$, then $u$ has $k + m$ derivatives in $L^2$ inside the domain.
