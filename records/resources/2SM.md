---
records:
    - id: 2SM6DM0RVQ
      kind: monograph
      title: Deformation Theory
      creators:
        - name: Robin Hartshorne
          role: author
      date: "2010"
      expressions:
        - key: e1
          kind: edition
          date: "2010"
          ids:
            doi: 10.1007/978-1-4419-1596-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2010"
              ids:
                isbn:
                    - "9781441915955"
                    - "9781441915962"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-1596-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 2SMJ5V7FZ7
      kind: preprint
      title: Topological edge spectrum along curved interfaces
      creators:
        - name: Alexis Drouot
          role: author
        - name: Xiaowen Zhu
          role: author
      date: "2023-11-02"
      subjects:
        - system: arxiv
          code: math-ph
        - system: arxiv
          code: cond-mat.mes-hall
        - system: arxiv
          code: math.MP
        - system: arxiv
          code: math.SP
        - system: arxiv
          code: quant-ph
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2023-11-02"
          ids:
            arxiv: "2311.00918"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2311.00918"
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
