---
records:
    - id: 2GC6K487FE
      kind: preprint
      title: Boundary Value Correction for the Boundary Element Method
      creators:
        - name: Erik Burman
          role: author
        - name: Peter Hansbo
          role: author
        - name: Mats G. Larson
          role: author
      date: "2026-09-25"
      subjects:
        - system: arxiv
          code: math.NA
        - system: arxiv
          code: cs.NA
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-25"
          ids:
            arxiv: "2609.31555"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.31555"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: 2GCSZBDYEX
      kind: monograph
      title: An Introduction to Delay Differential Equations with Applications to the Life Sciences
      creators:
        - name: Hal Smith
          role: author
      date: "2010-09-15"
      expressions:
        - key: e1
          kind: edition
          date: "2010-09-15"
          ids:
            doi: 10.1007/978-1-4419-7646-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2010-09-15"
              ids:
                isbn:
                    - "9781441976451"
                    - "9781441976468"
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-7646-8
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
