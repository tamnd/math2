---
records:
    - id: VNE2TKHQZN
      kind: monograph
      title: Combinatorial Theory
      creators:
        - name: Dieter Jungnickel
          role: editor
        - name: Klaus Vedder
          role: editor
      date: "1982"
      expressions:
        - key: e1
          kind: edition
          date: "1982"
          ids:
            doi: 10.1007/bfb0062982
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783540119715"
                    - "9783540393801"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0062982
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: VNE8N0D2FB
      kind: preprint
      title: Equivariant isometric immersions of surfaces in hyperbolic space
      creators:
        - name: Jean-Marc Schlenker
          role: author
      date: "2026-09-26"
      subjects:
        - system: arxiv
          code: math.DG
        - system: arxiv
          code: math.GT
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-26"
          ids:
            arxiv: "2609.32300"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.32300"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
