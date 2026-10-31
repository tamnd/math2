---
records:
    - id: XB8NYRD86J
      kind: preprint
      title: 'Brenier Meets Adversarial Training: Optimal Transport Geometry for Robust Learning'
      creators:
        - name: Alireza Abdollahpoorrostam
          role: author
        - name: Ehsan Sharifian
          role: author
        - name: Buse Şen
          role: author
        - name: Marco Cuturi
          role: author
        - name: Daniel Kuhn
          role: author
      date: "2026-09-25"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.OC
        - system: arxiv
          code: stat.ML
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-25"
          ids:
            arxiv: "2609.31363"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.31363"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: XB8XVTXDHH
      kind: monograph
      title: 'An Introduction to the Mathematical Theory of the Navier-Stokes Equations: Steady-State Problems'
      creators:
        - name: G.P. Galdi
          role: author
      date: "2011"
      expressions:
        - key: e1
          kind: edition
          date: "2011"
          ids:
            doi: 10.1007/978-0-387-09620-9
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2011"
              ids:
                isbn:
                    - "9780387096193"
                    - "9780387096209"
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-09620-9
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
